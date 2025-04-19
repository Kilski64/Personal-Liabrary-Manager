# Personal Library Manager

## Overview
This project is a command-line application written in Python, designed to manage a personal book collection. It uses a list of dictionaries (`entries`) to store book details (title, author, year), allowing users to add books, delete books by index, view the collection, or exit the program with a confirmation prompt (`Y/N`).

## Features
- **Add Books**: Users can add a book by typing `add` (case-insensitive), providing the title, author, and year, stored as a dictionary (e.g., `{'Title': '1984', 'Author': 'George Orwell', 'Year': '1949'}`).
- **Delete Books**: Users can remove books by typing `delete` (case-insensitive), viewing the numbered collection, and entering the number of the book to delete.
- **View Collection**: Users can display the book collection by typing `show books` (case-insensitive), showing each book’s title, author, and year.
- **Exit with Confirmation**: Users can exit by typing `exit` (case-insensitive), with a confirmation prompt (`Y/N`) to confirm or return to the main menu.

## Setup
1. **Prerequisites**:
   - Python 3.6 or later
2. **Clone the Repository**:

## Usage
1. **Run the Program**:
- Execute the script in your terminal or command prompt:
  ```
  python library_manager.py
  ```
2. **Interact with the Library Manager**:
- The program prompts: `To add a book insert 'add', to delete a book insert 'delete', to show collection insert 'show books', to exit application insert 'exit':`
- **Add a Book**: Type `add` (e.g., `add`, `Add`, or `ADD`), then enter the title (e.g., `1984`), author (e.g., `George Orwell`), and year (e.g., `1949`). The book is added to the collection.
- **Delete a Book**: Type `delete` (e.g., `delete`, `Delete`, or `DELETE`), view the numbered collection, and enter the number of the book to delete (e.g., `1` to delete the first book).
- **Show the Collection**: Type `show books` (e.g., `show`, `Show`, or `SHOW`) to view all books with their titles, authors, and years.
- **Exit**: Type `exit` (e.g., `exit`, `Exit`, or `EXIT`), then confirm by typing `Y` (or `y`) to quit, or `N` (or `n`) to return to the main menu.
3. **View Screenshots**:
- Screenshots of the program in action (e.g., adding a book, showing the collection) are in the `screenshots/` folder.

## File Structure
- `library_manager.py`: Python script containing the personal library manager application.
- `screenshots/`: Folder containing example screenshots (e.g., `add_book.png`, `show_collection.png`).
- `README.md`: This file.

## Limitations
- **Command-Line Only**: The application runs in the terminal with no graphical user interface (GUI).
- **Non-Persistent Storage**: Books are stored in memory and lost when the program exits (no file or database storage).
- **Case Sensitivity**: Commands are case-insensitive (e.g., `add`, `Add`, `ADD`), but users must follow prompts carefully to avoid errors (e.g., invalid numbers for deletion).
- **Basic Error Handling**: Invalid inputs (e.g., non-numeric input for deletion) are handled, but empty inputs for book details are not validated.
