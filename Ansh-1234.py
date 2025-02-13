#SINGLE QUOTE STATEMEMTS

print('vratej dwivedi')
print('BCA')
print('United University')
print('Rawatpur')
print('Jhalwa')
print('Prayagraj')
print('Python')
print('Paradigm')
print('Paradigm')
print('2 types of Paradigm\n')

'''DOUBLE QUOTE STATEMEMTS'''

print("Virat kohli")
print("Rohit sharma")
print("Rishab pant")
print("cricketer")
print("Indian cricket team")
print("T20")
print("ODI")
print("Test")
print("Super over\n")

#TRIPLE QUOTE STATEMEMTS

print('''vratej''')
print('''dwivedi''')
print('''BCA''')
print('''PHP''')
print('''Instagram''')
print('''Facebook''')
print('''Google''')
print('''X''')
print('''C++''')
print('''Bharat\n''')

'''MULTI LINE STATEMENTS'''

print('''MY NAME IS
vratej dwivedi\n''')
print("""My address is varansi. \n""")
print("""My DOB is 8 august 2005.\n""")
print("""There are 3 Sections in BCA.\n""")
print("""A , B & C\n""")
print("""Python is 1st programing language for me.\n""")
print("""The match
is going to
start today.\n""")
print(""" There are 3 CRs in our class\n""")
print("""Ronaldo
is a professional
football player.\n""")
print("""virat kohli is best cricketer in the world.\n""")


print("Error in Multi Line Statements shown when using single or double quotes\n")

#VARIABLES

a=3213252
print(a)
b='c'
print(b)
c=44458295.624562
print(c)
d=a*c
print(d)
e='BCA'
print(e)
f=32
f+=524
print(f)
g=2148
g-=6589
print(g)
h=20154
h/=36
print(h)
i=15
i%=78
print(i)
j=54
j//=65
print(j)
k=4
k*=25
print(k)


#Operators in Python


print("Implementation of different operators in Python\n")

print("Arithmetic Operators\n")

a=int(input("Enter the 1st number : "))
b=int(input("Enter the 2nd number : "))

print("Addition = ",a+b)
print("Subtraction = ",a-b)
print("Multiplication = ",a*b)
print("Division = ",a/b)
print("Modulus = ",a%b)
print("Exponentiation = ",a**b)
print("Floor Division = ",a//b,"\n")

print("Assignment Operators\n")

c=int(input("Enter a number : "))

c+=8
print("Assignment Addition = ",c)
c-=1
print("Assignment Subtraction = ",c)
c*=7
print("Assignment Multiplication = ",c)
c/=6
print("Assignment Division = ",c)
c%=3
print("Assignment Modulus = ",c)
c**=9
print("Assignment Exponentiation = ",c)
c//=2
print("Assignment Floor Division = ",c,"\n")

print("Relational Operators\n")

d=int(input("Enter 1st number : "))
e=int(input("Enter 2nd number : "))

f=d==e
print("1st number == 2nd number : ",f)
g=d!=e
print("1st number != 2nd number : ",g)
h=d<e
print("1st number < 2nd number : ",h)
i=d>e
print("1st number > 2nd number : ",i)
j=d<=e
print("1st number <= 2nd number : ",j)
k=d>=e
print("1st number >= 2nd number : ",k,"\n")

print("Logical Operators\n")

l=int(input("Enter 1st number : "))

m=l>1 and l<10
print (f"{l}>1 and {l}<10 : {m}")
n=l>1 or l>1054
print (f"{l}>1 or {l}<1054 : {n}")
o=not(l>1 and l<10)
print (f"not({l}>1 and {l}<10) : {o}\n")

print("Bitwise Operators\n")

p=int(input("Enter 1st number : "))
q=int(input("Enter 2nd number : "))

r=p&q
print("1st number & 2nd number : ",r)
s=p|q
print("1st number | 2nd number : ",s)
t=p^q
print("1st number ^ 2nd number : ",t)
u=~p
print("~ 1st number : ",u)
v=p<<q
print("1st number << 2nd number : ",v)
w=p>>q
print("1st number >> 2nd number : ",w,"\n")





print ("PATTERNS\n")
print ("*\n**\n***\n****\n*****\n")
print ("*****\n ****\n  ***\n   **\n    *\n")
print ("*****\n****\n***\n**\n*\n")
print ("**********\n ********\n  ******\n   ****\n    **\n   ****\n  ******\n ********\n**********\n")
print ("a\naa\naaa\naaaa\naaaaa\n")
print ("aaaaa\n aaaa\n  aaa\n   aa\n    a\n")
print ("aaaaa\naaaa\naaa\naa\na\n")
print ("aaaaaaaaaa\n aaaaaaaa\n  aaaaaa\n   aaaa\n    aa\n   aaaa\n  aaaaaa\n aaaaaaaa\naaaaaaaaaa\n\n")

print ("CIRCLE :\n")

radius1 = 3
area1=3.14*radius1*radius1
print ("Area of the circle is",area1,"cm^2\n")

peri1=2*3.14*radius1
print ("Perimeter of the circle is",peri1,"cm\n\n")

print ("RECTANGLE :\n")

length1 = 8
breadth1 = 3
area2=length1*breadth1
print ("Area of the rectangle is",area2,"cm^2\n")

peri2=2*(length1+breadth1)
print ("Perimeter of the rectangle is",peri2,"cm\n\n")

print ("SQUARE :\n")

length2 = 9
area6=length2*length2
print ("Area of the square is",area6,"cm^2\n")

peri4=4*(length2)
print ("Perimeter of the square is",peri4,"cm\n\n")

print ("TRIANGLE :\n")

side1 = 3
side2 = 4
side3 = 5
base = 4
height1 = 3
area3 = 0.5*(base*height1)
print ("Area of the triangle is",area3,"cm^2\n")

peri3 = side1+side2+side3
print ("Perimeter of the triangle is",peri3,"cm\n\n")

print ("CUBE :\n")

side4 = 7
area4 = 6*side4*side4
print ("Surface area of the cube is",area4,"cm^2\n")

vol1 = side4*side4*side4
print ("Volume of the cube is",vol1,"cm^3\n\n")

print ("CUBOID :\n")

side5 = 9
side6 = 3
side7 = 5
area5 = 2*((side5*side6)+(side6*side7)+(side5*side7))
print ("Surface area of the cuboid is",area5,"cm^2\n")

vol2 = side5*side6*side7
print ("Volume of the cuboid is",vol2,"cm^3\n\n")

print ("RHOMBUS :\n")

diagonal1 = 6
diagonal2 = 8
side8 = 9
area7 = 0.5*(diagonal1*diagonal2)
print ("Surface area of the rhombus is",area7,"cm^2\n")

peri5 = 4*side8
print ("Perimeter of the rhombus is",peri5,"cm\n\n")

print ("CYLINDER :\n")

radius2 = 6
height2 = 9
area8 = 2*3.14*radius2*height2*(radius2+height2)
print ("Surface area of the cylider is",area8,"cm^2\n")

vol3 = 3.14*radius2*radius2*height2
print ("Volume of the cylinder is",vol3,"cm^3\n\n")

print ("TABLE OF 7 :\n")
num = 7

for i in range(1, 11):
   print(num, 'x', i, '=', num*i)
print("\n\n")

x = 24
  
if x % 2 == 0:
    print(x,"Is Even Number\n")
else:
    print(x, "Is Odd Number\n")
    
y = 19
  
if y % 2 == 0:
    print(y,"Is Even Number\n")
else:
    print(y, "Is Odd Number\n")

print ("SPECIAL PATTERNS :\n")

print ("    *\n   * *\n  *   *\n *     *\n*********\n *     *\n  *   *\n   * *\n    *\n")

print ("    *\n   ***\n  * * *\n *  *  *\n*   *   *\n *  *  *\n  * * *\n   ***\n    *\n")

print ("    *\n   ***\n  *****\n *******\n*********\n *******\n  *****\n   ***\n    *\n")

print ("    *\n   * *\n  * *\n * *\n* *\n * *\n  * *\n   * *\n    *\n")





print("Name Printer\n")

name=input("Enter a name : ")
y=int(input("Enter a number : "))

for z in range(0 , y):
   print(name)
print("\n\n")


print("Calculator\n")
def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    return num1 / num2

print("Please select an operation : \n" \
        "1. Add\n" \
        "2. Subtract\n" \
        "3. Multiply\n" \
        "4. Divide\n")

select = int(input("Select operations from 1, 2, 3, 4 :"))

number1 = int(input("Enter first number: "))
number2 = int(input("Enter second number: "))

if select == 1:
    print(number1, "+", number2, "=",
                    add(number1, number2))

elif select == 2:
    print(number1, "-", number2, "=",
                    subtract(number1, number2))

elif select == 3:
    print(number1, "*", number2, "=",
                    multiply(number1, number2))

elif select == 4:
    print(number1, "/", number2, "=",
                    divide(number1, number2))
else:
    print("Invalid input")

print("\n")


print("Quadratic Equation Solver\n")

import cmath

a=int(input("Enter the first coefficient : "))
b=int(input("Enter the second coefficient : "))
c=int(input("Enter the third coefficient : "))

d = (b**2) - (4*a*c)

sol1 = (-b-cmath.sqrt(d))/(2*a)
sol2 = (-b+cmath.sqrt(d))/(2*a)

print("The solution are",sol1,"and",sol2)

print("\n")


print("Body Temperature Check")

name1=input("Enter your name : ")
temp=int(input("Enter your body temperature in Fahrenheit : "))

if(temp<98.6):
   print("Wrong temperature entered !\n")
elif(temp==98.6):
   print("You are healthy and fine !\n")
elif(98.6<temp<=102.4):
   print("You have mild fever !\n")
else:
   print("You have high fever !\n")




#Prime Number Check

a = int(input("Enter a number to check whether it is a Prime Number : "))
if a<=1:
    print(a,"is not a Prime Number .")
elif a ==2:
    print(a,"is a Prime Number .")
else :
  for i in range(2,a):
    if(a%i==0):
        print(a,"is not a Prime Number .")
        break
    else:
        print(a,"is a Prime Number .")
        break

#Reversing a Number

b = int(input("Enter a number to reverse it : "))
rev=0
while b > 0:
    rem=b%10
    rev=rev*10 + rem
    b = b//10
print("Reverse number is ",rev)

#HCF of 2 Numbers (1st Technique)

c = int(input("Enter 1st number to find HCF : "))
d = int(input("Enter 2nd number to find HCF : "))
while d!=0:
    c,d=d,c%d
print(f"The HCF is {c}")

#HCF of 2 Numbers (2nd Technique)

e = int(input("Enter 1st number to find HCF : "))
f = int(input("Enter 2nd number to find HCF : "))
if e > f:
   smaller = f
else:
   smaller = e
for j in range(1,smaller+1):
   if e%j==0 and f%j==0:
       hcf = j
print(f"The HCF of {e} and {f} is {hcf}.")

#Factors of a number

g = int(input("Enter a number to find its factors : "))
print(f"The factors of {g} are : ")
for k in range(1,g+1):
    if g%k==0:
        print(k)

#Automorphic Number

h = int(input("Enter a number to check whether it is Automorphic : "))        
square=h*h
str_num=str(h)
str_square=str(square)
if str_square.endswith(str_num):
   print(h,"is an Automorphic Number .")
else:
   print(h,"is not an Automorphic Number .")
        
#Harshad Number

i = int(input("Enter a number to check whether it is Harshad : "))
sum_of_digits=sum(int(digit) for digit in str(i))
if i%sum_of_digits==0:
    print(i,"is a Harshad Number .")
else:
    print(i,"is not a Harshad Number .")

#Perfect Number

j = int(input("Enter a number to check whether it is Perfect : "))    
sum_of_divisors=0
for a in range(1,j):
    if j%a==0:
        sum_of_divisors+=a
if sum_of_divisors==j:
    print(j,"is a Perfect Number .")
else:
    print(j,"is not a Perfect Number .")

#Strong Number

import math
k = int(input("Enter a number to check whether it is Strong : "))    
l=k
sum_of_factorials=0
while k>0:
    digit=k%10
    sum_of_factorials+=math.factorial(digit)
    k//=10
if sum_of_factorials==l:
    print(l,"is a Strong Number .")
else:
    print(l,"is not a Strong Number .")

#LCM of 2 Numbers

m = int(input("Enter 1st number to find LCM : "))
n = int(input("Enter 2nd number to find LCM : "))
o,p=m,n
while p!=0:
    o,p=p,o%p
lcm=(m*n)//o
print(f"The LCM of {m} and {n} is {lcm}. ")

#Abundant Number

q = int(input("Enter a number to check whether it is Abundant : "))    
divisors_sum=0
for a in range(1,q):
    if q%a==0:
        divisors_sum+=a
if divisors_sum>q:
    print(q,"is an Abundant Number .")
else:
    print(q,"is not an Abundant Number .")

#Friendly Pair

r = int(input("Enter 1st number to check whether it is Friendly Pair : "))
s = int(input("Enter 2nd number to check whether it is Friendly Pair : "))
sum_divisors_r=0
for i in range(1,r):
    if r%i==0:
        sum_divisors_r+=i
sum_divisors_s=0
for i in range(1,s):
    if s%i==0:
        sum_divisors_s+=i
if sum_divisors_r==s and sum_divisors_s==r:
    print(f"{r} and {s} form a friendly pair .")
else:
    print(f"{r} and {s} are not a friendly pair .")


#String Functions


str1="Python Language"
print(len(str1)) #len() function


str2="PyTHOn"
print(str2.lower()) #lower() function
print(str2.upper()) #upper() function


name1="Section A CS"
old="Section A"
new="Section B"
str3=name1.replace(old,new) #replace() function
print(name1)
print(str3)


name2=('Aman','Raman','Naman','Daman')
str4=' '.join(name2) #join() function
print(name2)
print(str4)


name3="Aman-Raman-Naman-Daman"
str5=name3.split('-') #split() function
print(name3)
print(str4)


str6="python is a programming language"
str7=str6.find("p") #find() function
str8=str6.find("i",5,15)
print(str7,str8)


str9="python is a programming language"
str10=str9.index("is") #index() function
str11=str9.index("p",5)
str12=str9.index("i",5,25)
print(str10)
print(str11)
print(str12)


str13="python"
str14="python123"
str15="12345"
str16="python@123"
str17="python 123"
print(str13.isalnum()) #isalnum() function
print(str14.isalnum())
print(str15.isalnum())
print(str16.isalnum())
print(str17.isalnum())


str18="python"
str19="python123"
str20="12345"
str21="python@123"
print(str18.isdigit()) #isdigit() function
print(str19.isdigit())
print(str20.isdigit())
print(str21.isdigit())


str22="python"
str23="python123"
str24="12345"
print(str22.isnumeric()) #isnumeric() function
print(str23.isnumeric())
print(str24.isnumeric())


str25="python"
str26="PytHOn"
str27="python 3.7.3"
print(str25.islower()) #islower() function
print(str26.islower())
print(str27.islower())


str28="python"
str29="PytHOn"
str30="python 3.7.3"
print(str28.isupper()) #isupper() function
print(str29.isupper())
print(str30.isupper())

#Tuple Functions

num1 = (1,2,3,4,5,6)
print("Length of tuple : ",len(num1))


num2 = (1,6,3,2,4,5)
lang1 = ('java','c','python','php')
print("Max of tuple : ",max(num2))
print("Max of tuple : ",max(lang1))


num3 = (6,4,3,5,1,2)
lang2 = ('java','c','python','php')
print("Min of tuple : ",min(num3))
print("Min of tuple : ",min(lang2))


num4 = (6,3,5,4,1,2)
print("Sum of tuple items :",sum(num4))


num5 = (1,3,2,4,6,5)
lang3 = ('java','c','python','php')
print(sorted(num5))
print(sorted(lang3))
print(sorted(num5,reverse = True))


str31 = "python"
tuple1 = tuple(str31)
print(tuple1)
num6 = [1,2,3,4,5,6]
tuple2 = tuple(num6)
print(tuple2)


num7 = (1,2,3,4,2,2,1,3,4,5,7,8)
cnt1 = num7.count(2)
print("Count of 2 is : ",cnt1)
cnt2 = num7.count(10)
print("Count of 10 is : ",cnt2)


lang4 = ('p','y','t','h','o','n','p','r','o','g','r','a','m')
print("Index of t is : ",lang4.index('t'))
print("Index of p is : ",lang4.index('p'))
print("Index of p is : ",lang4.index('p',3,10))

        


