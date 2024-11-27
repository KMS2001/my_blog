import pytest
from elenizado.models import Categorie, Publication, Commentaire

@pytest.mark.django_db
def test_create_commentaire():
    categorie = Categorie.objects.create(nom="Tech", description="Description Tech")
    publication = Publication.objects.create(
        titre="Test Publication",
        description="Description",
        categorie=categorie
    )
    commentaire = Commentaire.objects.create(
        publication=publication,
        nom="John Doe",
        email="john@example.com",
        commentaire="Super post !"
    )
    assert commentaire.nom == "John Doe"
    assert commentaire.email == "john@example.com"
    assert commentaire.commentaire == "Super post !"
