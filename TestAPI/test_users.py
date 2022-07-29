import requests
import json

baseUrl= "https://reqres.in/"

def test_fecth_user():
    path = "api/users/2"
    response = requests.get(url=baseUrl+path)
    responseJson = response.json()
    print(response)
    print("------------")
    print(responseJson)
    assert response.status_code == 200
    assert responseJson["data"]["id"] == 2
    assert responseJson["data"]["first_name"] == 'Janet'
    

    
    