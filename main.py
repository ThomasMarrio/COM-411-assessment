import csv

def main_menu():
    while True:
        print("Please enter the letter which corresponds with your desired menu choice:\n   [A] View Data\n   [B]Visualise Data\n   [X]Exit")
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
    while True:
        print("Please choose one of the following options\n    [A] Most reviewed Parks\n    [B] Park Ranking by Nationality\n   [C] Most Popular Month by Park")
        choice = input().lower()
        if choice == 'a':
            print("You have chosen option A - Most reviewed Parks")
        elif choice == 'b':
            print("You have chosen option B - Park Ranking by Nationality")
        elif choice == 'c':
            print("You have chosen option C - Most Popular Month by Park")
        else:
            print("Please enter a valid choice")

def A_menu():
    while True:
        print("Please enter one of the following options:\n [A] View Reviews by Park\n   [B] Number of Reviews by Park and Reviewer Location\n  [C] Average Score per year by Park\n  [D] Average Score per year by Park by Reviewer Location")
        choice = input().lower()
        if choice == 'a':
            print("You have chosen option A - View Reviews by Park")
        elif choice == 'b':
            print("You have chosen option B - Number of Reviews by Park and Reviewer Location")
        elif choice == 'c':
            print("You have chosen option C - Average Score per year by Park")
        elif choice == 'd':
            print("You have chosen option D - Average Score per year by Park by Reviewer Location")
        else:
            print("Please enter a valid choice")

def CSVloader():
    reviews = []
    count = 0
    with open('disneyland_reviews.csv') as csvfile:
        csvreader = csv.reader(csvfile)
        for row in csvreader:
            if row == "Review_ID,Rating,Year_Month,Reviewer_Location,Branch": # Prevents the headers from being added to the list of reviews
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