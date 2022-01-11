import random
import time

names=['sunny','Bunny','vinny','chinny']
subjets=['Python','Java','BlockChain']

def people_list(num):
    results=[]
    for i in range(num):
        person={
            'id':i,
            'name':random.choice(names),
            'subject':random.choice(subjets)
            }
        results.append(person)
    return results
def people_generator(num):

    for i in range(num):
        person={
            'id':i,
            'name':random.choice(names),
            'subject':random.choice(subjets)
            }
    yield person
#t1=time.clock()
people=people_list(100000)
print(people)
#t2=time.clock()
print('Time taken for List:',t2-t1)

#t1=time.clock()
people=people_generator(100000)
#t2=time.clock()

print('Time taken for Generator:',t2-t1)
