import matplotlib.pyplot as plt
from process import *

def B_Submenu_A(reviews):
    ParkLocations =[]
    numberOfReviews =[]
    for review in reviews:
        if ParkLocations.count(review[4]) == 0:
            ParkLocations.append(review[4])
            numberOfReviews.append(1)
        else:
            numberOfReviews[ParkLocations.index(review[4])] += 1
    plt.pie(numberOfReviews,autopct = lambda pct: Label_On_Pie_Chart(pct, numberOfReviews), labels=ParkLocations)
    plt.show()

def Label_On_Pie_Chart(pct, allvalues): # This function is not mine however its only purpose is to make the pie chart look nicer
    absolute = int(pct / 100.*sum(allvalues))
    return "{:.1f}%\n({:d})".format(pct, absolute)

def B_Submenu_B(reviews):
    while True:
        print("\nPlease enter what park you would like to use: (Please only enter the location, ie for Disneyland Paris enter 'Paris' (case sensitive))")
        location = input()
        temp = get_all_reviews_for_park(location, reviews)
        count = temp[1]
        reviews_For_Park = temp[0]
        locations_Of_Reviews = []
        if location is not None:
            break
    if count == 0:
        print("No reviews found for that location, please try reentering the location.")
    else:
        total_score = []
        numberOfReviews = []
        for review in reviews_For_Park:
            if locations_Of_Reviews.count(review[3]) == 0:
                locations_Of_Reviews.append(review[3])
                numberOfReviews.append(1)
                total_score.append(int(review[1]))
            else:
                numberOfReviews[locations_Of_Reviews.index(review[3])] += 1
                total_score[locations_Of_Reviews.index(review[3])] += int(review[1])
        average_score =[]
        for location in locations_Of_Reviews:
            index = locations_Of_Reviews.index(location)
            average_score.append(total_score[index]/numberOfReviews[index])
            locations_Of_Reviews[index] = (location, (total_score[index] / numberOfReviews[index]))
        locations_Of_Reviews = sorted(locations_Of_Reviews, key=lambda tup: tup[1])
        Top10location = []
        Top10AverageScore = []
        for i in range(len(locations_Of_Reviews)):
            if i < 10:
                Top10location.append(locations_Of_Reviews[i][0])
                Top10AverageScore.append(locations_Of_Reviews[i][1])
            locations_Of_Reviews[i] = locations_Of_Reviews[i][0]
        plt.figure(figsize=(10,6))
        plt.bar(Top10location, Top10AverageScore)
        plt.title('Top 10 location average review For Park')
        plt.xlabel("Location of Reviews")
        plt.ylabel("Average Score")
        plt.tight_layout()
        plt.xticks(rotation=8)
        plt.show()

def B_Submenu_C(reviews):
    months_of_year = ["January","February","March","April","May","June","July","August","September","October","November","December"]
    print("\nPlease enter what park you would like to use: (Please only enter the location, ie for Disneyland Paris enter 'Paris' (case sensitive))")
    location = input()
    temp = get_all_reviews_for_park(location, reviews)
    count = temp[1]
    reviews_For_Park = temp[0]
    Average_score_for_Month = []
    if count == 0:
        print("No reviews found for that location, please try reentering the location.")
    else:
        for i in range(12):
            reviews_For_Month= get_all_reviews_for_month(i+1,reviews_For_Park)
            Average_score_for_Month.append(get_average_score(reviews_For_Month))
        plt.figure(figsize=(10, 6))
        plt.bar(months_of_year, Average_score_for_Month)
        plt.title("Average Score for Month")
        plt.xlabel("Month of Year")
        plt.ylabel("Average Score")
        plt.tight_layout()
        plt.xticks(rotation=8)
        plt.show()