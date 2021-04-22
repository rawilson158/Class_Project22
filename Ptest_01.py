import requests
from bs4 import BeautifulSoup

#with open("doc.html") as fp:
 # soup = BeautifulSoup(fp, "html.parser")



'''
url = 'https://www.bop.gov/inmates/custody_and_care/female_offenders.jsp'
myobj = {'rollout_tracking': ''}

x = requests.post(url, data = myobj)

print(x.text)
# please ignore the aformentioned.


# my hope here is to create a class that we can mass replicate per user.

#page = soup.find('Women').getText()
#wanted_text = BeautifulSoup(html, 'html.parser')

aforementioned is prior to 04/14/2021

'''
'''
import json
import csv

with open ("02_scvs.csv", "r") as f:
    reader = csv.reader(f)
    next(reader)
    data = {"name": []}
    for row in reader:
        data["name"].append({"name":
        row[0], "website": row[1]})
    print(data)

[
  {
    "name": "Ryan Health",
    "wesite": "https://ryanhealth.org/",
    "description": "Ryan Health delivers exceptional primary care to our patients, as well as a range of services from women's health and pediatrics, to behavioral health, HIV care, and chronic disease management.",
    "location": "New York City",
    "phone": "212-749-1820",
    "email": "communityoutreach@ryanhealth.org",
    "subcategory": "health_scvs",
    "param 1": "primary_care",
    "param 2": "insurance",
    "param 3": "",
    "param 4": ""
  },
  {
    "name": "Healthfirst",
    "wesite": "https://hfrepdirectory.healthfirst.org/?",
    "description": "Connecting you and your family to health insurance plans and resources that meet your needs.",
    "location": "All 5 boroughs of New York City",
    "phone": "844-488-1486",
    "email": "N/A",
    "subcategory": "health_scvs",
    "param 1": "primary_care",
    "param 2": "insurance",
    "param 3": "",
    "param 4": ""
  },
  {
    "name": "Workforce1",
    "wesite": "https://dol.ny.gov/location/brooklyn-workforce1-career-center",
    "description": "We help New Yorkers find the careers they will love by connecting them to new job opportunities, referring them to training opportunities that build their skills, and by ensuring they are paid the proper wage and have a safe working environment when they're on the job.",
    "location": "New York State (Brooklyn, NY location)",
    "phone": "718-246-5219",
    "email": "mailto:Workforce1Brooklyn@grantassociatesinc.com",
    "subcategory": "job_scvs",
    "param 1": "full_time",
    "param 2": "part_time",
    "param 3": "temporary",
    "param 4": "permanent"
  },
  {
    "name": "",
    "wesite": "",
    "description": "",
    "location": "",
    "phone": "",
    "email": "",
    "subcategory": "housing_scvs",
    "param 1": "income",
    "param 2": "duration",
    "param 3": "single_occupancy",
    "param 4": "comm_housing"
  }
]

class services:
    def __init__(self, name, website, description, location, phone, email):
        self. name = name
        self.website = website
        self.description = description
        self.location = location
        self.phone = phone
        self.email = email



    def housing_scvs(self, income, duration, single_occupancy, comm_housing):
        self.website = income
        self.duration = duration
        self.single_occpancy = single_occupancy
        self.comm_housing = comm_housing


    def job_scvs(self, full_time, part_time, temporary, permanent):
        self. full_time = full_time
        self.part_time = part_time
        self.temporary = temporary
        self.permanent = permanent



    def health_scvs(self, primary_care, insurance):
        self.primary_care = primary_care
        self.insurance = insurance

'''









'''
class user:
    def __init__(self, name, age, need_1):
        self.name = string(name)
        # I am not sure how to print out the type method here to verify why I am getting the error of user_00.name = Shawn
        #is not defined. 
        
        self.age = float(age)
        self.need_1 = need_1
       # self.need_2 = need_2- Robert/Tanya's area
        #self.need_3 = need_3- Tanya/Robert's area 

#user_00 = user(name, age, need_1, need_2, need_3)



#I have found a sample outline that I am using to create an outline for questions to get a gague of each new user.
#I know from my own story that what I thougt I needed wasn't always what I needed.


need_1 = "This is a task for Shawn."
user_00.name = Shawn
user_00.age = 34
user_00.need_1 = print(f'We want to start with {need_1}')
#user_00.need_2 = "thanks"
u#ser_00.need_3 = 'you are welcome'

user_00 = user()
print(user_00)


'''

### this is the main source that I will be using. 
#https://www.careercenteroffices.com/brooklyn-ny/


# please ignore the aformentioned.


# my hope here is to create a class that we can mass replicate per user.

#page = soup.find('Women').getText()
#wanted_text = BeautifulSoup(html, 'html.parser')

#aforementioned is prior to 04/14/2021



'''
url = 'https://www.careercenteroffices.com/brooklyn-ny/' 
myobj = {'rollout_tracking': ''}

x = requests.post(url, data = myobj)

print(x.text)
# please ignore the aformentioned.

import time
import random

greeting_reply = ['thank you for choosing our team.']



hey_there = "Hey There."
print(hey_there.center(40, '-'))
time.sleep(2)
print("WE CAN PLACE TEAM TEXT HERE")
time.sleep(2)
print("We would like for you to take a few moments and complete a survey.")
time.sleep(2)
print('This survey will outline target areas for planned resolution.')
time.sleep(4)
print('intro and obtain vital info here')
time.sleep(2)
print('store values here')

name = input('What is your name? ')

print(f'thanks {name}. We are ready to begin')

time.sleep(5)
print(f'{name}, this is one of the first steps to rebuilding the life you want to live. Here at, TEAM NAME, we\npartner with...')

team_mate =  https://www.careercenteroffices.com/brooklyn-ny//aria-hidden+"false" style ="padding:px;"/id="footer" class="container" style="height: auto !important;"/div[1]/div[2]/p style='margin-top:2020px:'

print(team_mate)
### Joseph this is where I am having my error. When I am able to resolve this I will be able to complete my 10 questions and post to repo prior to monday. 


'''
'''
url = 'https://www.careercenteroffices.com/brooklyn-ny/' 
myobj = {'rollout_tracking': ''}
x = requests.post(url, data = myobj)
print(x.text)

team_mate =  html/body/footer/div[1]/div[2]/p style='margin-top:2020px:'
print(team_mate)
'''





"Are you on any form of supervised probation? "

"When was you last medical evaluation? "
"How many days have you secured lodging at for the next week ?"
"Do you curently have any of the following: ...Each one of us can add something"



#this is where I am starting as of 04/19 1203PM

'''
url = 'https://www.stnicksalliance.org/workforce'
requests.get(url)
response = requests.get(url)
#print(response.status_code)
#prints status code 200. It works

if response.status_code == 200:
  print('success')
elif response.status_code == 400:
  print('not working')


print(response.headers = )

'''
'''
url = 'https://www.stnicksalliance.org/workforce'
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')
results = soup.find_all('section', class_='white-space:pre-wrap;')
#print(results.prettify())
print(results)
#I have followed the links. This is where I get stuck. I have to attend to some matters with our group. When we sync tonight getting this to work is my first goal.
#on the inspect page this is what the path to the desired text is located. 
#/html/body/div[3]/main/div[2]/div/div[1]/div[1]/div[1]/div/p/em
'''
'''
import csv
f = open('people.csv', 'a', newline="")
tup1 = ('bob', 19)
writer = csv.writer(f)
writer.writerow(tup1)
f.close()
'''

#area for questions
#question 1 is probation
#q 2-4 are for jobs
#q 5-7 are healthcare
#q 8-10 are housing
#easch should have options 1,2,3 that can be amend by each of us at a later time.

#this is new info
import time
import random

trs_reply = ['Thank you for your honesty.' 'One moment please', 'Great answer']

#print(random.choice(trs_reply))
hey_there = "Hello and welcome."
print(hey_there.center(40, '-'))
time.sleep(2)
print("INPUT text of our group")
time.sleep(2)
print("Thank you for taking the time to complete the survey.")
time.sleep(2)


user1= input("What is your name? ")
#name
#age
#how long release...months


#variable = {stored data}

time.sleep(2)

greeting_here = "One moment please"
print(greeting_here.center(30,'*'))

time.sleep(1)
print('Let us begin.')
time.sleep(1)
input(f'Thanks {user1}. I can not wait to get started.\nPlease press enter.')
time.sleep(2)

print('Today we are going to take a survey to best assist you with our resources.')
time.sleep(1)
print('This is merely a starting step.')
print("please use the letter to match your desired answer.")
my_list = ['a: yes', 'b: no', 'c: it varies']
print(my_list)
q_1 = input(' Question: Are you on any type of probation? ')

if q_1 == "a":
    print("please provide the name of your PO ")
elif q_1 == "b":
    print('good')
else:
    print("ok. no worries")
print(random.choice(trs_reply))
#trs_reply = []
for reply in trs_reply:
    if reply == trs_reply[1]:
        print('thanks')
time.sleep(2)
random.choice(trs_reply)
print(my_list)
q_2 = input('Question: Are you currently employed? ')
if q_2 == "a":
    print("option 1")
elif q_2 == "b":
    print('option 2')
else:
    print("option 3")
print(random.choice(trs_reply))
for reply in trs_reply:
    if reply == trs_reply[1]:
        print('thank you.')
time.sleep(2)
print(my_list)
q_3 = input('Question: what is your highest level of completed education? ')
if q_3 == "a":
    print("option 1")
elif q_3 == "b":
    print('option 2.')
else:
    print("option 3.")
print(random.choice(trs_reply))
for reply in trs_reply:
    if reply == trs_reply[0]:
        print('thanks')
time.sleep(2)
print(my_list)
q_4 = input('Question: 4 Would you like to attend school and be given a counselor? ')
if q_4 == "a":
    print("option 1")
elif q_4 == "b":
    print('option 2')
else:
    print("option 3.")
print(random.choice(trs_reply))
for reply in trs_reply:
    if reply == trs_reply[1]:
        print('thanks.')
time.sleep(2)
print(my_list)

q_5 = input('Question: 5 Do you have health care? ')
if q_5 == "a":
    print("option 1. ")
elif 5 == "b":
    print('option 2')
else:
    print("option 3")
print(random.choice(trs_reply))
for reply in trs_reply:
    if reply == trs_reply[1]:
        print('thanks.')
time.sleep(2)
print(my_list)
q_6 = input("Question: 6 When was you last physical? ")
if q_6 == "a":
    print('option 1')
elif q_6 == "b":
    print('optino 2.')
else:
    print("option 3")
print(random.choice(trs_reply))
for reply in trs_reply:
    if reply == trs_reply[0]:
        print('thanks')
time.sleep(2)
print(my_list)
q_7 = input('Question: 7 Do you have any high risk behavior? ')
if q_7 == "a":
    print("option 1 ")
elif q_7 == "b":
    print('option 2')
else:
    print("option 3")
print(random.choice(trs_reply))
time.sleep(2)
print(my_list)
q_8 = input('Question: 8 Do you have lodging currently?  ')
if q_8 == "a":
    print("option 1")
elif q_8 == "b":
    print('option 2.')
else:
    print("option 3.")
print(random.choice(trs_reply))
time.sleep(2)
print(my_list)
q_9 = input('Question: 9 How long are you able to live there? ')
if q_9 == "a":
    print("option 1")
elif q_9 == "b":
    print('option 2')
else:
    print("option 3")
print(random.choice(trs_reply))
for reply in trs_reply:
    if reply == trs_reply[1]:
        print('thanks')
time.sleep(2)
print(my_list)
q_10 = input('Question: 10 Would you like to have your own home within a year? ')
if q_10 == "a":
    print("Great.")
elif q_10 == "b":
    print('Great.')
else:
    print("Get lost then")
for reply in trs_reply:
    if reply == trs_reply[0]:
        print('thanks')
time.sleep(2)
print("Good bye. Again, thank you for parterning with trs. I hope you have an amazing day.")

