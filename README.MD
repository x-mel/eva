#EVA - Extraordinary Video App
Java RMI Application for downloading, streaming not-so-totally legally acquired movies. Developped for our class of Distributed Systems.

#Contributors
Ahmad Mel  
Ruben Ruperez 

#What is madness?
Remember that last time you were trying to watch that episode of Game of thrones on a streaming website? 500 pop ads, and
lots of clicks to get to the actual video, and bummer, you can't even download it for free. Just sitting there waiting for it
to buffer, and praying nothing goes wrong. That's by no mean a way to watch Arya Stark beating the shit out of the Lannisters.  
Cry no more. God exists and he's here to save you from the devil's minions, those evil ads.  
You send us a link for the movie hosted by selected file hosting websites, and the server return a link to the video, that you
can use to directly download it, or stream it with your favorite video player. You don't even have to go the website.  
Just sit, chill, and enjoy!


#Usage
##Standalone Python Core
The python code is the core of EVA. It utilizes selenium webdriver and phantomjs to crawl webservices to snatch the direct video link. Only few  [web hosting services](#Supported-web-hosting-services) are supported so far.Adding support for additional webservices will be slower, if I have time.   
Now the code can be used seperately than the Java RMI application, just run it from the command line with weblink as an argument (or multiple arguments). Here is an example.    
```
python pridown.py http://vodlocker.com/z9x78jygfhme
```
It will print the link to the video on the stdout.  
Of course you need to install [selenium](http://selenium-python.readthedocs.org/installation.html) and [phantomjs](http://phantomjs.org/).

##Java RMI application
The app was developped for a class project, implementing Java RMI application. We set up 2 machines on the same network, a server and a client. 
The client send the webservice link to the server and the server return the direct video link.   
There are 2 client versions. [Client](Client.java) and [GuiClient](GuiClient.java), the former being a command-line program with only one functionality to print the returned direct video link, and the latter being an advanced version incorporating a graphical user interface and additional functionalities, like streaming the video, downloading it, or generating a qr code for streaming on mobile devices. The usage is listed in the file [usage](usage).  
###Usage
Clone the repo (download the files) and compile them
```
javac *.java
```
If everything goes smooth, run the java rmi registry
```
rmiregistry
```
Now run the server from another terminal session while specifiying the security policy
```
java -Djava.security.policy=java.policy Server
```
It will print the IP address of the server. Use that IP address to connect to the server when you're running Client or GuiClient.
Now in another tab (or on another machine) start the Client or GuiClient.
```
java -Djava.security.policy=java.policy Client
```
Now enter the IP address you got from the server. And enter your web link. The program returns the direct video link. You can use download commands like the famous [wget](https://www.gnu.org/software/wget/) to download it, or players like [smplayer](http://www.smplayer.eu/) to stream it. Your link, your choice.  

![command-line Client](https://github.com/x-mel/eva/blob/master/demo/cmdclient.png "Command-line demo")

If you want to run the GuiClient, stop the Client (usually by Crtl+C) and run
```
java -Djava.security.policy=java.policy GuiClient
```
I think you'll figure out how to use it. Enter the IP address and the link. If you press Enter, you will a 
link printed in the lower line. And press any of the button for more functionalities. You need to have [smplayer](www.smplayer.eu/) and [qrencode](https://fukuchi.org/works/qrencode/) installed of course.

![GuiClient printing the download link](https://github.com/x-mel/eva/blob/master/demo/gen.png "Printing Video Demo")
![GuiClient streaming the video to smplayer](https://github.com/x-mel/eva/blob/master/demo/stream.png "Stream Demo")
![GuiClient generating QR code](https://github.com/x-mel/eva/blob/master/demo/qrc.png "Qr Code demo")


#Supported web hosting services
promptfile.com  
vodlocker.com  
briskfile.com  

##Comments
We had lots of fun making this application, with brain crushing moments, especially serializing that image on java to send it over rmi, took nearly 6hrs to solve. Thanks to everyone involved :)  
