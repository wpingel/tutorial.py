#I am a single line comment.

"""
I am a multi line comment.
The sets of three quotation marks surround me.
"""

"""
The following series of commands were used in the shell to direct to the folder where this file is contained, and to subsequently call it.

import os									Import Python's OS module to use operating system dependent functionality.
os.getcwd()									Use the OS module function "getcwd" to return the current working directory.
os.chdir('C:\\foo')							Use the OS module function "chdir" to change the current working directory.
import subprocess							Import Python's subprocess module to use subprocess functions.
subprocess.call(['python', 'foo.py'])		Use the subprocess "call" function to call a Python script in the working directory.
"""

#From here on are sets of introductory code. Remove the multi-line comments to access each section.

#Basic while loop with some experimentation in the body. 
"""
a = 0																#Create variable a and assign value 0 to it.
while a < 10:														#Make while loop with the condition that a < 10 to repeat.
	print('There are', a, 'commas here:', a*',', end='\n' '\n')		#Indent content of while loop for convention and readability. String concatonate example. Can also concatonate via 'string' + 'string'. This is useful for x*'string' + y*'string'.
																	#End keyword is redundant here, and same functionality can be achieved through various methods, but demonstrates control of what is default \n (new line carriage). 
	a = a + 1														#Count variable a by 1 per iteration so that the while loop may complete.
"""


#Introductory if, else-if (elif), else case checking. Use of some functions like len for length and str to convert floats to strings. 
"""
x = float(input("Enter a float number: "))
if x < 0:
	print('Your number was', x, 'which is negative and has', len(str(x))-2, 'significant figures.')
elif x == 0:
	print('Your number was', x, 'congratulations.')
elif x > 0:
	if x < 100:
		print('You chose a standard 0-100 number. It was', x, 'which has', len(str(x))-1, 'significant figures.')
	elif x > 100:
		print('Nice. You choose a big number. It was', x, 'which has a whopping', len(str(x))-1, 'significant figures.')
else:
	print('Looks like you encountered some error. Maybe you didn\'t even put in a number?')
"""

