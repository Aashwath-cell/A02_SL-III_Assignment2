# StudentProject

A multi-app Django project with no database, containerized with Docker, and deployed via Jenkins.

## Running Locally
1. Clone the repo: `git clone https://github.com/Aashwath-cell/A02_SL-III_Assignment2.git`
2. Build the Docker image: `docker build -t studentproject .`
3. Run the container: `docker run -p 8000:8000 studentproject`
4. Visit `http://localhost:8000`.

## Docker Hub
- Image: `yourusername/studentproject`
- Link: [https://hub.docker.com/r/yourusername/studentproject](https://hub.docker.com/r/yourusername/studentproject)