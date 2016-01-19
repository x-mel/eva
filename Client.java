/**This program obtains a reference of the remote 
 * object of server and invokes remote methods.
 * There is another GUI version of the Client
 * that is more advanced and has additional functionalities
 */

import java.rmi.*;
import java.rmi.server.*;
import java.util.*;
 

public class Client {
	public static void main (String[] argv) {
	    try { // again we try to define the security manager
                 
                 System.setSecurityManager(new SecurityManager());
                    
                /** The "client" on client side is a reference object that refers "server" on server side.
                 * which means that "server" on the server is known as remote object. Now "client" refers the remote object
                 * So basically every method we call with "client" like client.getvid(blablabla), 
                 * becomes server.getvid(blablabla) on the server. 
                 * The remote object "server" invokes the remote method getvid(blablabla) on the server and 
                 * returns the return value to local variable msg.
                 * And every method we do on "client" on the client side will be executed on the server side with object "server"
                 * "client" and "server" communicates each other and it is known as object communication. 
                 * This is how remote method invocation and object communication works.
                 */
                 
                // The user input the ip address of the server (it should be known by him)
                System.out.println("Enter the ip address of the server:");
                Scanner s=new Scanner(System.in);
                String IPad=s.nextLine().trim(); // we save the ip address
                
                Interface client = (Interface)Naming.lookup("rmi://"+IPad+"/getvid");
                
        while(true) //as long as the client is running our code runs
        {
                System.out.println("Enter Your link and press Enter:");     
                String link=s.nextLine().trim(); // we save the input of user in link
		    	
                String msg = client.getvid(link); // we call the method getvid
                System.out.println(msg);
        }
	    	}catch (Exception e) {
	    		System.out.println("[System] Server failed: " + e);
	    	}
		}
}
