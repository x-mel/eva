/**This is a simple interface with some abstract 
 * methods and extending Remote interface.
 */
import java.rmi.*;

//defining the remote interface 
public interface Interface extends Remote{
   
    // takes the webservise link as input and print the video link function
    public String getvid(String msg) throws RemoteException;

    // takes the webservise link as input generate qr code function as serialized image
    public byte[] qrvid(String msg) throws RemoteException;
}
