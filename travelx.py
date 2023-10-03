import pandas as pd
import os
import random

def itinerary_optimization(W, wt, val, n, attractions, cost, cost_constraint):
    K = [[0 for w in range(W + 1)]
         for i in range(n + 1)]

    for i in range(n + 1):
        for w in range(W + 1):
            if i == 0 or w == 0:
                v = ""
                c = 0
                K[i][w] = 0, v, c
            elif wt[i - 1] <= w:

                cond1 = val[i - 1], attractions[i - 1], cost[i - 1]
                cond2 = [K[i - 1][w - wt[i - 1]][0], K[i - 1][w - wt[i - 1]][1], K[i - 1][w - wt[i - 1]][2]]

                first_option = cond1[0] + cond2[0], cond1[1] + cond2[1], cond1[2] + cond2[2]
                second_option = [K[i - 1][w][0], K[i - 1][w][1], K[i - 1][w][2]]

                maximum = max(first_option[0], second_option[0])
                if maximum == first_option[0]:
                    K[i][w] = maximum, first_option[1], first_option[2]

                else:
                    K[i][w] = maximum, second_option[1], second_option[2]
            else:

                value = K[i - 1][w]

                K[i][w] = value

    res = K[n][W][1]


    filtered_K = []

    for i in range(n + 1):
        for w in range(W + 1):
            if K[i][w][2] <= cost_constraint:
                filtered_K.append(K[i][w])


    filtered_K = set(filtered_K)

    filtered_K2 = []
    for i in filtered_K:
        if i[0] != 0.0 or i[2] != 0.0:
            filtered_K2.append(i)


    filtered_K2 = sorted(filtered_K2, key=lambda tup: tup[0], reverse=True)

    return res, filtered_K2





def city_error_handling(city_input):
    city_input = city_input.capitalize()
    city_input = city_input.strip()
    return city_input


def filter_adjust_data(city_input, travel):
    print(travel, "would like to ask you about your preferences to make the \n"
                  "Right travel itinerary for you! \n")

    choices = ['yes', 'no']
    error_msg = "Invalid input. Try again. Answer 'Yes' or 'No"
    error_msg = (color.RED + color.BOLD + error_msg + color.END)
    question = "Would you like to tells us about your preferences? (yes or no) "

    choice = get_choice(choices, question, error_msg)

    first_input = choice
    first_input.lower()

    df = pd.read_csv('dataset.csv')

    newdf = df[(df['City'] == city_input)]

    invalid_input = "Invalid input. Try again. Enter number from 0 to 5"
    invalid_input = (color.RED + color.BOLD + invalid_input + color.END)
    if first_input == "yes":
        choices = ["0", "1", "2", "3", "4", "5"]
        question = "- From 0 to 5 how much do you like Nightlife "

        night_life = get_choice(choices, question, invalid_input)
        night_life = float(night_life)

        question2 = "- From 0 to 5 how much do you like Landmarks "
        landmarks = get_choice(choices, question2, invalid_input)
        landmarks = float(landmarks)

        question3 = "- From 0 to 5 how much do you like Spas and Wellness "
        spa_wellness = get_choice(choices, question3, invalid_input)
        spa_wellness = float(spa_wellness)

        question4 = "- From 0 to 5 how much do you like Fun and Games "
        fun_games = float(get_choice(choices, question4, invalid_input))

        question5 = "- From 0 to 5 how much do you like Museums "
        museums = float(get_choice(choices, question5, invalid_input))

        question6 = "- From 0 to 5 how much do you like Classes and Workshop "
        classes_workshop = float(get_choice(choices, question6, invalid_input))

        question7 = "- From 0 to 5 how much do you like Nature and Parks "
        nature_parks = float(get_choice(choices, question7, invalid_input))

        question8 = "- From 0 to 5 how much do you like Boat Tours and WaterSports "
        boattours_waterSports = float(get_choice(choices, question8, invalid_input))

        question9 = "- From 0 to 5 how much do you like Casinos "
        casinos = float(get_choice(choices, question9, invalid_input))

        question10 = "- From 0 to 5 how much do you like Water and Amusement Parks "
        water_amusementPark = float(get_choice(choices, question10, invalid_input))

        question11 = "- From 0 to 5 how much do you like Zoo and Aquariums "
        zoo_aquariums = float(get_choice(choices, question11, invalid_input))

        cond = df['Category'] == "Night Life"
        df.loc[cond, 'Rating'] = df['Rating'] * (0.4 + 2 * (night_life / 10))

        cond = df['Category'] == "Landmarks"
        df.loc[cond, 'Rating'] = df['Rating'] * (0.4 + 2 * (landmarks / 10))

        cond = df['Category'] == " Spas and Wellness"
        df.loc[cond, 'Rating'] = df['Rating'] * (0.4 + 2 * (spa_wellness / 10))

        cond = df['Category'] == "Fun and Games"
        df.loc[cond, 'Rating'] = df['Rating'] * (0.4 + 2 * (fun_games / 10))

        cond = df['Category'] == "Museums"
        df.loc[cond, 'Rating'] = df['Rating'] * (0.4 + 2 * (museums / 10))

        cond = df['Category'] == "Classes and Workshop"
        df.loc[cond, 'Rating'] = df['Rating'] * (0.4 + 2 * (classes_workshop / 10))

        cond = df['Category'] == "Nature and Parks"
        df.loc[cond, 'Rating'] = df['Rating'] * (0.4 + 2 * (nature_parks / 10))

        cond = df['Category'] == "BoatTours and WaterSports"
        df.loc[cond, 'Rating'] = df['Rating'] * (0.4 + 2 * (boattours_waterSports / 10))

        cond = df['Category'] == "Casinos"
        df.loc[cond, 'Rating'] = df['Rating'] * (0.4 + 2 * (casinos / 10))

        cond = df['Category'] == "Water and AmusementPark"
        df.loc[cond, 'Rating'] = df['Rating'] * (0.4 + 2 * (water_amusementPark / 10))

        cond = df['Category'] == "Zoo and Aquariums"
        df.loc[cond, 'Rating'] = df['Rating'] * (0.4 + 2 * (zoo_aquariums / 10))

    csv_name = city_input + '.csv'
    newdf.to_csv(csv_name, header=False)

    return csv_name


def read_data_city(csv_name):
    infileName = csv_name
    infile = open(infileName, "r")
    attractions = []
    values = []
    weights = []
    final_attractions = []
    cost_list = []
    for line in infile:
        entry = line.split(",")

        attraction = entry[2]
        attractions.append(attraction)
        hours = int(entry[4])
        weights.append(hours)
        ratings = float(entry[5])
        values.append(ratings)
        cost = float(entry[6])
        cost_list.append(cost)

    for i in attractions:
        x = i + ";"
        final_attractions.append(x)
    infile.close()

    return final_attractions, values, weights, cost_list


def file_remove(csv_name):
    file = csv_name
    if (os.path.exists(file) and os.path.isfile(file)):
        os.remove(file)

    else:
        print(file, "file not found")


def hours_by_attraction(csv_name, attraction):
    final_attractions, values, weights, cost_list = read_data_city(csv_name)

    for attrac in final_attractions:
        if attrac == attraction:
            index = final_attractions.index(attraction)
            return weights[index]


def itinerary_attrac_hours(csv_name, itinerary):
    hours_itinerary = []

    for attrac in itinerary:
        attrac = attrac + ';'
        hours = hours_by_attraction(csv_name, attrac)
        hours_itinerary.append(hours)

    hours_itinerary = list(filter(None, hours_itinerary))
    return hours_itinerary


def cost_by_attraction(csv_name, attraction):
    final_attractions, values, weights, cost_list = read_data_city(csv_name)

    for attrac in final_attractions:
        if attrac == attraction:
            index = final_attractions.index(attraction)
            return cost_list[index]


def itinerary_attrac_cost(csv_name, itinerary):
    cost_itinerary_list = []
    for attrac in itinerary:
        attrac = attrac + ';'
        cost = cost_by_attraction(csv_name, attrac)
        cost_itinerary_list.append(cost)

    return cost_itinerary_list


def join_attrac_hours_cost(hours_itinerary, itinerary3, cost_itinerary_list):
    it = []

    for i in range(len(itinerary3)):
        item = itinerary3[i], hours_itinerary[i], cost_itinerary_list[i]

        it.append(item)

    return it


def string_max_len(list):
    longest_string = max(list, key=len)
    maxlen = len(longest_string)
    return maxlen





def division_day(hours_list, hours_constraint):
    sum_list = []
    final_list = []
    for i in range(len(hours_list)):

        x = hours_list[i]

        checker = sum(sum_list, x[1])

        if checker <= hours_constraint:

            sum_list.append(x[1])
        elif checker > hours_constraint:

            final_list.append(sum_list)
            sum_list = [x[1]]


    last_last = final_list + [sum_list]
    per_day = []
    for i in last_last:
        count = len(i)
        per_day.append(count)
    days = len(per_day)
    return per_day, days


def main_division_day(hours_constraint, days_constraint, hours_list):
    per_day, days = division_day(hours_list, hours_constraint)

    final_itinerary = 0
    count = 0
    while days > days_constraint:
        new_list = tuple(random.sample(hours_list, len(hours_list)))
        per_day, days = division_day(new_list, hours_constraint)

        final_itinerary = new_list
        count = count + 1
        if count > 100000:
            final_itinerary = 0
            print("ALERTTTTT")
            break

    return final_itinerary, per_day


def get_choice(choices, question, error_msg):
    choice = ""
    while choice not in choices:
        choice = input(question)
        choice = choice.lower()
        if choice not in choices:
            print(error_msg)

    return choice


class color:
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'

def add_hotel_list(daylist, maxlen, hotel_price):
    daylist = tuple(daylist)
    hotel_item = tuple([('Hotel'.ljust(maxlen), 0, hotel_price)])
    daylist = daylist + hotel_item

    return daylist




def main():
    travel = (color.BLUE + color.BOLD + 'TRAVELX' + color.END)
    cities_list = ["madrid", "barcelona", "london", "berlin", "manchester", "rome", "lisboa", "paris", "marseille"]
    slogan_text = (color.BOLD + "the perfect Itinerary Optimization App!" + color.END)
    print("Hello welcome to", travel, ",", slogan_text)
    print("Our possible destinations are the following:")
    for i in cities_list:
        print("-", i.capitalize())
    print()
    question = "What city would you like to visit? "
    error_message = "**Currently,TRAVELX doesnt have an Itinerary for that destination. Try Again!**"
    error_message = (color.UNDERLINE + color.BOLD + error_message + color.END)
    city_input = get_choice(cities_list, question, error_message)
    city_input = city_error_handling(city_input)
    print()
    csv_name = filter_adjust_data(city_input, travel)

    attractions, values, weights, cost = read_data_city(csv_name)
    valid_int_msg = "Non valid integer! Please try again ..."
    valid_int_msg = (color.RED + valid_int_msg + color.END)
    while True:
        try:
            days_constraint = int(input("How many days will you stay? "))
            while int(days_constraint) > 9 or int(days_constraint) < 0:
                if int(days_constraint) > 9:
                    string = (travel + " can only accept trips of less than 10 days")
                    recomend_msg = (color.BLUE + color.UNDERLINE + string + color.END)
                    message = "Currently," + recomend_msg
                    print("-", message)
                if int(days_constraint) < 0:
                    msg = "Cannot input negative values! Try again"
                    msg = (color.RED + msg + color.END)
                    print(msg)
                days_constraint = int(input("How many days will you stay? "))
            break
        except ValueError:
            print(valid_int_msg)

    while True:
        try:
            hours_per_day = int(input("How many hours per day will you like to spend doing tourism? "))
            while int(hours_per_day) > 16 or int(hours_per_day) <= 0:
                if int(hours_per_day) > 16:
                    print("- Dont you think this is a but too much? Try again with less hours, please!")
                    string = (travel + " advises you to choose between 6 and 10 hours")
                    recomend_msg = (color.BLUE + color.UNDERLINE + string + color.END)
                    print("-", recomend_msg)
                if int(hours_per_day) < 0:
                    msg = "Cannot input negative values! Try again"
                    msg = (color.RED + msg + color.END)
                    print(msg)
                if int(hours_per_day) == 0:
                    msg = "Cannot input 0 as a value! Try again"
                    msg = (color.RED + msg + color.END)
                    print(msg)
                hours_per_day = int(input("How many hours per day will you like to spend doing tourism? "))
            break
        except ValueError:
            print(valid_int_msg)
    hours = days_constraint * hours_per_day

    need_hotel_choices = ['yes','no']
    need_hotel_ques = "Will you use an hotel? (Yes or No) "
    error_msg = "Invalid input. Try again. Answer 'Yes' or 'No"
    error_msg = (color.RED + color.BOLD + error_msg + color.END)
    need_hotel = get_choice(need_hotel_choices,need_hotel_ques,error_msg  )
    if need_hotel == "yes":
        need_hotel = 1
    if need_hotel == "no":
        need_hotel = 0






    hotel_price = 0
    question_hotel = "Write the number of stars that will have the hotel that\n" \
                     " you will use to accommodate your trip "
    hotel_choice = ["5", "4", "3", "2", "1"]

    n = len(attractions)

    if need_hotel == 1:
        hotel_price = [45, 47, 55, 74, 182]
        print()
        print(travel,"cannot book you an Hotel. However, we can account for\n"
                     "the average price of your Hotel\n")

        print("Here at", travel,"we have the following assumptions of hotel stars\n"
                                "and their daily average price \n")
        for i in range(len(hotel_price)):
            if i == 0:
                print((i + 1), "star hotels have an average price of", hotel_price[i])

            else:
                print((i+1),"stars hotels have an average price of",hotel_price[i])




        stars_choice = get_choice(hotel_choice,question_hotel, "Wrong. Try again")

        stars_choice = int(stars_choice)



        hotel_price = hotel_price[stars_choice - 1]


    while True:
        try:
            cost_constraint = float(input("What is your budget (€) "))
            while float(cost_constraint) < 44:
                if float(cost_constraint) < 0:
                    msg = "Cannot input negative values! Try again"
                    msg = (color.RED + msg + color.END)
                    print(msg)

                if float(cost_constraint) < 44 and float(cost_constraint) > 0 and need_hotel == 1:
                    msg = "Your budget doesnt satisfy any possible hotel stays"
                    msg = (color.RED + msg + color.END)
                    print(msg)
                cost_constraint = float(input("What is your budget (€) "))
            break
        except ValueError:
            print(valid_int_msg)

    total_hotel_cost = hotel_price * days_constraint
    cost_contraint_attrac = cost_constraint-total_hotel_cost
    total_cost_constraint = cost_constraint + total_hotel_cost
    print()


    if cost_contraint_attrac < 0:
        print("The total hotel cost is greater than your budget")
        print("Please input a new hotel category or new budget")
        choices = ["hotel", "budget"]
        question = "Which one do you wish to change (hotel) or (budget)"
        error = "Error"
        choice = get_choice(choices,question,error )
        if choice == "hotel":
            while cost_contraint_attrac < 0:
                stars_choice = get_choice(hotel_choice, question_hotel, "Wrong.try again")
                stars_choice = int(stars_choice)
                print("type:", type(stars_choice))
                print("stars_choice",stars_choice)
                hotel_price2 = [45, 47, 55, 74, 182]
                hotel_price = hotel_price2[stars_choice - 1]
                total_hotel_cost = hotel_price * days_constraint
                cost_contraint_attrac = cost_constraint - total_hotel_cost
                if cost_contraint_attrac < 0:
                    msg = "Error. Total hotel cost still is greater than your budget. TryAgain"
                    msg = (color.RED + color.BOLD + msg + color.END)
                    print(msg)




        if choice == "budget":
            while True:
                try:
                    cost_constraint = float(input("What is your new budget (€) "))
                    cost_contraint_attrac = cost_constraint - total_hotel_cost
                    print("total_hotel_cost",total_hotel_cost)
                    while cost_contraint_attrac < 0:
                        if float(cost_constraint) < 0:
                            msg = "Cannot input negative values! Try again"
                            msg = (color.RED + msg + color.END)
                            print(msg)


                        if cost_contraint_attrac < 0:
                            msg = "With that budget you can't satisfy any hotel"
                            msg = (color.RED + msg + color.END)
                            print(msg)


                        cost_constraint = float(input("What is your budget (€) "))
                        cost_contraint_attrac = cost_constraint - total_hotel_cost
                        print("cost_contraint_attrac",cost_contraint_attrac)
                    break
                except ValueError:
                    print(valid_int_msg)




    res, filtered_K = itinerary_optimization(hours, weights, values, n, attractions, cost, cost_contraint_attrac)
    filtered_K_sorted = sorted(filtered_K, key=lambda tup: tup[0], reverse=True)

    itinerary = filtered_K_sorted[0]

    itinerary2 = itinerary[1]

    itinerary3 = itinerary2.split(";")

    itinerary3 = list(filter(None, itinerary3))

    hours_itinerary = itinerary_attrac_hours(csv_name, itinerary3)

    cost_itinerary_list = itinerary_attrac_cost(csv_name, itinerary3)

    itinerary5 = []

    maxlen = string_max_len(itinerary3)
    for i in itinerary3:
        item = i.ljust(maxlen)
        itinerary5.append(item)

    itinerary4 = join_attrac_hours_cost(hours_itinerary, itinerary5, cost_itinerary_list)

    final_iti, order_iti = main_division_day(hours_per_day, days_constraint, itinerary4)

    for i in range(len(order_iti)):
        day_list = []
        number = str(i)
        day_string = "Day" + number
        day_list.append(day_string)

    print_iti = final_iti
    if final_iti == 0:
        print_iti = itinerary4

    if final_iti == 0 and len(order_iti) != days_constraint:
        text = (color.BOLD + color.RED + "YOUR ITINERARY TO MAXIMIZE RATING COULDNT BE FITTED IN " + str(days_constraint) +
                " DAYS" + color.END)
        print(text)
        if days_constraint >= len(order_iti):
            tex2 = (color.BOLD + "HOWEVER, TRAVELX COULD DO IT IN " + str(len(order_iti)) +
                " DAYS" + color.END)
            print(tex2)




    print()
    iti_text = (color.BOLD + color.GREEN + "Itinerary to Maximize Rating" + color.END)
    print(iti_text)
    attraction_word = "Attractions".ljust(maxlen)
    print(' {}{} {} {}'.format(" ", attraction_word, '  Hours', '   Cost'))

    first = 0

    blank_text = "".ljust(maxlen - 1)
    for i in range(len(order_iti)):
        last = order_iti[i]

        total = first + last
        if i != 0:
            print()
        day_text = (color.BOLD + "Day" + color.END)
        number_text = str(i + 1)
        number_text = (color.BOLD + number_text + color.END)


        day_list = print_iti[first:total]
        if need_hotel == 1:
            day_list = add_hotel_list(day_list, maxlen, hotel_price)



        first = total
        for i in range(len(day_list)):

            if i == (len(day_list) - 1):
                last_line = ' {} {}  {}hrs    ${}'.format("-", day_list[i][0], day_list[i][1], round(day_list[i][2],2))
                last_line = (color.UNDERLINE + last_line + color.END)
                print(last_line)
                break
            print(' {} {}  {}hrs    ${}'.format("-", day_list[i][0], day_list[i][1], day_list[i][2]))

        total_text = (color.BOLD + "TOTAL" + color.END)
        total_hr_txt = str(sum(j for i, j, x in day_list))
        total_hr_txt = (color.BOLD + total_hr_txt + color.END)
        hrs_text = (color.BOLD + "hrs" + color.END)
        total_cost_txt = str(round(sum(x for i, j, x in day_list), 2))
        total_cost_txt = (color.BOLD + total_cost_txt + color.END)

        print("{}{} {}{}    ${}".format(blank_text, total_text, total_hr_txt, hrs_text, total_cost_txt))

    print()
    waw_txt = (color.GREEN + color.BOLD + "Your Optimize Itinerary has a" + color.END)
    print(waw_txt)
    avg_rtg = round(itinerary[0] / len(print_iti), 2)
    print(" - Average Rating of: ".ljust(maxlen + 3), "", avg_rtg)
    cost_text = "- Total Cost of:".ljust(maxlen + 2)
    hours_text = "- Average hours per day of tourism are:".ljust(maxlen + 3)
    if need_hotel ==1:
        print(" {} {}{}".format(cost_text, "$", round(sum(cost_itinerary_list), 2) + (hotel_price*days_constraint)))

    if need_hotel ==0:
        print(" {} {}{}".format(cost_text, "$", round(sum(cost_itinerary_list), 2)))
    print(" {} {} {}".format(hours_text, round(sum(hours_itinerary) / days_constraint, 2), "hrs"))
    print()
    file_remove(csv_name)
    warning_txt = "**This program doesnt take into account inside attraction costs, only entry cost**\n"
    warning_txt = (color.UNDERLINE + color.BOLD + warning_txt + color.END)
    print(warning_txt)

    print("Would you like to run again", travel, "?")

    cities_txt = (color.PURPLE + color.BOLD + 'cities' + color.END)
    preferences_txt = (color.PURPLE + color.BOLD + 'preferences' + color.END)
    print("You can change " + cities_txt + " or even change your " + preferences_txt + ".")

    question = "Wish to repeat? (yes or no) "
    answer_list = ['yes', 'no']
    error_msg = "Try Again. Answer 'Yes' or 'No'"
    error_msg = (color.RED + color.BOLD + error_msg + color.END)

    choice = get_choice(answer_list, question, error_msg)

    if choice == "yes":
        main()


main()


def goodbye_msg(travel):
    print()
    print(travel, "thanks you for using our app!")


goodbye_msg((color.BLUE + color.BOLD + 'TRAVELX' + color.END))

