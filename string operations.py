'''s="hello"
print(s.capitalize())      #capialise first letter

s="hello corona"
print(s.center(28,'&'))    #return string to the centre and replace gaps by any symbol(or anything)

s="india is my country. my country is a prosperous country"
print(s.count("country"))
a="is"
print(s.count(a,0,len(s)))             #noof times any substring occurs

s="rhutvij chiplunkar"
print(s.endswith("kar"))
print(s.endswith("h"))
print(s.endswith("j",0,7))             #to check the last occurence of letter(s) in a particuar string-returns TRUE or FALSE


s="kolhapur city"
print(s.startswith("k"))
print(s.startswith("c",9,len(s)))'''         #to check the starting occurence of letter(s) in a particuar string-returns TRUE or FALSE


'''a="        chips   $"
b="   &   chips           "
c="    chips   "
print(a.lstrip())                  #removespaces from LHS
print(b.rstrip())                  #removespaces from RHS
print(c.strip())'''                   #removespaces from both sides


'''str="corona virus is sprreading rapidly"
print(str.find('virus'))             #find-used to find string index from LHS
print(str.find("o"))                 #returns with first occurence of any letter(word)
print(str.find("z"))                 #if not present return with -1
print(str.find("i",0,13))'''            #(substring,start,end)



'''str="corona virus is sprreading rapidly"
print(str.index('virus'))             #find-used to find string index from LHS
print(str.index("o"))                 #returns with first occurence of any letter(word)
print(str.index("z"))                 #if not present return with value error
print(str.index("i",0,13))'''         #(substring,start,end)



'''str="corona virus is sprreading rapidly"
print(str.rfind("i"))                #find string from RHS
print(str.rfind("is"))
print(str.rfind(("z")))              #if not found return with -1
print(str.rfind("r",0,5))'''         #(substring,start,end)




'''str="corona virus is sprreading rapidly"
print(str.rindex("i"))               #find string from RHS
print(str.rindex("is"))
print(str.rindex(("z")))             #if not found return with value error
print(str.rindex("r",0,5))'''           #(substring,start,end)



'''a="jamesbond007"
print(a.isalnum())           #TRUE if every character is number or alphabet
b="james bond 007"
print(b.isalnum())'''          #FALSE even if space or symbol is included



'''a="rhutvij"
print(a.isalpha())         #TRUE if all characters are alphabets
b="9784"
print(b.isdigit())          # TRUE if all characters are digits
c="abcde"
print(c.islower())          #TRUE if all charcters are in lower case
d="ABCDEFGHIJKL"
print(d.isupper())          #TRUE if all charcters are in upper case
e="   "
print(e.isspace())'''          #TRUE if all characters are spaces


'''a="Otawane"
print(a.ljust(12,'#'))        #takes all characters to LHS & fills spaces with any given character (length,'filling char')
print(a.rjust(12,'$'))'''     #takes all characters to RHS & fills spaces with any given character (length,'filling char')


'''s='65948'
print(s.zfill(10))            #adds zero to the prefix to fulfill given length(if lenth is smaller than len("str") original string is printed)
t='rhutvij'
print(t.zfill(12))'''


'''u="HELLO WORLD"
print(u.lower())              #coverts all characers to lower case
v="hello india"
print(v.upper())              #coverts all characers to upper case
w="heLlo WOrlD WelCOMe"
print(w.lower())
print(w.upper())'''


'''str="Dog is a loyal animal"
print(max(str))               #returms alphabet with maximum alphabetical order
print(min(str))
b="sherlock"
print(min(b))'''

'''c="chiplunkar"
print(min(c))              #returms alphabet with minimum alphabetical order
print(max(c))'''           #returms alphabet with maximum alphabetical order


'''a="he is very famous person"
print(a.replace("very","most"))
b="hello hi hello hi hello hi hello hi"      
print(b.replace("h","k"))                     #replace particular character(s) by other character ('origial','replaced')
print(b.replace("hi","bye",3))'''                #('original','replaced',no of times replacement)


'''s="the corona virus outbreak is causing lot of deaths"
print(s.title())                       #convert string to title case
t="IndIa Is DeveLOPInG coUnTRy"
print(t.swapcase())'''                  #swap the case of every letter

'''a="abc def ghi jkl mno"
print(a.split(' '))                  #create a list of spring by considering separation element 
b="fhi:jud:swd:erf:dsq"
print(b.split(':'))'''                 #(string.split("separating character"))


'''str="20kolhpaur"
print(str.isidentifier())         #check whether string is identifier or not
str1="Indiana"                    #returns TRUE or FALSE
print(str1.isidentifier())'''

'''str="pict pune"
print(list(enumerate(str)))          #cresates list of dictionry containing keys=index & value=string character
a="corona virus china"
print(list(enumerate(a)))
print(enumerate(a))'''


'''a="MS dhoni was a great captain"
print('a' in a)                       #TRUE if particular letter(s) are present in given string otherwise FALSE
print('z'in a)
print('x' not in a)                   #TRUE if particular letter(s) are not present in given string otherwise FALSE (reverse of "IN")
print('c'not in a)'''


'''str="india is a great country"
if 'acg' in str:
    print("string is present")
else:
    print("string is absent")'''


#ASCII values
'''print(ord("A"))                        #ord function-used to give ASCII code for given character (charater to ASCII)
print(ord("b"))
print(ord("z")+ord("c"))
print(ord("&"))
print(ord("0"))
print(chr(66))                         #chr fuunction-used to give symbol/letter to ASCII code (ASCII to character)
print(chr(105))
print(chr(124))
print(chr(128))
print(chr(84))'''

#comparison operators
'''print("8">"6" )                      #All these are used to compare two given stings-(returns TRUE or FALSE) 
print("abc"=="abc")
print("aBC"=="ABc")
print("aBC"!="ABc")
print("abc">="pqr")
print("xy"<"yz")
print("defghi"<="klm")'''


#iterations of strings
'''a="python programming"        #using for loop
for i in a:
    print(i,end=" ")'''

'''b="object oriented programing"    #using while loop
k=0
while k<len(b):
    m=b[k]
    print(m,end=" ")
    k+=1'''


'''c="digital electronics"
for i in c:
    if i=="i":
        print(i,": present")
    else:
        print(i,": absent")'''



#string modyles in python
'''import string
print(string.digits)
print(string.hexdigits)
print(string.ascii_letters)
print(string.ascii_lowercase)
print(string.ascii_uppercase)
print(string.octdigits)
print(string.punctuation)
print(string.printable)
print(string.whitespace)



print('2' in string.hexdigits)
print('94' in string.digits)
print('A' in string.hexdigits)
print('~' in string.printable)
print('~' in string.punctuation)'''


#splitting of a string
'''str="Print words that start with s in this given statement"
for i in str.split():
    if i[0]=="s":
        print(i,end=" ")'''



'''str="Print words that start with s in this given statement"
L1=[]
L2=[]
for i in str.split():
    if i[0]=='w' or i[0]=='s':
        L1.append(i)
    else:
        L2.append(i)
print("L1=",L1)
print("L2=",L2)'''


#f-strings
'''country="INDIA"
state="Maharashtra"              #f-strings - used to substitute the values assigned to given variables
print(f"{country} is my country,I am from {state} state")

name="rhutvij"
sur="chiplunkar"
print(f"my name is {name} {sur}")'''


#format() operator
'''str="python programming"
print("i study {}".format(str))
print("i study {str1}".format(str1="coding"))           #format-used to add the values in sequence in given string
for i in range(0,10):
    print("the nos are {}".format(i))
for j in range(2000,2021,4):
    print("the leap years are {}".format(j))'''


#%operator
'''str="INDIA"
str2='country' 
print("%s is my %s"%(str,str2))                 %s operator-used to substitue value of tring vaiables

a='corona'
b="china"
print("%s virus was made in %s"%(a,b))'''


'''from string import Template
str=Template(" My name is $name $surname")
str1=str.substitute(name="rhutvij",surname="chiplunkar")    #templte-create a string template and substitute it further
print(str1)

a=Template("$name is a great $sport player. He has many $runs")
print(a.substitute(name="Virat Kohli",sport="cricket",runs="70 hundreds"))'''


'''a="Python "
b="rhutvij"
print(a.istitle())       #istitle-used to check if string is in title case or not
print(b.istitle())'''


#join funnction
'''str="#"
print(str.join(["i","am","from","kolhapur"])      #join-used to join the strings given in the list.
str1=" "
print(str1.join(["i","am","from","kolhapur"]))'''

#splitlines
'''str="programmin\nis\nvery\nimportant"
print(str.splitlines())             #splitlines-used to split the string and write in a list
print(str.splitlines(45))'''         #***if no is there in the bracket line breaks are included


#identity operators
'''print("python" is "python")     #is operator- TRUE if same string FALSE if not same string
print("python" is "bad")
print("python" is not "ok")     #is operator- TRUE if not same string FALSE if same string
print("abcd" is not "abcd")'''

#Logical operators
'''str="python"
str1="programming"
str2=""
print(str and str1)
print(str1 and str)
print(str and str2,":empty")
print(str2 and str1,":empty")
print(str or str1)
print(str1 or str)
print(str1 or str2)
print(str2 or str)
print(not str)
print(not str1)
print(not str2)'''

#string module capwords
'''import string
str="python\n\n programming\n"         #string.capwords- used to capitalize each word and then join the words
print(string.capwords(str))'''
