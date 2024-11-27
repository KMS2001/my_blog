import pytest
from website.models import SiteInfo, SocialCount

@pytest.mark.django_db
def test_siteinfo_socialcount_integration():
    site = SiteInfo.objects.create(
        email="info@example.com", nom="MySite", telephone=123456789, description="Description"
    )
    SocialCount.objects.create(nom="Facebook", lien="https://facebook.com", icones="fa-facebook-f")
    SocialCount.objects.create(nom="Twitter", lien="https://twitter.com", icones="fa-twitter")
    
    assert SiteInfo.objects.count() == 1
    assert SocialCount.objects.count() == 2
    assert site.nom == "MySite"
