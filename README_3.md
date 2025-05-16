# FastAPI microservices with Podman orchestration

### Author
**Anastasia Plaskonis**

This project showcases how to containerize and deploy a microservice-based architecture using FastAPI, Podman, and Podman Compose. It extends the functionality built in the previous homework assignment by introducing multi-container coordination, token-based security, and internal API interactions.

## System components

The application is composed of three independent services, each running on a dedicated port:

### `client_interface.py` - client interface (port 8000)
- Main entry point for incoming requests
- Protected with a Bearer Token
- Coordinates requests between business logic and storage services

### `business_logic.py` – business logic (port 8001)
- Simulates a computationally intensive process
- Handles transformation of input data

### `db_service.py` – in-memory database (port 8002)
- Offers a basic RESTful API for storing and retrieving data
- Works without persistent storage

---

## Authorization

The `/run` endpoint of the client service expects a token:
```
Authorization: Bearer Secret123
```

Requests without this token will be rejected.

---

## Containerization overview

Each service has its own build configuration:

- `Dockerfile.cs` – for the client service
- `Dockerfile.bs` – for the business logic
- `Dockerfile.dbs` – for the database service

All services are described in the `podman-compose.yml` file and share a common virtual network called `backend`.

---

## Environment setup

### Prerequisites:
- Podman
- Podman Compose

### Installation on macOS:

```bash
brew install podman podman-compose
podman machine init
podman machine start
```

## Python dependencies

Make sure the following packages are installed before running the services:

- FastAPI
- Uvicorn
- Requests

You can install them using:

```bash
pip install -r requirements.txt
```

## Running the project

To build all containers and bring up the entire system, run:

```bash
podman-compose up --build
```

The logs for each container will appear in your terminal window once the system is active.

## How to test the system

### 1. Check health endpoints

```bash
curl http://localhost:8000/health
curl http://localhost:8001/health
curl http://localhost:8002/health
```

All should respond with:

```json
{ "status": "OK" }
```

---

### 2. Store sample data in the DB

```bash
curl -X POST http://localhost:8002/save \
     -H "Content-Type: application/json" \
     -d '{"text": "Hello!"}'
```

---

### 3. Trigger orchestration via client

```bash
curl -X POST http://localhost:8000/run \
     -H "Authorization: Bearer Secret123"
```

Expected result:

```json
{
  "result": {
    "original": {
      "text": "Hello!"
    },
    "processed": true
  }
}
```

---

## Shutting everything down

When you're done, stop and remove all containers with:

```bash
podman-compose down
```