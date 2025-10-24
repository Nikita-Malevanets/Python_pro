"""Views for the 'home' application.

Each function below handles a specific page or dynamic route.
"""

from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    """Render the main (home) page."""
    return render(request, 'home/index.html')


def about(request):
    """Display the 'About us' page."""
    return HttpResponse("Сторінка про нас")


def contact(request):
    """Display the 'Contact' page."""
    return HttpResponse("Зв'яжіться з нами")


def post_view(request, id):
    """Show a specific post by its numeric ID."""
    return HttpResponse(f"Ви переглядаєте пост з ID: {id}")


def profile_view(request, username):
    """Show a user's profile by username."""
    return HttpResponse(f"Ви переглядаєте профіль користувача: {username}")


def event_view(request, year, month, day):
    """Display an event page for the given date."""
    return HttpResponse(f"Дата події: {year}-{month}-{day}")
