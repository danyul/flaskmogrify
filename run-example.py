import flaskmogrify

flaskmogrify.app.config['transmogrify_functions'] = [
    lambda x: x[::-1],
    lambda x: "X"+x+"X"
]
flaskmogrify.app.config['transmogrify_functions'][0].__name__ = "reversal"
flaskmogrify.app.config['transmogrify_functions'][1].__name__ = "x_on_both_sides"

flaskmogrify.app.config['transmogrify_sample_text'] =  \
    "Lorum ipsum dolor sit amet. Copy-paste me into the textbox."

if __name__ == '__main__':
    flaskmogrify.app.run(debug=True,port=5001)
