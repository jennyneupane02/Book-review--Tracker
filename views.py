from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from .models import Book, Review

def home(request):
    books = Book.objects.all()
    reviews = Review.objects.select_related("book", "user").all()
    return render(request, "reviews/home.html", {
        "books": books,
        "reviews": reviews
    })


def add_review(request):
    if request.method == "POST":
        title = request.POST["title"]
        author = request.POST["author"]
        rating = int(request.POST["rating"])
        comment = request.POST["comment"]

        # This creates a simple default user for classroom testing.
        user, created = User.objects.get_or_create(username="student")

        book = Book.objects.create(
            title=title,
            author=author
        )

        Review.objects.create(
            user=user,
            book=book,
            rating=rating,
            comment=comment
        )

        return redirect("/")

    return render(request, "reviews/add_review.html")
