from flask import Flask, render_template, redirect, url_for, flash
from forms import NumberForm
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'

@app.route('/', methods=['GET', 'POST'])
def index():
    form = NumberForm()
    if form.validate_on_submit():
        number = form.number.data
        if len(set(str(number))) == len(str(number)):
            flash('Цифри не повторюються!', 'success')
            result = 'yes'
        else:
            flash('Є повторювані цифри!', 'danger')
            result = 'no'
        return redirect(url_for('result', outcome=result))
    return render_template('index.html', form=form)

@app.route('/result/<outcome>')
def result(outcome):
    return render_template('result.html', outcome=outcome)

if __name__ == '__main__':
    app.run(debug=True)