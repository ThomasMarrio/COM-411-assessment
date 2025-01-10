import csv
from visual import *
from tui import *
from process import *
reviews = []

def main_menu():
    while True:
        print("\nPlease enter the letter which corresponds with your desired menu choice:\n   [A] View Data\n   [B] Visualise Data\n   [X] Exit")
        choice = input().lower()
        if choice == 'a':
            print("You have chosen option A - View Data")
            A_menu()
        elif choice == 'b':
            print("You have chosen option B - Visualise Data")
            B_menu()
        elif choice == 'x':
            break
        else:
            print("Please enter a valid choice")

def B_menu():
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

def A_menu():
    print("\nPlease enter one of the following options:\n   [A] View Reviews by Park\n   [B] Number of Reviews by Park and Reviewer Location\n   [C] Average Score per year by Park\n   [D] Average Score per year by Park by Reviewer Location")
    choice = input().lower()
    if choice == 'a':
        print("You have chosen option A - View Reviews by Park")
        A_Submenu_A()
    elif choice == 'b':
        print("You have chosen option B - Number of Reviews by Park and Reviewer Location")
        A_Submenu_B()
    elif choice == 'c':
        print("You have chosen option C - Average Score per year by Park")
        A_Submenu_C()
    elif choice == 'd':
        print("You have chosen option D - Average Score per year by Park by Reviewer Location")

def A_Submenu_A():
    print("\nPlease enter what park you would like to see all the reviews for: (Please only enter the location, ie for Disneyland Paris enter 'Paris' (case sensitive))")
    location = input()
    count = 0
    for review in reviews:
        if review[4].__contains__(location):
            print(review)
            count += 1
    if count == 0:
        print("No reviews found for that location, please try reentering the location.")

def A_Submenu_B():
    print("\nPlease enter what park you would like to see the number of reviews for: (Please only enter the location, ie for Disneyland Paris enter 'Paris' (case sensitive))")
    park_location = input()
    print("Please enter the origin of the reviews you would like to see the number of: (Same rules apply)")
    review_location = input()
    count = 0
    for review in reviews:
        if review[3].__contains__(review_location) and review[4].__contains__(park_location):
            count += 1
    if count == 0:
        print("No reviews found for that location for that park, please try reentering the locations.")
    else:
        print(f"Disneyland {park_location} has {count} reviews from {review_location}.")

def A_Submenu_C():
    print("\nPlease enter what park you would like to see the average score for: (Please only enter the location, ie for Disneyland Paris enter 'Paris' (case sensitive))")
    location = input()
    print("Please enter the year you would like to see the average score for:")
    year = input()
    total = 0
    count = 0
    for review in reviews:
        if review[2].__contains__(year) and review[4].__contains__(location):
            total += int(review[1])
            count += 1
    average = total / count
    print(f"The Average Score for Disneyland {location} in {year} is {average}.")

def CSVloader():
    count = 0
    with open('disneyland_reviews.csv') as csvfile:
        csvreader = csv.reader(csvfile)
        for row in csvreader:
            if row == ["Review_ID","Rating","Year_Month","Reviewer_Location","Branch"]: # Prevents the headers from being added to the list of reviews
                continue # This skips the rest of the loop for only the current iteration
            reviews.append(row)
            count += 1
        print(f"Finished loading reviews, there are currently {count} reviews.")
    return reviews

def run():
    print("--------------------------\nDisneyland Review Analyser\n--------------------------")
    reviews = CSVloader()
    main_menu()

run()