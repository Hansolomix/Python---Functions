# def greet( ):
#  return "Hello Kingsley "
# print( greet() )

# ==========

#  Function with parameters

def greet( names ):
  '''
  greets a person passed in an argument
  name: a name of a person to greet
  '''
  return f"Hello {names} , Good Morning"

print ( greet ("Felis"))
print ( greet ("Kinhgsley"))
print ( greet ("Adriana"))

help(greet)

# =========

'''
Arbitrary parameters
'''

def fruits( *names ):
  '''Accepts unknown number of fruit names and prints each of them
  *names: list of fruits
  '''
  
  # names are tuple
  for fruit in names:
   print( fruit )

fruits("Orange", "Banana", "Apple", "Grapes")

help(fruits)

# ============

'''
Keyword parameters
'''

# def greet ( name , msg ):
#     '''
#     this function greets a person with given message
#     name: person to greet
#     msg: message to greet person with
#     '''
    
#     return f"Hello {name} , {msg} "

# print ( greet( name="Kingsley", msg="Good morning!" ))
# print ( greet( msg="Good morning!",name= "Kingsley" ))

# help(greet)

# =========

'''
Arbitrary keyword parameters
'''

def person( **student ):
  # print( type(student))
  # print( student )

  for key in student:
    print ( student [key] )
  
# person ( fname= "Kingsley" , lname= "ijomah")
person ( fname= "Kingsley", lname="Ijomah", subject= "Python" )

#  ========

'''
Default parameters values
'''

def greet( name= "David" ):
    return f"Hello , {name} "

print(greet())
print(greet("Dayana"))

#  ======

'''
pass statement
'''

def greet():
  pass
  
  #  ========
  
'''
Recursion
'''''
  
def factorial_recursive( n ):

    '''
    Multiply a given number by every number less than itt down to 1 in a factorial way
    e.g if n is 5 then calculate 5*4*3*2*1 = 120
    '''
    
    if n == 1:
        return True
        
    else:
        return n* factorial_recursive (n-1) 
    
print( factorial_recursive(5))





    



