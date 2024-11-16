# Create Operation

## Command:
```python
from bookshelf.models import Book
book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)
print(book)


#Output
1984 by George Orwell (1949)

---

### **2. Retrieve Operation (`retrieve.md`)**

```markdown
# Retrieve Operation

## Command:
```python
from bookshelf.models import Book
books = Book.objects.all()
for book in books:
    print(book.title, book.author, book.publication_year)
