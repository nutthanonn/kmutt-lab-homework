public class OverloadConstructors {
    public static void main(String[] args) {
        Room a = new Room(20, 30, 40);
        Room b = new Room();
        Room c = new Room(10);

        double vol;
        vol = a.volume();
        System.out.println("vol a: " + vol);

        vol = b.volume();
        System.out.println("vol b: " + vol);

        vol = c.volume();
        System.out.println("vol b: " + vol);
    }
}
