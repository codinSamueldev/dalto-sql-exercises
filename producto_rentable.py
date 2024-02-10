""" Returns profitable product. """

import sqlite3
from plot_services.bar_chart import BarChart

def connection_and_retrieve_db_info():
    with sqlite3.connect("Northwind.db") as DB_CONNECTION:
        cursor = DB_CONNECTION.cursor()

        cursor.execute("""
                       SELECT
                            Products.ProductName,
                            OrderDetails.ProductID, 
                            SUM(Quantity) AS TotalSales,
                            Products.Price AS ProductPrice,
                            SUM(OrderDetails.Quantity * Products.Price) AS Revenue
                        FROM OrderDetails
                        JOIN Products ON OrderDetails.ProductID = Products.ProductID
                        WHERE Products.Price > 40
                        GROUP BY OrderDetails.ProductID
                        HAVING ProductPrice IS NOT NULL AND ProductPrice > 50
                        ORDER BY Revenue DESC
                        LIMIT 3;""")
        
        profitable_products = cursor.fetchall()

        profitable_product_name = [product[0] for product in profitable_products]
        profitable_product_revenue = [product[-1] for product in profitable_products]

        return profitable_product_name, profitable_product_revenue



if __name__ == "__main__":
    BarChart.bar_chart(connection_and_retrieve_db_info(), "Best 3 profitable products.", "Product Name", "Total Revenue")
    