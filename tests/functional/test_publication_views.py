import pytest
from django.urls import reverse

@pytest.mark.django_db
def test_publication_list_view(client):
    url = reverse('publication-list')  # Remplacez par le nom correct de l'URL
    response = client.get(url)
    assert response.status_code == 200
    assert "Publications" in response.content.decode()
