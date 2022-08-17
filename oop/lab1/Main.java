
class IndentifyMyParts{
    public static int x = 7;
    public int y = 3;
}

public class Main {
    public static void main(String[] args) {
        IndentifyMyParts a = new IndentifyMyParts();
        IndentifyMyParts b = new IndentifyMyParts();
        a.y = 5;
        b.y = 6;
        a.x = 1;
        b.x = 2;
        System.out.println("a.y = " + a.y);
        System.out.println("b.y = " + b.y);
        System.out.println("a.x = " + a.x);
        System.out.println("b.x = " + b.x);
        System.out.println("IndentifyMyParts.x = " + IndentifyMyParts.x);
    }
}