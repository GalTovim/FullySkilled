class Employee:
    """Employee Class"""

    def __init__(self, first, last, id):
        self.first = first
        self.last = last
        self.id = id

    @property
    def email(self):
        return '{}.{}@email.com'.format(self.first, self.last)

    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def __repr__(self):
        return "Employee {} {} {}".format(self.first, self.last, self.id)
