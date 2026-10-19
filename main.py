import sqlite3
import pandas as pd

conn = sqlite3.connect('data.sqlite')

q = """PRAGMA table_info(offices);"""
 
q = """PRAGMA table_info(employees);"""
 

q = """SELECT * FROM offices;"""
 
q = """SELECT * FROM employees;"""
 

q = """SELECT firstName, lastName FROM employees JOIN offices USING(officeCode) WHERE city = 'Boston';"""

#Are there any offices that have zero employees?
q = """SELECT
    o.officeCode,
    o.city,
    COUNT(e.employeeNumber) AS n_employees
FROM offices AS o
LEFT JOIN employees AS e
    USING(officeCode)
GROUP BY officeCode
HAVING n_employees = 0
;"""

#How many customers are there per office?
q = """
SELECT
    o.officeCode,
    o.city,
    COUNT(c.customerNumber) AS n_customers
FROM offices AS o
JOIN employees AS e
    USING(officeCode)
JOIN customers AS c
    ON e.employeeNumber = c.salesRepEmployeeNumber
GROUP BY officeCode
;
"""


#Display the names of every individual product that each employee has sold as a dataframe
q = """
SELECT firstName, lastName, productName
FROM employees AS e
JOIN customers AS c
    ON e.employeeNumber = c.salesRepEmployeeNumber
JOIN orders
    USING(customerNumber)
JOIN orderdetails
    USING(orderNumber)
JOIN products
    USING(productCode)
;
"""
print(pd.read_sql(q, conn))