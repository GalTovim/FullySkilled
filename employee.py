class Employee:
    """Employee Class"""

    def __init__(self, first, last, id, mail, cv, phone, skill):
        self.first = first
        self.last = last
        self.id = id
        self.mail = mail
        self.cv = cv
        self.phone = phone
        self.skill = skill

    @property
    def email(self):
        return '{}.{}@email.com'.format(self.first, self.last)

    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def __repr__(self):
        return "Employee {} {} {}".format(self.first, self.last, self.id, self.mail, self.cv, self.phone, self.skill)
