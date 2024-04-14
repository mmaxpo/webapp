# Webapp

A brief description of what this project does and who it's for.

## Installation

Instructions on how to get your development environment running.

### Prerequisites

List any prerequisites, libraries, OS version, etc., that are needed before installing the program.

### Setup

A step-by-step series of examples that tell you how to get a development environment running.
### Postgres

```bash
psycopg==3.1.18

psql postgres
CREATE ROLE myuser WITH LOGIN PASSWORD 'mypassword';
ALTER ROLE myuser CREATEDB;
CREATE DATABASE mydatabase WITH OWNER myuser;
psql -U xpo -d webapp -h localhost



brew services start postgresql@14
brew services list
```

### NGINX
```
server {
    listen 80;
    server_name 54.152.174.29;  # Change this to your domain

    location /static/ {
        alias /var/lib/docker/volumes/webapp_static/_data/;  # Ensure the path points to your static files directory
        expires 30d;
    }

    location /media/ {
        alias /var/lib/docker/volumes/webapp_media/_data/;  # Ensure the path points to your media files directory
        expires 30d;
    }

    location / {
        proxy_pass http://localhost:8000;  # Forward requests to your Docker container
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
```
