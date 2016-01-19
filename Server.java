/** This program creates a remote object, links with an 
 * alias name (ip address and some identifier) and binds 
 * with the RMI registry, linked to RMI runtime mechanism.
 */

import java.rmi.*;
import java.rmi.server.*;
import java.util.*;
import java.net.*;
 
public class Server {
public static void main (String[] argv) {
  		
      try {		
		  
		 // we get the server ip address on the network
			Socket s = new Socket("www.uab.cat", 80); //we can try too using www.google.com or 192.168.1.1
			String IPad = String.format(s.getLocalAddress().getHostAddress());
			s.close();

        /* it's importand to define the security manager as it handles the policies over the network,
         * and specify a security policy file so that the code is granted the security permissions it needs to run.*/      
			System.setSecurityManager(new SecurityManager());

        // We define the remote interface object "server" by using the implementation program constructor Impl()
            Interface server = new Impl();	

	    /** RMI uses a naming service where an alias name is maintained and should be 
	     * known and used by the client to invoke the remote method.
	     * 
         * The rebind() method of Naming class binds the object "server" along 
         * alias name "getvid" with the RMI registry.
         * 
         * Alias name "getvid" refers the object "server" on server side. Object "server" 
         * RMI registry is connected internally with the Remote reference layer.
         */
	    	Naming.rebind("rmi://"+IPad+"/getvid", server); 
	    	System.out.println("Server is ready and reachable on "+IPad);// we print a message to clarify the binding
    	}
    
    catch (Exception e) {
    		System.out.println("[System] Server failed: " + e);
    	}
	}
}
