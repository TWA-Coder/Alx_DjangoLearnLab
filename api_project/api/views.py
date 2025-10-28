# api/views.py
from rest_framework import viewsets, permissions
from .models import Book
from .serializers import BookSerializer

class BookViewSet(viewsets.ModelViewSet):
    """
    A viewset for managing Book instances.
    Only authenticated users can create, update, or delete books.
    Everyone can view (GET) books.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
