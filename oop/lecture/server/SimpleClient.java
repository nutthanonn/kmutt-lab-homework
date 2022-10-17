import java.net.*;
import java.io.*;

public class SimpleClient {
    public static void main(String[] args) throws IOException{
        try (Socket s1 = new Socket("localhost", 1234)) {

            InputStream s1in = s1.getInputStream();
            DataInputStream dis = new DataInputStream(s1in);

            String st = new String(dis.readUTF());
            System.out.println(st);
            

            dis.close();
            s1in.close();
            s1.close();
        }
    }
}
