import os

def welcome(width=100):
    # Calculate the number of dashes
    dashes = '-' * width

    # Print the dashes above
    print(dashes)

    # Calculate spaces for centering the title
    spaces = ((width - len("Records System")) // 2)
    print(" " * int(spaces) + "Records System")

    # Print the dashes below
    print(dashes)


def main_menu():
    #os.system('cls' if os.name == 'nt' else 'clear')
    while True:
        try:
            option = int(input('''
    Main Menu:
      [1] Load Different Data
      [2] Process Data
      [3] Visualise Data (Dashboard)
      [4] Export sales summary

      [5] Exit
    Select option:
    '''))
            if option in range(1,6):
                return option
            else:
                print("Choose an option between 1 and 4. ")
        except Exception as e:
            error("please enter a number.")
            pass



def data_file_path():
    default_path = "retail_sales_data.csv"
    user_input = input("Please enter the file path for the data file (default: retail_sales_data.csv): ")

    if not user_input.endswith('.csv'):
        error("The file path must end with '.csv'. Using the default path.")
        return default_path

    return user_input

def progress(operation, percent):
    if percent == 0:
        print()
        print(f'~~~ {operation.upper()}: STARTED ~~~')
    elif percent == 100:
        print(f'~~~ {operation.upper()}: COMPLETED ~~~')
        print()
    else:
        print(f'~~~ {operation.upper()}: IN PROGRESS ({percent}%) ~~~')


def error(error_msg):
    print(f"Error! {error_msg}")


def process_menu():
    os.system('cls' if os.name == 'nt' else 'clear')
    while True:
        try:
            option = int(input('''
        Select option:
        [1] Retrieve Total Number of Transactions
        [2] Retrieve unique store locations and product categories
        [3] Retrieve details of a specific transaction using the TransactionID
        [4] Retrieve all transactions for a specific store location
        [5] Retrieve all transactions for a specific product category
        [6] Group transactions by store location and calculate the total revenue
        per location.
        [7] Provide a summary of sales for a specific store location

        [0] Return to main menu
    '''))
            if option in range(0,8):
                return option
            else:
                print("Choose an option between 1 and 7. ")
        except Exception as e:
            error("please enter a number.")
            pass
