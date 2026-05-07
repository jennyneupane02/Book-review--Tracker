# Book Review Tracker

This is a small Django web application where users can add and view book reviews. Users can enter a book title, author name, rating, and short comment, and the review appears on the homepage.

The project includes automated tests for Python logic, Django models, model relationships, and HTTP responses using Django's test client. The tests check rating calculations, valid and invalid rating inputs, saved model fields, model methods, ForeignKey relationships, page content, status codes, and form redirect behavior.

This project also includes a GitHub Actions workflow for Continuous Integration. Every time code is pushed to the repository, GitHub Actions automatically installs the dependencies from requirements.txt and runs `python manage.py test` to make sure the application still works correctly.
