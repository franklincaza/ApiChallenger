import pyodbc
import pandas as pd
import time
import models_html
import email_

def conexionBD():
    """
    datos para conectar la base datos con pyodbc los datos ejemplo
        server : 'tcp:myserver.database.windows.net'
        database : 'mydb'
        username : 'myusername'
        password : 'mypassword'
    """
    try:
        server = "baan"
        database = "baan"
        username = "comunit"
        password = "CHAL2023"

        
        connection =pyodbc.connect(
            'DRIVER={Oracle en OraDB21Home1};SERVER=' + server +
            ';DATABASE=' + database + ';UID=' + username + ';PWD=' + password)

        print("Conectando ala base datos con exito")
      
    except Exception as e :

         print("Error en conectar , la base de datos ", e)





def Select_datos_sql(query):
    """
    funcion para leer tabla  valores en SQLserve:
    debe consultar el config.xlsx que esta en el archivo de excel en la carpeta
    data por ejemplo :
    ____________________________________________________________________________
    Select_datos_sql(NOMINA_COBRO_TRAB_VCTO )
    ____________________________________________________________________________
    """
    try:
        connection = conexionBD()
        cursor = connection.cursor()
        Dt= cursor.execute(query)
        return Dt
        cursor.close()
    except Exception as e:
        print("Error en el select revisar la funcion def Select_datos_sql(query) ",e)




def task ():
    DF= pd.read_excel("BDemails.xlsx",sheet_name="Hoja1")

    f= models_html.html
    for i in range(len(DF)):
       
       fecha_pago = DF.iloc[i]['fecha pago']
       valor_a_pagar = DF.iloc[i]['valor a pagar']
       identificacion = DF.iloc[i]['doc']
       partner = DF.iloc[i]['partner']
       banco =  DF.iloc[i]['banco']
       cuenta = DF.iloc[i]['orden']
       email = DF.iloc[i]['email']

       body=str(f).replace("T$PDAT",str(fecha_pago))
       body=body.replace("T$AMTH$1",str(valor_a_pagar))
       body=body.replace("T$FNUM",str(identificacion))
       body=body.replace("T$NAMA",str(partner))
       body=body.replace("T$CB",str(banco))
       body=body.replace("T$BANO",str(cuenta))
       body=body.replace("T$REFR",str(valor_a_pagar))
       body=body.replace("T$AMNT",str(valor_a_pagar))
       body=body.replace("t$DISA",str(valor_a_pagar))
       body=body.replace("@RETEFTE",str(valor_a_pagar))
       body=body.replace("@RETEICA",str(valor_a_pagar))
       body=body.replace("@RETEIVA",str(valor_a_pagar))
      
       w = open("EmailOut/"+str(cuenta)+"-"+str(partner)+".html","w")
       w.write(body)
       w.close()

       email_.enviarEmail(remitente=email,
                          body=body,
                          asunto="factura "+str(cuenta))
    exportar =DF.to_html() 
    return exportar

