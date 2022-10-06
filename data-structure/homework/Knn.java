import java.io.File;
import java.io.FileNotFoundException;
import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class Knn {
    public static double calDistance(String[] data, String[] myData) {
        double distance = 0;
        for (int i = 1; i < 9; i++) {
            distance += Math.pow(Double.parseDouble(data[i]) - Double.parseDouble(myData[i]), 2);
        }
        return Math.sqrt(distance);
    }

    public static void main(String[] args) {
        String[] myData = { "64090500429", "30.4", "35.4", "34", "26", "26", "35", "33", "22", "ISTP" };
        List<List<String>> other_distance = new ArrayList<List<String>>();

        try (Scanner sc = new Scanner(new File("./mbti.txt"))) {
            sc.useDelimiter("\n");
            while (sc.hasNext()) {
                List<String> temp = new ArrayList<String>();
                String[] arrOfStr = sc.next().split("\t");
                double distance = calDistance(arrOfStr, myData);
                temp.add(arrOfStr[0]);
                temp.add(distance + "");
                temp.add(arrOfStr[9]);
                other_distance.add(temp);
            }
        } catch (FileNotFoundException e) {
            e.printStackTrace();
        }
    }
}