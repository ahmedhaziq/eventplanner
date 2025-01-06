data = {'Apples':4,'Bananas':4,'Oranges':3,'Grapes':9,'Peaches':2}

calendar_list = []
list_length = 21
for i in range(1,22):
    calendar_list.append('')


for food_item in data:
    number = data[food_item]
    spacing = int(list_length/number)
    if spacing == 0:
        spacing = 1
    counter = 0
    second_counter = 0
    place_value = 0
    while True:
        if counter == len(calendar_list):
            print('food items too much')
            break
        if calendar_list[counter] == '':
            if second_counter%spacing == 0:
                calendar_list[counter] = food_item
                place_value = place_value + 1
                if place_value == number:
                    break
            second_counter = second_counter + 1
        counter = counter + 1



    ## decreaing the list length
    list_length = list_length - number



## converting the food item to a list
calendar_dictionary = {}
weekdays = ['Monday','Tuesday','Wendnessday','Thursday','Friday','Saturday','Sunday']
for weekday in range(len(weekdays)):
    sub_list = []
    for i in range(0,3):
        food_item = calendar_list[weekday*3 + i]
        sub_list.append(food_item)
    calendar_dictionary[weekdays[weekday]] = sub_list
        
print(calendar_dictionary)
