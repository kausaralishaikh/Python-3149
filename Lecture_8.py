#lecture8
#code1
import catch 
a=1
b=5
c=6
d=(b**2)-(4*a*c)
sol1=(-b-cmath.sqrt(d))/(2*a)
sol2=(-b+cmath.sqrt(d))/(2*a)
print('the solution are {0} and {1}'.format(sol1,sol2))
#code2
import calendar 
mm=int(input("entry month"))
yy=int(input("enter year"))
print(calendar.month(yy,mm))
#code3
import datetime 
name=input("hello! please enter your name:") 
print("hello"+name)
age=int(input("enter your age:"))
year_now=datetime.datetime.now()
print("you will turn 100 in" , (100-age) + (year_now.year)) 
        
