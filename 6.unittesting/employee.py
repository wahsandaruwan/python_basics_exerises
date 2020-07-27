class Employee:
    """A Simple employee class
    """    
    raise_amt = 1.05 #5% --> 105/100

    def __init__(self, first, last, pay):
        self.fname = first
        self.lname = last
        self.payment = pay

    def email(self):
        return '{}.{}@email.com'.format(self.fname, self.lname)

    def fullname(self):
        return '{} {}'.format(self.fname, self.lname)

    def apply_raise(self):
        self.payment = int(self.payment * self.raise_amt)