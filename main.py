#import proccess
import tui
import os
import process

source = []

def run():
    global records

    # clearing a terminal
    os.system('cls' if os.name == 'nt' else 'clear')
    tui.welcome()
    while True:
         #draw menu from tui module
        option = tui.main_menu()
        os.system('cls' if os.name == 'nt' else 'clear')
        if option == 1:
            # load data using path to a file and save to records
            records = (process.load_data(tui.data_file_path()))

run()
