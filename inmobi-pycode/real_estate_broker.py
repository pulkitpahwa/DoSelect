user_input = map(int, raw_input().split())
users_choices = []
for i in range(user_input[0]) :
    users_choices.append(map(int, raw_input().split()))

flats_sold = []  
count = 0 
for i in users_choices :
    if not i[0] in flats_sold :
        count += 1
        flats_sold.append(i[0])
    elif not i[1] in flats_sold :
        count +=1
        flats_sold.append(i[1])

print count

