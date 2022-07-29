from sample import StudentData
import pytest
import os


db = None
#arrange
def setup_module(module):
    print('*****SETUP*****')
    global db
    db = StudentData()
    db.connect('data/data.json')


def teardown_module(module):
    print('******TEARDOWN******')
    db.close()

@pytest.mark.parametrize('FirstName',
                         [
                             ('Joseph'),
                             ('Joseph'),
                             ('Joseph')
                         ]
                        )
def test_scott_data(FirstName):
   # act
    scott_data = db.get_data(FirstName)
   # assert
    assert scott_data['id'] == 1
    assert scott_data['name'] == 'Joseph'
    assert scott_data['result'] == 'pass'


def test_mark_data():
    mark_data = db.get_data('Jaden')
    assert mark_data['id'] == 2
    assert mark_data['name'] == 'Jaden'
    assert mark_data['result'] == 'fail'