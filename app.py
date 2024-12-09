from flask import Flask, request, jsonify
from models import books, members, book_id_counter, member_id_counter
from authentication import authenticate
from helpers import search_books, paginate

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to the Library Management System API!"


# Add a book (POST)
@app.route('/books', methods=['POST'])
def add_book():
    global book_id_counter
    if not authenticate(request):
        return jsonify({"error": "Unauthorized"}), 401
    
    data = request.get_json()
    new_book = {
        "id": book_id_counter,
        "title": data["title"],
        "author": data["author"],
        "available": True
    }
    books.append(new_book)
    book_id_counter += 1
    return jsonify(new_book), 201


# Get all books (GET)
@app.route('/books', methods=['GET'])
def get_books():
    query = request.args.get('query', '')
    page = int(request.args.get('page', 1))
    per_page = int(request.args.get('per_page', 5))
    
    result = search_books(query, books) if query else books
    paginated_books, total = paginate(result, page, per_page)
    return jsonify({"books": paginated_books, "total": total}), 200

# Get a book by ID (GET)
@app.route('/books/get/<int:book_id>', methods=['GET'])
def get_book(book_id):
    for book in books:
        if book["id"] == book_id:
            return jsonify(book), 200
    return jsonify({"error": "Book not found"}), 404


# Update a book (PUT)
@app.route('/books/put/<int:book_id>', methods=['PUT'])
def update_book(book_id):
    if not authenticate(request):
        return jsonify({"error": "Unauthorized"}), 401

    data = request.get_json()
    for book in books:
        if book["id"] == book_id:
            book.update(data)
            return jsonify(book), 200
    return jsonify({"error": "Book not found"}), 404


# Delete a book (DELETE)
@app.route('/books/delete/<int:book_id>', methods=['DELETE'])
def delete_book(book_id):
    if not authenticate(request):
        return jsonify({"error": "Unauthorized"}), 401

    global books
    books = [book for book in books if book["id"] != book_id]
    return jsonify({"message": "Book deleted"}), 200


# Add a member (POST)
@app.route('/members', methods=['POST'])
def add_member():
    global member_id_counter
    if not authenticate(request):
        return jsonify({"error": "Unauthorized"}), 401

    data = request.get_json()
    new_member = {
        "id": member_id_counter,
        "name": data["name"],
        "email": data["email"]
    }
    members.append(new_member)
    member_id_counter += 1
    return jsonify(new_member), 201


# Get all members (GET)
@app.route('/members', methods=['GET'])
def get_members():
    return jsonify(members), 200


# Get a member by ID (GET)
@app.route('/members/get/<int:member_id>', methods=['GET'])
def get_member(member_id):
    for member in members:
        if member["id"] == member_id:
            return jsonify(member), 200
    return jsonify({"error": "Member not found"}), 404


# Update a member (PUT)
@app.route('/members/put/<int:member_id>', methods=['PUT'])
def update_member(member_id):
    if not authenticate(request):
        return jsonify({"error": "Unauthorized"}), 401

    data = request.get_json()
    for member in members:
        if member["id"] == member_id:
            member.update(data)
            return jsonify(member), 200
    return jsonify({"error": "Member not found"}), 404


# Delete a member (DELETE)
@app.route('/members/delete/<int:member_id>', methods=['DELETE'])
def delete_member(member_id):
    if not authenticate(request):
        return jsonify({"error": "Unauthorized"}), 401

    global members
    members = [member for member in members if member["id"] != member_id]
    return jsonify({"message": "Member deleted"}), 200


if __name__ == "__main__":
    app.run(debug=True)
