from django.contrib import admin

# Register your models here.
from .models import Book

# Custom configuration for Book model in the admin interface
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    # Fields to display in the admin list view
    list_display = ('title', 'author', 'publication_year')

    # Filters in the sidebar for easy navigation
    list_filter = ('author', 'publication_year')

    # Enable search functionality for these fields
    search_fields = ('title', 'author')

    # Optional: Define how records are ordered
    ordering = ('title',)

    # Optional: Set the number of entries per page
    list_per_page = 20