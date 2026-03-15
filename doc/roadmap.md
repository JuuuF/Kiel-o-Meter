# Redditor Roadmap

This project follows a more or less strict roadmap. Since I am new to pretty much everything this project encompasses, I cannot determine whether this roadmap holds up during the project's lifetime nor am I even able to come up with such a roadmap in the first place. Hence, this roadmap was AI generated in order to give me something to orient myself to.

## Week 1 - Infrastructure Foundation

### W1 Goal

Build the base data platform environment.

### W1 Tasks

Set up services using Docker:

- MinIO (data lake storage)
- PostGreSQL (warehouse)
- Spark (processing)
- Airflow (pipeline scheduler)
- Superset (BI)

### W1 Techniques to Learn

- Docker Compose multi-service environments
- Service networking
- Environment variables
- Data persistence with volumes

### W1 Checklist

Infrastructure is ready when:

- [X] `docker compose up` starts all services
- [X] MinIO dashboard is accessible
- [X] PostgreSQL accepts connections
- [X] Spark container starts successfully
- [X] Airflow UI loads
- [X] Superset UI loads
- [X] All services can communicate via Docker network

## Week 2 - Reddit Data Ingrestion

### W2 Goal

Build your first data ingestion pipeline.

Write a Python service that collects Reddit data.

### W2 Tasks

- Learn Reddit API
- Authenticate
- Fetch posts from chosen subreddits
- Store raw results locally

Example subreddits:

- r/technology
- r/gaming
- r/music
- r/worldnews

### W2 Techniques to Learn

- REST APIs
- HTTP requests
- JSON data parsing
- API rate limiting
- Pagination

Libraries you may use:

- requests
- praw

### W2 Checklist

Your collector works when:

- [ ] API authentication works
- [ ] You can fetch posts from multiple subreddits
- [ ] Each post includes metadata (score, comments, etc.)
- [ ] The script runs repeatedly without crashing
- [ ] Results are saved locally as JSON
