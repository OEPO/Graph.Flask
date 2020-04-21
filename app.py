from flask import Flask, render_template, url_for, redirect
from forms import NodesClass
import networkx as nx
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

app= Flask(__name__,static_url_path='/static')

app.config['SECRET_KEY'] = '64fa09145bd39641bbc316d33c351458'   #Proteccion contra ataques por cookies,etc.
#token HEX(16) generado con la libreria secrets
@app.route("/")
def pload():
     return render_template("pre-load.html")
     






@app.route("/home",methods=['GET','POST'])
def home():
    
    form = NodesClass()
    if form.validate_on_submit():
        # pasa el dato de node a grafos.
        return redirect(url_for("plot",form = str(form.node.data))) 
    return render_template("index.html", title='Home',form = form)

@app.route("/grafo<string:form>")
def plot(form):

    g = nx.DiGraph()

    g.clear()
    plt.clf()

    a = []
    s = form.split(";")
    for i in s:
        b = i.split(",")
        a.append(b)
    
    g.add_edges_from(a)
    nx.draw(g)
    plt.savefig('static/images/graph.png')

    return render_template("grafo.html",url='/static/images/graph.png')


if __name__ == '__main__':
    app.run(debug=True)