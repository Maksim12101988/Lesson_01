import pytest
import yaml
import requests

with open("config.yaml", encoding='utf-8') as f:
    data = yaml.safe_load(f)
S = requests.Session()


@pytest.fixture()
def get_title_notmypost():
    return 'Configuration'


@pytest.fixture()
def login():
    responce = S.post(url=data['url_login'],
                      data={"username": data['username'], "password": data['password']})
    if responce.status_code == 200:
        return responce.json()['token']


@pytest.fixture()
def get_description():
    return 'Гидро архонт Фонтейна'