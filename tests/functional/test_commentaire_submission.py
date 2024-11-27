import pytest
from django.urls import reverse
from elenizado.models import Publication, Commentaire, Categorie

@pytest.mark.django_db
def test_submit_commentaire(client):
    categorie = Categorie.objects.create(nom="Tech", description="Description Tech")
    publication = Publication.objects.create(
        titre="Test Publication",
        description="Description",
        categorie=categorie
    )
    url = reverse('commentaire-submit', args=[publication.id])  # Vérifiez le nom de l'URL
    data = {
        "nom": "John Doe",
        "email": "john@example.com",
        "commentaire": "Super post !"
    }
    response = client.post(url, data)
    assert response.status_code == 200
    assert Commentaire.objects.count() == 1
