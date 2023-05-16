from flask import Flask,request,render_template
import triangulo 

app = Flask(__name__)

@app.route("/", methods=["GET"])
def pedir_datos():
    return render_template("mostrar.html",datos="")
@app.route("/", methods=["POST"])
def mostrar():
    try:
        base = float(request.form['base'])
        altura = float(request.form['altura'])
    except ValueError:
        a="Deben ser números"
    except:
        a="fallo general"
    else:
        a=str(triangulo.Triangulo(base,altura))
    finally:
        return render_template("mostrar.html",datos=a)