import flaskmogrify

def x_on_both_sides(x:str) ->str:
    return "X"+x+"X"

flaskmogrify.app.config['transmogrify_functions'] = [
    lambda x: x[::-1],
    x_on_both_sides
]

flaskmogrify.app.config['transmogrify_functions'][0].__name__ = "reversal"

flaskmogrify.app.config['transmogrify_sample_text'] =  \
    "Lorum ipsum dolor sit amet. Copy-paste me into the textbox."

if __name__ == '__main__':
    flaskmogrify.app.run(debug=True,port=5001)
