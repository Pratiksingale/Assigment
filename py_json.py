"""
Solved with this Output
Average emp age is: 40.0
d1 == [38, 40]
Average emp age for dept d1: 39.0
d2 == [39, 43]
Average emp age for dept d2: 41.0
"""

import json


emp = []
age = []
deptsage = []
depts = []
f = open('emp.json') 
  
data = json.load(f) 

def read_records():
    for person in data['people']:
        #print(person['name'])
        emp.append(person)

    
def correct_types():
    for e in emp:
        e['age'] = int(e['age'])
        e['dept'] = str(e['dept'])
        #print(e['dept'])
        depts.append(e['dept'])
        



def find_average_age():
    avg_age = sum([x['age'] for x in emp]) / len(emp)
    return avg_age

def find_average_age_for_dept(dept):
    #print(depts)
    i = 0
    for a in emp:
        if (depts[i] == dept):
            deptsage.append(a['age'])
        i = i + 1

    print(dept,"==",deptsage)
            
    avgd = sum(deptsage)/len(deptsage)   

    deptsage.clear()

    return avgd
    



def main():
    read_records()
    correct_types()
    #print(emp)
    print("Average emp age is:", find_average_age())

    print("Average emp age for dept d1:", find_average_age_for_dept("d1"))
    print("Average emp age for dept d2:", find_average_age_for_dept("d2"))

    # TODO: Do same thing with json file instead of csv file


if __name__ == "__main__":
    main()