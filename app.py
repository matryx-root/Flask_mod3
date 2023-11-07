from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ejercicio1')
def ejercicio1():
    return render_template('/ejercicio1.html')

@app.route('/ejercicio2')
def ejercicio2():
    return render_template('/ejercicio2.html')

@app.route('/procesar_ejercicio1', methods=['POST'])
def procesar_ejercicio1():
    nota1 = int(request.form['nota1'])
    nota2 = int(request.form['nota2'])
    nota3 = int(request.form['nota3'])
    asistencia = int(request.form['asistencia'])

    promedio = (nota1 + nota2 + nota3) / 3

    if promedio >= 40 and asistencia >= 75:
        resultado = "Aprobado"
    else:
        resultado = "Reprobado"

    return jsonify({"promedio": promedio, "estado": resultado})



@app.route('/procesar_ejercicio2', methods=['POST'])
def procesar_ejercicio2():
    nombre1 = request.form['nombre1']
    nombre2 = request.form['nombre2']
    nombre3 = request.form['nombre3']

    nombres = [nombre1, nombre2, nombre3]
    nombre_mas_largo = max(nombres, key=len)
    longitud_nombre = len(nombre_mas_largo)

    return jsonify({"nombre_mas_largo": nombre_mas_largo, "longitud_nombre": longitud_nombre})


if __name__ == '__main__':
    app.run(debug=True)

