print("hello world")
print('IN THIS PROGRAM WE WILL CREATE A PYTHON PROGRAM TO CALCUTIONS')
print("enter 2 numbers")
x=int(input())
y=int(input())
answer = 0
print("choose any of these option (+,-,*,/) ")
option=input()
if option == '+':
  answer=x+y
elif option == '-':
  answer=x-y
elif option == '*':
  answer=x*y
elif option == '/':
  answer=x / y
else:
  print("wrong option")

print(x,option,y,":",answer)


