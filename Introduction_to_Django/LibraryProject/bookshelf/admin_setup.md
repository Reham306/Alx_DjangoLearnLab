### Django Admin Integration for Book Model

**Steps Taken:**

1. Registered the `Book` model in `bookshelf/admin.py`:
    ```python
    from django.contrib import admin
    from .models import Book

    @admin.register(Book)
    class BookAdmin(admin.ModelAdmin):
        list_display = ('title', 'author', 'publication_year')
        search_fields = ('title', 'author')
        list_filter = ('publication_year',)
    ```

2. Enabled admin functionalities for the `Book` model:
    - Displayed `title`, `author`, and `publication_year` in the list view.
    - Added search capabilities for `title` and `author`.
    - Configured list filters for `publication_year`.

3. Verified the setup via the Django admin interface:
    - Successfully added, edited, and deleted `Book` entries.
    - Tested search functionality by searching for specific titles and authors.
    - Filtered books by `publication_year` using the sidebar.

**Screenshots:**
Include screenshots of the list view, search results, and filter functionality.
