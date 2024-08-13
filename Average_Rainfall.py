num_of_years = int(input("Number of Years: "))
total_rainfall = 0

for year_index in range(0,num_of_years):
    for month_index in range(0,12):
        monthly_rainfall = input("Enter Monthly Rainfall for month " + str(month_index +1) + " ")
        total_rainfall += float(monthly_rainfall)

print("Number of Months "+str(num_of_years*12))
print("Total Rainfall: " + str(total_rainfall))
print("Average: " + str(total_rainfall/(num_of_years *12)))