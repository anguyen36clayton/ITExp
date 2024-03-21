from flask import Flask, request, render_template
import markdown2

app = Flask(__name__, static_url_path='/static')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/render', methods=['POST'])
def render_markdown():
    if request.method == 'POST':
        markdown_content = request.form.get('markdown_content', '')
        html_content = markdown2.markdown(markdown_content, extras=["fenced-code-blocks"])
        return html_content

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)