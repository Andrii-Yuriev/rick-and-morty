from django.urls import path
from characters.views import get_random_character, CharacterListView

urlpatterns = [
    path(
        "characters/random/", get_random_character, name="get_random_character"
    ),
    path("characters/", CharacterListView.as_view(), name="character-list"),
]

app_name = "characters"
