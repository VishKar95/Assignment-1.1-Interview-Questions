'''
TOPIC --->  DATA TYPES INTERVIEW QUESTIONS

Q.1. What are the key features of Python?
Ans) If it makes for an introductory language to programming, Python must mean something. These are its qualities:
Interpreted
Dynamically-typed
Object-oriented
Concise and simple
Free
Has a large community

--------------------------------------------------------------------------------------------------------------------------------------------------

Q.2. Differentiate between lists and tuples.
Ans) The major difference is that a list is mutable, but a tuple is immutable. Examples:
>>> mylist=[1,3,3]
>>> mylist[1]=2
>>> mytuple=(1,3,3)
>>> mytuple[1]=2
Traceback (most recent call last):

File “<pyshell#97>”, line 1, in <module>

mytuple[1]=2

TypeError: ‘tuple’ object does not support item assignment

Python Tuples vs Lists – A Detailed Comparison

--------------------------------------------------------------------------------------------------------------------------------------------------

Q.3. Explain the ternary operator in Python.
Ans)Unlike C++, we don’t have ?: in Python, but we have this:

[on true] if [expression] else [on false]

If the expression is True, the statement under [on true] is executed. Else, that under [on false] is executed.

Below is how you would use it:

>>> a,b=2,3
>>> min=a if a<b else b
>>> min
2

>>> print("Hi") if a<b else print("Bye")
Hi
--------------------------------------------------------------------------------------------------------------------------------------------------

Q.4. What are negative indices?
Ans) Let’s take a list for this.

>>> mylist=[0,1,2,3,4,5,6,7,8]
A negative index, unlike a positive one, begins searching from the right.

>>> mylist[-3]
6

This also helps with slicing from the back:

>>> mylist[-6:-1]
[3, 4, 5, 6, 7]
--------------------------------------------------------------------------------------------------------------------------------------------------

Q.5. Name four of the main data types in Python
Ans) Numbers, strings, lists, dictionaries, tuples, files, and sets are generally considered the main types of data. Types, None, and Booleans 
are sometimes also classified this way. The integer, floating-point, complex, fraction and decimal are numerical data types and simple strings 
and Unicode strings in Python 2 and text strings and byte strings in Python 3 are the types of string data types.

--------------------------------------------------------------------------------------------------------------------------------------------------

Q.6. What does immutable mean and what three types of Python core data types are considered immutable?
Ans) An immutable data type is a type of object which cannot be modified after its creation. Numbers, strings, and tuples in Python fall into this 
category. Although you cannot modify an immutable object in place, you can always create a new one by running an expression.

--------------------------------------------------------------------------------------------------------------------------------------------------

Q.7. What is meant by an Operator in Python?
Ans) These are the special symbols in python and are used to execute an Arithmetic or Logical computation. An operator alone cannot perform an
activity, it needs an Operand. What is an operand? An Operand is a value that the operator needs to complete a task.

Types of operators in Python:

We have multiple operators in Python, and each operator is subdivided into other operators. Let’s list them down and know about each operator in detail.

Arithmetic operators
Comparison operators
Assignment operators
Logical operators
Bitwise operators
Membership operators
Special operators
Identity operators
Membership operators

--------------------------------------------------------------------------------------------------------------------------------------------------

Q.8. Which operator has the highest precedence in Python?

Ans) () parentheses has the highest precedence in python.

--------------------------------------------------------------------------------------------------------------------------------------------------

Q.9. Which operator has the lowest precedence Python?

Ans) Logical OR has the lowest precedence in python.

--------------------------------------------------------------------------------------------------------------------------------------------------

Q.10. What is Floor Division Python?

Ans) The Floor Operator is used to make a Division that results in the whole number adjusted to the left in the number line.

ex: When 5 is divided by 2, the answer is 2.5

When you apply floor division to it, it becomes 2 (left side adjustment).

--------------------------------------------------------------------------------------------------------------------------------------------------

Q.11. Is there a "not equal" operator in Python?

Ans) Yes! We have Not equal operator in python, and it is used to compare two operands and returns True statement if they are Not equal, 
and False if they are Equal.
--------------------------------------------------------------------------------------------------------------------------------------------------

Q.12.When programming in Python operators with the same precedence are evaluated in which manner?
Ans) When two python operators have the same precedence, you use associativity to determine the order. Almost all operators have associativity 
of left to right. For example, multiplication and division have the same precedence. So, the operator on the left will be evaluated first.

--------------------------------------------------------------------------------------------------------------------------------------------------

Q.13. What are the two types of functions in Python?
Ans) There are two types of functions in Python: built-in functions and user-defined functions. Built-in functions are functions that are already
 defined in the Python language, such as the print() function. User-defined functions are functions that are created by the user, and they can 
 be created to do anything that the user wants them to do.
--------------------------------------------------------------------------------------------------------------------------------------------------

Q.14. Can you explain what a call graph is? How do you create one?
Ans) A call graph is a visual representation of the relationships between the various functions in a Python program. It can be used to help debug code, 
optimize code, and understand code flow. To create a call graph, you can use the pycallgraph library.

--------------------------------------------------------------------------------------------------------------------------------------------------

Q.15. When should you use anonymous functions and when should you use regular ones?
Ans) There is no definitive answer to this question, as it depends on the specific situation and what you are trying to accomplish. However, a general
a rule of thumb is that anonymous functions are best used for simple tasks that can be easily expressed in a single line of code. Regular functions,
on the other hand, are better suited for more complex tasks that require multiple lines of code.

--------------------------------------------------------------------------------------------------------------------------------------------------

Q.16. Do Python functions have return values? If yes, then how many can they have?
Ans) Yes, Python functions can have return values. They can have a single return value, or they can have multiple return values.

--------------------------------------------------------------------------------------------------------------------------------------------------

Q.17.  What is pass in Python?
Ans) Pass means, no-operation Python statement, or in other words it is a place holder in compound statement, where there should be a blank left and 
nothing has to be written there.

--------------------------------------------------------------------------------------------------------------------------------------------------

Q.18.  What Does The Continue Do In Python?
Ans) The continue is a jump statement in Python which moves the control to execute the next iteration in a loop leaving all the remaining instructions 
in the block unexecuted.
 
The continue statement is applicable for both the “while” and “for” loops.

--------------------------------------------------------------------------------------------------------------------------------------------------

Q.19.  When Should You Use The “Break” In Python? 
Ans) Python provides a break statement to exit from a loop. Whenever the break hits in the code, the control of the program immediately exits from the body of the loop.
 
The break statement in a nested loop causes the control to exit from the inner iterative block.

--------------------------------------------------------------------------------------------------------------------------------------------------

Q.20 What Is The Difference Between Pass And Continue In Python? 
Ans) The continue statement makes the loop to resume from the next iteration.
 
On the contrary, the pass statement instructs to do nothing, and the remainder of the code executes as usual.

--------------------------------------------------------------------------------------------------------------------------------------------------

'''