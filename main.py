contacts = {}
while True:
 print("Choose any of the following options")
 print("\n1. Add Contact\n2. View Contacts\n3. Delete Contact\n4. Exit")
 choice = int(input("Enter your choice:"))
 if choice == 1:
  name = input("Enter contact name:")
  phone = input("Enter contact phone number:")
  contacts[name] = phone
  print(f"Contact {name} added")
 elif choice == 2:
  if contacts:
   for name, phone in contacts.items():
    print(f"{name}: {phone}")
  else:
   print("No contacts found")
 elif choice == 3:
   name = input("Enter contact name to delete:")
   if name in contacts:
    del contacts[name]
    print(f"Contact {name} deleted")
   else:
    print(f"Contact {name} not found")
 elif choice == 4:
  break 
 else:
  print("Invalid choice. Please try again")
