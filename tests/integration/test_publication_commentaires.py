import pytest
from elenizado.models import Publication, Commentaire, Categorie

@pytest.mark.django_db
def test_publication_with_commentaires():
    categorie = Categorie.objects.create(nom="Tech", description="Description Tech")
    publication = Publication.objects.create(
        titre="Test Publication",
        description="Description",
        categorie=categorie
    )
    Commentaire.objects.create(
        publication=publication,
        nom="John Doe",
        email="john@example.com",
        commentaire="Super post !"
    )
    Commentaire.objects.create(
        publication=publication,
        nom="Jane Doe",
        email="jane@example.com",
        commentaire="Très intéressant !"
    )
    assert publication.publication_commentaire.count() == 2
