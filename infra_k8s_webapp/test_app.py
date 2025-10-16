"""Unit tests for the Flask web application."""

import pytest
from app import app as flask_app

@pytest.fixture
def app():
    """Create and configure a new app instance for each test."""
    yield flask_app

@pytest.fixture
def client(app):
    """A test client for the app."""
    return app.test_client()

def test_hello_world_endpoint(client):
    """Test the hello-world endpoint."""
    response = client.get('/')
    assert response.status_code == 200
    assert b"Hello, World!" in response.data
