""" Returns total sales an employee has made. """
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
            -- Returns list of best salesperson employee :D
            SELECT Employees.EmployeeID, Employees.FirstName, SUM(OrderDetails.Quantity) AS BestSalesPerson FROM OrderDetails
            JOIN Orders ON OrderDetails.OrderID = Orders.OrderID
            JOIN Employees ON Orders.EmployeeID = Employees.EmployeeID
            GROUP BY FirstName
            ORDER BY BestSalesPerson DESC;
            """)

        employees = cursor.fetchall()

        employees_list = [employee[1] for employee in employees]
        employees_sales = [employee[2] for employee in employees]

        return employees_list, employees_sales



if __name__ == "__main__":
    BarChart.bar_chart(connect_and_retrieve_db_data(), "Best Salesperson", "Employee", "Total Sales")
