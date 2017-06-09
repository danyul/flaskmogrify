import flaskmogrify

flaskmogrify.app.config['transmogrify_function'] = lambda x: x[::-1]
flaskmogrify.app.config['transmogrify_sample_text'] =  \
    "Lorum ipsum dolor. Copy-paste me into the textbox and I'll be reversed.)"

if __name__ == '__main__':
    flaskmogrify.app.run(debug=True)
