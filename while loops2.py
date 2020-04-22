command=''
started=False
while command!='quit':
    command=input('>').lower()
    if command=='start':
        if started:
            print('car is already started')
        else:
            print('car started')
            started=True
    elif command=='stop':
        if not started:
            print('car is already stopped')
        else:
            print('car stopped')
            started=False
    elif command=='help':
        print('''
start-to start the car
stop-to stop the car
quit-to exit
        ''')
    elif command=='quit':
        print('to exit')
        break
    else:
        print('i do not understand that...')



