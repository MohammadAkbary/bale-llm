"""
Wrapper for Render deployment
Gunicorn looks for 'app:app' in app.py by default
This file imports the Flask app from main.py
"""

from main import app

if __name__ == '__main__':
    app.run()
