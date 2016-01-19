/**This is a simple interface with some abstract 
 * methods and extending Remote interface.
 */

import java.rmi.*;
//defining the remote interface 
public interface Interface extends Remote{
   
    // prin the video link function
    public String getvid(String msg) throws RemoteException;
    
    // stream the video function
    public void streamvid(String msg) throws RemoteException;

    // generate qr code function
    public void qrvid(String msg) throws RemoteException;

    // download video function 
    public void downvid(String msg) throws RemoteException;
}
