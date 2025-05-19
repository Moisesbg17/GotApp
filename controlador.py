from flask import Flask
app=Flask(__name__)

@app.route('/')
def inicio():
 return "<html> <h1> Primer Aplicación Web ADSO 3 </h1></html>"

@app.route('/otro')
def salir():
 return "<html> <h1> Nos vemos mañana </h1></html>"
if __name__ == '__main__':
 app.run('127.0.0.1', 5000, debug=True)