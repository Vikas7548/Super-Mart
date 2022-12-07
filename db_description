####SUPER MART MANAGEMENT SYSTEM####

Description:

This project deals with a super mart system where customers buy products from the super
marts at different locations, the database stores all the product details, txn date time and the
revenue etc

We have designed 4 database tables(customers,locations,orders and producers) with at least 5 rows of data in each table, with each table
in 3NF and performed the CRUD operations

TABLES:

1. Customers table:

Attributes:

cust_id int NOTNULL, PRIMARY KEY,

cust_name varchar(50) DEFAULT NULL,

contact_no int DEFAULT NULL,

payment_method varchar(50) DEFAULT NULL;

->Cust_id is the primary key in customers table

Sample data for customers table:
-----------------------------------------------------
| Cust_id | Cust_name | Contact_no | Payment_method |
-----------------------------------------------------
| 1001    | sri       | 93949602   | payTm          |
-----------------------------------------------------

2. Locations table:

trans_id int NOT NULL, PRIMARY KEY

cust_id int NOTNULL,

city varchar(50) DEFAULT NULL,

states varchar(50) DEFAULT NULL,

country varchar(50) DEFAULT NULL,

postal_code float DEFAULT NULL;

->Here trans_id is primary key and cust_id is foreign key

Sample data for locations table:
----------------------------------------------------------------------------
| trans_id | Cust_id | city       | states         | country | Postal_code |
----------------------------------------------------------------------------
| 22212041 | 1001    | vijayawada | AndhraPradhesh | INDIA   | 520001      |
----------------------------------------------------------------------------

3.Orders table:

trans_id int NOT NULL primary key,

cust_id int DEFAULT NULL,

purch_date int DEFAULT NULL,

units_sold int DEFAULT NULL;

In the above table trans_id is primary key & cust_id is foreign key

Sample data for orders table:
------------------------------------------------
| Trans_id | Cust_id | Purch_date | Units_sold |
------------------------------------------------
| 22212041 | 1001    | 2010       | 3          |
------------------------------------------------

4.Producers table:

trans_id int NOT NULL PRIMARY KEY,

prod_category varchar(50) DEFAULT NULL,

prod_type varchar(50) DEFAULT NULL,

revenue` float DEFAULT NULL,

purch_date` int DEFAULT NULL;

->here trans_id is primary key

sample data for producers table:
--------------------------------------------------------------------
| Trans_id | Prod_category | Prod_type      | revenue | Purch_date |
--------------------------------------------------------------------
| 22212041 | ghee          | Dairy products | 400000  | 2010       |
--------------------------------------------------------------------
