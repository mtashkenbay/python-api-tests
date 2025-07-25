import requests
import json


def test_response_code():
    url = "https://reqres.in/api/users?page=2"
    response = requests.get(url)
    json_body = json.load(response.content)
    print(json_body)
    assert response.status_code == 200

def test_response_content():
    url = "https://reqres.in/api/users/2"
    response =requests.get(url).json()
    print(response)

def test_response_status_code_404():
    url = "https://reqres.in/api/users/23"
    response = requests.get(url)
    assert response.status_code == 404