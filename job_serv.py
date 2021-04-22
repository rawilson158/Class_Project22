
import time
import random

trs_reply = ['Thank you for your honesty.' 'One moment please', 'Lets move along']

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
print("please use the letter to match your desired answer for each question.")
my_list = ['a: yes', 'b: no', 'c: it varies']
my_list2 = ['a: yes. I have something now.' 'b: no; however, I hav something lined up in the next___weeks. (will store this value and call later in a fstring']
my_list3 = ['a: yes', 'b: no']
my_list4 = ['a: k-8' 'b: 9-12' 'c: any post HS degree' 'd: more than one post HS degree']
print(my_list3)
q_1 = input(' Question: Are you on any type of probation? ')

if q_1 == "a":
    probation_officer = input("please provide the name of your PO? ")
elif q_1 == "b":
    print('good')
else:
    print("ok. we can come back to this later.")
print(random.choice(trs_reply))
#trs_reply = []
#for reply in trs_reply:
    #if reply == trs_reply[1]:
        #print('thanks')
time.sleep(2)
#random.choice(trs_reply)
print(my_list2)
q_2 = input('Question: Are you currently employed? ')
if q_2 == "a":
    print("option 1")
elif q_2 == "b":
    print('option 2')
else:
    print("option 3")
print(random.choice(trs_reply))
#for reply in trs_reply:
    #if reply == trs_reply[1]:
        #print('thank you.')
time.sleep(2)
print(my_list4)
q_3 = input('Question: what is your highest level of completed education? ')
if q_3 == "a":
    print("option 1")
elif q_3 == "b":
    print('option 2.')
else:
    print("option 3.")
print(random.choice(trs_reply))
#for reply in trs_reply:
    #if reply == trs_reply[0]:
        #print('thanks')
time.sleep(2)
print(my_list3)
q_4 = input('Question: 4 Would you like to attend school and be given a counselor? ')
if q_4 == "a":
    print("option 1")
elif q_4 == "b":
    print('option 2')
else:
    print("option 3.")
print(random.choice(trs_reply))
#for reply in trs_reply:
    #if reply == trs_reply[1]:
       # print('thanks.')
time.sleep(2)
