"""
 Basics 1,2,3,4,5,6
"""





class Person:
  def __init__(mysillyobject, name, age):
    mysillyobject.name = name
    mysillyobject.age = age

  def myfunc(abc):
    print("Hello my name is " + abc.name)

p1 = Person("Harika", 21)
p1.myfunc()
