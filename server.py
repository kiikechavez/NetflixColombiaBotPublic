from flask import Flask

PORT = 3000

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def main(*args, **kwargs):
    return "<h1>¡Bienvenido a Netflix Colombia!</h1>"

@app.route('/NetflixColombiaBot')
def bienvenida(*args, **kwargs):
    return "Bienvenido a Netflix"

if __name__ == '__main__':
    app.run('0.0.0.0', port=PORT)

