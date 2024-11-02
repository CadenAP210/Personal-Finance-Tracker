import csv
import os
from datetime import datetime
import matplotlib.pyplot as plt
import pandas as pd

# Define the CSV file to store expenses
EXPENSES_FILE = 'expenses.csv'

# Function to initialize the CSV file if it doesn't exist
def initialize_csv():
    if not os.path.exists(EXPENSES_FILE):
        with open(EXPENSES_FILE, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Date', 'Category', 'Amount'])

# Function to add an expense
def add_expense(date, category, amount):
    with open(EXPENSES_FILE, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([date, category, amount])

# Function to view expenses
def view_expenses():
    with open(EXPENSES_FILE, mode='r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip header
        for row in reader:
            print(row)

# Function to summarize expenses by category
def summarize_expenses():
    df = pd.read_csv(EXPENSES_FILE)
    summary = df.groupby('Category')['Amount'].sum()
    print(summary)

# Function to visualize expenses
def visualize_expenses():
    df = pd.read_csv(EXPENSES_FILE)
    summary = df.groupby('Category')['Amount'].sum()
    
    # Bar chart
    summary.plot(kind='bar', title='Expenses by Category')
    plt.ylabel('Amount')
    plt.xlabel('Category')
    plt.show()

# Main function to run the application
def main():
    initialize_csv()
    
    while True:
        print("\nPersonal Expense Tracker")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Summarize Expenses")
        print("4. Visualize Expenses")
        print("5. Exit")
        
        choice = input("Choose an option: ")
        
        if choice == '1':
            date = input("Enter date (YYYY-MM-DD): ")
            category = input("Enter category: ")
            amount = float(input("Enter amount: "))
            add_expense(date, category, amount)
            print("Expense added successfully!")
        
        elif choice == '2':
            print("Expenses:")
            view_expenses()
        
        elif choice == '3':
            print("Expense Summary:")
            summarize_expenses()
        
        elif choice == '4':
            visualize_expenses()
        
        elif choice == '5':
            print("Exiting the application.")
            break
        
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
