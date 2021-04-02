from flask import Flask, jsonify, render_template
from api.dados import Dados

app = Flask('api-dados')
dados = Dados()
dados.start()

@app.route('/', methods=['GET'])
def inicial():
    return render_template('inicial.html', lista_dados=dados.get())

if __name__ == "__main__":
    app.run(port=5000, debug=True, host='0.0.0.0')