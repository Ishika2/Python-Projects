import mysql.connector
con = mysql.connector.connect(host = "localhost", user = "root", passwd = "")
mc = con.cursor()
mc.execute("Use test")
ACC = 2
DEPTAMT = 2000
mc.execute("UPDATE TRANSACTION SET BAL_IN_ACC = BAL_IN_ACC + {} WHERE ACC_NO = {}".format(DEPTAMT,ACC))
mc.execute("Commit")
print("Transaction done !!!")
mc.close()
