#create list holding name of 20 friends

my_friends = [
    'Dell',
    'Camille',
    'James',
    'Charlise',
    'Donna',
    'Steven',
    'Angelique',
    'Whitley',
    'Vanessa',
    'Andre',
    'Amelia',
    'Juliet',
    'Angelita',
    'Warner',
    'Tiffany',
    'Anthony',
    'Trinette',
    'Patrice',
    'Margaret',
    'Bud', 
]

print(my_friends)

#slice 1st 4 people from the list
dinner_guest = my_friends[:4]
print(dinner_guest)

#slice last 4 people from the list
out_for_drinks = my_friends[16:0]  
print(out_for_drinks)

#middle 4 friends 
hiking_friends = my_friends[10:14]
print(hiking_friends)

#best friend to hike with
hike_with_friend = my_friends[2:3]
print(hike_with_friend)

#output length of list
print(len(my_friends))


