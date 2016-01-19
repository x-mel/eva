/**This program obtains a reference of the remote 
 * object of server and invokes remote methods.
 * This is the GUI version of the Client
 * that is more advanced and has additional functionalities
 */

import java.rmi.*;
import java.rmi.server.*;
import java.util.*;
import java.awt.*;        // Using AWT container and component classes
import java.awt.event.*;  // Using AWT event classes and listener interfaces
 
/******** A GUI program using container java.awt.Frame ************/

public class GuiClient extends Frame implements ActionListener {
   private Label lblInput;     // Declare input Label
   private Label lblOutput;    // Declare output Label
   private Label lbIP;         // Declare IP Label
   private TextField tfIP;     // Declare IP TextField
   private TextField tfInput;  // Declare input TextField
   private TextField tfOutput; // Declare output TextField
   private Button Butqr;	   // Declare the Button to generate QR code
   private Button Butstr;	   // Declare the Button to stream
   private Button Butdow;	   // Declare the Button to download
   private String link;        // Input link
   private String vlink;       // Output link 
   private String ipadd;	   // IP address of the server
  
   public GuiClient() {
      setLayout(new FlowLayout());
 
 /**** We define the textfields and buttons*******/ 
 
      lbIP = new Label("Enter the IP address of the server: "); // Construct Label
      add(lbIP);               
 
      tfIP = new TextField(110); 	// Construct TextField
      add(tfIP);                	// "super" Frame adds TextField
	  tfIP.setText("192.168.1.8");	// Set a default value 
	  
      tfIP.addActionListener(this);
         // Hitting Enter on TextField fires ActionEvent
         // tfInput (TextField) registers this instance as ActionEvent listener
 
      lblInput = new Label("Enter a link below: "); 
      add(lblInput);              
   
      tfInput = new TextField(110); 
      add(tfInput);                
	  tfInput.setText("http://vodlocker.com/budq9rt5wt0e"); 
      tfInput.addActionListener(this);
 
      lblOutput = new Label("The download link is below: ");
      add(lblOutput);               
 
      tfOutput = new TextField(110); 
      tfOutput.setEditable(false);  // read-only
      add(tfOutput);                
 
 
 /**************QR CODE***************/
      Butqr = new Button("Qr Code");   
      add(Butqr);                    
	
	  Butqr.addActionListener(new ActionListener() {
         public void actionPerformed(ActionEvent e) {
            qrvidlink();
            tfOutput.setText("The Qr code will be generated");
         }
      });

 /**************Stream***************/
      Butstr = new Button("Stream");   // construct Button
      add(Butstr);                    // "super" Frame adds Button
	  
	  Butstr.addActionListener(new ActionListener() {
         public void actionPerformed(ActionEvent e) {
				streamvidlink();
				tfOutput.setText("The video is being streamed");
         }
      });
      
 /**************Download***************/
      Butdow = new Button("Download");   
      add(Butdow);                    
 
 	  Butdow.addActionListener(new ActionListener() {
         public void actionPerformed(ActionEvent e) {
				 downvidlink();
				tfOutput.setText("The video is being downloaded");
         }
      });
 

      setTitle("Client");  // "super" Frame sets title
      setSize(900, 300);  // "super" Frame sets initial window size
      setVisible(true);   // "super" Frame shows
   }
 

   public static void main(String[] args) 
   {
      // Invoke the constructor to setup the GUI, by allocating an anonymous instance
      new GuiClient();
      		}
      		
/*********************************************************************/
/******** functionality when we press enter on the text field *******/
/*******************************************************************/

   @Override
   public void actionPerformed(ActionEvent evt) {
			   vlink = getvidlink(); // it gets the video link from the text input
               tfOutput.setText(vlink); // and tries to set the direct link to the video
            }
            

/**********************************************************************************/
/************ Here we define the functionality of the buttons ********************/
/********************************************************************************/
// we define the method for getting a video link when pressing enter
	public String getvidlink() {
		try {
				System.setSecurityManager(new SecurityManager()); 
	    	
				ipadd= tfIP.getText();
                Interface client = (Interface)Naming.lookup("rmi://"+ipadd+"/getvid");
             	    	
                // Get the String entered into the TextField tfInput, convert to int
                link = tfInput.getText();
                vlink = client.getvid(link);
            
            }catch (Exception e) {
	    		System.out.println("[System] Server failed: " + e);
	    	} 
	    	return vlink;
	}

// we define the method for getting a streaming link when pressing on the stream button
	public void streamvidlink() {
		try {
                System.setSecurityManager(new SecurityManager()); 
	    	
				ipadd= tfIP.getText();
                Interface client = (Interface)Naming.lookup("rmi://"+ipadd+"/getvid");
             	    	
                // Get the String entered into the TextField tfInput, convert to int
                link = tfInput.getText();
                vlink = client.getvid(link);
                client.streamvid(vlink);
      
            }catch (Exception e) {
	    		System.out.println("[System] Server failed: " + e);
	    	} 
	    	
			
	}

// we define the method for downloading when pressing on the download button 
	public void downvidlink() {
		try {
                System.setSecurityManager(new SecurityManager()); 
	    	
				ipadd= tfIP.getText();
                Interface client = (Interface)Naming.lookup("rmi://"+ipadd+"/getvid");
             	    	
                // Get the String entered into the TextField tfInput, convert to int
                link = tfInput.getText();
                vlink = client.getvid(link);
                client.downvid(vlink);
      
            }catch (Exception e) {
	    		System.out.println("[System] Server failed: " + e);
	    	} 		
	}

// we define the method for downloading when pressing on the download button 
	public void qrvidlink() {
		try {
                System.setSecurityManager(new SecurityManager()); 
	    	
				ipadd= tfIP.getText();
                Interface client = (Interface)Naming.lookup("rmi://"+ipadd+"/getvid");
             	    	
                // Get the String entered into the TextField tfInput, convert to int
                link = tfInput.getText();
                vlink = client.getvid(link);
                client.qrvid(vlink);
      
            }catch (Exception e) {
	    		System.out.println("[System] Server failed: " + e);
	    	} 
	    	
			
	}
} 
