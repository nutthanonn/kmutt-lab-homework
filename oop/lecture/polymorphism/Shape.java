abstract public class Shape {
    public String color;
    
    public Shape(String color){
        this.color = color;
    }

    @Override
    public String toString(){
        return "Shape of color" + color + "\"";
    }


    abstract public double getArea();
}
