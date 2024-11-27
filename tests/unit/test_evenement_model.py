import pytest
from elenizado.models import Evenement

@pytest.mark.django_db
def test_create_evenement():
    evenement = Evenement.objects.create(
        titre="Concert 2024",
        description="<p>Un super concert</p>",
        image="image/concert.jpg"
    )
    assert evenement.titre == "Concert 2024"
    assert evenement.slug.startswith("concert-2024-")
    assert evenement.status is True
