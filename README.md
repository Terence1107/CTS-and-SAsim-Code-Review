# How to Explore

If you want a quick look, I suggest:

- **Start with the Round Robin scheduler** for an algorithmic sample
- **Check out the Oral History API** for a taste of backend work  
- **Take a look at the Financial Sentiment Analysis** for my first ML project
- **Browse the LeetCode solutions** if you'd like to see more of my problem-solving process

# Code Samples

## Round Robin CPU Scheduler

A small simulation of the Round Robin scheduling algorithm I wrote from my operating systems course in University. Each process gets a fixed time slice, and if it's not finished, it's preempted and re-scheduled. The code demonstrates basic data structures, queue management, and scheduling logic.

## Oral History Archive API (Flask)

Part of a full stack project for an oral history archive where I query and retrieve metadata that accompanies interview videos. This set of files shows how the API layer and data model fit together in a larger application.

**Routes (video_route.py):** Flask blueprint with endpoints to fetch, create, and delete videos.

**Model (video_model.py):** Mirrors the database schema, with fields for filename, storage URL, duration, etc., plus helper methods for data serialization and display formatting.

## Financial News Sentiment Analysis with FinBERT
My first real dive into machine learning. I built a sentiment classifier for financial news articles I scrape. FinBERT was used to extract embeddings from about 6,700 articles to help train and pass through a custom 3-layer neural network. A 98.4% accuracy was achieved on the test set which was pretty exciting for a first ML project! Great introduction to data preprocessing, model design, training loops, and evaluation.

## LeetCode Practice

I've also included a collection of solved problems. Most of them have my initial thoughts written out, followed by attempts to refine and optimize the code. They cover a variety of topics which include algorithms, data structures, and problem-solving approaches.

# Me!

Thanks for taking the time to explore and review some of my code! I’m a third-year Computer Science student at Queen’s University with a strong background in Python and exposure to C and C++. Most of my projects involve  full-stack applications, but I’ve also taken on work requiring performance and system integration. I’ve also had the opportunity to lead coding camps focused on Roblox development with Lua, and gained exposure to Unity through a university course. Altogether, these experiences have built my interest in simulation, real-time systems, and how software connects with hardware. As someone who grew up tinkering with games, it’s exciting to think about bringing that same interactive, immersive energy into aviation training. Cheers!