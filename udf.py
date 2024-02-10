""" User Defined Functions. """

import sqlite3

squared = lambda n: n*n


def retrieve_db_data(conn: sqlite3.connect, function_name):
    """
    Retrieve all DB data based on the sqlite connection.

    create_function method receives: 
    ° The name we want to give to our function (1st param).
    ° How many params should receive the function (2nd param).
    ° Which Python function does what you want to do (3rd param). 
    """
    return conn.create_function("Squared", 1, function_name)


with sqlite3.connect("Northwind.db") as DB_CONNECTION: 
    cursor = DB_CONNECTION.cursor() # A cursor will help us to do SQL queries so as to retrieve DB data.
    
    retrieve_db_data(DB_CONNECTION, squared)

    cursor.execute(
        """
        SELECT *, ROUND(Squared(Price)) FROM Products LIMIT 5
        """)

    employees = cursor.fetchall()

    for employee in employees:
        print("ProductID:", employee[0])
        print("ProductName:", employee[1])
        print("SupplierID:", employee[2])
        print("CategoryID:", employee[3])
        print("Unit:", employee[4])
        print("Price:", employee[5])
        print("PriceSquared:", employee[6])
        print("\n")
    
