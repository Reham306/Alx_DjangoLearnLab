### Update Operation
**Command:**
```python
retrieved_book.title = "Nineteen Eighty-Four"
retrieved_book.save()
print(retrieved_book.title)

---

#### **4. Delete the Book**
```python
# Delete the book instance
retrieved_book.delete()

# Verify deletion
print(Book.objects.all().count())  # Expected output: 0
