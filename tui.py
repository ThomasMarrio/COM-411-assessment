from visual import *
from process import *

def main_menu(reviews):
    while True:
        print("\nPlease enter the letter which corresponds with your desired menu choice:\n   [A] View Data\n   [B] Visualise Data\n   [X] Exit")
        choice = input().lower()
        if choice == 'a':
            print("You have chosen option A - View Data")
            A_menu(reviews)
        elif choice == 'b':
            print("You have chosen option B - Visualise Data")
            B_menu(reviews)
        elif choice == 'x':
            break
        else:
            print("Please enter a valid choice")

def B_menu(reviews):
    print("\nPlease choose one of the following options\n   [A] Most reviewed Parks\n   [B] Park Ranking by Nationality\n   [C] Most Popular Month by Park")
    choice = input().lower()
    if choice == 'a':
        print("You have chosen option A - Most reviewed Parks")
        B_Submenu_A(reviews)
    elif choice == 'b':
        print("You have chosen option B - Park Ranking by Nationality")
        B_Submenu_B(reviews)
    elif choice == 'c':
        print("You have chosen option C - Most Popular Month by Park")
        B_Submenu_C(reviews)

def A_menu(reviews):
    print("\nPlease enter one of the following options:\n   [A] View Reviews by Park\n   [B] Number of Reviews by Park and Reviewer Location\n   [C] Average Score per year by Park\n   [D] Average Score per year by Park by Reviewer Location")
    choice = input().lower()
    if choice == 'a':
        print("You have chosen option A - View Reviews by Park")
        A_Submenu_A(reviews)
    elif choice == 'b':
        print("You have chosen option B - Number of Reviews by Park and Reviewer Location")
        A_Submenu_B(reviews)
    elif choice == 'c':
        print("You have chosen option C - Average Score per year by Park")
        A_Submenu_C(reviews)
    elif choice == 'd':
        print("You have chosen option D - Average Score per year by Park by Reviewer Location")
        A_Submenu_D(reviews)
