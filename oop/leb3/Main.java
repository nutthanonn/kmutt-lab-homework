import java.util.ArrayList;
import java.util.List;

public class Main {

    public static int fib(int n) {
        List<Integer> f = new ArrayList<>();
        f.add(1);
        f.add(2);
        for (int i = 2; i < n; i++)
            f.add(f.get(i-1) * (i + 1));
        return f.get(n - 1);
    }

    public static void main(String[] args) {
        int a = fib(20);
        System.out.println(a);
    }
}