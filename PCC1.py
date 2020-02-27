#PCC

#Ch. 1 

message = 'Hello Python World'
print(message)

#Ch. 2

#2.1

message1 = 'This is the first sample message'
print(message1)

#2.2
#Change the value of the previous variable and print
message1 = 'This is the second sample message'
print(message1)

#2.3
person = 'Eric'
print(person + ', have a good day!')

#2.4
peep = 'sean'
peep.upper()
peep.title()

#2.5 - 2.7 is repetitive

#2.8
print(5+3)
print(9-1)
print(16/2)
print(4*2)

#2.9
fav_num = 0
print("I love " + str(fav_num) + ". It's my favorite number") #Can only concatenate strings not integers in. 

#Did the 'import this' entry into terminal and read The Zen of Python


#Ch. 3 

#3.1
friends = ['sean','tess','blair']
print(friends[0])
print(friends[1])
print(friends[2])
friends[0] = friends[0].title()
friends[1] = friends[1].title()
friends[2] = friends[2].title()

#3.2
print(friends[0] + ", what's up?")
print(friends[1] + ", what's up?")
print(friends[2] + ", what's up?")

#3.3
#this is just more of the same

#3.4

guest_list = ['Caesar','Einstein','Alexander','Sinatra']
print(guest_list[0] + ", you are invited to dinner.")
print(guest_list[1] + ", you are invited to dinner.")
print(guest_list[2] + ", you are invited to dinner.")
print(guest_list[3] + ", you are invited to dinner.")

#3.5
print(guest_list[2] + " had to cancel. He can't make it.")

guest_list[2] = 'Eleanor'

print(guest_list[0] + ", you are invited to dinner.")
print(guest_list[1] + ", you are invited to dinner.")
print(guest_list[2] + ", you are invited to dinner.")
print(guest_list[3] + ", you are invited to dinner.")

#3.6
print("We've found a bigger table. Let's invite some more people.")

guest_list.insert(0,'Ezio')

guest_list.insert(2,'Alexios') #this code places a new name in the spot designated in the first parameter. In this case, the third parameter

guest_list.append('Katerina') #places name on the end of the list

#3.7

guest_list.pop()
#the above code would remove the last person on the list


del guest_list[0] #this deleted the first entry in the list

#3.8

locations = ['paris', 'tokyo', 'rio', 'new york','rome','barcelona','london']

sorted(locations) #temporary alphabetical order

locations #show that the order is unchanged

locations.reverse() #put the list in reverse order

locations.sort() #permanently change the lsit

locations.sort(reverse = True) #this put the list in reverse abc order

#3.9
message = ("I want to visit at least " + str(len(locations)) + " locations.")

#3.11

print(locations[9]) #this will make an error because it call an index higher than the length of list




















