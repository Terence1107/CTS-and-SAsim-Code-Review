from dataclasses import dataclass
from typing import Optional

@dataclass
class Video:
    id: Optional[str] = None  # DB generates this
    filename: str = ""
    storage_url: str = ""
    storage_type: str = "Vimeo"  # stored in Vimeo
    format: str = "mp4"  
    duration_seconds: Optional[int] = None  
    resolution: Optional[str] = None  # "1920x1080" 
    language: Optional[str] = None
    notes: Optional[str] = None  # any extra info
    
    def __post_init__(self):
        # Basic validation
        if not self.filename:
            raise ValueError("filename is required")
        if not self.storage_url:
            raise ValueError("storage_url is required")
    
    def to_dict(self):
        return {
            'id': self.id,
            'filename': self.filename,
            'storage_url': self.storage_url,
            'storage_type': self.storage_type,
            'format': self.format,
            'duration_seconds': self.duration_seconds,
            'resolution': self.resolution,
            'language': self.language,
            'notes': self.notes
        }
    
    @classmethod
    def from_dict(cls, data):
        return cls(**data)
    
    def get_duration_display(self):
        if not self.duration_seconds:
            return "Unknown"
        
        # Convert seconds to readable format
        hours = self.duration_seconds // 3600
        mins = (self.duration_seconds % 3600) // 60
        secs = self.duration_seconds % 60
        
        if hours > 0:
            return f"{hours}h {mins}m {secs}s"
        elif mins > 0:
            return f"{mins}m {secs}s"
        else:
            return f"{secs}s"
    
    def is_valid(self):
        """Quick validation check"""
        return bool(self.filename and self.storage_url)
