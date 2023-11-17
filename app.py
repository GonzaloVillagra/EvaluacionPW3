from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def inicio():
    return render_template('index.html')


@app.route('/ejercicio1', methods=['GET', 'POST'])
def ejercicio1():
    resultado = None
    mensaje = None

    if request.method == 'POST':
        nota1 = float(request.form['nota1'])
        nota2 = float(request.form['nota2'])
        nota3 = float(request.form['nota3'])
        asistencia = float(request.form['asistencia'])
        promedio = (nota1 + nota2 + nota3) / 3

        if promedio >= 40 and asistencia >= 75:
            resultado = f'Tu promedio es: {promedio:.2f}'
            mensaje = 'Aprobado'

        else:
            resultado = f'Tu Promedio es: {promedio: }'
            mensaje = 'Reprobado'

    return render_template('ejercicio1.html', resultado=resultado, mensaje=mensaje)



@app.route('/ejercicio2', methods=['GET', 'POST'])
def ejercicio2():
    resultado = None

    if request.method == 'POST':
        nombre1 = request.form['nombre1']
        nombre2 = request.form['nombre2']
        nombre3 = request.form['nombre3']

        nombres = [nombre1, nombre2, nombre3]

        # Encuentra el nombre más largo
        nombre_mas_largo = max(nombres, key=len)
        longitud = len(nombre_mas_largo)

        resultado = f'El nombre más largo es: {nombre_mas_largo},<br>con una longitud de {longitud} caracteres'

    return render_template('ejercicio2.html', resultado=resultado)


if __name__ == '__main__':
    app.run(debug=True)
