from django.db import models

# Profile model representing a user's profile information
class Profile(models.Model):
    # Full name of the user
    name = models.CharField(max_length=200)

    # Email address of the user
    email = models.CharField(max_length=200)

    # Phone number of the user
    phone = models.CharField(max_length=200)

    # A brief summary or description of the user
    summary = models.TextField(max_length=2000)

    # Highest degree attained by the user
    degree = models.CharField(max_length=200)

    # School or institution where the user studied
    school = models.CharField(max_length=200)

    # University where the user pursued their education
    university = models.CharField(max_length=200)

    # Previous work experience or employment history of the user
    previous_work = models.TextField(max_length=1000)

    # Skills possessed by the user, stored as a comma-separated string or JSON, etc.
    skills = models.TextField(max_length=1000)
