from tui import *
from process import *

def run():
    print("--------------------------\nDisneyland Review Analyser\n--------------------------")
    main_menu(csv_loader())

run()