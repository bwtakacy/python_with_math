'''
1-2. Multiplication table printer
'''
def multi_table(a, b):
    for i in range(1, b+1):
        print('{0} x {1} = {2}'.format(a, i, a*i))

if __name__ == '__main__':
    a = input('Enter a number: ')
    b = input('How many?: ')
    multi_table(float(a), int(b))
