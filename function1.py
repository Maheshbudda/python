'''def mahesh(m,n):
    print("hello world")
    print("mahesh")
    print(m+n)
   
   
mahesh(10,20)    
'''
#lambda function
'''
x=lambda a,b,c:a+b+c
print(x(10,20,30))

mahesh=lambda a,b,c:a+b+c
print(mahesh(10,20,40)) 

'''
"""
ages=[10,20,30,40,50,60]
def myfunction(ages):
    if ages>=18:
        return True
    else:
        return False


adults=filter(myfunction,ages)
print(list(adults))
        
        
        """
        
'''

num=[11,22,33,44,55,66,]
def even(x):
    if x%2==0:
        print(x)
        
even(20)
filter=list (filter(lambda x:x%2==0,num))
print(filter)'''

'''num=[10,20,30,40,50,60,70]
def even(x):
    if x%2==0:
        return(x)
    
map=list(map(lambda x:x*2,num))
print(list(map))
'''

'''
m = "mahesh"
n = lambda a: (a + "\n") * 20
print(n(m))
'''
'''
num=int(input("enter a number:-"))
while True:
    if num % 2==0:
        print("number is even")
    else:
        print("number is not even number")
'''
num=2
if num > 0:
    print("number is positive")
elif num < 0:
    print("number is negavtive")
else:
    print("number is zero")
    
    

