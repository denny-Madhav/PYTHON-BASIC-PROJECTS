#set of square brackets which can store many items
#example : fruits =["cherry","apple","orange"]

cities = ["vizag","vijayawada","kakinada","rajmundary"]

print(cities[0]) #first postion
print(cities[-1]) #last postion

cities.append("kassi") #add new item to list
print(cities)

cities[4]="Tirupati" #Replace

print(cities)

cities.extend(["bhimavaram","karnool","guntur"]) # add multiple items in the list
print(cities)