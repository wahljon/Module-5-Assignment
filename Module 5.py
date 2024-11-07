def main():
    # Prompt user to enter the number of years to track
    num_years = int(input("How many years would you like to track rainfall for? "))
    
    # Initialize variables for total rainfall and month count
    total_rainfall = 0.0
    month_counter = 0
    
    # Loop through each year
    for year in range(num_years):
        print("\nYear {}:".format(year + 1))
        
        # Loop through each month in the current year
        for month in range(12):
            while True:
                try:
                    rainfall = float(input("  Month {}: Enter rainfall in inches: ".format(month + 1)))
                    if rainfall < 0:
                        print("  Rainfall cannot be negative. Please try again.")
                    else:
                        break
                except ValueError:
                    print("  Invalid input. Please enter a numeric value.")
            total_rainfall += rainfall
            month_counter += 1
    
    # Calculate average monthly rainfall
    average_rainfall = total_rainfall / month_counter if month_counter > 0 else 0
    
    # Display summary
    print("\nSummary:")
    print("  Total number of months tracked: {}".format(month_counter))
    print("  Total rainfall: {:.2f} inches".format(total_rainfall))
    print("  Average monthly rainfall: {:.2f} inches".format(average_rainfall))

    # Part 2: CSU Global Bookstore Points Program
    try:
        books_purchased = int(input("\nEnter the number of books purchased this month: "))
    except ValueError:
        print("Invalid input. Setting books purchased to 0.")
        books_purchased = 0
    
    # Calculate points based on books purchased
    if books_purchased <= 0:
        points = 0
    elif books_purchased == 2:
        points = 5
    elif books_purchased == 4:
        points = 15
    elif books_purchased == 6:
        points = 30
    elif books_purchased >= 8:
        points = 60
    else:
        points = 0
    
    # Display the points earned
    print("Points earned this month: {} points".format(points))

# Execute the program
if __name__ == "__main__":
    main()

