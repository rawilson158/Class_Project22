'''
Code : Implementing Polymorphism
The functions --> housing_scvs, job_scvs, health_scvs & mental_health will inherent parameters from the "User Class"

'''
class User: # class is like an template
    def __init__(self, vfirst, vlast, vage, vemail, vprob_parl):
        self.first = vfirst
        self.last = vlast 
        self.age = vage
        self.email = vfirst + '.' + vlast + '@tsr.org'
        self.prob_parl = vprob_parl
        if self.age <18 or self.age > 90:
            print("Invalid age specified. Execution cannot continue, exiting.")
            exit

    def fullname(self):
        return '{} {}, Email: {} {}'.format(self.first, self.last, self.email.lower(), self.prob_parl)


client_1 = User("Trevor", "Adams", 23, "trevor.adams@tsr.org", "yes") # object client_1 > from class User
client_2 = User("Keith", "Wilson", 42, "keith.wilson@tsr.org", "no")

print(client_1.first) # attribute or property

print(client_1.fullname()) # method or function and requires () in the print statement
print(client_2.fullname())