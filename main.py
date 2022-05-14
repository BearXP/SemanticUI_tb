# Importing flask module in the project is mandatory
# An object of Flask class is our WSGI application.
from flask import Flask, render_template, request

fileBeingProcessed = {}

# Flask constructor takes the name of 
# current module (__name__) as argument.
app = Flask(__name__)

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('HelloWorld.html', name=name)

@app.route('/')
# ‘/’ URL is bound with hello_world() function.
def hello_world():
    return 'Hello World'

@app.route('/WhereUsedGraph/')
@app.route('/whereusedgraph/')
def whereUsedGraph():
    return render_template('UploadWhereUsed.html')

@app.route('/StartProcessing', methods=['POST'])
def startProcessing():
    print('Processing...')
    retVal = request.form.get('filename')
    print( f" -> Filename: {retVal}" )
    return 'Hello from Python'
  
# main driver function
if __name__ == '__main__':
    # run() method of Flask class runs the application 
    # on the local development server.
    app.run(port=5000, debug=True)