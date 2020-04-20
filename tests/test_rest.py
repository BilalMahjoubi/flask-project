import pytest
import requests

url = 'http://127.0.0.1:5000' # The root url of the flask app

def test_index_page():
    r = requests.get(url+'/') # Assumses that it has a path of "/"
    assert r.status_code == 200 # Assumes that it will return a 200 response

def test_get():
    r = requests.get(url+'/todo')
    
    assert r.status_code == 200


def test_getId():
  r = requests.get(url+'/todo/1')
  data = r.json()
  #assert r.status_code == 200
  assert data['id']==1

def test_put():
    r = requests.get(url+'/todo/4')
    data = r.json()
  #assert r.status_code == 200
    assert data['complete']==True

