'''
1-1. Check an integer is even or odd
'''
import sys

def print_menu():
    print('1. Check Even or Odd')
    print('2. Show the following even or odd numbers')

def check_even_or_odd():
    num = input('Enter a number: ')
    validate(num)
    if int(num) % 2 == 0:
        print('{0} is even'.format(num))
    else:
        print('{0} is odd'.format(num))

def show_following_nines():
    num = input('Enter a number: ')
    validate(num)
    for i in range(1, 10):
        print(int(num) + 2*i)

def validate(a):
   if float(a).is_integer():
       return True
   else:
       print('Please enter an integer')
       sys.exit(-1)

if __name__ == '__main__':
    print_menu()
    choice = input('Which function would you like to do?: ')
    if choice == '1':
        check_even_or_odd()
    if choice == '2':
        show_following_nines()
