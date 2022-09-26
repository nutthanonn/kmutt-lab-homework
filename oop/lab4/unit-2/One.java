
public class One {
    public static void main(String[] args) {
        int increment = 0;
        increment++;
        ++increment;

        int decrement = 10;
        decrement--;
        -- decrement;

        System.out.println(increment);
        System.out.println(decrement);

        int a = 1;
        int b = 0;
        System.out.println(a != b);
        System.out.println(a < b);
        System.out.println(a > b);
        System.out.println(a == b);

        System.out.println(a == b ? "IS_EQUAL": "NOT_EQUAL");
    }
}
