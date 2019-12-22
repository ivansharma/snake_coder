# Creator: Ivan Sharma.
# Date: 22nd December 2019.
# Desc: Ask the user to enter a number between 1 and 5 then print "hello world" that many times


number = input('Enter a number between 1 and 5:')
number = float(number)
if number < 1:
    print('Error.')
    quit()
elif number > 5:
    print('Error.')
    quit()
    #the first two if/elif statements can be combined into one.
elif number == 1:
    print('Hello World')
elif number == 2:
    print('Hello World')
    print('Hello World')
elif number == 3:
    print('Hello World')
    print('Hello World')
    print('Hello World')
elif number == 4:
    print('Hello World')
    print('Hello World')
    print('Hello World')
    print('Hello World')
elif number == 5:
    print('Hello World')
    print('Hello World')
    print('Hello World')
    print('Hello World')
    print('Hello World')


#I need to learn how to do this with loops.
    
