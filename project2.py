# Contact management system- Add, Search, Delete
import json
def add_person(): 
    name = input("name: " ) 
    age = input("Age: ") 
    email = input("Email: ")
    person = { 
        "name": name, 
        "age": age, 
        "email": email,
        }
    return person 


def display_people(people): 
    for i, person in enumerate(people): 
        print(i+1, "--", person["name"], " | ", person["age"], " | ", person["email"] )



def delete_contact(people): 
    if not people: 
        print("Add person first, the list is empty")
        return

    for i, person in enumerate(people): 
        print(i+1, "--", person["name"], " | ", person["age"], " | ", person["email"] )
    while True: 
        try: 
            number = input("Enter the number you want to delete \n")
            number = int(number) 
            if number <= 0 or number > len(people): 
                print("Invalid number, Out of range. Try again.")
            else: 
                break 
        except: 
            print("Invalid number")

    people.pop(number - 1)

def search(people): 
    search_name = input("Search for a name: ").lower()
    results = [] 

    for person in people: 
          name = person["name"] 
          if search_name in name.lower(): 
              results.append(person)
    
    display_people(results)

with open("contacts.json", 'r') as f: 
    people = json.load(f)["contacts"]


print("Hi, welcome to the contact management system")
while True: 
    command = input("You can 'Add', 'Delete' or 'Search' and 'q' for quit \n").lower()
    
    if command == "add":
        person = add_person() 
        people.append(person)
        print("Person Added!")
    elif command == "delete": 
        delete_contact(people)
        print("Person deleted")
    elif command == "search": 
        search(people)
    elif command =='q': 
        break
    else: 
        print("invalid command") 

    print(people)

with open("contacts.json", 'w') as f: 
    json.dump({"contacts": people}, f)
