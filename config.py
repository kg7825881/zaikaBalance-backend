import os

class Config:
    DEBUG = os.environ.get("FLASK_DEBUG", False)
    TESTING = os.environ.get("FLASK_TESTING", False)
    SECRET_KEY = os.environ.get("SECRET_KEY", "super-secret-key")

    # Optional CORS setup if you want to enforce it here
    CORS_ORIGINS = [
        "http://localhost:3000",
        "https://your-production-frontend.com"
    ]

    # Optional: future configs like DB_URI, mail config, etc. can go here
