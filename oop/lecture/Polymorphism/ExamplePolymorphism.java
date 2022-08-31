class Animal {
    protected String name;
   
    public Animal(String name) {
        this.name = name;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public void animalSound() {
        System.out.println("The animal makes a sound");
    }
}

class Pig extends Animal {

    public Pig(String name) {
        super(name);
    }

    @Override
    public void animalSound() {
        System.out.println("The pig says: wee wee");
    }
}

class Dog extends Animal {

    public Dog(String name) {
        super(name);
    }


    @Override
    public void animalSound() {
        System.out.println("The dog says: bow wow");
    }
}

class ExamplePolymorphism {
    public static void main(String[] args) {
        Animal myDog = new Dog("Boo");
        String name = myDog.getName();
        System.out.println(name);

        myDog.animalSound();
    }
}