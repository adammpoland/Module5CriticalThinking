num_of_books = int(input("Number of books purchased this month "))
points = 0
if num_of_books == 0:
    points +=0
if num_of_books == 2 or num_of_books ==3:
    points +=5
if num_of_books ==4 or num_of_books ==5:
    points +=15
if num_of_books ==6 or num_of_books ==7:
    points += 30
if num_of_books >= 8:
    points +=60

print("Points Awarded: "+ str(points))
