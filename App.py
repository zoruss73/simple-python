command = ""
start = True

while command != 'QUIT':
    command = input('> ').upper()

    if command == 'START' or command == 'STOP' or command == 'QUIT' or command == 'HELP':
        if command == 'HELP':
            print("start - to start the car")
            print("stop - to stop the car")
            print("quit - to  quit")
        elif command == 'START':
            if start:
                print('Car started...Ready to go!')
                start = False
            else:
                print('Car already started')
        elif command == 'STOP':
            if not start:
                print('Car stopped.')
                start = True
            else:
                print('Car already stopped.')
    else:
        print("I don't understand that.")
