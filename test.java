import java.applet.Applet;
import java.awt.*;
import java.awt.event.*;
import java.awt.image.*;
import java.io.*;
import javax.imageio.*;
import javax.swing.*;

public class test extends Applet{
public static void main(String[] args)
//public void init() {
{
try {

BufferedImage buffimg = ImageIO.read(new File("tmp.png"));


ByteArrayOutputStream baos = new ByteArrayOutputStream();
ImageIO.write(buffimg, "png", baos);
byte[] bytimg = baos.toByteArray();

BufferedImage img = ImageIO.read(new ByteArrayInputStream(bytimg));

File outputfile = new File("test.png");
ImageIO.write(img,"png",outputfile);


}catch(Exception e){e.printStackTrace();}

}

}
