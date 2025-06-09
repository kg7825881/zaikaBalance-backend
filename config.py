import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'your-secret-key'
    JWT_SECRET = os.environ.get('JWT_SECRET') or 'your-jwt-secret'
    # Add other config variables as needed