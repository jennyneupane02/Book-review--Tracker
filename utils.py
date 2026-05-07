def calculate_average_rating(ratings):
    if len(ratings) == 0:
        raise ValueError("Ratings list cannot be empty.")
    return sum(ratings) / len(ratings)


def is_valid_rating(rating):
    return 1 <= rating <= 5
