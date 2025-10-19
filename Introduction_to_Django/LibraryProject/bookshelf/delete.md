# Delete Operation

# Command:
>>> from library.models import Book
>>> book = Book.objects.get(title="Nineteen Eighty-Four")
>>> book.delete()
>>> Book.objects.all()

# Expected Output:
(<Book: Nineteen Eighty-Four by George Orwell (1949)>,)
(0)  # or an empty queryset
<QuerySet []>