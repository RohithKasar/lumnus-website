from flask import Flask, render_template, request, redirect, url_for


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/team')
def team():
    return render_template('team.html')


@app.route('/clients-1')
@app.route('/clients')
def clients():
    return render_template('clients.html')


@app.route('/work-with-us')
def work():
    return render_template('work.html')


@app.route('/projects')
def projects():
    return render_template('project.html')


@app.route('/join-us')
def join():
    return render_template('join.html')


if __name__ == "__main__":
    app.run()

