import os
import django
from django.conf import settings
from django.test import Client
import pytest
@pytest.fixture
def client():
    return Client()


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'my_blog.settings')
django.setup()
