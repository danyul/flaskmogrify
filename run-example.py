import flaskmogrify

def func(text):
    transmogrification_result = text[::-1]
    return transmogrification_result

flaskmogrify.TRANSMOGRIFY_FUNCTION = func
flaskmogrify.EXAMPLE_TEXT =  "Lorum ipsum dolor sit amet.  Copy-paste me into the text box and I'll be reversed.)"

if __name__ == '__main__':
    flaskmogrify.app.run(debug=True)
