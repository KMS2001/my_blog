import pytest
from elenizado.models import Categorie, Publication

@pytest.mark.django_db
def test_create_publication():
    categorie = Categorie.objects.create(nom="Tech", description="Description Tech")
    publication = Publication.objects.create(
        titre="Test Publication",
        description="<p>Description de test</p>",
        image="image/test.jpg",
        categorie=categorie
    )
    assert publication.titre == "Test Publication"
    assert publication.categorie.nom == "Tech"
    assert publication.slug.startswith("test-publication-")
