file = open("restaurants.txt", "r")
restaurants = list(file)


def strip_list(liste):
    new_list = []
    for i in liste:
        i = i[:-1]
        new_list.append(i)
    return new_list

list_of_resturants = strip_list(restaurants)

print(list_of_resturants)



# string1 = "Alt-Treptow\n"
# string1 = string1[:-1]
# print(string1)



file.close()