def cal():
    b=0
    for i in range(1,10):
        print('Enter no for Question',i )
        a=int(input())
        b=b+a
    print('Result',b)
cal()

while True:
    choice=input("Do you want to run again? ")
    if choice == 'y'or choice == 'yes' or choice == '':
        cal()
    else:
        print('Thanks for using the program')
        break