# BINARY SEARCH
search_array = [1,2,3,9,11,13,17,25,57,90]
search_term = int(input("Please enter your search criteria")) #99

low = 0
high = len(search_array)-1
mid = (high + low)//2 #integer division - cuts off the decimal
found = False # flag

while found == False and low < high:
    mid = (high + low) //2
    if search_term == search_array[mid]:
        found = True
    else:
        if search_term > search_array[mid]:
            low = mid + 1
        else:
            high = mid - 1
            
if found == True:
    print("Found")
else:
    print("Number not found")