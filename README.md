# TravelX
An Algorithm that allows the user to optimize their trip.

Our algorithm is able to carry out the following task:
- It enables users to optimize their vacation based on the city they select and the number of days and hours they wish to spend doing tourism.
- All of these while taking into account the budget the user selects and an approximation of their hotel bill.

# Installation

- Python programming language (version 3.9)
- Libraries: In order for the program to run the user needs to download three libraries pandas, os and random.

- Download data.csv file (can be found in the repository)

After downloading and importing each city's information via csv file into Python, import the libraries and open the file travelx.py to execute the application.

# Data Description
- Our data set includes 9 cities, each with 30 attractions, as well as the category, duration, rating, and cost of each attraction.

**Source**: The data was collected from Tripadvisor https://www.tripadvisor.com/ .

The cities and categories of attractions included in this data are listed below:

<img width="321" alt="Data Summary" src="https://user-images.githubusercontent.com/94702966/144243252-2125e70e-3008-4620-bff8-9a8c7b1e1806.png">


# User Journey
User is welcomed "Hello welcome to TRAVELX , the perfect Itinerary Optimization App!"

A list of all the possible destinations is presented.

- **Input #1**: What city would you like to visit?

Algorithm prints "TRAVELX would like to ask you about your preferences to make the 
Right travel itinerary for you!" 

- **Input #2**: Would you like to tells us about your preferences? (yes or no)

If the user enters yes, the algorithm will ask the user to rate each category of attraction on a scale of 0 to 5, and it will then proceed to **Input #3**.
If the user enters no, they will proceed to **Input #3** directly.

- **Input #3**: How many days will you stay? (Algorithm can only accept trips of less than 10 days)
- **Input #4**: How many hours per day will you like to spend doing tourism? (Algorithm can only accept times between 0 and 16 hours). Even though it 
    recommends from 6 to 10 hours.
- **Input #5**: Will you use an hotel? (Yes or No)? 

If the user enters no, they will proceed directly to input 6.
If the user enters yes, it will first display the following message:
  TRAVELX cannot book you an Hotel. However, we can account for the average price of your Hotel
  
  Here at TRAVELX we have the following assumptions of hotel stars
  and their daily average price
  
  -1 star hotels have an average price of 45
  -2 stars hotels have an average price of 47
  -3 stars hotels have an average price of 55
  -4 stars hotels have an average price of 74
  -5 stars hotels have an average price of 182
  Important to highlight this Average Daily Rate (ADR) is taken from https://www.statista.com/statistics/750602/hotel-adr-in-spain-by-star-rating/
  
- **Input #5.1**: Write the number of stars that will have the hotel that you will use to accommodate your trip
This input only runs if you select that you will use an hotel. It then takes ADR for your hotel and calculates your total hotel cost.
- **Input #6**: What is your budget(€)?
Here if your budget is lower than your total hotel cost. It will make the user repeat the input 5 or input 6 (user choice). 
This will repeat until the the user changes the hotel or the budget and the budget covers at least the total hotel cost.

- **Final Output #1**: The algorithm will generate the itinerary that maximizes rating; the result will be divided by day and include all of the attractions for that day (including the hotel), as well as the total time and cost each day.
- **Final Output #2**: The algorithm outputs the average rating, total cost, and average amount of hours of tourism each day for the whole trip.
- **Input #6**: The user is prompted if he wants to run the program again.

If the user has selected yes, the program will be restarted from the beginning.
If the user enters no, the algorithm will respond, "TRAVELX thanks you for using our app!"


# Methods and Data Structures Used

- We used the **dynammic programming** as our programming method which through tabulation helps maximize a value (in this case ratings) under the constraint of the weight (which in this cases are the days of the trip and how much time every attraction takes).
- 
- We first used dataframe from pandas to filter the city that the user wanted and then from that dataframe create a csv. 
- From this csv, we used **lists** as data structures to store all of the cities' information (attractions, ratings of these attractions, and duration of these attractions, cost).

# Future additions to the code
- A program export the data automatically from travel reccommendation engines.
- Travel length, which is currently set to 10 days, should be lengthier. 
- Travelers with some long-duration activities may not be satisfied with the service. 
- Implement activities that, if maximized, will cover the whole iteration days of the voyagers.
- Implementation of costs inside the attractions. 
- Increment number of cities available for customers to visit
- Reservations and suggestions of restaurants and hotels. 
- Finally, we would also develop the loyalty program. This would mean some travelers will be assigned “secret locations”.

# Credits
  Arturo Camarena,
  Daniel Villalain,
  Edwin Marmolejos,
  Facundo Exposito,
  Francisco Jimenez,
  Sebastian Vasquez,
  






