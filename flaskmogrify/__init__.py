from flask import Flask, request, redirect, render_template, flash, jsonify
from flaskmogrify.forms import TransmogrificationForm

__author__ = 'Daniel Langsam'
__email__ = 'daniel@langsam.org'
__version__ = '0.0.6'

app = Flask(__name__)
app.config.from_object(__name__)

app.config.update(dict(
    SECRET_KEY='super_hard_to_guess_secret_key',
))

@app.route('/get_transmogrification_by_ajax', methods=['POST'])
def ajax_transmogrify():
    return jsonify({ 'text': app.config['transmogrify_function'](request.form['text'])})

@app.route('/transmogrify', methods=['GET','POST'])
def transmogrify_main():
    form = TransmogrificationForm()
    if form.validate_on_submit(): # non-AJAX fallback, e.g. if Javascript disabled
        flash("Transmogrification complete!")
        return render_template('/results_by_GET.html',
            display_text = app.config['transmogrify_function'](form.data_to_transmogrify_field.data))
    return render_template('transmogrify.html',
                           title="Lab Data Entry",
                           form=form, example_text=app.config['sample_text'])

@app.route('/')
def redirect_to_transmogrify_main():
    return redirect("/transmogrify")
