# Import Library

import psycopg2
from psycopg2 import Error

# Function to create connection

def getConnection():
    # Write Your Code Here
    connection = psycopg2.connect(host= 'localhost', user='postgres', password='omaAptd1', 
                    database='postgres')
    return connection
    
# Function to close connection   
def closeConnection(connection):
    connection.close()
    print("Connection is Closed")


def getCustomer(customer_id):
    try:
        # Create a connection using the connection function
        connection = getConnection()  

        #create cursor object
        cursor=connection.cursor()

        #Create a query variable, by writing a SELECT query to fetch the customer using the customer_id as the filter.
        query = ''' SELECT *
                        FROM customer
                        WHERE customer_id = %s
                    '''
        cursor.execute(query, (customer_id,))

        #Create an object that will hold the records, Hint use fetchall()
        records= cursor.fetchall()

        #Using a for loop to iterate through the records to print each record instance of the customer table. 
        print("Printing Records")
        for row in records:
            print("customer_id", row[0])
            print("store_id", row[1])
            print("first_name", row[2])
            print("last_name", row[3])
            print("email", row[4])
            print("address_id", row[5])
            print("activebool", row[6])
            print("create_table", row[7])
            print("last_update", row[8])
            print("active", row[9], '\n')

   
    except Error as e:
        getConnection.rollback()
        print("Error: Reading Record")


    # Closes the connection
    finally:
        closeConnection(connection) 

# Using the getCustomer function, print out the customer information for customer_id = 34
getCustomer(34)
