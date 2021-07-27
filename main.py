'''
Name: Ahmed Elshahat Saad Abdelazeez Dawood
Task: Enozom Internship Technical Task
'''

import hashlib

def MD5(str2hash):
    result = hashlib.md5(str2hash.encode())

    return f"The hexadecimal equivalent of hash is : {result.hexdigest().upper()}"

f=open('annual-enterprise-survey-2020-financial-year-provisional-csv.csv','r')
cnt=0
concatenated_string=''

for i in f.readlines()[1:]:                          # skipping the first row of column names
    cnt += 1
    if cnt%2==1:                                     # choosing the odd numbered rows
        concatenated_string+=i.split(',')[2]         # choosing the 3rd column of each row

f.close()

print(concatenated_string)                           # printing the string
print(MD5(concatenated_string))                      # calling the MD5 function