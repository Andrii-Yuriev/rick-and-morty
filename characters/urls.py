from django.urls import path
from characters.views import get_random_character

urlpatterns = [
    path(
        "characters/random/", get_random_character, name="get_random_character"
    )
]

app_name = "characters"
