from flask import Blueprint, jsonify, request, current_app
from models.videos import Video

videos_bp = Blueprint('videos', __name__)

@videos_bp.route('/<video_id>', methods=['GET'])
def get_video(video_id):
    db = current_app.config.get('SUPABASE_CLIENT')
    if not db:
        return jsonify({'error': 'DB not available'}), 500
    
    video = db.get_video(video_id)
    if not video:
        return jsonify({'error': 'Video not found'}), 404
    
    return jsonify(video)

@videos_bp.route('/', methods=['POST'])
def create_video():
    # Get the data first
    req_data = request.get_json()
    if req_data is None:
        return jsonify({'error': 'No data provided'}), 400
    
    try:
        # Use the Video model for validation
        clean_data = {k: v for k, v in req_data.items() if k != 'interview_id'}
        video_obj = Video(**clean_data)  # This will validate required fields
        
        db_client = current_app.config.get('SUPABASE_CLIENT')
        if not db_client:
            return jsonify({'error': 'Database connection not available'}), 500
        
        new_video = db_client.create_video(video_obj.to_dict())
        if not new_video:
            return jsonify({'error': 'Failed to create video'}), 500
        
        # Link to interview if provided
        interview_id = req_data.get('interview_id')
        if interview_id:
            result = db_client.update_interview(interview_id, {'video_id': new_video['id']})
            if not result:
                # Log warning but don't fail the whole request
                current_app.logger.warning(f"Couldn't link video {new_video['id']} to interview {interview_id}")
        
        return jsonify({
            'message': 'Video created successfully',
            'video': new_video
        }), 201
        
    except ValueError as ve:
        return jsonify({'error': str(ve)}), 400
    except Exception as ex:
        current_app.logger.error(f"Error creating video: {str(ex)}")
        return jsonify({'error': 'Failed to create video'}), 500

@videos_bp.route('/<video_id>', methods=['DELETE'])
def delete_video(video_id):
    try:
        db = current_app.config.get('SUPABASE_CLIENT')
        if db is None:
            return jsonify({'error': 'Database connection not available'}), 500
        
        deleted = db.delete_video(video_id)
        if deleted:
            return jsonify({'message': 'Video deleted successfully'})
        
        return jsonify({'error': 'Video not found'}), 404
        
    except Exception as e:
        print(f"Delete error: {e}")  # Quick debug print
        return jsonify({'error': 'Failed to delete video'}), 500
