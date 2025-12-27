from app import app


def test_index():
    """Test the index route."""
    with app.app_context():
        client = app.test_client()
        response = client.get('/')
        assert response.status_code == 200
        assert b'Hello' in response.data


def test_health():
    """Test the health check route."""
    with app.app_context():
        client = app.test_client()
        response = client.get('/health')
        assert response.status_code == 200
