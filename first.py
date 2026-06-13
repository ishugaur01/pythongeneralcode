print("hello")
arr=[11,28,69,40]
sum=0
for i in arr:
    sum+=i
    print(sum)
    print(i)

print(sum) 
a=100   
if a%2==0:
    print("a is even")
else:
    print("a is odd")
arr1=[10,20,30,40]
arr2=[20,30,40,50]
# for x in arr1-1:
#     for y in arr2-1:
#         print(arr[x][y]+" ")

name=input()
print(name)
a=20
b=30
c=a+b
print(c)
a=int(input("enter your age"))
print(a)
i=10
j=100
arr=[10,23,45,67,77]
for i in arr:
    print(i)

a = int(input("enter first number"))
b = int(input("enter sec number"))
c = int(input("enter thirs number"))
if(a>b):
    print(a)
elif(b>c):
    print(b)
else:
    print(c)

# single line condition ternary operator
food= input("food")
print("sweet") if food=="jalbi" or food == "barfi" else print(" not sweet")
# clever if ternary operator
age = int(input("enter your age"))
vote = ("yes","no") [age>18]
print (vote)

sal = float(input("salray"))
tax =sal*(0.1,0.2) [sal<50000]
print(tax)