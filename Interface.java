/**This is a simple interface with some abstract 
 * methods and extending Remote interface.
 */
import java.awt.image.BufferedImage;
import java.rmi.*;
import java.io.*;

//defining the remote interface 
public interface Interface extends Remote{
   
    // prin the video link function
    public String getvid(String msg) throws RemoteException;

    // generate qr code function
    public byte[] qrvid(String msg) throws RemoteException;
}
