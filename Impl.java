/** This is simple detailed program where we implement 
 *  all the abstract methods of the remote interface, and
 *  we explain explicitely their functionality
 */
import java.awt.image.BufferedImage;
import java.rmi.*;        // for remote exception
import java.rmi.server.*; // this one for the Unicast Remote Object
import java.io.*;
import javax.imageio.*; 

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
				System.out.println("GetVid failed: " + ex);
			}
			return L;
    }
	public byte[] qrvid(String msg) throws RemoteException
     {ByteArrayOutputStream bytimg = null;
		try {
				Runtime.getRuntime().exec("qrencode "+msg + " -o tmp.png"); //we save the image into a file
				BufferedImage buffimg = null;
				buffimg = ImageIO.read(new File("tmp.png")); //we load the image into a buffered image

				bytimg = new ByteArrayOutputStream();// we transform it into byte arrays
				ImageIO.write(buffimg, "png", bytimg);		
        }
        catch (Exception e){
            System.out.println("QR code failed: " + e);
        }
       return bytimg.toByteArray(); //we return it to the client as bytes
      }

}
