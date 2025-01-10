from tui import *
from process import *

def run():
    print("--------------------------\nDisneyland Review Analyser\n--------------------------")
    reviews = CSVloader()
    main_menu(reviews)

run()