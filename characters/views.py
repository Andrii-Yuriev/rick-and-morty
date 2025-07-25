import random
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.request import Request
from characters.models import Character
from characters.serializers import CharacterSerializer
from rest_framework import generics
from django.db.models.query import QuerySet
from drf_spectacular.utils import extend_schema, OpenApiParameter


@extend_schema(
    responses={status.HTTP_200_OK: CharacterSerializer},
)
@api_view(["GET"])
def get_random_character(request: Request) -> Response:
    """Get a random character from Rick and Morty world."""
    pks = Character.objects.values_list("pk", flat=True)
    random_pk = random.choice(pks)
    random_character = Character.objects.get(pk=random_pk)
    serializer = CharacterSerializer(random_character)

    return Response(serializer.data, status=status.HTTP_200_OK)


class CharacterListView(generics.ListAPIView):
    serializer_class = CharacterSerializer

    def get_queryset(self) -> QuerySet:
        queryset = Character.objects.all()

        name = self.request.query_params.get("name")
        if name is not None:
            queryset = queryset.filter(name__icontains=name)

        return queryset

    @extend_schema(
        parameters=[
            OpenApiParameter(
                name="name",
                description="Filter characters by name",
                required=False,
                type=str,
            ),
        ]
    )
    def get(self, request, *args, **kwargs) -> Response:
        """List all characters or filter by name."""
        return super().get(request, *args, **kwargs)
