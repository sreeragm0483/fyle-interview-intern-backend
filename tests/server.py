def test_server_status(client):
    """
    Is alive
    """
    response = client.get(
        '/',
    )

    assert response.status_code == 200

    data = response.json
    assert data['status'] == 'ready'

def test_server_invalid_route(client):
    """
    Not found endpoint
    """
    response = client.get(
        '/invalid',
    )

    assert response.status_code == 404