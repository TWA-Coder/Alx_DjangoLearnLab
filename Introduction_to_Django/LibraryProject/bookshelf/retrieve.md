# Retrieve Operation

# Command:
>>> from library.models import Book
>>> book = Book.objects.get(title="1984")
>>> book.title, book.author, book.publication_year

# Expected Output:
('1984', 'George Orwell', 1949)