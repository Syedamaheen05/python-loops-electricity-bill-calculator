# Program 2: Smart Electricity Bill Calculator
# Topic: for loop, range(), accumulators, and conditional statements inside loops.

# Real-World Scenario
# Imagine an electricity company that wants to calculate the monthly electricity bills of multiple households.
# Instead of writing the same code repeatedly for every household, the company wants a program that:
# 1. Asks how many households need their bills calculated.
# 2. Takes the electricity units consumed by each household.
# 3. Calculates the bill using the following rates:
#    - First 100 units: Rs. 10 per unit.
#    - Next 100 units (101–200): Rs. 15 per unit.
#    - Units above 200: Rs. 20 per unit.
# 4. Calculates the total bill for every household.
# 5. Displays the combined electricity revenue collected from all households.
# Important: These rates are fictional and intended for programming practice, not actual electricity tariffs.

# Smart Electricity Bill Calculator


print("===== ELECTRICITY BILL SYSTEM =====")

# Taking number of households
try:
    households = int(input("Enter the number of households: "))

except ValueError:
    print("Invalid input! Please enter a whole number.")

else:

    # Validate number of households
    if households <= 0:
        print("Number of households must be greater than zero.")

    else:

        # Initializing variables
        total_revenue = 0
        valid_households = 0
        highest_bill = 0
        highest_household = 0

        # Processing each household
        for household in range(1, households + 1):

            print(f"\n--- Household {household} ---")

            # Taking electricity units
            try:
                units = int(input("Enter electricity units consumed: "))

            except ValueError:
                print("Invalid input! Please enter a whole number.")
                continue

            # Checking negative units
            if units < 0:
                print("Invalid units! Please enter a non-negative value.")
                continue

            # Calculating electricity bill
            if units <= 100:
                bill = units * 10

            elif units <= 200:
                bill = (100 * 10) + ((units - 100) * 15)

            else:
                bill = (100 * 10) + (100 * 15) + ((units - 200) * 20)

            # Displaying household bill
            print(f"Units Consumed: {units}")
            print(f"Electricity Bill: Rs. {bill}")

            # Adding bill to total revenue
            total_revenue += bill

            # Counting valid households
            valid_households += 1

            # Finding highest bill
            if valid_households == 1 or bill > highest_bill:
                highest_bill = bill
                highest_household = household

        # Displaying final report
        print("\n===== MONTHLY REVENUE REPORT =====")

        print(f"Total Households: {households}")
        print(f"Valid Households: {valid_households}")
        print(f"Total Revenue: Rs. {total_revenue}")

        # Calculating average and displaying highest bill
        if valid_households > 0:

            average_bill = total_revenue / valid_households

            print(f"Average Bill: Rs. {average_bill:.2f}")
            print(f"Highest Electricity Bill: Rs. {highest_bill}")
            print(f"Household with Highest Bill: {highest_household}")

        else:
            print("No valid household bills were calculated.")
