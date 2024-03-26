import pytest
import requests
import yaml

S = requests.Session()

with open("config.yaml", encoding='utf-8') as f:
    data = yaml.safe_load(f)


def test01_check_notmypost(login, get_title_notmypost):
    url = data['url_post']
    headers = {'X-Auth-Token': login}
    not_my_post = {"owner": "notMe"}
    data_json = S.get(url=url,params=not_my_post, headers=headers).json()['data']
    res = [x['title'] for x in data_json]
    print(res)
    assert get_title_notmypost in res, "Пост не найден"


def test02_create_post(login):
    url = data['url']
    headers = {'X-Auth-Token': login}
    data_post = {'title': data['title'],'description': data['description'], 'content': data['content']}
    res = S.post(url=url, headers=headers, data=data_post)
    assert str(res) == '<Response [200]>', "Пост не найден"


def test03_check_description(login, get_description):
    url = data['url_post']
    headers = {'X-Auth-Token': login}
    data_json = S.get(url=url, headers=headers).json()['data']
    res = [x['description'] for x in data_json]
    print(res)
    assert get_description in res, "Пост не найден"


if __name__ == "__main__":
    pytest.main(["-vv"])