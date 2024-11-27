import pytest
from elenizado.models import Publication, Categorie
from django.test import Client, TestCase


@pytest.mark.django_db
def test_publication_detail_view(client):
    categorie = Categorie.objects.create(nom="Tech", description="Description Tech")
    publication = Publication.objects.create(
        titre="Test Publication",
        description="Description",
        categorie=categorie
    )
    url = reverse('publication-detail', args=[publication.id])  # Assurez-vous du nom de l'URL
    response = client.get(url)
    assert response.status_code == 200
    assert publication.titre in response.content.decode()
