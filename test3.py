#This program simulates a simple car control system. It allows the user to start and stop the car, as well as request help for available commands. The program runs in a loop, continuously prompting the user for input until they choose to quit.
command = ""
started = False
while True:
    command = input("> ").lower()
    if command == "start":
        if started:
            print("car is already started!")
        else:
            started = True
            print("car started...")
    elif command == "stop":
        if not started:
            print ("car is already stopped!")
        else:
            started = False
            print("car stopped.")
    elif command == "help":
        print("""
start - to start the car
stop - to stop the car
quit - to exit
            """)
    elif command == "quit":
        break
    else:
        print("I don't understand that...")