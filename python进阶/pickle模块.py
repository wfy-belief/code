import pickle


class Student(object):
    def __init__(self):
        self.name = 'name'
        self.data = {
            'test': 0,
            'test2': [1, 2, 3, 4]
        }

    def __str__(self):
        print(self.data)
        return self.name


student = Student()
print(student)
with open('./data/pickle.pickle', 'wb') as file:
    pickle.dump(student, file)
    file.close()

with open('./data/pickle.pickle', 'rb') as file:
    data = pickle.load(file)
    print(data)
    file.close()
