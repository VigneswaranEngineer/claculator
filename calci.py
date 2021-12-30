def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    return a/b

print('select operation')
print('1.Add')
print('2.Subtract')
print('3.Multiply')
print('4.division')

while True:
    choice = input('enter your choice:')

    if choice in ('1','2','3','4'):
        num1 = float(input('enter a first number:'))
        num2 = float(input('enter a second number:'))

        if choice == '1':
            print(num1,'+',num2,'=',add(num1,num2))
        elif choice == '2':
            print(num1,'-',num2,'=',sub(num1,num2))
        elif choice == '3':
            print(num1,'*',num2,'=',mul(num1,num2))
        elif choice == '4':
            print(num1,'/',num2,'=',div(num1,num2))

        next_step = input('do you want to continue calculation?(yes/no)')
        if next_step == 'no':
                  print('think for using calculator')
                  break;
    else:
        print('invalid operation')

