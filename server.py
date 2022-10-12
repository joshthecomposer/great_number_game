from flask import Flask, session, render_template, redirect, request
import random
app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe'

@app.route('/', methods=['GET', 'POST'])
def index():
    if 'total' in session:
        if session['total'] >= 5:
            return redirect('/lose')
    if 'guess' not in session:
        session['secret_number'] = int(random.randint(0, 100))
    return render_template('index.html')

@app.route('/guess', methods=['GET', 'POST'])
def guess():
    session['guess'] = int(request.form.get('guess'))
    return redirect('/check_guess')

@app.route('/check_guess', methods=['GET', 'POST'])
def check_guess():
    if 'total' not in session:
        session['total'] = 0
    if session['guess'] == session['secret_number']:
        return redirect('/success')
    session['total'] += 1
    return redirect('/')

@app.route('/success', methods=['GET', 'POST'])
def success():
    return render_template('success.html')

@app.route('/reset', methods=['GET', 'POST'])
def reset():
    session.clear()
    return redirect('/')

@app.route('/lose', methods=['GET', 'POST'])
def lose():
    return render_template('lose.html')

if __name__ == '__main__':
    app.run(debug=True)