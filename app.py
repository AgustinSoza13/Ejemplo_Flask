from flask import Flask,jsonify,render_template,request
from clase_1 import main


def lista(conjunto):
    if conjunto!=None:
        return conjunto
    else:
        return "Película no encontrada"
    
def get_message(r):
    if r==True:

        return "Película encontrada"
    else:
        return "película no encontrada"
    


app=Flask(__name__)#instacimos flask

@app.route("/usuario",methods= ['POST','GET'])#ir aesta ruta
def catalogo():
    if request.method == 'POST':
        pelicula = request.form["peli"]
        respuesta,conjunto=main(pelicula)
        return render_template("respuesta.html", message=get_message(respuesta)+pelicula,mensaje=lista(conjunto)) #deben ir a respuesta.html  

        #return "<h1>Pelicula"+pelicula+"encontrada</h1><br>"+
    #"pelicula encontrada dentro del conjunto"
    
    
    else:
        return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True,port=7000)