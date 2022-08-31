package inheritance;

class Vehicle {
    protected String brand = "Ford";
    

    public Vehicle(String brand) {
        this.brand = brand;
    }


    public String getBrand() {
        return brand;
    }


    public void setBrand(String brand) {
        this.brand = brand;
    }


    public void honk() {
        System.out.println("Tuut, tuut!");
    }

}

public class Car extends Vehicle {
    private static String modelName = "Mustang";


    public Car(String name) {
        super(name);
    }

    @Override
    public void honk(){
        super.honk();
        System.out.println("Preen, Preen!!");
    }


    public static void main(String[] args) {
        Car myCar = new Car(modelName);

        myCar.honk();

        System.out.println(myCar.brand + " " + modelName);
    }
}

