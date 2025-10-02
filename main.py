from flask import Flask

app = Flask(__name__)

@app.route("/")
def Pagina_inicial():
    return "<h1>Olá, Flask!Minha primeira pagina web!</h1>"

@app.route("/sobre")
def Pagina_sobre():
    return "<h3>Sobre</h3>" "<p>Estou fazendo programa com flask</p>"
    

@app.route("/Calculadora")
def Calculadora():
    a = 10
    b = 10
    c = a * b
    return f"{c}"

@app.route("/pkm")
def pkm():
    pkm = "<h1>Lista de pokemons</h1>"
    pokemons = [
    "bulbasaur",
    "charmander",
    "squirtle",
    "chikorita",
    "cyndaquil",
    "totodile"
]

    for pokemon in pokemons:
        pkm += f"<p>{pokemon}</p>"
    return pkm

@app.route("/sorteio")
def mostrar_sorteio():
    import random
    numero = random.randint(1,100)
    return f"<h1>Seu numero da sorte é: {numero}</h1>"

@app.route("/saudacao")
def rota_saudacao():
    nome = "Bruno" 
    return f"Bem vindo {nome}!" 

@app.route("/calculo")
def soma(a,b):
    a = 15
    b = 27
    soma = a + b
    return f"<h1>{a}+{b}={soma}</h1>"
    

if __name__ == '__main__':
    app.run(debug=True)


        