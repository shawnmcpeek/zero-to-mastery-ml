# Import pandas
import pandas as pd

# Create a series of three different colours
colors = pd.Series(["Red", "Blue", "Green"])
# View the series of different colours
print(colors)
# Create a series of three different car types and view it
cars = pd.Series(["EV", "Duck", "Flying Car"])
print(cars)
# Combine the Series of cars and colours into a DataFrame
car_data = pd.DataFrame({"Car make": cars, "Colour": colors})
print(car_data)
# Import "../data/car-sales.csv" and turn it into a DataFrame
car_sales = pd.read_csv(
    "C:/Users/shawn/OneDrive/Documents/ZTMREACT/zero-to-mastery-ml/data/car-sales.csv"
)
print(car_sales)
# Note: Since you've imported ../data/car-sales.csv as a DataFrame, we'll now refer to this DataFrame as 'the car sales DataFrame'.

# Export the DataFrame you created to a .csv file
car_sales.to_csv(
    "C:/Users/shawn/OneDrive/Documents/ZTMREACT/zero-to-mastery-ml/data/exported-car-sales.csv"
)
# Find the different datatypes of the car data DataFrame
print(car_sales.dtypes)
# Describe your current car sales DataFrame using describe()
car_sales.describe()
print(car_sales.describe())
# Get information about your DataFrame using info()
print(car_sales.info())

# Create a Series of different numbers and find the mean of them
numbers1 = pd.Series([7, 2, 14])
print(numbers1.mean())
# Create a Series of different numbers and find the sum of them
numbers2 = pd.Series([1, 4, 12])
print(numbers2.sum())
# List out all the column names of the car sales DataFrame
print(car_sales.columns)
# Find the length of the car sales DataFrame
print(len(car_sales))
# Show the first 5 rows of the car sales DataFrame
print(car_sales.head(5))
# Show the first 7 rows of the car sales DataFrame
print(car_sales.head(7))
# Show the bottom 5 rows of the car sales DataFrame
print(car_sales.tail())
# Use .loc to select the row at index 3 of the car sales DataFrame
car_sales.loc[3]
# Use .iloc to select the row at position 3 of the car sales DataFrame
print(car_sales.iloc[3])
# Notice how they're the same? Why do you think this is?

# Check the pandas documentation for .loc and .iloc. Think about a different situation each could be used for and try them out.

# Select the "Odometer (KM)" column from the car sales DataFrame
car_sales["Odometer (KM)"]
# Find the mean of the "Odometer (KM)" column in the car sales DataFrame
car_sales["Odometer (KM)"].mean()
# Select the rows with over 100,000 kilometers on the Odometer
# Create a crosstab of the Make and Doors columns
pd.crosstab(car_sales["Make"], car_sales["Doors"])
# Group columns of the car sales DataFrame by the Make column and find the average
# Import Matplotlib and create a plot of the Odometer column
# Don't forget to use %matplotlib inline
# Create a histogram of the Odometer column using hist()
# Try to plot the Price column using plot()
# Why didn't it work? Can you think of a solution?

# You might want to search for "how to convert a pandas string column to numbers".

# And if you're still stuck, check out this Stack Overflow question and answer on turning a price column into integers.

# See how you can provide the example code there to the problem here.

# Remove the punctuation from price column
# Check the changes to the price column
# Remove the two extra zeros at the end of the price column
# Check the changes to the Price column
# Change the datatype of the Price column to integers
# Lower the strings of the Make column
# If you check the car sales DataFrame, you'll notice the Make column hasn't been lowered.
# How could you make these changes permanent?

# Try it out.

# Make lowering the case of the Make column permanent
# Check the car sales DataFrame
# Notice how the Make column stays lowered after reassigning.

# Now let's deal with missing data.

# Import the car sales DataFrame with missing data ("../data/car-sales-missing-data.csv")


# Check out the new DataFrame
# Notice the missing values are represented as NaN in pandas DataFrames.

# Let's try fill them.

# Fill the Odometer column missing values with the mean of the column inplace
# View the car sales missing DataFrame and verify the changes
# Remove the rest of the missing data inplace
# Verify the missing values are removed by viewing the DataFrame
# We'll now start to add columns to our DataFrame.

# Create a "Seats" column where every row has a value of 5
# Create a column called "Engine Size" with random values between 1.3 and 4.5
# Remember: If you're doing it from a Python list, the list has to be the same length
# as the DataFrame
# Create a column which represents the price of a car per kilometer
# Then view the DataFrame
# Remove the last column you added using .drop()
# Shuffle the DataFrame using sample() with the frac parameter set to 1
# Save the the shuffled DataFrame to a new variable
# Notice how the index numbers get moved around. The sample() function is a great way to get random samples from your DataFrame. It's also another great way to shuffle the rows by setting frac=1.

# Reset the indexes of the shuffled DataFrame
# Notice the index numbers have been changed to have order (start from 0).

# Change the Odometer values from kilometers to miles using a Lambda function
# Then view the DataFrame
# Change the title of the Odometer (KM) to represent miles instead of kilometers
# Extensions
# For more exercises, check out the pandas documentation, particularly the 10-minutes to pandas section.

# One great exercise would be to retype out the entire section into a Jupyter Notebook of your own.

# Get hands-on with the code and see what it does.

# The next place you should check out are the top questions and answers on Stack Overflow for pandas. Often, these contain some of the most useful and common pandas functions. Be sure to play around with the different filters!

# Finally, always remember, the best way to learn something new to is try it. Make mistakes. Ask questions, get things wrong, take note of the things you do most often. And don't worry if you keep making the same mistake, pandas has many ways to do the same thing and is a big library. So it'll likely take a while before you get the hang of it.
