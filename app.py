from flask import Flask, render_template, request, make_response
from weasyprint import HTML

app = Flask(__name__)

@app.route('/')
def index():
    return '''
    <!DOCTYPE html>
    <html>
    <head>
        <title>Exportar PDF</title>
    </head>
    <body>
        <h1>Generar PDF</h1>
        <form method="POST" action="/generate-pdf">
            <button type="submit">Exportar PDF</button>
        </form>
    </body>
    </html>
    '''

@app.route('/generate-pdf', methods=['POST'])
def generate_pdf():
    html_content = '''
    <!DOCTYPE html>
    <html>
    <head>
        <title>PDF</title>
    </head>
    <body>
        <h1>Este es tu PDF generado</h1>
        <p>Hola, mundo desde Flask y WeasyPrint</p>
    </body>
    </html>
    '''
    pdf = HTML(string=html_content).write_pdf()
    response = make_response(pdf)
    response.headers['Content-Type'] = 'application/pdf'
    response.headers['Content-Disposition'] = 'inline; filename=output.pdf'
    return response

if __name__ == '__main__':
    app.run(debug=True)
