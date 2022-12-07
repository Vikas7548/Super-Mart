#########CRUD OPERATIONS ON SQL#################

1) ORDERS TABLE:

select * from orders;   -- displays all the rows of orders table
select * from orders where cust_id=1001;  --displays all column values where cust_id=1001

##update operation

update orders             
set units_sold=8
where cust_id=1001;   ----updates order table of units_sold from 3to8 where    cust_id=1001

##delete operation 

delete from orders where trans_id=22212041;     ---deletes the row where trans_id=22212041;

##truncate operation

truncate table orders; --deletes data from the orders table but not the structure


