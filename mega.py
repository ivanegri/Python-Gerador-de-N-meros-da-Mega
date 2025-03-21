from flask import Flask, render_template, request
import random

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        quantidade = int(request.form['quantidade'])
        if 1 <= quantidade <= 60:
            numeros_aleatorios = random.sample(range(1, 61), quantidade)
            return render_template('index.html', numeros=numeros_aleatorios, quantidade=quantidade)
        else:
            mensagem_erro = "Por favor, insira um número entre 1 e 15."
            return render_template('index.html', mensagem_erro=mensagem_erro)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)