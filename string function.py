"""
string is a collection of characters and a character is a simple a symbol for example the english language
has 26 characters and computer don't deal with character the deal with binary number even though you may see characters on 
your screen internally it is stored and maniplated as combination of 0's and 1's
representation(''),(" "),(""" """) 
excessing the elememts in the string index and slicing"""

a='software/industry'
print(a[0:12])
print(a[2:17:3]) 

v='IT' '&'
print(type(v))

v1="ece" '&'
print(type(v1))

v2="""ists""" '&'
print(type(v2))

"""
string methods:
syntax: variable.name methods()"""

#upper():convert from lower to upper
w="python"
print(w.upper())
#lower():convert from upper to lower
w1="PYTHON"
print(w1.lower())

#count():this method is count the number of repeated words in a string 
m="i love pravi pravi"
print(m.count("pravi"))
#index method: this method is used to return the index position of a string
n="gopalapuram"
print(n.index('p'))

#strip method():this method is used to remove the space in a string 
s1=" this is my book "
print(len(s1))
print(s1)
s2=s1.strip()
print(len(s2))
print(s2)
#rstrip:it is used to remove the right side space in the string
s1="this is my book  "
print(len(s1))
print(s1)
s2=s1.rstrip()
print(len(s2))
print(s2)
#lstrip:it is used to remove the left side space in the string
s1="  i love lord shiva"
print(len(s1))
print(s1)
s2=s1.lstrip()
print(len(s2))
print(s2)

#fromate():then method in used to return the string in a automated/realformate

names=["raj","jai","arjun"]
for i in names:
      print("hi {} tinnava?".format(i)) 
      
#find method():which return -1 when the string element is not present
m="prashu"
print(m.find("a"))
print(m.find("p"))

#strat with ():start with given string it return true to when the startwith given string with exesiting string
n="i love lordshiva" 
print(n.startswith("i"))

#ends with():end with given string it return flase to when the startwith given string with exesiting string
m="i love python"
print(m.endswith("O"))
website=["amazon.com","myntra.in","ajo.in"]
in_website=[ ]
for i in website:
      if i.endswith("in"):
         in_website.append(i)
print(in_website)
#is alpha():in check if the all the character is string are alphabates are not it return the boolean values
print("openai".isalpha())#truefalse(contain number)
print("openai123".isalpha())#false(contain number)
print("open a".isalpha())#false

"""isalnum():checks if all character the stream alphanumeric that is:letter ,number"""
print("openai123".isalpha())#false
print("openai123".isalnum())#true
print("openai!".isalnum())#false
print("openai 123".isalnum())#false
#title():it just return the given string in a title formate
p="om namah shivaya"
print(p.title())
v="radha krishna"
print(v.title())
#split():it spilit the given string into list
k="hello"
print(k.split())
#join():if join the splited list into string
k1="  ".join(k)
print(k1)
"""
disctonary(): a disctonary  in python is delcrete  by encolsed a(,) 
comma separeted list of key value pairs using curly braces{ }
disctonary are muntable i.e: is we can change add and remove item from a disctonary that has been created
duplicate are not allowed, discinary can not have 2 items with same key
the value in the disctonary can be of any type while the keys must be immutable like number,tuple,list.
these means discinary are unique key sentive """
#creation of dicitonaries:
#1.empty dicitonary
c1={}
print(type(c1))
#key values
mydict={1:"arjun",2:"goa"}
print(type(mydict))
#acessing the elements in dicitonary : using the keys we can  get the values of dicitonary
d2={100:"sujii",200:"pav","phno":"6301680","place":"lolla"}
print (d2[100])
print (d2["place"])
#updating dicionary: we can use the keys updating dicitonary
d2[100]="praveena"
print(d2)
#dicionary method:to access the methods the 
#syntax:is varibalename.methodname():
m={"name":"raj","sno":1,"phno":6301680}
print(m)
print(m.get("name"))
print(m.get("sno"))
#keys(): this method is used to get only keys in a dictionary
print(m.keys()) 
#value():this method is used to retrive the value in adictionary
print(m.values())
#items():this method is used toget all the available items
print(m.items())
#updating dictionary into list():in this particular senario by converting the dictionary into list we
#can retive only keys
print(list(m))
#update():to update any new value pairs for an existing dictionary we use this update function
m.update({"food":"biryani"})
print(m)
#pop():this method is used to delete a keys in a dictionary
m.pop('sno')
print(m)
