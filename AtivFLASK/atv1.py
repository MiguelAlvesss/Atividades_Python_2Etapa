from flask import Flask

app = Flask(__name__)

@app.route('/decorator')
def home():
    return '''<h1> O que é um decorator em Python</h1> 
    <p> é uma função que recebe outra função como argumento, estende ou modifica o seu comportamento e retorna uma nova função, tudo isso sem alterar o código-fonte original da função decorada </p> 

    <h1> Para que ele serve </h1>

    <p> Um decorator serve principalmente para separar a lógica principal do seu código de tarefas secundárias ou repetitivas, permitindo modificar o comportamento de funções ou classes sem mexer na estrutura interna delas. </p>

    <h1> Como ele é utilizado no Flask (exemplo: @app.route) </h1> 

    <p> No framework Flask, o decorator @app.route serve para vincular uma URL específica (rota) a uma função Python (chamada de view function). Quando um usuário acessa essa URL no navegador, o Flask executa a função associada e exibe o retorno na tela [1]. </p>
    '''


if __name__ == '__main__':
    app.run(debug=True)