from visual import *
from process import *
def main_menu(list_of_reviews):
    while True:
        print("\nPlease enter the letter which corresponds with your desired menu choice:\n   [A] View Data\n   [B] Visualise Data\n   [X] Exit")
        choice = input().lower()
        if choice == 'a':
            print("You have chosen option A - View Data")
            a_menu(list_of_reviews)
        elif choice == 'b':
            print("You have chosen option B - Visualise Data")
            b_menu(list_of_reviews)
        elif choice == 'x':
            break
        else:
            print("Please enter a valid choice")

def b_menu(list_of_reviews):
    print("\nPlease choose one of the following options\n   [A] Most reviewed Parks\n   [B] Park Ranking by Nationality\n   [C] Most Popular Month by Park")
    choice = input().lower()
    if choice == 'a':
        print("You have chosen option A - Most reviewed Parks")
        b_submenu_a(list_of_reviews)
    elif choice == 'b':
        print("You have chosen option B - Park Ranking by Nationality")
        b_submenu_b(list_of_reviews)
    elif choice == 'c':
        print("You have chosen option C - Most Popular Month by Park")
        b_submenu_c(list_of_reviews)

def a_menu(list_of_reviews):
    print("\nPlease enter one of the following options:\n   [A] View Reviews by Park\n   [B] Number of Reviews by Park and Reviewer Location\n   [C] Average Score per year by Park\n   [D] Average Score per year by Park by Reviewer Location")
    choice = input().lower()
    if choice == 'a':
        print("You have chosen option A - View Reviews by Park")
        a_submenu_a(list_of_reviews)
    elif choice == 'b':
        print("You have chosen option B - Number of Reviews by Park and Reviewer Location")
        a_submenu_b(list_of_reviews)
    elif choice == 'c':
        print("You have chosen option C - Average Score per year by Park")
        a_submenu_c(list_of_reviews)
    elif choice == 'd':
        print("You have chosen option D - Average Score per year by Park by Reviewer Location")
        a_submenu_d()
