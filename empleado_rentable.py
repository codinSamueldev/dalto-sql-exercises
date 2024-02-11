""" Returns Best Employees. """
import sqlite3
from plot_services.bar_chart import BarChart


def connect_and_retrieve_db_data() -> list:
    """
    Query database in order to fetch employees with most orders filled.
    No params
    Returns:
        list()
    """
    with sqlite3.connect("Northwind.db") as DB_CONNECTION: 
        cursor = DB_CONNECTION.cursor() # A cursor will help us to do SQL queries so as to retrieve DB data.

        cursor.execute(
            """
            SELECT Employees.EmployeeID, Employees.FirstName, COUNT(OrderDetails.OrderID) AS TotalEmployeeOrdersFilled FROM OrderDetails
            JOIN Orders ON OrderDetails.OrderID = Orders.OrderID
            JOIN Employees ON Orders.EmployeeID = Employees.EmployeeID
            GROUP BY FirstName
            ORDER BY TotalEmployeeOrdersFilled DESC
            LIMIT 5;
            """)

        employees = cursor.fetchall()

        employees_list = [employee[1] for employee in employees]
        employees_orders_filled = [employee[2] for employee in employees]

        return employees_list, employees_orders_filled


if __name__ == "__main__":
    BarChart.bar_chart(connect_and_retrieve_db_data(), "5 most productive employees.", "Employees", "Total orders employee has filled")
