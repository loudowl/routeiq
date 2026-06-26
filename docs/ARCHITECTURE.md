# RouteIQ Architecture Document

## 1. Tech Stack

### Frontend
- **Framework**: React (Next.js) 13
- **State Management**: Redux 8
- **Styling**: Tailwind CSS 3
- **Charts**: Chart.js 3

### Backend
- **Framework**: FastAPI 0.95
- **Task Queue**: Celery 5
- **Classifier Runtime**: ONNX Runtime 1.13
- **Caching**: Redis 6

### Database
- **Primary**: PostgreSQL 14
- **In-memory**: Redis 6 (for rate limiting and caching)

### Hosting & Infrastructure
- **Proxy Server**: Fly.io
- **Containerization**: Docker 24
- **Orchestration**: Kubernetes 1.28
- **CI/CD**: GitHub Actions

### Mobile
- **Framework**: React Native 0.72
- **iOS Support**: Swift 5

### Payment & Billing
- **Payments**: Stripe API (latest)

### ML Models
- **On-device Classifier**: DistilBERT fine-tuned, deployed with ONNX
- **Local Model**: Llama 3.1 8B via Ollama

## 2. Project Structure

```
RouteIQ/
├── backend/
│   ├── app/
│   │   ├── main.py
│   │   ├── routes/
│   │   │   ├── api.py
│   │   │   ├── auth.py
│   │   ├── models/
│   │   │   ├── user.py
│   │   │   ├── request.py
│   │   ├── services/
│   │   │   ├── routing.py
│   │   │   ├── classifier.py
│   │   ├── utils/
│   │   │   ├── logger.py
│   │   │   ├── redis_client.py
│   ├── celery_tasks/
│   │   ├── evaluator.py
│   │   ├── billing.py
├── frontend/
│   ├── pages/
│   │   ├── index.js
│   │   ├── dashboard.js
│   ├── components/
│   │   ├── Navbar.js
│   │   ├── Chart.js
│   ├── store/
│   │   ├── index.js
│   │   ├── reducers/
│   │   ├── actions/
│   ├── styles/
│       ├── global.css
├── mobile/
│   ├── App.js
│   ├── components/
│   ├── screens/
│   ├── store/
│   ├── styles/
├── infra/
│   ├── Dockerfile
│   ├── docker-compose.yml
│   ├── k8s/
│       ├── deployment.yaml
│       ├── service.yaml
├── scripts/
│   ├── deploy.sh
│   ├── setup_db.py
```

## 3. API Design

### Proxy Endpoint
- **Method**: POST
- **Path**: `/v1/chat/completions`
- **Request**: 
  ```json
  {
    "model": "string",
    "prompt": "string",
    "max_tokens": "integer"
  }
  ```
- **Response**:
  ```json
  {
    "id": "string",
    "object": "chat.completion",
    "created": "integer",
    "model": "string",
    "choices": [
      {
        "text": "string",
        "index": "integer",
        "logprobs": null,
        "finish_reason": "string"
      }
    ]
  }
  ```

### Dashboard Endpoint
- **Method**: GET
- **Path**: `/api/dashboard/metrics`
- **Response**:
  ```json
  {
    "cost_per_request": "float",
    "model_distribution": "object",
    "quality_scores": "object",
    "projected_savings": "float"
  }
  ```

### Authentication
- **Method**: POST
- **Path**: `/api/auth/login`
- **Request**:
  ```json
  {
    "username": "string",
    "password": "string"
  }
  ```
- **Response**:
  ```json
  {
    "token": "string"
  }
  ```

## 4. Data Models

### User Table
- **id**: UUID
- **username**: VARCHAR(255)
- **password_hash**: VARCHAR(255)
- **email**: VARCHAR(255)
- **created_at**: TIMESTAMP

### Request Log Table
- **id**: UUID
- **user_id**: UUID (FK)
- **model_used**: VARCHAR(255)
- **tokens**: INTEGER
- **latency**: FLOAT
- **estimated_cost**: FLOAT
- **created_at**: TIMESTAMP

### Evaluation Table
- **id**: UUID
- **request_id**: UUID (FK)
- **quality_score**: FLOAT
- **evaluation_date**: TIMESTAMP

## 5. Authentication

### Approach
- **JWT (JSON Web Tokens)**: Securely manage user sessions.
- **Flow**:
  1. User logs in with credentials.
  2. Server verifies credentials and issues a JWT.
  3. JWT is sent with every request in the `Authorization` header.
  4. Server verifies JWT for protected routes.

## 6. State Management

- **Redux**: Centralized store for managing application state.
- **Slices**: Divide state into logical slices for user data, model metrics, and settings.
- **Asynchronous Actions**: Use `redux-thunk` for async operations like API calls.

## 7. Key Dependencies

### Backend
- **FastAPI**: Web framework for building APIs.
- **SQLAlchemy**: ORM for database operations.
- **Celery**: Task queue for background tasks.
- **ONNX Runtime**: Run the task complexity classifier.

### Frontend
- **Next.js**: React framework for server-side rendering.
- **Redux**: State management.
- **Tailwind CSS**: Utility-first CSS framework.
- **Chart.js**: Library for creating charts.

### Mobile
- **React Native**: Cross-platform mobile app development.
- **Redux**: State management for React Native.

### Payments
- **Stripe**: Payment processing and billing.

## 8. Deployment

### Recommended Hosting
- **Proxy Server**: Deploy on Fly.io for global edge distribution.
- **Dashboard**: Host on Vercel for optimized Next.js deployment.
- **Mobile App**: Distribute via Apple App Store and Google Play Store.

### CI/CD Approach
- **GitHub Actions**:
  - **Build**: Automated builds for each push to the repository.
  - **Test**: Run unit and integration tests.
  - **Deploy**: Deploy to Fly.io and Vercel on successful builds.
- **Kubernetes**: Use for container orchestration to ensure high availability and scalability.

This architecture ensures RouteIQ is robust, scalable, and optimized for performance, providing seamless integration and significant cost savings for enterprises.