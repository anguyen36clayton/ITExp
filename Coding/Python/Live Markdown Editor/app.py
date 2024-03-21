from flask import Flask, render_template, request
import markdown2

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        markdown_content = request.form['markdown_content']
        html_content = markdown2.markdown(markdown_content)
        return render_template('index.html', html_content=html_content, markdown_content=markdown_content)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)