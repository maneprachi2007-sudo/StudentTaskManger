import mysql.connector

def get_database_connection():

    connection = mysql.connector.connect(
        host="gateway01.ap-southeast-1.prod.aws.tidbcloud.com",
        user="jv3Yu2NL1ExHgCF.root",
        password="XoCSBiaITHYCcB4B",
        database="student_task_manager",
        port=4000
    )
    
    return connection
    