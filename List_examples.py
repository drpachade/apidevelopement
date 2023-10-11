# List Examples

l1 = [1,2,3,4,5,6,7]
print("The Result List is :--",l1)

# Nested List 

l1 = [1,2,["rahul",None,10],1.5,25]
result = []
for i in l1:
    if type(i) == int or type(i) == str or type(i) == float:
        result.append(i)
    else:
        result.extend(i)
print(f"The Single List is : {result}")            

# Missing Number from List

list = [1,2,4,5,6,8]
res = []
for i in range(list[0],list[-1]+1):
    if i not in list:
        res.append(i)
print(res)

# Remove Duplicate
l1 = [1,2,3,4,2,3,5,6,7,4,3,9]
r1 = []
for i in l1:
    if i not in r1:
        r1.append(i)
print(r1)       

# Lambda Programs

# Filter for Even Number 
lst = [1,2,3,4,5,6,7,8,9]
result = list(filter(lambda x : x % 2 ==0,lst))
print("The Even Numbers is:--",result) 

# Filter for Odd Number 
result = list(filter(lambda x : x % 2 == 1, lst))
print("The Odd Numbers is:--",result)

# Map for Lambda

lst1 = ['rah','sur','pac','man','dip'] 
lst2 = ['ul','esh','hade','omay','ika']

result = list(map(lambda x , y: x + y , lst1,lst2))
print(result)

# Reduce in Lambda
from functools import reduce

l1 = [1,2,3,4,5,6,7,8,9]
result = reduce(lambda x,y : x+y ,l1)
print(result)

# Factorial of number
num = 5
fact = 1
for i in range(1,num+1):
    fact = fact * i
print(f"Factorial of {num} is {fact}")

#Difference Between the content of List

l10 = [1,3,5,7,9,10,11,13]
target = [2,-2]
count = 0
for i in range(0,len(l10)):
    for j in range(i+1,len(l10)):
        c = l10[i] - l10[j]
        if c in target:
            count += 1
            print("Pair Found",l10[i],l10[j])
print("Counter",count)
