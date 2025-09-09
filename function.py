""" function is a block of code it is a executed when it is called in 
python to create function "def" keyword is used"""
"""syntax:def functionname():
                statement/function body
         function calling()"""
         
def arjun():
    print("good nigth")
arjun()

def mouni(a):
    print("this is value",a)
mouni(2025)
#note:1) the value that was passed into a function definition is called parameters
#2)the value that was passed into function calling is called orguments
#passing  parameterers arguments to a function

#multiple parameter: passing a multipe value to a function is called as multiple paameter function

def srujji(a,b):
    print("the result:",a+b)
srujji(143,246)

def pravi(v):
    print(v)
pravi(45.78)
#arbitary argument(*): arbitary argument is an argument  which is denoted by (*) which takes multiple argument 
#per a  single parameter when return  result in form of touple 
def function(*s):#the only one  argument 
       print(s)
       function (11,20,30)  
#key arguments :
#  key word  argument  is a function  which takes single parameter for 
#multiple arguments  in the form of key value pairs so that the outout is dictionary formate
#key args():
def function2 (*name):
    print("hi",name)
    #function2 (name:"sruji",place:"rjy")

#nested function :A function with in a function is called nested function 
#def outer function ():
#    print ("outer function staement")
# def inner  function ():
#    print ("inner function statement")
#   innerfunction ()
#outer function
