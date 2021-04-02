from flask import Flask, jsonify, render_template
from api.dados import Dados

app = Flask('api-dados')
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = False

dados = Dados()
dados.start()

@app.route('/', methods=['GET'])
def inicial():
    return render_template('inicial.html', titulo='Pedidos a Separar' ,lista_dados=dados.get())


@app.route('/finalizar-separacao-pedido/<id_pedido>', methods=['GET'])
def finalizar_separacao_pedido(id_pedido):
    # finalizar_pedido()
    return jsonify({
        'id_pedido' : id_pedido,
        'status'    : 'finalizado'
    })


if __name__ == "__main__":
    app.run(port=5000, debug=True, host='0.0.0.0')