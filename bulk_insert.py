import pyodbc

conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=10.162.226.96,1435;'
                      'Database=BD_RMCA;'
                      'Trusted_Connection=yes;')
cursor = conn.cursor()

csv_file_nm = 'C:\\Users\\1015943\\Desktop\\Repository\\PPD_04102023.csv'
db_table_nm = 'db.TBL_VEP'

qry = "BULK INSERT " + db_table_nm + " FROM '" + csv_file_nm + "' WITH (FORMAT = 'CSV', FIRSTROW = 2)"

success = cursor.execute(qry)
conn.commit()
cursor.close