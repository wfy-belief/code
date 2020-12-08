# content of test_class.py
class TestClass(object):
    def add(self, a, b):
        """
        a + b       
        """
        return a + b

    def test_one(self):
        assert self.add(1, 2) == 3

    def test_two(self):
        x = "hello"
        assert hasattr(x, 'find')

    def test_3(self):
        assert self.add(1, 5) == 6
