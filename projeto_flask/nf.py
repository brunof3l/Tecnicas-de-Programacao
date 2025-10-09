from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def lanca():
    return render_template('lançar.html')
        

@app.route("/")
def validar():
    return render_template('validar.html')



if __name__ == '__main__':
    app.run(debug=True)