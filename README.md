# book_manager
An app that keeps track of book you have read and their rating and you can also delete or add the book
# Book List Web Application

This is a simple Flask web application that allows users to add books with their names, authors, and ratings to a CSV file and view the list of added books.

## Features
- Add books to a CSV file.
- Display the list of books from the CSV file.
- Simple form validation with Flask-WTF.

## Requirements

Before running the application, ensure that you have the necessary packages installed.

**setup**   
1. clone the repository
   ```bash
   git clone https://github.com/Pooja389/book_manager.git
   ```
2. Navigate into your project directory
   ```bash
   cd book_manager
   ```
### Install Dependencies

1. Create a virtual environment (optional but recommended):
   - On Windows:
     ```bash
     python -m venv venv
     ```
   - On MacOS/Linux:
     ```bash
     python3 -m venv venv
     ```

2. Activate the virtual environment:
   - On Windows:
     ```bash
     .\venv\Scripts\activate
     ```
   - On MacOS/Linux:
     ```bash
     source venv/bin/activate
     ```

3. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```
## run it
1. Run the application
   ```bash
   python main.py
   ```  
2. press ctrl +click on http://127.0.0.1:5000 in terminal
