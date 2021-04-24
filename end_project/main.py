import csv
import map_1

# Function to print all rows from the three service listings (housing_scv, health_scv, and job_scv)
def printservice(serv_list):
    print(serv_list[0].title)
    for serv in serv_list:
        print(serv.printme())  


class User: # class is like an template
    def __init__(self, first, last, sex_at_birth, gender_identity, age, email, prob_parl):
        self.first = first
        self.last = last 
        self.age = age
        self.email = first + '.' + last + '@tsr.org'
        self.prob_parl = prob_parl
        self.sex_at_birth = sex_at_birth
        self.gender_identity = gender_identity
        # if self.age < 18 or self.age > 90:
        #     print("Invalid age specified. Execution cannot continue, exiting.")
        #     exit

    def fullname(self):
        return '{} {}, Email: {} {}'.format(self.first, self.last, self.email.lower(), self.prob_parl)

class services:
    def __init__(self, name, website, description, location, phone, email):
        self.name = name
        self.website = website
        self.description = description
        self.location = location
        self.phone = phone
        self.email = email        

class housing_scv(services):
    def __init__(self, name, website, description, location, phone, email, income, duration, single_occupancy, comm_housing):
        super().__init__(name, website, description, location, phone, email)        
        self.income = income
        self.duration = duration
        self.single_occpancy = single_occupancy
        self.comm_housing = comm_housing
    def printme(self):
        print('"',self.name, self.website, self.description, self.location, self.phone, self.email, self.income, self.duration, self.single_occpancy, self.comm_housing,'"')
    title = 'name,   wesite,   description,   location,   phone,   email,   email,   income,   duration,   single_occupancy,   comm_housing'.title()

class job_scv(services):
    def __init__(self, name, website, description, location, phone, email, full_time, part_time, temporary, permanent):
        super().__init__(name, website, description, location, phone, email)  
        self.full_time = full_time
        self.part_time = part_time
        self.temporary = temporary
        self.permanent = permanent
    def printme(self):
        print('"',self.name, self.website, self.description, self.location, self.phone, self.email, self.full_time, self.part_time, self.temporary, self.permanent,'"')
    title = 'name,   wesite,   description,   location,   phone,   email,   full_time,   part_time,   temporary,  permanent'.title()

class health_scv(services):
    def __init__(self, name, website, description, location, phone, email, primary_care, insurance):
        super().__init__(name, website, description, location, phone, email)
        self.primary_care = primary_care
        self.insurance = insurance
    def printme(self):
        print('"',self.name, self.website, self.description, self.location, self.phone, self.email, self.primary_care, self.insurance,'"')
    title = 'name,   wesite,   description,   location,   phone,   email,   primary_care,   insurance'.title()

# Ask the user for first, last, age, email, prob_parl and save the user answers in variables (Prompt user ---> Google)
def getUser(): 
    first_name = input('What is your first name?: ')
    last_name = input('What is your Last name?: ')
    sex_at_birth = input('Sex at Birth - Male/ or Female?: ')
    gender_identity = input('Gender Identity: Heterosexual, Gay, Lesbian, Transgender, or Non-binary?: ')
    age = input('How old are you?: ')
    email_address = input('What is your email address?: ')
    release_status = input('Are you currently on probation or parole?: ')
    print()
    user = User(first_name, last_name, sex_at_birth, gender_identity, age, email_address, release_status)
    return user

def read_health():
    health_scvs = []
    title = ""
# open the csv file
    with open('services_csv_files\health_scvs.csv') as csv_file:
    # read the csv file
        csv_reader = csv.reader(csv_file, delimiter=',')
        row_num = 0
        # loop through each line in csv
        for row in csv_reader:
            # skip the first line, which has the column names
            if row_num != 0:
                cur_scv = health_scv(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7])
                health_scvs.append(cur_scv)
            row_num = row_num + 1
    return health_scvs

def read_housing():
    housing_scvs = []
    title = "" 
    # open the csv file
    with open('services_csv_files\housing_scvs.csv') as csv_file:
    # read the csv file
        csv_reader = csv.reader(csv_file, delimiter=',')
        row_num = 0
        # loop through each line in csv
        for row in csv_reader:
            # skip the first line, which has the column names
            if row_num != 0:
                cur_scv = housing_scv(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9])
                housing_scvs.append(cur_scv)
            row_num = row_num + 1            
    return housing_scvs    

def read_job():
    job_scvs = []
    title = ""  
    # open the csv file
    with open('services_csv_files\job_scvs.csv') as csv_file:
    # read the csv file
        csv_reader = csv.reader(csv_file, delimiter=',')
        row_num = 0
        # loop through each line in csv
        for row in csv_reader:
            # skip the first line, which has the column names
            if row_num != 0:
                cur_scv = job_scv(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9])
                job_scvs.append(cur_scv)
            row_num = row_num + 1
    return job_scvs        

user = getUser()
print(f"Hello {user.first} {user.last}, let's find some services that are right for you!")

serv_list = read_health()
print("\nHere are some health services for you: ")
printservice(serv_list)

serv_list = read_housing()
print("\nHere are some housing services for you: ")
printservice(serv_list)

serv_list = read_job()
print("\nHere are some job services for you: ")
printservice(serv_list)

map_1.domap()