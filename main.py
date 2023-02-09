import pyodbc
import pandas as pd

dbcn = pyodbc.connect('DSN=JUDB')

print("DB접속 완료")

rows = pd.read_sql("""
    SELECT DISTINCT ADMIN_ID, MEAS_DT FROM IST_METER_DATA
""", dbcn)


df = pd.DataFrame(rows)

# df.to_excel("test.xlsx",index=None)

print(df)

dbcn.close()