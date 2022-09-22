public class TestCylinder {
    public static void main(String[] args) {
        Cylinder cy1 = new Cylinder();
        System.out.println(cy1.getRadius());
        System.out.println(cy1.getHeight());
        System.out.println(cy1.getColor());
        System.out.println(cy1.getArea());
        System.out.println(cy1.getVolume());
        System.out.println("------------------");
        
        Cylinder cy2 = new Cylinder(5.0, 2.0);
        System.out.println(cy2.getRadius());
        System.out.println(cy2.getHeight());
        System.out.println(cy2.getColor());
        System.out.println(cy2.getArea());
        System.out.println(cy2.getVolume());
    }
}
