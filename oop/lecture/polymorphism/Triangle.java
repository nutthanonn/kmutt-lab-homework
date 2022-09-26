public class Triangle extends Shape {
    private int base;
    private int height;

    public Triangle(String color, int base, int height) {
        super(color);
        this.base = base;
        this.height = height;
    }

    @Override
    public String toString() {
        return "Rectangle of base = " + base + " and height = " + height + " subclass of " + super.toString();
    }

    @Override
    public double getArea() {
        return .5 * base * height;
    }
}
