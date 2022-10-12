class NewClass{

    public static class superClass {
        static void print(){
            System.out.println("super class is called");
        }
    }

    public static class subClass extends superClass {
        static void print(){
            System.out.println("sub class is called");
        }
    }


    public static void main(String[] args) {
        superClass A = new superClass();
        superClass B = new subClass();

        A.print();
        B.print();
    }
}