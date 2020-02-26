#!/usr/bin/env python3

file = open("restaurants.txt", "r")
restaurants = list(file)
file.close()

# this function takes care of removing the "\n" at the end of each list item
def strip_list(liste):
    new_list = []
    for i in liste:
        i = i[:-1]
        new_list.append(i)
    return new_list

# this will be the list to work with:
list_of_resturants = strip_list(restaurants)

website = f"""
<!DOCTYPE html>
<html>
    <head>
        <title>Restaurants in Berlin</title>
    </head>
    <body>
        <h1>This is a website of restaurants in Berlin</h1>
        <p>There are numerous:</p>
        <p>{list_of_resturants[0]}</p>
        <p>{list_of_resturants[1]}</p>
        <p>{list_of_resturants[2]}</p>
    </body>
</html>
"""
print(website)