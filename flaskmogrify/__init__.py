from flask import Flask, request, redirect, render_template, flash, jsonify
from flaskmogrify.forms import TransmogrificationForm


__author__ = 'Daniel Langsam'
__email__ = 'daniel@langsam.org'
__version__ = '0.0.11'

app = Flask(__name__)
app.config.from_object(__name__)

app.config.update(dict(
    SECRET_KEY='super_hard_to_guess_secret_key_1231214123167545',
))

@app.route('/get_transmogrification',methods=['POST'])
def transmogrify_wihtout_AJAX():
    fcn_index = int(request.form['radio_tfunction'])
    tfunction = app.config['transmogrify_functions'][fcn_index]
    return render_template('/results_non_AJAX.html',
                           display_text=str(tfunction(request.form['data_to_transmogrify_field'])))

@app.route('/get_transmogrification_by_ajax', methods=['POST'])
def ajax_transmogrify():
    tfunction = app.config['transmogrify_functions'][int(request.form['tfunction_index'])]
    return jsonify({ 'text': tfunction(request.form['text'])})


@app.route('/transmogrify', methods=['GET','POST'])
def transmogrify_main():
    form = TransmogrificationForm()
    if form.validate_on_submit(): # non-AJAX fallback, e.g. if Javascript disabled
        flash("Transmogrification complete!")
        return redirect('/get_transmogrification') #/results_non_AJAX.html',

    form.radio_choices.choices = [fcn.__name__ for fcn in app.config['transmogrify_functions']]
    return render_template('transmogrify.html',
                           title="Lab Data Entry",
                           form=form,
                           example_text=app.config['transmogrify_sample_text'])

@app.route('/')
def redirect_to_transmogrify_main():
    return redirect("/transmogrify")
