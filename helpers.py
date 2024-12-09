# helpers.py

def search_books(query, books):
    query = query.lower()
    return [book for book in books if query in book["title"].lower() or query in book["author"].lower()]

def paginate(items, page, per_page):
    start = (page - 1) * per_page
    end = start + per_page
    return items[start:end], len(items)
