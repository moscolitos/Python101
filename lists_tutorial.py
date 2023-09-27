
# -*- coding: utf-8 -*-
"""
This script demonstrates the use of Python lists and their methods. 
It includes examples of how lists can be used to 
manage and analyze inventory in a grocery store and 
to handle patient information and medical records in a healthcare setting.
"""

# Initial List Definition

# Define a list containing mixed data types including another list
my_list = [1, 'Python', 3.14, [1, 2, 3]]

# Demonstrating List Methods

# Append Method
my_list.append('new_item')  # Append 'new_item' to the end of my_list

# Copy Method
my_list_2 = my_list.copy()  # Create a shallow copy of my_list

# Clear Method
my_list_2.clear()  # Remove all items from my_list_2

# Count Method
# Count occurrences of 'Python' in my_list
count_of_item = my_list.count('Python')

# Extend Method
my_list.extend(['49.2', True])  # Extend my_list with more than one item

# Index Method
# Find the index of the first occurrence of 'Python' in my_list
index_of_item = my_list.index('Python')

# Insert Method
my_list.insert(3, 'Python')  # Insert 'Python' at the third index of my_list

# Pop Method
item = my_list.pop(1)  # Remove the item at index 1 and return it

# Remove Method
# Remove the first occurrence of 'new_item' from my_list
my_list.remove('new_item')

# Reverse Method
my_list.reverse()  # Reverse the elements of my_list

# Sort Method
my_list_2 = [4, 23, 42, 8, 16, 15]  # Define a new list of integers
my_list_2.sort()  # Sort the items of my_list_2 in ascending order

# Example 1: Inventory Management

# Define a list of items in inventory
items_list = ['apples', 'bananas', 'milk', 'bread', 'eggs']
# Define a list of quantities corresponding to items_list
quantity_list = [10, 15, 20, 25, 30]
# Define a list of prices corresponding to items_list
price_list = [2.00, 1.00, 1.50, 2.50, 3.00]

# Define a function to check inventory and calculate total value of inventory


def check_inventory(items, quantities, prices, threshold=15):
    low_stock = []  # List to hold items with quantity below the threshold
    total_value = 0  # Initialize the total_value of inventory to 0

    for i in range(len(items)):
        # Calculate total value of inventory
        total_value += quantities[i] * prices[i]
        if quantities[i] < threshold:  # Check if quantity of item is below threshold
            low_stock.append(items[i])  # Append item to low_stock list

    # Return the list of items with low stock and the total value of inventory
    return low_stock, total_value


# Execute the function and print the results
low_stock_items, inventory_value = check_inventory(
    items_list, quantity_list, price_list)
print(f"Items that need reordering: {low_stock_items}")
print(f"Total value of inventory: ${inventory_value}")

# Example 2: Healthcare Management

# Define a list of dictionaries, representing a patient's informations

patients_list = [{"Name": "Red Doe", "Age": 30, "Gender": "Male", "Medical History": [
    "Hypertension"], "Test Results": {"Blood Pressure": "140/90", "Cholesterol": "200"}},
    {"Name": "Jane Mary", "Age": 25, "Gender": "Female", "Medical History": [
        "Diabetes"], "Test Results": {"Blood Sugar": "150", "Cholesterol": "180"}}
]

# Define a function to add a new patient to patients_list


def add_patient(patients, name, age, gender):
    new_patient = {"Name": name, "Age": age, "Gender": gender,
                   "Medical History": [], "Test Results": {}}
    patients.append(new_patient)

# Define a function to update the medical history of a patient in patients_list


def update_medical_history(patients, name, condition):
    for patient in patients:  # Iterate over each patient dictionary in patients_list
        if patient["Name"] == name:
            patient["Medical History"].append(condition)

# Define a function to analyze patients_list and count the number of
# patients with a specific condition


def analyze_data(patients, condition):
    count = 0
    for patient in patients:
        # Check if the provided condition is in the 'Medical History' list
        # of the current patient dictionary
        if condition in patient["Medical History"]:
            count += 1  # Increment the count by 1 if the condition is found
    return count


# Execute the functions and print the results
# Add a new patient named 'Mike Jordan' to patients_list
add_patient(patients_list, "Mike Jordan", 35, "Male")
# Update the medical history of 'Mike Jordan' to add a new condition: 'Asthma'
update_medical_history(patients_list, "Mike Jordan", "Asthma")
# Analyze patients_list to count the number of patients with 'Asthma'
asthma_count = analyze_data(patients_list, "Asthma")
# Print the number of patients with 'Asthma'
print(f"Number of patients with Asthma: {asthma_count}")

# Output the final state of patients_list
patients_list
