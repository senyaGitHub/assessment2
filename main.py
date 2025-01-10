#import proccess
import tui
import os


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
            print(tui.data_file_path())
run()
