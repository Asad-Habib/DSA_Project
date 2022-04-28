from flask import Flask, render_template, request,redirect
from algorithm import *
from Edges import G, addNodes,edges, G1,positions1


   

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')



@app.route('/path_final')
def path_final():
    return render_template('path.html')



@app.route('/path', methods = ['POST'])
def path():

    destination = request.form['destination']
    print("Your destination is '" + destination + "'")

    current = request.form['Current_Location']
    print("Your location is '" + current + "'")

    
    final_output = a_star_algorithm(G,current, destination ,edges)
    
    stroutput=''
    c=1
    for a in range(len(final_output)):
        if a==0:
            stroutput+=final_output[a]+'\n'
        elif a==len(final_output)-1:
            stroutput+='->'+final_output[a]+'\n'
        else:
            stroutput+='->'+final_output[a]+'\n'
            c+=1
            

    return render_template('path.html', output = stroutput)



if __name__=="__main__":
    app.run(debug=True)
