from flask import Flask, url_for, request, redirect, render_template


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('login_form.html')

@app.route('/success/<name>')
def success(name):
    return 'welcome %s' % name

@app.route('/login', methods = ['POST', 'GET'])
def login():
    user = ''
    if request.method =='POST':
        user = request.form['nm']
    else:
        user = request.args.get('nm')

    return redirect(url_for('success', name = user))

if __name__ == '__main__':
    app.run(debug = True)

