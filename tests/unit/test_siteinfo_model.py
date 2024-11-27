import pytest
from website.models import SiteInfo

@pytest.mark.django_db
def test_create_siteinfo():
    site = SiteInfo.objects.create(
        email="info@example.com",
        nom="Mon Site",
        telephone=123456789,
        description="Description du site",
        logo="logo.jpg"
    )
    assert site.email == "info@example.com"
    assert site.nom == "Mon Site"
    assert site.telephone == 123456789
    assert site.status is True
