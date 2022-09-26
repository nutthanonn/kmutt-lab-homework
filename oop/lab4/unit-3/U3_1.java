import java.util.Scanner;

public class U3_1 {
    public static void main(String[] args) {
        try (Scanner input = new Scanner(System.in)) {
            double celsius = input.nextDouble();
            double Fahrenheit = (9.0/5.0)*celsius + 32;
            System.out.println(Fahrenheit);
        }
    }
}
