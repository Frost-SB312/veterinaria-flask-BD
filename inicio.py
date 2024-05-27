from flask import Flask, render_template, request, redirect, url_for, flash
import pymysql

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")
@app.route('/pp')
def pg_prin():
    return render_template("index.html")
@app.route('/gt')
def pg_gt():
    return render_template("gato.html")
@app.route('/pr')
def pg_pr():
    return render_template("perro.html")
@app.route('/qt')
def pg_qt():
    return render_template("quetzal.html")
@app.route('/car')
def pg_car():
    return render_template("carrusel.html")
@app.route('/con')
def pg_con():
    return render_template("contacto.html")
@app.route('/agrega_comenta', methods=['POST'])
def agrega_comenta():
    if request.method == 'POST':
        aux_Correo = request.form['correo']
        aux_Comentarios = request.form['comentarios']
        conn = pymysql.connect(host='localhost', user='root', passwd='', db='agenda' )
        cursor = conn.cursor()
        cursor.execute('insert into comenta (correo,comentarios) values (%s, %s)',(aux_Correo, aux_Comentarios))
        conn.commit()
    return redirect(url_for('home'))

if __name__ == "__main__":
    app.run(debug=True)