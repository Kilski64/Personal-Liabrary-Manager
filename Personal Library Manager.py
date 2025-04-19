entries = []

while True:
    print("Personal Library Manager")
    command = input("To add a book insert 'add', to delete a book insert 'delete', to show collection insert 'show books', to exit application insert 'exit': ")

    if command == 'add' or command == 'Add' or command == 'ADD':
        title = input("Insert the title of the book: ")
        author = input("Insert the name of the author: ")
        year = input("Insert the year of when the book was written: ")

        entry = {'Title': title, 'Author': author, 'Year': year}
        entries.append(entry)
        print(f"-- ENTRY ADDED --\nTitle: {entry['Title']}\nAuthor: {entry['Author']}\nYear: {entry['Year']}")

    elif command == 'delete' or command == 'Delete' or command == 'DELETE':
        try:
            print("-- All Entries --")
            for i, entry in enumerate(entries, 1):
                print(f"Entry {i}\nTitle: {entry['Title']}\nAuthor: {entry['Author']}\nYear: {entry['Year']}")

            del_entry = int(input("Which entry would you like to delete 'insert number corresponding to entry': "))

            if 1 <= del_entry <= len(entries):
                entries.pop(del_entry-1)
                print("Entry deleted.")
            else:
                print(f"Must be a number between 1 and {entries}.")
             
        except ValueError:
            print("Invalid command. Must be a number")

    elif command == 'show' or command == 'Show' or command == 'SHOW':
        print("-- All Entries --")
        for i, entry in enumerate(entries, 1):
            print(f"Entry {i}\nTitle: {entry['Title']}\nAuthor: {entry['Author']}\nYear: {entry['Year']}")

    elif command == 'exit' or command == 'Exit' or command == 'EXIT':
        while True:
            quit_app = input("Are you sure you would like to quit this application (Y/N)? ")

            if quit_app == 'Y' or quit_app == 'y':
                print("Goodbye. Hope to see you again.")
                exit()
            elif quit_app == 'N' or quit_app == 'n':
                break
            else:
                print("Invalid command.")
    
        
    else:
        print("Invalid command.")



    


    

