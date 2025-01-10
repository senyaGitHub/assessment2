#import proccess
import tui
import process
import os

source = []

def run():
    #data is stored in array
    global records

    # clearing a terminal
    os.system('cls' if os.name == 'nt' else 'clear')
    tui.welcome()
    records = (process.load_data(tui.data_file_path()))
    while True:
         #draw menu from tui module
        option = tui.main_menu()
        if option == 1:
            # load data using path to a file and save to records
            tui.progress("Data loading", 0)
            records = (process.load_data(tui.data_file_path()))
            tui.progress("Data loading", 100)
        elif option == 2:

            #here its a bit of a mess with nested if statments most of it is error checks
            process_option = tui.process_menu()
            if process_option == 1:
                tui.calculate_total_transactions(records)
            if process_option == 2:
                tui.get_unique_store_locations_and_categories(records)
            if process_option == 3:
                transaction_id = input("Please input TransactionID: ")
                if transaction_id == '':
                    tui.error("Empty string detected, please enter transaction_id. ")
                if tui.get_transaction_details_by_id(records, transaction_id) == None:
                    tui.error("Uknown error, possibly wrong input or exceded transaction id?")
                else:
                    print(tui.get_transaction_details_by_id(records, transaction_id))
            if process_option == 4:



run()
