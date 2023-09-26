class MyClass:
    """ Documentation of my class """
    x = 125
    y = "My secret code"
    z = 1
    INFO = (5,)

    def __init__(self):
        self.x = None
        self._y = "protected"
        self.__z = 10

    def __myMethod(self, a):
        self.x = a
        self._y = "%s" % (a)
        self.__z += 2

    def __str__(self):
        return "MyClass x=%s, y='%s, z=%s" % (self.x, self._y, self.__z)
