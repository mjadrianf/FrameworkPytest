import json


class StudentData:
    def __init__(self):
        self.__data = None

    def connect(self, data_file):
        with open(data_file) as json_file:
            self.__data = json.load(json_file)

    def get_data(self, name):
        for stu in self.__data['students']:
            if stu['name'] == name:
                return stu
            
    def close(self):
        pass