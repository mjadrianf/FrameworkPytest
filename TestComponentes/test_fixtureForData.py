from sample import StudentData
import pytest

def test_scott_data():
    db = StudentData()
    db.connect('data/data.json')
    scott_data = db.get_data('Joseph')
    assert scott_data['id'] == 1
    assert scott_data['name'] == 'Joseph'
    assert scott_data['result'] == 'pass'

def test_mark_data():
    db = StudentData()
    db.connect('data/data.json')
    mark_data = db.get_data('Jaden')
    assert mark_data['id'] == 2
    assert mark_data['name'] == 'Jaden'
    assert mark_data['result'] == 'fail'