from flask import Blueprint, jsonify, request

users_bp = Blueprint('books', __name__)

# GET /books - Retrieve all books
@users_bp.route('/books', methods=['GET'])
def get_books():
    return jsonify(books)

# GET /books/<id> - Retrieve a specific book
@users_bp.route('/books/<int:book_id>', methods=['GET'])
def get_book(book_id):
    book = next((book for book in books if book["id"] == book_id), None)
    if book:
        return jsonify(book)
    else:
        return jsonify({"error": "Book not found"}), 404

# POST /books - Create a new book
@users_bp.route('/books', methods=['POST'])
def create_book():
    new_book = {
        "id": len(books) + 1,
        "title": request.json.get('title'),
        "author": request.json.get('author')
    }
    books.append(new_book)
    return jsonify(new_book), 201

# PUT /books/<id> - Update a specific book
@users_bp.route('/books/<int:book_id>', methods=['PUT'])
def update_book(book_id):
    book = next((book for book in books if book["id"] == book_id), None)
    if book:
        book["title"] = request.json.get('title')
        book["author"] = request.json.get('author')
        return jsonify(book)
    else:
        return jsonify({"error": "Book not found"}), 404

# DELETE /books/<id> - Delete a specific book
@users_bp.route('/books/<int:book_id>', methods=['DELETE'])
def delete_book(book_id):
    global books
    books = [book for book in books if book["id"] != book_id]
    return jsonify({"message": "Book deleted"})