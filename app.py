from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/')
def hello_world():
    data = ['1', '2', '3', '4', '5', '6', '7']
    if 'name' in request.args:
        return render_template('index.html',
                               name=request.args["name"],
                               lastname=request.args["lastname"],
                               data=data,
                               flag=False)
    else:
        return render_template('index.html',
                               name='Olena',
                               lastname='Bdzhilka',
                               data=data,
                               flag=False)


@app.route('/data')
def data():
    return render_template('data.html')


if __name__ == '__main__':
    app.run()
