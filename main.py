# Importing flask module in the project is mandatory
# An object of Flask class is our WSGI application.
from flask import Flask, render_template, request
from time import sleep
import random

filesBeingProcessed = {}

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
    filename = request.form.get('filename')
    filesBeingProcessed[filename] = {'error' : '', 'status' : 0, 'step' : 0, 'stepProgress' : 0}
    for i in range(4):
        print(f"Processing {filename} - status moving to {i}")
        filesBeingProcessed[filename]['step'] = i
        timetoSleep = random.randrange(1,3)
        for progress in range(timetoSleep*100):
            # sleep(timetoSleep/1000000)
            stepProgress = progress / timetoSleep
            filesBeingProcessed[filename]['stepProgress'] = int(stepProgress) # percent
    filesBeingProcessed[filename]['stepProgress'] = 100
    import DemoGraph
    return DemoGraph.graphs

@app.route('/GetProcess/<filename>', methods=['POST'])
def getProcess(filename):
    if filename in filesBeingProcessed:
        return filesBeingProcessed[filename]
    return {'error' : 'File not in queue', 'status' : -1}
  
# main driver function
if __name__ == '__main__':
    # run() method of Flask class runs the application 
    # on the local development server.
    app.run(port=5001, debug=True)