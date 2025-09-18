from django.shortcuts import render, redirect, get_object_or_404
from .models import Book
from django.contrib.auth.decorators import login_required

# List all books
@login_required
def book_list(request):
    books = Book.objects.all()
    return render(request, "book_list.html", {"books": books})

# Create a new entry
@login_required
def book_create(request):
    if request.method == "POST":
        bookid = request.POST["bookid"]
        name = request.POST["name"]
        author = request.POST["author"]
        price = request.POST["price"]

        Book.objects.create(bookid=bookid, name=name, author=author, price=price)
        return redirect("book_list")

    return render(request, "book_form.html")

# Update existing entries
@login_required
def book_update(request, pk):
    book = get_object_or_404(Book, pk=pk)

    if request.method == "POST":
        book.bookid = request.POST["bookid"]
        book.name = request.POST["name"]
        book.author = request.POST["author"]
        book.price = request.POST["price"]
        book.save()
        return redirect("book_list")

    return render(request, "book_form.html", {"book": book})

# Delete a book entry
@login_required
def book_delete(request, pk):
    book = get_object_or_404(Book, pk=pk)

    if request.method == "POST":
        book.delete()
        return redirect("book_list")

    return render(request, "book_confirm_delete.html", {"book": book})
