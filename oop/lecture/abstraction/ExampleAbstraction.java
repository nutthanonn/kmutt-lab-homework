package abstraction; //delete it when you want to run this file

abstract class Animal {
    public abstract void animalSound();

    public void sleep() {
        System.out.println("zzz");
    }
}

class Pig extends Animal {
    public void animalSound() {
        System.out.println("The pig says: wee wee");
    }
}

public class ExampleAbstraction {
    public static void main(String[] args) {
        Pig myPig = new Pig();
        myPig.animalSound();
        myPig.sleep();
    }
}
