package writefile;

import java.io.File;
import java.io.IOException;

public class writefile {
    public static void main(String[] args) {
        try {
            File myObj = new File("filename.txt");
            if(myObj.createNewFile()){
                System.out.println(myObj.getName());
            }else{
                System.out.println("Erorr");
            }
        } catch (IOException e) {
            System.out.println("Error");
            e.printStackTrace();
        }
    }    
}
