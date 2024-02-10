""" Returns 5 most loyal companies. """
import sqlite3
from plot_services.bar_chart import BarChart

def connect_and_retrieve_db_data() -> list:
    """
    Query database in order to fetch customers with most orders made.
    No params
    Returns:
        list()
    """
    with sqlite3.connect("Northwind.db") as DB_CONNECTION: 
        cursor = DB_CONNECTION.cursor() # A cursor will help us to do SQL queries so as to retrieve DB data.

        cursor.execute(
            """
            SELECT Orders.CustomerID, Customers.CustomerName, COUNT(Orders.CustomerID) AS CustomerOrders FROM Orders
            JOIN Customers ON Orders.CustomerID = Customers.CustomerID
            GROUP BY CustomerName
            HAVING CustomerOrders > 3
            ORDER BY CustomerOrders DESC
            LIMIT 5;
            """)

        customers = cursor.fetchall()

        customer_list = [employee[1] for employee in customers]
        customer_orders = [employee[2] for employee in customers]

        return customer_list, customer_orders


if __name__ == "__main__":
    BarChart.bar_chart(connect_and_retrieve_db_data(), "5 most loyal customers", "Customer", "Total Orders")
