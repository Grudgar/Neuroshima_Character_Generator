import pytest

@pytest.mark.django_db
def test_welcome_page(client):
    response = client.get('')
    assert response.status_code == 200

@pytest.mark.django_db
def test_login_page(client):
    response = client.get('/login')
    assert response.status_code == 200

@pytest.mark.django_db
def test_register_page(client):
    response = client.get('/register')
    assert response.status_code == 200

@pytest.mark.django_db
def test_user_panel_page(client):
    response = client.get('/user-panel')
    assert response.status_code == 200

@pytest.mark.django_db
def test_char_card_page(client):
    response = client.get('/char-card')
    assert response.status_code == 200