from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return '''
        <html>
            <head><title>Hello Page</title></head>
            <body style="text-align: center; margin-top: 100px;">
                <h1 style="font-size: 72px;">HELLO WORLD</h1>
            </body>
        </html>
    '''

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
