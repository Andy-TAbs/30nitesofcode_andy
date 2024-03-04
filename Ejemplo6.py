# Write code below 💖
books = ['Zero to One', 'The Lean Startup', 'The mom Test', 'Make It Stick' 'Life in Code']
print(books)
Add = str(input('Add the new Book: '))
books.append(Add)
print(books)
Del = int(input('Instert the number of the book you want to delete(0,5): '))
books.pop(Del)
print(books)
Del1 = str(input('Instert the name of the book you want to delete: '))
books.remove(Del1)

print(books)
