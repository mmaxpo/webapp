# Project Name

A brief description of what this project does and who it's for.

## Installation

Instructions on how to get your development environment running.

### Prerequisites

List any prerequisites, libraries, OS version, etc., that are needed before installing the program.

### Setup

A step-by-step series of examples that tell you how to get a development environment running.
### Postgres
psycopg==3.1.18
```bash
psql postgres
CREATE ROLE myuser WITH LOGIN PASSWORD 'mypassword';
ALTER ROLE myuser CREATEDB;
CREATE DATABASE mydatabase WITH OWNER myuser;
psql -U xpo -d webapp -h localhost



brew services start postgresql@14
brew services list
```


