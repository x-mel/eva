/** This is simple detailed program where we implement 
 *  all the abstract methods of the remote interface, and
 *  we explain explicitely their functionality
 */

import java.rmi.*;        // for remote exception
import java.rmi.server.*; // this one for the Unicast Remote Object
import java.io.*;

// here we define the implementation that extends the UnicastRemote object and implement the interface
public class Impl extends UnicastRemoteObject implements Interface  {

    public String link; // the link provided by the user
    
    // we define a constructor that invokes the superclass constructor
    public Impl() throws RemoteException
    {
        super(); // super class constructor of the Object class
    }

/*
 * All the functions implemented utilize external commands of the server OS
 * which is already configure. We already installed all the dependencies like
 * python, selenium (the library for webdriver) and the qr code program.
 */

/******************* Printing the video function ******************/

// getvid returns a string which is the direct link to the video
    public String getvid(String link) throws RemoteException 
    {
		String line;
		String L="";
			try {
				Process p = Runtime.getRuntime().exec("python pridown.py "+ link);
				BufferedReader input = new BufferedReader
					(new InputStreamReader(p.getInputStream()));
				while ((line = input.readLine()) != null) {
					L += (line + '\n');
				}
				input.close();
				}
			catch (Exception ex) {
				L+="Error in executing the python command";
				ex.printStackTrace();
			}
			return L;
    }
    
 /******************* Streaming the video function ******************/
 // this function requires smplayer to be installed as media player
     public void streamvid(String msg) throws RemoteException
     {try {

        Runtime.getRuntime().exec("smplayer " +msg);     }
        catch (IOException e) 
        {
            e.printStackTrace();
            System.exit(-1);
        }
      }
      
  /******************* Downloading the video function ******************/
	public void downvid(String msg) throws RemoteException
     {try {
        Runtime.getRuntime().exec("wget -c " +msg);     }
        catch (IOException e) 
        {
            e.printStackTrace();
            System.exit(-1);
        }
     }
     
   /******************* Qr Code Generation function ******************/
     public void qrvid(String msg) throws RemoteException
     {try {
        Runtime.getRuntime().exec("qrencode "+msg + " -o temp.png");
        Runtime.getRuntime().exec("display temp.png");     }
        catch (IOException e) 
        {
            e.printStackTrace();
            System.exit(-1);
        }

     }

}
