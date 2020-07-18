**TL;DR; : This tool allows you to send javascript code from terminal to your browser. Can be useful when testing mobile browsers for bugs.**

**WTF is this?**

    jsHELL tries to simulate javascript console for Mobile Browsers. Normally javascript consoles are available for Desktop browsers but not for Mobile browsers. jsHELL uses WebSocket to establish connection between the mobile browser and your Desktop terminal to send the javascript code and receive it's output.

**Why we need something like that?**
    
    We need this because mobile browsers doesn't provide any way to execute JS directly like Desktop browsers (via Developer Console). 

**Why would anyone need to executed JS in mobile browser like this?**

    To find browser bugs. Creating a whole HTML page for executing a small JS code like "<html><script>x=window.open('http://xyz.com')</script></html>" is waste of time. Instead we can just start jsHELL and type our code in terminal directly and see the result.

**How it's different than existing ones?**

    I couldn't really find any similar tool. The one I find uses "netcat" and some shit which isn't working in my Macbook for some unknown reasons so I developed this tool. jsHELL doesn't rely on any external tools, it uses WebSocket for communication with browser. Plus the the code of jsHELL is very simple and straighforward so anyone can modify it as per their needs.

**How to run?** 

    rlwrap ./jsHELL.py IpAddress Port
    
    Example: rlwrap ./jsHELL.py 127.0.0.1 8080
    

