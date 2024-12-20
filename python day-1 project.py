#Database connection details
import mysql.connector

conn_obj=mysql.connector.connect(
    host="localhost",
    user="root",
    password="R@jdeep123",
    database="sept_python_project_da_1")
cur_obj=conn_obj.cursor()

#Define function data_entry_sql
def data_entry_sql(user_name,user_address,user_phone_no,user_id,user_password):

    # Build the query with user-provided name using LIKE operator
    sql = "INSERT INTO cust_details (cust_name, cust_address, cust_phone_no, cust_user_id, cust_password) VALUES (%s, %s, %s, %s, %s)"
    data = (user_name,user_address,user_phone_no,user_id,user_password)

    try:
        cur_obj.execute(sql, data)
        print("Your data entered in our database succesfully")
        conn_obj.commit()
    except mysql.connector.Error as e:
        print("Error retrieving data from MySQL:", e)
        conn_obj.rollback()

#Define function data_retrieve
def data_retrieve(user_id):
    # Build the query with user-provided name using LIKE operator
    #select * from students_details WHERE Roll_no=1;
    query = f"select * from cust_details WHERE cust_user_id=\'{user_id}\'"
    #print(query)
    try:
        cur_obj.execute(query)
        result = cur_obj.fetchone()
        conn_obj.commit()
    except mysql.connector.Error as e:
        print("Error retrieving data from MySQL:", e)
        conn_obj.rollback()
    return result

def new_cust_registration(user_id):
    user_name=input("Please enter your full name- ")
    user_address = input("Please enter your full address- ")
    user_phone_no = input("Please enter your phone number- ")
    user_password = input("Please enter your password- ")
    data_entry_sql(user_name,user_address,user_phone_no,user_id,user_password)

def login_check(details_from_database):
    user_password=input("please enter your password- ")
    if user_password==details_from_database[-1]:
        #print("access granted")
        return 1
    else:
        #print("access denied")
        return 0

def login_entry(cust_id, cust_name,logout_time=None):

    # Build the query with user-provided name using LIKE operator
    sql = "INSERT INTO audit_table (cust_id, cust_name,logout_time) VALUES (%s, %s,%s)"
    data = (cust_id, cust_name, logout_time)

    try:
        cur_obj.execute(sql, data)
        #print("Your data entered in our database succesfully")
        conn_obj.commit()
    except mysql.connector.Error as e:
        print("Error retrieving data from MySQL:", e)
        conn_obj.rollback()

def logout_entry(cust_id, cust_name,login_time=None):

    # Build the query with user-provided name using LIKE operator
    sql = "INSERT INTO audit_table (cust_id, cust_name,login_time) VALUES (%s, %s,%s)"
    data = (cust_id, cust_name, login_time)

    try:
        cur_obj.execute(sql, data)
        #print("Your data entered in our database succesfully")
        conn_obj.commit()
    except mysql.connector.Error as e:
        print("Error retrieving data from MySQL:", e)
        conn_obj.rollback()

user_id=input("Please enter your user_name- ")
details_from_database=data_retrieve(user_id)
#print(details_from_database)
if details_from_database:
    result_from_login_check=login_check(details_from_database)
    if result_from_login_check:
        # login time should be recorded
        login_entry(details_from_database[-2],details_from_database[1])
        print("Access granted.")
        cust_choice=input("Do you want to logout ? enter y/n")
        if cust_choice=='y' or cust_choice=='Y':
            logout_entry(details_from_database[-2],details_from_database[1])
            print("You have logged out")
    else:
        print("access denied")
else:
    new_cust_registration(user_id)
conn_obj.close()
