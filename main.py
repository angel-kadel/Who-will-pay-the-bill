import random

print("Who is going to buy a meal today?\n")

num_of_people= int(input("How many people are there?\n"))
name= []
i = 0

while i < num_of_people:

  name.append(input(f"\nEnter name{i+1}:\n"))
  i+= 1

bill_payment = random.randint(0,len(name)-1)
print(f"\n{name[bill_payment]} is gong to pay the bill")


