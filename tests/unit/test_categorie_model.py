import pytest
from elenizado.models import Categorie

@pytest.mark.django_db
def test_create_categorie():
    categorie = Categorie.objects.create(
        nom="Tech",
        description="Description de la catégorie"
    )
    assert categorie.nom == "Tech"
    assert categorie.description == "Description de la catégorie"
    assert categorie.status is True
