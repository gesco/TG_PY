# Get the desired futrue value.
future_value = float(input('Enter the desired future value: '))

# Get the annual intersest rate.
rate = float(input('Enter the annual interest rate: '))

# Get the number of years that the money will appreciate.
years = int(input('Enter the number of years the money will grow: '))

# Calculate the amount needed to deposit.
present_value = future_value / (1.0 + rate)**years

# Display the amount needed to deposit.
print('You will need to deposit this amount:', present_value)

# OUTPUT
# Enter the desired future value: 10000.0
# Enter the annual interest rate: 0.05
# Enter the number of years the money will grow: 10
# You will need to deposit this amount: 6139.132535407592
