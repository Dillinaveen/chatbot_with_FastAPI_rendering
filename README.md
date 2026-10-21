Secure FastAPI Chatbot
A modular chatbot backend built with FastAPI, featuring JWT-based
authentication, a protected chat API, WebSocket messaging, configurable
settings, and application logging.
Features
1) FastAPI REST API for authentication and chat endpoints.
2) JWT authentication using OAuth2 password-flow conventions.
3) Protected WebSocket chat at /chat/ws, with a token supplied as
  a query parameter.
4) Hugging Face Transformers chatbot model, configured through
  MODEL_NAME (default: facebook/blenderbot-400M-distill).
5) Centralized configuration using environment variables and
  Pydantic Settings.
6) Logging for application events and errors.
7) Modular structure separating configuration, security, model
  handling, routes, and utilities.