import csv

reviews = []

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

def get_average_score(reviews):
    total_score = 0
    count = 0
    for review in reviews:
        total_score += int(review[1])
        count +=1
    average_score = total_score/count
    return average_score

def get_all_reviews_for_month(month,reviews):
    reviews_For_Month = []
    for review in reviews:
        if review[2].__contains__("-10"):
            if month == 10:
                reviews_For_Month.append(review)
        elif review[2].__contains__("-11"):
            if month == 11:
                reviews_For_Month.append(review)
        elif review[2].__contains__("-12"):
            if month == 12:
                reviews_For_Month.append(review)
        elif review[2].__contains__(f"-{month}"):
            reviews_For_Month.append(review)
    return reviews_For_Month

def get_all_reviews_for_park(location,reviews):
    count = 0
    reviews_For_Park = []
    for review in reviews:
        if review[4].__contains__(location):
            reviews_For_Park.append(review)
            count += 1
    return reviews_For_Park , count

def get_all_reviews_for_park_from_location(location,park,reviews):
    reviews_For_Park = []
    count = 0
    for review in reviews:
        if review[3].__contains__(location) and review[4].__contains__(park):
            count += 1
            reviews_For_Park.append(review)
    return reviews_For_Park , count

def A_Submenu_A(reviews):
    print("\nPlease enter what park you would like to see all the reviews for: (Please only enter the location, ie for Disneyland Paris enter 'Paris' (case sensitive))")
    location = input()
    count = 0
    for review in reviews:
        if review[4].__contains__(location):
            print(review)
            count += 1
    if count == 0:
        print("No reviews found for that location, please try reentering the location.")

def A_Submenu_B(reviews):
    print("\nPlease enter what park you would like to see the number of reviews for: (Please only enter the location, ie for Disneyland Paris enter 'Paris' (case sensitive))")
    park_location = input()
    print("Please enter the origin of the reviews you would like to see the number of: (Same rules apply)")
    review_location = input()
    count = get_all_reviews_for_park_from_location(review_location,park_location,reviews)[1]
    if count == 0:
        print("No reviews found for that location for that park, please try reentering the locations.")
    else:
        print(f"Disneyland {park_location} has {count} reviews from {review_location}.")

def A_Submenu_C(reviews):
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

def A_Submenu_D(reviews):
    pass
    # ParkLocations = []
    # reviews_For_Park = []
    # locations_of_reviews = []
    # reviews_for_location_for_park = []
    # average_score_for_park_from_location = []
    # for review in reviews:
    #     if ParkLocations.count(review[4]) == 0:
    #         ParkLocations.append(review[4])
    # for parks in ParkLocations:
    #         reviews_For_Park.append(get_all_reviews_for_park(parks,reviews))
    #         locations_of_reviews.append([])
    #         average_score_for_park_from_location.append([])
    #         index = ParkLocations.index(parks)
    #         for review in reviews_For_Park[index]:
    #             if locations_of_reviews[index].count(review[3]) == 0:
    #                 locations_of_reviews[index].append(review[3])
    #         for location in locations_of_reviews[index]:
    #             reviews_for_location_for_park.append(get_all_reviews_for_park_from_location(location,locations_of_reviews[index],reviews))
    #             average_score_for_park_from_location[index].append(get_average_score(reviews_for_location_for_park[locations_of_reviews.index(location)]))
    # for parks in ParkLocations:
    #     index = ParkLocations.index(parks)
    #     for location in locations_of_reviews[index]:
    #         index1 = ParkLocations.index(location)
    #         print(f"{parks} has average score {average_score_for_park_from_location[index][index1]} from {location}.")