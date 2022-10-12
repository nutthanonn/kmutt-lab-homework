class Animal {
    public void speak(){
        System.out.println("Aniaml Speak");
    }
}


class Dog extends Animal{
    public void bark(){
        System.out.println("woof !");
    }

    public void speak(){
        bark();
    }
}

class Seal extends Animal {
    public void bark(){
        System.out.println("Arf !");
    }
}

class Bird extends Animal {
    public void bark(){
        System.out.println("Tweet !");
    }
}


public class Example {
    public static void main(String[] args) {
        Animal a = new Animal();
        Animal d = new Dog();
        Animal s = new Seal();
        Animal b = new Bird();

        a.speak();
        d.speak();
        s.speak();
        b.speak();
    }
}
