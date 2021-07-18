import random
import string

# a = int(input("How many number do want to input?"))
list_nb_str = []
for i in range(0,1000):
    if (i%2)==0:
        list_nb_str.append(random.random())
    else:
        my_str = ''.join(random.choices(string.ascii_uppercase + string.digits, k=10 ))
        list_nb_str.append(my_str)
        
        
with open('my_file.txt', 'w') as fp:
    fp.write(','.join(map(str, list_nb_str)))

