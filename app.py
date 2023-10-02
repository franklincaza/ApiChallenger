from flask import Flask 
from flask import Flask,render_template
import models
import pythoncom
import pandas as pd



app = Flask(__name__) #→Ruta Url "Creamos una ruta"

app.config.from_mapping(
DEBUG = False,
SECRET_KEY = 'devtod')

@app.route("/Enviarcorreos", methods =['GET']) 
def task_():
    pythoncom.CoInitialize()
    models.task ()
  
    return "<p>ejecucion realizada con exito</p>"

@app.route("/") 
def index():
   return render_template("index.html")


if __name__ == '__main__':#→Recomiendo poder ejecutar el servidor "
    app.run(debug = True)


