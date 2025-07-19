import requests


url = "https://reqres.in/api/users?page=2"
def test_response_code():
    response = requests.get(url)
    assert response.status_code == 200

def test_response_content():
    response = requests.get(url)
    print(response.content)