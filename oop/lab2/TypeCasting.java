public class TypeCasting {
    public static void main(String[] args) {

        // Widening Casting (small to large)
        int a = 10;
        double b = a;

        // Narrowing Casting (large to small)
        double c = 15.5;
        int d = (int) c;
        System.out.println(b);
        System.out.println(d);
    }
}
