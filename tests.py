import unittest
from django.test import TestCase
from django.contrib.auth.models import User
from .models import Book, Review
from .utils import calculate_average_rating, is_valid_rating


# Python unit tests for logic outside Django models and views.
class PythonLogicTests(unittest.TestCase):

    def test_average_rating_normal_list(self):
        # This checks that the average rating is calculated correctly for normal input.
        self.assertEqual(calculate_average_rating([5, 4, 3]), 4)

    def test_valid_rating_true(self):
        # This checks that a rating between 1 and 5 is accepted as valid.
        self.assertTrue(is_valid_rating(5))

    def test_valid_rating_false(self):
        # This checks that an invalid rating is rejected.
        self.assertFalse(is_valid_rating(8))

    def test_empty_rating_list_raises_error(self):
        # This checks bad input and proves that the function fails safely.
        with self.assertRaises(ValueError):
            calculate_average_rating([])


# Django model and client tests for the Book Review Tracker app.
class ReviewTestCase(TestCase):

    def setUp(self):
        # Create sample user, book, and review before each test runs.
        self.user = User.objects.create_user(username="jeni", password="test123")

        self.book = Book.objects.create(
            title="Atomic Habits",
            author="James Clear"
        )

        self.review = Review.objects.create(
            user=self.user,
            book=self.book,
            rating=5,
            comment="This book was very helpful."
        )

    def test_book_fields_saved_correctly(self):
        # This checks that the book title and author are saved correctly.
        self.assertEqual(self.book.title, "Atomic Habits")
        self.assertEqual(self.book.author, "James Clear")

    def test_book_model_method(self):
        # This checks that the full_title model method returns the expected text.
        self.assertEqual(self.book.full_title(), "Atomic Habits by James Clear")

    def test_review_model_method(self):
        # This checks that a rating of 5 is treated as a positive review.
        self.assertTrue(self.review.is_positive_review())

    def test_foreign_key_relationship(self):
        # This verifies the relationship between User, Book, and Review.
        self.assertEqual(self.review.user.username, "jeni")
        self.assertEqual(self.review.book.title, "Atomic Habits")

    def test_homepage_status_code(self):
        # This checks that the homepage loads successfully.
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    def test_homepage_content(self):
        # This checks that the book title appears in the page content.
        response = self.client.get("/")
        self.assertIn("Atomic Habits", response.content.decode())

    def test_add_review_page_status_code(self):
        # This checks that the add review page loads successfully.
        response = self.client.get("/add/")
        self.assertEqual(response.status_code, 200)

    def test_add_review_redirect(self):
        # This checks that submitting the form redirects back to the homepage.
        response = self.client.post("/add/", {
            "title": "The Alchemist",
            "author": "Paulo Coelho",
            "rating": 4,
            "comment": "Interesting and inspiring."
        })
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, "/")
