from flask import Flask, Response

app = Flask(__name__)

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    with open('templates/contacts.html', 'r', encoding='utf-8') as file:
        html_content = file.read()
    return Response(html_content, mimetype='text/html')

if __name__ == '__main__':
    app.run(debug=True)
