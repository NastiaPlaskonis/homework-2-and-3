# FastAPI Microservices 

### Author
**Anastasia Plaskonis**

This project showcases a simple microservice-based application using Python and FastAPI. It consists of three separate services that communicate over HTTP and form a basic processing pipeline. The gateway service includes token-based authorization to protect access.

---

## Objective

The goal of this assignment was to explore:
1. The fundamentals of microservice design.
2. How to run and organize multiple FastAPI apps as independent services.
3. Service orchestration and data transfer via HTTP.
4. A basic security layer using token authentication.

---

## System components

### 1. Database service (`db_service.py`)
Acts as a simple in-memory data store using Python lists.

**Available endpoints:**
- `POST /save`: stores data received in JSON format.
- `GET /get`: retrieves all stored entries.
- `GET /health`: basic health check.
- `GET /`: brief description of the service.

---

### 2. Business logic service (`business_logic.py`)
Processes data (e.g., simulates heavy computation with a delay).

**Available endpoints:**
- `POST /process`: processes incoming data (uses `time.sleep(2)`).
- `GET /health`: confirms the service is running.
- `GET /`: description endpoint.

---

### 3. Client (Gateway) service (`client_interface.py`)
Handles all incoming external requests and delegates work to the other services. Secured with a static token.

**Available endpoints:**
- `POST /run`: initiates the process flow (requires token).
- `GET /health`: service status.
- `GET /`: short description.

---

## Access control

The `/run` endpoint is restricted by token-based authentication.

**Token in code:**
```python
APP_TOKEN = "Secret123"
```

**Header format (required):**
```
Authorization: Bearer Secret123
```

Requests without this header will be rejected with `401 Unauthorized`.

---

## Workflow overview

```text
User
  ↓
Client service (/run)
  → fetches data from Database Service (/get)
  → sends data to Business Logic Service (/process)
  → stores result back to Database Service (/save)
  ↓
Returns processed response to user
```

---

## Example requests (Using `curl`)

### 1. Add data to the database:

```bash
curl -X POST http://localhost:8002/save \
     -H "Content-Type: application/json" \
     -d '{"text": "Hello!"}'
```

### 2. Start the orchestration via client service:

```bash
curl -X POST http://localhost:8000/run \
     -H "Authorization: Bearer Secret123"
```

### Response example:

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

## Service health checks

Each service responds to:
- `GET /` with a service description.
- `GET /health` with:
```json
{"status": "OK"}
```

Test with:
```bash
curl http://localhost:8000/health
curl http://localhost:8001/health
curl http://localhost:8002/health
```

---

## Setup and running the project

### 1. Create and activate a virtual environment

```bash
python -m venv venv
source venv/bin/activate  
```

### 2. Install project dependencies

```bash
pip install -r requirements.txt
```

### 3. Launch services in separate terminals

**Terminal 1 – Start database service:**
```bash
uvicorn db_service:app --port 8002
```

**Terminal 2 – Start business logic service:**
```bash
uvicorn business_logic:app --port 8001
```

**Terminal 3 – Start client service:**
```bash
uvicorn client_interfacee:app --port 8000
```

---

## Dependencies

Listed in `requirements.txt`:
```
fastapi
uvicorn
requests
```

Install using:
```bash
pip install -r requirements.txt
```

