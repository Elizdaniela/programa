from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/mensaje', methods=['POST'])
def mensaje():
    if request.method == 'POST':
        
        nombre = request.form.get('name')  
        email = request.form.get('email')
        telefono = request.form.get('telefono')
        
        
        if not nombre or not email or not telefono:
            return render_template('mensaje.html', name='Desconocido', email='No proporcionado', telefono='No proporcionado')
        
        
        return render_template('mensaje.html', name=nombre, email=email, telefono=telefono)

if __name__ == '__main__':
    app.run(debug=True)