public class Shape {
    public String color;
    
    public Shape(String color){
        this.color = color;
    }

    @Override
    public String toString(){
        return "Shape of color" + color + "\"";
    }


    public double getArea() {
        System.out.println("Shape unknow Cannot");
        return 0;
    }
}
