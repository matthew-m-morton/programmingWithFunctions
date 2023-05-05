# Import csv module so that the program can read csv files
# Import the datetime module so that we can access the date and time
import csv
from datetime import datetime

#Indexes for the products dictionary
DB_PRODUCT_CODE  = 0
DB_PRODUCT_NAME  = 1
DB_PRODUCT_PRICE = 2

#Indexes for the request list
REQUEST_PRODUCT_CODE     = 0
REQUEST_PRODUCT_QUANTITY = 1


def main():
    try:    
        # Create the products dictionary
        products_dict = read_dict("products.csv", DB_PRODUCT_CODE)
        
        # Create the request list
        request_list = read_list("request.csv")   
    
        # Prints the receipt header
        print("          Matt's Bazaar\n")
        print("---------Requested Items---------\n")


        # Variables for running total and total number of items
        run_total = 0
        number_of_items_total = 0


        # For loop that runs through the items in the request list
        # Also calculates the running total and number of items
        for item in range(len(request_list)):

            # From the request list, retrieve the product code
            product_code = request_list[item][REQUEST_PRODUCT_CODE]

            # Quantity of item from request list
            # Total number of items calculation
            quantity = int(request_list[item][REQUEST_PRODUCT_QUANTITY])
            number_of_items_total += quantity

            # Calculation of the running total
            price = float(products_dict[product_code][DB_PRODUCT_PRICE])
            run_total += (price * quantity)

            # Print the information for each item
            # Product name: quantity @ price
            print(f"{products_dict[product_code][DB_PRODUCT_NAME]:19}:{quantity:-3} @{price:-7}$")
        

        # Calculate the the Sales Tax and the Total
        sales_tax = run_total * .06
        total = run_total + sales_tax

        # Print number of items, Subtotal, Sales Tax, and Total 
        print(f"\nNumber of items:  {number_of_items_total:-15}")
        print(f"Subtotal: {run_total:-23.2f}")
        print(f"Sales Tax: {sales_tax:-22.2f}")
        print(f"Total: {total:-26.2f}")


        # Retrieve the date and time from the datetime module
        current_sate_and_time = datetime.now()
        
        # Print graditude for service
        # Print the date in a specific format
        print("\nThank you for shopping with us.")
        print(f"{current_sate_and_time:%A %B %d,%Y  %I:%M:%S }")
    
    except FileNotFoundError as not_found_err:
        # This code will be executed if the file is mislabeled or misplaced
        print("Error: missing file")
        print(type(not_found_err).__name__, not_found_err, sep=": ")

    except PermissionError as perm_err:
        # This code will execute if the user tries to access 
        # a file without the proper permissions
        print("Error: missing permission")
        print(type(perm_err), perm_err, sep= ": ")
        print("Oh no. It seems that you do not have\n"/
                "permission to access this file")

    except KeyError as key_err:
        # This code will execute if a Key doesn't exist in a dictionary
        print()
        print("Error: unknown product ID in the request.csv file")
        print(key_err)



def read_dict(filename, key_column_index):
    """Read the contents of a CSV file into a compound
    dictionary and return the dictionary.

    Parameters
        filename: the name of the CSV file to read.
        key_column_index: the index of the column
            to use as the keys in the dictionary.
    Return: a compound dictionary that contains
        the contents of the CSV file.
    """
    # This function has been adapted from 
    # example 5 from the 09 prepare section

    # Create an empty dictionary that will
    # store the data from the CSV file.
    dictionary = {}

    # Open the CSV file for reading and store a reference
    # to the opened file in a variable named csv_file.
    with open(filename, "rt") as csv_file:

        # Use the csv module to create a reader object
        # that will read from the opened CSV file.
        reader = csv.reader(csv_file)

        # The first row of the CSV file contains column
        # headings and not data, so this statement skips
        # the first row of the CSV file.
        next(reader)

        # Read the rows in the CSV file one row at a time.
        # The reader object returns each row as a list.
        for row_list in reader:

            # From the current row, retrieve the data
            # from the column that contains the key.
            key = row_list[key_column_index]

            # Store the data from the current row
            # into the dictionary.
            dictionary[key] = row_list

    # Return the dictionary.
    return dictionary


def read_list(filename):
    """Read the contents of a CSV file into a compound
    list and return the list.

    Parameters
        filename: the name of the CSV file to read.
        Return: a compound list that contains
        the contents of the CSV file.
    """
    # This function has been adapted from 
    # example 5 from the 09 prepare section

    # Create an empty list that will
    # store the data from the CSV file.
    file_list = []

    # Open the CSV file for reading and store a reference
    # to the opened file in a variable named csv_file.
    with open(filename, "rt") as csv_file:

        # Use the csv module to create a reader object
        # that will read from the opened CSV file.
        reader = csv.reader(csv_file)

        # The first row of the CSV file contains column
        # headings and not data, so this statement skips
        # the first row of the CSV file.
        next(reader)

        # Read the rows in the CSV file one row at a time.
        # The reader object returns each row as a list.
        for row_list in reader:

            # Store the data from the current row into the list
            file_list.append(row_list)

    # Return the list
    return file_list



if __name__ == "__main__":
    main()