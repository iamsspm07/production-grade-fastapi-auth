# 🔐 FastAPI JWT Authentication Service

> Enterprise-grade authentication microservice built with FastAPI, PostgreSQL, JWT, and Clean Architecture principles.

A scalable, production-ready authentication API implementing stateless JWT-based authentication, Argon2 password hashing, and layered repository-service architecture. Designed following enterprise backend standards for security, maintainability, and extensibility.

---

## 📌 Table of Contents

- [Overview](#overview)
- [Architecture](#architecture)
- [Tech Stack](#tech-stack)
- [Key Features](#key-features)
- [Security Design](#security-design)
- [Project Structure](#project-structure)
- [Installation & Setup](#installation--setup)
- [Environment Configuration](#environment-configuration)
- [API Endpoints](#api-endpoints)
- [Authentication Flow](#authentication-flow)
- [Production Considerations](#production-considerations)
- [Future Enhancements](#future-enhancements)
- [Author](#author)
- [License](#license)

---

# 📖 Overview

This project is a **production-grade authentication service** built using FastAPI and PostgreSQL.  
It follows a structured layered architecture:

Controller → Service → Repository → Database

The system ensures:

- Stateless authentication
- Secure password storage
- Layered separation of concerns
- Scalability for microservice deployment
- Clean and maintainable codebase

This repository demonstrates backend engineering best practices suitable for enterprise systems.

---

# 🏗 Architecture

The project follows a **Clean Architecture pattern** separating business logic, data access, and API layers.

```
Client Request
      ↓
FastAPI Controller Layer
      ↓
Service Layer (Business Logic)
      ↓
Repository Layer (Data Access)
      ↓
PostgreSQL Database
```

### Architectural Principles Applied

- Separation of Concerns
- Dependency Injection
- Repository Pattern
- Service Abstraction
- Stateless Authentication Design
- Modular Package Structure

---

# 🛠 Tech Stack

| Layer | Technology |
|-------|------------|
| Backend Framework | FastAPI |
| Database | PostgreSQL |
| ORM | SQLAlchemy |
| Authentication | JWT (HS256) |
| Password Hashing | Argon2 (Passlib) |
| Validation | Pydantic |
| ASGI Server | Uvicorn |

---

# 🚀 Key Features

- User Registration
- Secure Login with JWT Access Token
- Argon2 Password Hashing
- Update User Profile
- Delete User
- Fetch Users
- Custom Exception Handling
- Dependency-Injected DB Sessions
- Layered Architecture
- Unique Constraint Enforcement (username & email)
- Token Expiration Control

---

# 🔐 Security Design

This system implements multiple security best practices:

### 1️⃣ Password Security
- Passwords are hashed using **Argon2**
- Plaintext passwords are never stored
- Secure verification using passlib context

### 2️⃣ JWT Authentication
- Stateless authentication model
- Access token expiration enforced
- Token signed using HS256 algorithm
- No session storage required

### 3️⃣ Database Protection
- Unique constraints on username & email
- ORM-based query building to reduce injection risk
- Controlled session lifecycle management

### 4️⃣ Exception Handling
- Custom HTTP exceptions
- Proper status code usage
- Controlled error exposure

---

# 📂 Project Structure

```
A_DatabasePackage/
    └── login_database_connection.py

B_EntityPackage/
    └── login_entity_master.py

C_SchemaPackage/
    └── request.py

D_CustomExceptionPackage/
    └── login_custom_exception_handling.py

E_SecurityPackage/
    └── login_auth_jwt.py

F_RepositoryPackage/
    └── login_repository.py

G_ServiceFunctionPackage/
    └── login_service_function.py

H_ServiceImplementationPackage/
    └── login_service_implementation.py

I_ControllerPackage/
    └── logic_controller.py
```

---

# ⚙ Installation & Setup

## 1️⃣ Clone Repository

```bash
git clone https://github.com/your-username/fastapi-jwt-auth-system.git
cd fastapi-jwt-auth-system
```

## 2️⃣ Create Virtual Environment

```bash
python -m venv venv
```

Activate environment:

Windows:
```bash
venv\Scripts\activate
```

Mac/Linux:
```bash
source venv/bin/activate
```

## 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

## 4️⃣ Configure Environment Variables

Create a `.env` file:

```
SECRET_KEY=your_secure_secret_key
DB_HOST=localhost
DB_PORT=5432
DB_NAME=jwt_auth
DB_USER=postgres
DB_PASSWORD=your_password
```

## 5️⃣ Run Application

```bash
uvicorn I_ControllerPackage.logic_controller:app --reload
```

Application runs at:

```
http://127.0.0.1:8000
```

Interactive API Docs:

```
http://127.0.0.1:8000/docs
```

---

# 🌐 API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/register` | Register new user |
| POST | `/login` | Authenticate user & generate JWT |
| GET | `/users` | Fetch all users |
| POST | `/users/code` | Fetch user by credentials |
| PUT | `/update` | Update user |
| DELETE | `/delete` | Delete user |

---

# 🔄 Authentication Flow

### Registration
1. User submits credentials
2. Password is hashed using Argon2
3. User record stored in PostgreSQL

### Login
1. User submits credentials
2. Password verified against hashed value
3. JWT access token generated
4. Token returned to client

### Subsequent Requests
- Client sends token in Authorization header
- Server validates token signature and expiration

---

# 🏭 Production Considerations

To deploy in production, consider:

- Use environment variables for secrets
- Enable HTTPS
- Implement refresh tokens
- Add role-based access control
- Integrate logging (e.g., Loguru)
- Add monitoring (Prometheus/Grafana)
- Containerize using Docker
- Deploy via CI/CD pipeline
- Add unit & integration tests

---

# 📈 Future Enhancements

- Refresh Token Mechanism
- Role-Based Authorization
- OAuth2PasswordBearer Integration
- Redis Token Blacklisting
- Rate Limiting
- Multi-Factor Authentication (MFA)
- API Gateway Integration
- Docker + Kubernetes Deployment
- Unit Testing with Pytest
- Swagger Security Integration

---

# 👨‍💻 Author

**Sujit Shibaprasad Maity**

Backend Engineer | AI/ML Enthusiast  
Focused on building scalable, secure, and production-ready backend systems.

---

## ⭐ If You Found This Useful

Feel free to fork, contribute, or star the repository.
