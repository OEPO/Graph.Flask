from flask import Flask, render_template, url_for, redirect
from forms import NodesClass
import networkx as nx
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

app= Flask(__name__)
app.config['SECRET_KEY'] = '64fa09145bd39641bbc316d33c351458'   #Proteccion contra ataques por cookies,etc.
#token HEX(16) generado con la libreria secrets
app.config['TEMPLATES_AUTO_RELOAD'] = True
@app.route("/")
def pload():
    return render_template("pre-load.html")

@app.route("/home",methods=['GET','POST'])
def home():
    form = NodesClass()
    if form.validate_on_submit():
        if form.check.data == True:
            info = "1"+"&"+form.edge.data
        else:
            info = "0"+"&"+form.edge.data
             #concadena los datos para enviarlos por url
        return redirect(url_for("plot",form = info))
    return render_template("index.html", title='Home',form = form)

@app.route("/grafo/<string:form>")
def plot(form):#ejemplo: 1&1,2;2,3;3,4;2,4;5,5;6,2 o 0&1,2;2,3;3,4;2,4;5,5;6,2
    separar_informacion = form.split("&")
    edges0 = separar_informacion[1].split(";")
    edges = []
    for i in edges0:
        edges.append(tuple(i.replace(',',''))) #agrega los vertices en tuplas tipo [('1', '2'), ('2', '3'), ('3', '4'), ('2', '4'), ('5', '5'), ('6', '2')]
    
    if separar_informacion[0] == "1":#Crea o no un grafo dirigido.
        g = nx.DiGraph()
    else:
        g = nx.Graph()
    
    g.add_edges_from(edges)
    nx.draw(g,with_labels=True)
    plt.savefig('static/images/graph.png')

    plt.clf()#limpia los parametros
    g.clear()
    return render_template("grafo.html",url='/static/images/graph.png')


if __name__ == '__main__':
    app.run(debug=True)