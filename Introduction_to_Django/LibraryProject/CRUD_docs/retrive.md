### Retrieve Operation
**Command:**
```python
retrieved_book = Book.objects.get(id=book.id)
print(retrieved_book.title, retrieved_book.author, retrieved_book.publication_year)

---

#### **3. Update the Book**
```python
# Update the book's title
retrieved_book.title = "Nineteen Eighty-Four"
retrieved_book.save()
print(retrieved_book.title)
