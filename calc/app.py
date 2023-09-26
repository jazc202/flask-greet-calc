import flask as fl
import operations as op

app = fl.Flask(__name__)


@app.route('/<math>')
def operation(math):
    a = int(fl.request.args.get('a'))
    b = int(fl.request.args.get('b'))

    operate = {
        'add': op.add(a, b),
        'sub': op.sub(a, b),
        'mult': op.mult(a, b),
        'div': op.div(a, b)
    }

    return str(operate.get(math))


@app.route('/math/<math>')
def doMath(math):
    a = int(fl.request.args.get('a'))
    b = int(fl.request.args.get('b'))

    operate = {
        'add': op.add(a, b),
        'sub': op.sub(a, b),
        'mult': op.mult(a, b),
        'div': op.div(a, b)
    }

    return str(operate.get(math))
