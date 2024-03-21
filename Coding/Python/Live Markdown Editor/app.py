from flask import Flask, render_template, request
import markdown2

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    markdown_content = ""
    html_content = ""

    if request.method == 'POST':
        # Get Markdown content from form submission
        markdown_content = request.form['markdown_content']

        # Convert Markdown to HTML
        html_content = markdown2.markdown(markdown_content)

    return render_template('index2.html', markdown_content=markdown_content, html_content=html_content)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)