Monthly Expense Tracker
This is a simple Django web application that helps users keep track of their monthly expenses. Each user can register for an account, log in, and manage their own expenses without interfering with others. The app is kept intentionally simple and clean, focusing on functionality over design.

Features:
•	User registration, login, and logout
•	Add new expenses with title, amount, and date
•	View a list of personal expenses
•	Delete expenses if needed
•	Monthly summary view showing total spending
•	Each user only sees their own expenses

Getting Started
Prerequisites
• Python 3 installed on your machine
• Virtual environment recommended
Installation
1.	Clone the repository to your local machine.
2.	Create and activate a virtual environment:
   python -m venv venv
   source venv/bin/activate   # On Windows use venv\Scripts\activate
3.	Install dependencies:
   pip install django
4.	Apply migrations:
   python manage.py migrate
5.	Run the server:
   python manage.py runserver
6.	Open the app in your browser at http://127.0.0.1:8000/

Usage
•	Register a new account under Accounts
•	Log in to access the expense tracker
•	Add, list, and delete expenses
•	View your monthly summary

Notes
This project is designed as a beginner-friendly Django capstone. It focuses on essential features without extra styling or external libraries. I'm working on future improvements.
