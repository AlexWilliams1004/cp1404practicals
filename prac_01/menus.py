"""
Menus - CP1404 Practicals

    - Alex Williams 16.08.2024 -

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
menu = """(H)ello
(G)oodbye
(Q)uit"""
name = input("Enter name: ").title()
print(menu)
choice = input(">>> ").upper()
while choice != "Q":
    if choice == "H":
        print(f"Hello {name}")
    elif choice == "G":
        print(f"Goodbye {name}")
    else:
        print("Invalid message")
    print(menu)
    choice = input(">>> ").upper()
print("Finished.")
