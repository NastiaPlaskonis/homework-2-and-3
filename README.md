# Homework 2-3 – FastAPI projects 

### Author
**Anastasia Plaskonis**

In this repository, you'll find two related assignments completed for the Architecture of IT Solutions course at the Ukrainian Catholic University. Both focus on building and containerizing a FastAPI-based microservice system using Podman.

---

## Project breakdown

### Part 1: microservices with authentication (Homework 2)

The first stage focuses on building a Python system with modular responsibilities, where services interact through RESTful APIs.

#### Implemented services:

- **Client service** (`client_interface.py`)  
  Handles incoming requests and applies Bearer Token validation.
  
- **Business service** (`business_logic.py`)  
  Mimics data processing logic that simulates heavy computation.

- **Database service** (`db_service.py`)  
  Simple in-memory store with GET/POST endpoints.

These services function independently but are connected logically through internal calls initiated by the client service.

**Key learning areas**:
- Splitting logic across dedicated services  
- Using token-based access mechanisms  
- Enabling inter-process communication within Python apps

More details: [`README_2.md`](README_2.md)

---

### Part 2: running services in containers (Homework 3)

In the follow-up assignment, we shift focus from implementation to deployment — each FastAPI service is containerized and launched via Podman and `podman-compose`.

#### Deployment features:
- A separate `Dockerfile` is created for each microservice
- Services are connected via a shared `backend` network
- The system is launched using `podman-compose up`

**Skills practiced**:
- Building minimal container images for FastAPI apps  
- Managing services with Podman CLI  
- Testing endpoints and flows from inside a containerized setup

More details: [`README_3.md`](README_3.md)

---
