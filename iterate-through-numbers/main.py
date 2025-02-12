years_list = [5,7,12,13,9,21,11,10]
num_eligible = 0

for years in years_list:
    if years > 9:
        num_eligible += 1
print(num_eligible)



# # my non pythonic code...lol
# for years in years_list:
#     if years >= 9:
#         print(f'Congratulations on your {years}th year anniversary!')
#     else:
#         print("Keep working, ya'll got a ways to go.")

