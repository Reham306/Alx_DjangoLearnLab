### Retrieve Operation

**Command:**
```python
retrieved_book = Book.objects.get(id=book.id)
print(retrieved_book.title, retrieved_book.author, retrieved_book.publication_year)


Save the file and exit the editor.

---

#### **4. Verify the File**
Ensure the file has been created correctly and has appropriate permissions:
```bash
ls retrieve.md
chmod 644 retrieve.md
