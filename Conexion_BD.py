import cx_Oracle
import querys
import pandas as pd

username = 'comunit'
password = 'chal2023'
dsn = '172.25.8.58/baan'
port = 1521
encoding = 'UTF-8'


try:
    connection = cx_Oracle.connect(
        username,
        password,
        dsn,
        encoding=encoding)

    #show the version of the Oracle Database
    print(connection.version)

    cursor = connection.cursor()
    filtro = 'PN0022000'
    query ='select * from baan.ttccom125120 where t$ptbp = :1'
    #query= querys.query01
    #cursor.execute(query,(filtro,))
    #df=pd.DataFrame(query)
    #df.to_excel("BDemails.xlsx",sheet_name="Hoja1",index=False)
    for row in cursor:
        print(row)

except cx_Oracle.Error as error:
    print(f"Error executing SQL: {error}")

#except cx_Oracle.Error as error:
#    logging.debug('Error conexion oracle\n')
#    print(error)

finally:
    cursor.close()
    connection.close()

