from flask import Flask, jsonify, request
from routes import users_bp

app = Flask(__name__)
app.register_blueprint(users_bp)
# Sample data
books = [
    {"id": 1, "title": "Book 1", "author": "Author 1"},
    {"id": 2, "title": "Book 2", "author": "Author 2"},
    {"id": 4, "title": "Book 2", "author": "Author 2"}
]

# Run the Flask application
if __name__ == '__main__':
    app.run()

