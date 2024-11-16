### Delete Operation
**Command:**
```python
retrieved_book.delete()
print(Book.objects.all().count())

---

### Step 5: Create `CRUD_operations.md`
Aggregate the operations:
```markdown
# CRUD Operations

## Create
```python
from bookshelf.models import Book
book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)
print(book)
