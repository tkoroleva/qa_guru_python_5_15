import requests

url_api = 'https://reqres.in/api'
url_users = 'https://reqres.in/api/users'


def test_create_user_post():
    response = requests.post(url=url_users,
                             json={
                                 "name": "Ada",
                                 "job": "Mathematician"}
                             )

    assert response.status_code == 201
    assert response.json()['job'] == 'Mathematician'


def test_update_user_put():
    response = requests.put(url=f'{url_users}/542',
                            json={
                                "name": "Ada Lovelace"}
                            )

    assert response.status_code == 200
    assert response.json()['name'] == 'Ada Lovelace'


def test_update_user_patch():
    response = requests.patch(url=f'{url_users}/542',
                              json={
                                "job": "Mathematician and writer"}
                              )

    assert response.status_code == 200
    assert response.json()['job'] == 'Mathematician and writer'


def test_delete_user():
    response = requests.delete(url=f'{url_users}/542')

    assert response.status_code == 204


def test_register_success():
    response = requests.post(url=f'{url_api}/register',
                             json={
                                 "email": "eve.holt@reqres.in",
                                 "password": "pistol"}
                             )

    assert response.status_code == 200
    assert response.json()['id'] != ''
    assert response.json()['token'] != ''


def test_register_not_success():
    response = requests.post(url=f'{url_api}/register',
                             json={
                                 "email": "sydney@fife"}
                             )

    assert response.status_code == 400
    assert response.json()['error'] == 'Missing password'


def test_login_success():
    response = requests.post(url=f'{url_api}/login',
                             json={
                                 "email": "eve.holt@reqres.in",
                                 "password": "cityslicka"}
                             )

    assert response.status_code == 200
    assert response.json()['token'] != ''


def test_login_not_success():
    response = requests.post(url=f'{url_api}/login',
                             json={
                                 "email": "peter@klaven"}
                             )

    assert response.status_code == 400
    assert response.json()['error'] == 'Missing password'


def test_user_found():
    response = requests.get(url=f'{url_users}/9')

    assert response.status_code == 200
    assert response.json()['data']['id'] == 9


def test_user_not_found():
    response = requests.get(url=f'{url_users}/13')

    assert response.status_code == 404
