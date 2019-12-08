class Employer:
        """Employer Class"""
        def __init__(self,first,last,id,mail,business_name):
            self.first=first
            self.last=last
            self.id=id
            self.mail=mail
            self.business_name=business_name

        @property
        def email(self):
            return '{}.{}@email.com'.format(self.first,self.last)
        @property
        def fullname(self):
            return '{} {}'.format(self.first,self.last)
        def __repr__(self):
            return "Employee('{}','{}',{},'{}','{}')".format(self.first,self.last,self.id,self.mail,self.business_name)