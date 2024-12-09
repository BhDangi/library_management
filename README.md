# library_management

# Library Management System API

## Overview
This project is a RESTful API for managing books and members in a library. Built using Flask, it includes features for CRUD operations, search functionality, and pagination.

## Features
- **Books Management**: Add, update, retrieve, and delete books.
- **Members Management**: Add, update, retrieve, and delete library members.
- **Authentication**: Basic authentication for secure operations.
- **Pagination**: Fetch paginated results for large datasets.

## How to Run the Project

### Prerequisites
Ensure you have the following installed on your system:
- Python 3.x
- `pip` (Python package manager)

### Steps to Run

1. **Clone the Repository**:
   ```bash
   git clone <repository-url>
   cd <repository-folder>

2. # Create virtual environment
python -m venv venv

# Activate virtual environment (Linux/Mac)
source venv/bin/activate

# Activate virtual environment (Windows)
venv\Scripts\activate

pip install flask

3. **Run the Server**:
   ```bash
   python app.py
   ```
   The API will run on `http://127.0.0.1:5000`.

4. **Testing the API**:
   Use tools like Postman or `curl` to test endpoints.

## API Endpoints
- **Books**
  - `POST /books`: Add a new book.
  - `GET /books`: Get all books (supports search and pagination).
  - `GET /books/get/<book_id>`: Get a specific book.
  - `PUT /books/put/<book_id>`: Update book details.
  - `DELETE /books/delete/<book_id>`: Delete a book.
- **Members**
  - `POST /members`: Add a new member.
  - `GET /members`: Get all members.
  - `GET /members/get/<member_id>`: Get a specific member.
  - `PUT /members/put/<member_id>`: Update member details.
  - `DELETE /members/delete/<member_id>`: Delete a member.

## Design Choices
- **Framework**: Flask was chosen for its simplicity and extensibility.
- **Modularity**: Separated helpers, authentication, and model data for maintainability.
- **Authentication**: Basic authentication ensures secure access to sensitive endpoints.

## Assumptions and Limitations
- Authentication is basic and can be extended using OAuth or JWT for production.
- Data is stored in-memory, so it resets when the server restarts.
- No database integration, assuming small-scale library usage.

## Future Enhancements
- Integrate with a database (e.g., SQLite, PostgreSQL).
- Enhance authentication using JWT.
- Add user roles and permissions (e.g., admin, member).

## Author
BHAVESH DANGI  
[GitHub Profile](https://[github.com/your-profile](https://github.com/BhDangi/library_management))  

 
