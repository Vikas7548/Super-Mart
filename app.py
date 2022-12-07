from flask import Flask, render_template, request
import mysql.connector

app = Flask(__name__)

def fetch_data(cust_id="", location="", trans_id="", prod_category=""):
    
    mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "vikas",
    database = 'super_mart'
    )
    cursor = mydb.cursor()
    # get all the employee details
    if len(cust_id)>1:
        query = """
                SELECT Cus.*, O.*
                FROM super_mart.customers Cus
                Join super_mart.Orders O
                on Cus.cust_id = O.cust_id and Cus.cust_id={id}
                
                """      
        main_query = query.format(id=int(cust_id))
        cursor.execute(main_query)
        sequence = cursor.column_names
        main_data = tuple()
        for result in cursor:
            main_data+=result
        return(sequence, main_data)
        
"""
    
    # get all the employee salaries greater than given input
    if len(salary)>1:
        query = "select * from emp_salary where salary = "+str(salary)
        cursor.execute(query)
    
 
    # get the projects and managers
    if len(project)>1:
        query = "select * from emp_data where emp_id = "+str(data)
        cursor.execute(query)

    
    # get the project details where income is greater than given input
    if len(income)>1:
        query = "select * from emp_data where emp_id = "+str(data)
        cursor.execute(query)


    # get the employee data who deals with the project greater than the income given
    if len(project)>1 and len(income)>1:
        query = "select * from emp_data where emp_id = "+str(data)
        cursor.execute(query)



    # get the details of the employees with there projects based on the salary
    if len(salary)>1 and len(project)>1:
        query = "select * from emp_data where emp_id = "+str(data)
        cursor.execute(query)
"""


@app.route("/", methods =["GET", "POST"])
def index():
    if request.method == "POST":
        cust_id = request.form['cust_id']
        location = request.form['location']
        trans_id = request.form['trans_id']
        prod_catgory = request.form['prod_category']
        headings, data = fetch_data(cust_id, location, trans_id, prod_catgory)
        return render_template("index.html", headings=headings, data=data)
    return render_template("index.html")


if __name__=="__main__":
    app.run(debug=True)
    