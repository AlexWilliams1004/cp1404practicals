"""
Menus

Pseudocode:
get name
print menu
get choice
while choice != Q
   if choice == H
       print "hello" name
   else if choice == G
       print "goodbye" name
   else
       print invalid message
   print menu
   get choice
print finished message
"""

MENU = "(H)ello\n(G)oodbye\n(Q)uit"
name = input("Enter name: ")
print(MENU)
choice = input(">>> ").upper()
while choice != "Q":
    if choice == "H":
        print(f"hello {name}")
    elif choice == "G":
        print(f"goodbye {name}")
    else:
        print("invalid message")
    print(MENU)
    choice = input(">>> ").upper()
print("Finished.")
