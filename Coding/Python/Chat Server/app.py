from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# This will store messages temporarily. In a real-world application, you'd use a database.
messages = []

@app.route('/')
def index():
    return render_template('index.html', messages=messages)

@app.route('/post_message', methods=['POST'])
def post_message():
    username = request.form['username']
    message = request.form['message']
    messages.append({'username': username, 'message': message})
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
