import pytest
from elenizado.models import Video

@pytest.mark.django_db
def test_create_video():
    video = Video.objects.create(
        titre="Vidéo Tutoriel",
        description="Apprenez Django",
        video="https://youtube.com/watch?v=test123"
    )
    assert video.titre == "Vidéo Tutoriel"
    assert video.description == "Apprenez Django"
    assert video.get_video == "test123"
