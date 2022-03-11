#!/usr/env/bin python3
print("Name: Sean Higgins")
password_database = {
    "Username":"dnedry",
    "Password":"please"}
command_database = {
    "reboot":"OK. I will reboot all park systems.",
    "shutdown":"OK. I will shutdown all park systems.",
    "done":"I hate all this hacker stuff."}
white_rabbit_object = 0;
counter = 0;

while (white_rabbit_object == 0 and counter < 3):
    input_user = input("Enter Username: ")
    input_password = input("Enter Password: ")
    if (input_user == password_database["Username"] and input_password == password_database["Password"]):
            white_rabbit_object = 1
            print("Hi, Dennis You're still the best hacker in Jurassic Park.")
            print(command_database.keys())
            input_command = input("Enter a command:")
            if (input_command == ""):
                print(command_database["reboot"])
            elif (input_command == "shutdown"):
                print(command_database["shutdown"])
            elif (input_command == "done"):
                print(command_database["done"])
            elif (input != "reboot","done","shutdown"):
                print("The Lysine Contigency has been put into effect") 
    elif (input_user != password_database['Username']) and \
        (input_password != password_database['Password']):
            counter += 1
            print(f"You did not say the magic word. {counter}")
            if counter == 3: 
                print("You did not say the magic word\n" * 25)
