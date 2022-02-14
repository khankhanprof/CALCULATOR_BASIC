from art import logo
from os import name,system
#to print calc logo
print(logo)
#to refresh screen for new calculation
def clear():
  if name=='nt':
    _=system('cls')
  else:
    _=system('clear')

def add(n1,n2):
  return n1+n2
def subract(n1,n2):
  return n1-n2
def multiply(n1,n2):
  return n1*n2
def divide(n1,n2):
  return n1/n2

opt={ "+":add ,
"-":subract ,
"*":multiply ,
"/":divide }



n1=int(input("enter first number: "))
a=True
while a:
  operation1=input("enter operation(+,-,*,/):")
  n2=int(input("enter second number: "))
  calc1=opt[operation1]
  answer=calc1(n1,n2)
  print(f"{n1}{operation1}{n2}={answer}")
  choice=input("\'y\'- to continue , \'n\'-to refresh calculation,\'b\'-to exit")
  if choice=="y":
    n1=answer
  elif choice=="n":
    clear()
    n1=int(input("enter first number: "))
    a=True
  else:
    a=False
    



  
