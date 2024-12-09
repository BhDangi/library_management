# Mock database
books = [
    {"id": 1, "title": "To Kill a Mockingbird", "author": "Harper Lee"},
    {"id": 2, "title": "1984", "author": "George Orwell"},
    {"id": 3, "title": "The Great Gatsby", "author": "F. Scott Fitzgerald"},
    {"id": 4, "title": "The Catcher in the Rye", "author": "J.D. Salinger"},
    {"id": 5, "title": "Moby-Dick", "author": "Herman Melville"}
]

members = [
    {"id": 1, "name": "Alice Johnson", "email": "alice.johnson@example.com"},
    {"id": 2, "name": "Bob Smith", "email": "bob.smith@example.com"},
    {"id": 3, "name": "Charlie Brown", "email": "charlie.brown@example.com"},
    {"id": 4, "name": "Diana Prince", "email": "diana.prince@example.com"},
    {"id": 5, "name": "Edward Norton", "email": "edward.norton@example.com"}
]

# Unique IDs for books and members
book_id_counter = len(books) + 1
member_id_counter = len(members) + 1
