import pytest
from website.models import SocialCount

@pytest.mark.django_db
def test_create_socialcount():
    social = SocialCount.objects.create(
        nom="Facebook",
        lien="https://facebook.com",
        icones="fa-facebook-f"
    )
    assert social.nom == "Facebook"
    assert social.lien == "https://facebook.com"
    assert social.icones == "fa-facebook-f"
    assert social.status is True
