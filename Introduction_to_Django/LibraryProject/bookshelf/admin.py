from django.contrib import admin
from .models import Book


# Register the Book model
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')  # Columns in the list view
    search_fields = ('title', 'author')  # Enable search by title and author
    list_filter = ('publication_year',)  # Add a filter for publication year
