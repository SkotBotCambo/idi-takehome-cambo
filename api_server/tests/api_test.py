import pytest
from ..app import app

def test_index_url():
    response = app.test_client().get()

    assert response.status_code == 200
    assert response.data.decode('utf-8') == 'Working!'