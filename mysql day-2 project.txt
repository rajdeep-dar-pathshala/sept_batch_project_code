create database sept_python_project_da_1;
use sept_python_project_da_1;
show tables;
select * from cust_details;
CREATE TABLE cust_details (
    cust_id INT AUTO_INCREMENT PRIMARY KEY,
    cust_name VARCHAR(100) NOT NULL,
    cust_address VARCHAR(255) not null,
    cust_phone_no VARCHAR(10) not null,
    cust_user_id VARCHAR(50) NOT NULL,
    cust_password VARCHAR(100) NOT NULL
)AUTO_INCREMENT=1;

INSERT INTO cust_details (cust_name, cust_address, cust_phone_no, cust_user_id, cust_password) 
VALUES 
('John Doe', '123 Main Street, Springfield', '9876543210', 'johndoe123', 'securepassword123');

truncate cust_details;

select * from cust_details where cust_id=1;

CREATE TABLE audit_table (
    sl_no INT AUTO_INCREMENT PRIMARY KEY,
    cust_id INT NOT NULL,
    cust_name VARCHAR(100) NOT NULL,
    login_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    logout_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)AUTO_INCREMENT=1;

select * from audit_table;

truncate table audit_table;

INSERT INTO audit_table (cust_id, cust_name,logout_time) VALUES (101, 'John Doe',null);
INSERT INTO audit_table (cust_id, cust_name,login_time) VALUES (101, 'John Doe',null);

drop table audit_table;


