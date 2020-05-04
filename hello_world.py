# Variables and simple data types
# Chapter 1 #
# message = 'hello world' #message is a variable
# print(message)

# message = 'hello python crash course'
# print(message)

# message = 'testing error mesage'
# print(mesage)

# message = 'testing error message again'
# print(message)

# traceback is a record of where the interpreter ran into trouble when trying to execute your code

#Changing Case in a string with methods

# name = 'ada lovelace'
# print(name.title())
# print(name.upper())
# print(name.lower())#lower method is useful for storing data 

#Method is an action that python can perform on a piece of data

#using variables in strings
#
# In some situations you will want to use variables inside a string. Example you want 
# to represent someones first and last name.
# 
# To insert a variable's value into a string, place the letter f immediately before the opening
# quotation mark#

# first_name = 'ada'
# last_name = 'lovelace'
# full_name = f'{first_name} {last_name}'
# print(full_name)
#
# f-strings: f is for format, because python formats strings by replacing the name of any variable
# in braces with it's value, the output from the previous code is
# 
# With f-strings you can compose complete messages using the information associated with a vriable,
# as shown here:
# print(f'Hello,{full_name.title()}!'
# 
# You can also use f-strings to compose a message, and then assign the entire message to a variable
# message = f'hello, {full_name.title()}!
# print(message)#

# print(f'Hello,{full_name.title()}!')

# message = f'Hello, {full_name.title()}!'
# print(message)

#
# Adding Whitespace to strings with tabs or newlines
# 
# Whitespace refers to any nonprinting character, such as spaces, tabs, abd end-of-line symbols.
# Whitespace can be used to organize ones output so it is easier for users to read
# 
# To add a tab to your text, use the character combination \t#

# print('Python')
# print('\tPython')

#
# To add a newline in a string, use the character combination \n:#
# print('Languages: \nPython\nC\nJavascript')
# print('Languages: \tPyhton\tC\tJavascript\ntesting')


# print('Languages: \n\tPyhton\n\tC\n\tJavascript')
# ^the \n\t means that you want to start a newline(\n) and enter a new tab (\t)
# #


#
# .rstrip() removes whitespaces on the right
# .lstrip() removes whitespaces on the left
# .strip() removes whitespaces overall#

#
# Avoiding Syntax Errors with Strings
# 
# How to use single and double quotes correctly#

#apostrophe within double quotes
# message = "one of python's strengths is its diverse community."
# print(message)
#no problem/no error messages

#apostrophe with single quotes
# message = 'one of python's strengths is its diverse community' 
# print(message)
#issue python does not recognize it as valid python code
