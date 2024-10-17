'''a=10
print('Welcome to module')
def f1():
    print('in f1')
def f2():
    print('in f2')
def _f3():
    print('in f3')'''

def display(str):
    return f'This is {str}'

def add(a,b):
    return a+b
if __name__=='__main__':
    print(display('hello python'))
    print(add(4,5))