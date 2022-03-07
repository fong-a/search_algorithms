# LINEAR SEARCH 



# v0.1
# for i in search_array:
#     if search_term == i:
#         print("Found")
        
# v0.2
# found = False
# for i in search_array:
#     if found == False:
#         if search_term == i:
#             found = True
# if found == True:
#     print("Found")

# v0.3 
search_array = ["Fast", "Foodie"]
search_term = input("Please enter your search criteria")
length_of_array = len(search_array)
current_item = 0
found = False
while found == False and current_item< length_of_array:
    if search_array[current_item] == search_term:
        found = True
    else:
        current_item += 1  

if found == True:
    print("Found")