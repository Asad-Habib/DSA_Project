from flask import Flask, render_template, request
from algorithm import *
from Edges import G, edges
from flask import Markup


   
# Flask is used to connect the backend and the frontend together
app = Flask(__name__)

@app.route('/') #the defalt homepage
def home():
    return render_template('home.html')



@app.route('/path_final')# used to output results
def path_final():
    return render_template('path.html')


# grabs results by adding the location and destination to algorithm.py and displays the results
#An angle is given along with the bearing, showing the bearing from north of the next node or checkpoint
@app.route('/path', methods = ['POST'])
def path():

    destination = request.form['destination']
    print("Your destination is '" + destination + "'")

    current = request.form['Current_Location']
    print("Your location is '" + current + "'")

    
    final_output = a_star_algorithm(G,current, destination ,edges,True)
    
    stroutput=''
    c=1
   

    stroutput=''
    c=1

    for a in range(len(final_output)):
        if a==0:
            stroutput+=Markup('<br>'+final_output[a][0]+'<br>')
        elif a==len(final_output)-1:
            stroutput+=Markup('->'+final_output[a][0]+'\t   : '+final_output[a][1]+'°<br>')
        else:
            stroutput+=Markup('->'+final_output[a][0]+'\t   : '+final_output[a][1]+'°<br>')
            c+=1

    return render_template('path.html', output = stroutput)




if __name__=="__main__":
    app.run(debug=True)
