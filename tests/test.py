
import requests

from utils.config import API_BASE_URL, CONFIG_HEADERS



def test_get_all_users_passed():
    response = requests.get(API_BASE_URL+'/database/search?q=Nirvana&type=release&title=nirvana - nevermind&country=canada&year=1991', headers=CONFIG_HEADERS)
    print(response)
    assert response.status_code == 200


def test_get_all_users_failed():
    response = requests.get(API_BASE_URL+'/database/search?q=Nirvana&type=release&title=nirvana - nevermind&country=canada&year=1991', headers=CONFIG_HEADERS)
    print(response)
    assert response.status_code == 201
