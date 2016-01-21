/** This is simple detailed program where we implement 
 *  all the abstract methods of the remote interface, and
 *  we explain explicitely their functionality
 */
import java.awt.image.BufferedImage;
import java.rmi.*;        // for remote exception
import java.rmi.server.*; // this one for the Unicast Remote Object
import java.io.*;
import javax.imageio.*;
import javax.swing.ImageIcon;
import javax.swing.ImageIcon.*;

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
				ex.printStackTrace();
			}
			return L;
    }

     
   /******************* Qr Code Generation function ******************
     public BufferedImage qrvid(String msg) throws RemoteException
     {BufferedImage img = null;
		try {
        Runtime.getRuntime().exec("qrencode "+msg + " -o tmp.png");
				try {
					img = ImageIO.read(new File("tmp.png"));
				} catch (Exception exx) {exx.printStackTrace();}
        //Runtime.getRuntime().exec("display temp.png");     
        }
        catch (Exception e) 
        {
            e.printStackTrace(System.out);
        }
        return img;
       }
       
          /******************* Qr Code Generation function ******************/
     public byte[] qrvid(String msg) throws RemoteException
     {ByteArrayOutputStream bytimg = null;
		try {
        Runtime.getRuntime().exec("qrencode "+msg + " -o tmp.png");
				try {
					
						BufferedImage buffimg = null;
							try {
								buffimg = ImageIO.read(new File("tmp.png"));
							} catch (Exception exxxx) {
							}
					
						bytimg = new ByteArrayOutputStream();
						ImageIO.write(buffimg, "png", bytimg);		

				} catch (Exception exx) {exx.printStackTrace();}
        //Runtime.getRuntime().exec("display temp.png");     
        }
        catch (Exception e) 
        {
            e.printStackTrace(System.out);
        }
        
       return bytimg.toByteArray();
      }

}
