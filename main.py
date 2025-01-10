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
    while True:
         #draw menu from tui module
        option = tui.main_menu()
        if option == 1:
            # load data using path to a file and save to records
            tui.progress("Data loading", 0)
            records = (process.load_data(tui.data_file_path()))
            tui.progress("Data loading", 100)
        elif option == 2:
            process_option = tui.process_menu()
            if process_option == 1:
                tui.calculate_total_transactions(records)
            if process_option == 2:


run()
