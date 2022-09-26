public class Main {
    public static void main(String[] args) {
        Employee emp1 = new Employee("Nutthanon tho", 555.555);
        System.out.println(emp1.toString());
        Manager m1 = new Manager("ComSci", "Nutthanon", 100000.0);
        System.out.println(m1.toString());
    }
}
