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
    while True:
        try:
            option = int(input('''
    Main Menu:
      [1] Load Data
      [2] Process Data
      [3] Visualise Data
      [4] Exit
    Select option:
    '''))
            if option in range(1,5):
                return option
            else:
                print("Choose an option between 1 and 4. ")
        except Exception as e:
            error("please enter a number.")
            pass



def data_file_path():
    default_path = "retail_sales_data.csv"
    user_input = input("Please enter the file path for the data file (e.g., data/titanic.csv): ")

    if not user_input.endswith('.csv'):
        print("The file path must end with '.csv'. Returning the default path.")
        return default_path

    return user_input
