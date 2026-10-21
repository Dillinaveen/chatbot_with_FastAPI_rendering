Secure FastAPI Chatbot
A modular chatbot backend built with FastAPI, featuring JWT-based
authentication, a protected chat API, WebSocket messaging, configurable
settings, and application logging.
Features
- FastAPI REST API for authentication and chat endpoints.
- JWT authentication using OAuth2 password-flow conventions.
- Protected WebSocket chat at /chat/ws, with a token supplied as
  a query parameter.
- Hugging Face Transformers chatbot model, configured through
  MODEL_NAME (default: facebook/blenderbot-400M-distill).
- Centralized configuration using environment variables and
  Pydantic Settings.
- Logging for application events and errors.
- Modular structure separating configuration, security, model
  handling, routes, and utilities.