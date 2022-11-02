import java.util.List;
import java.util.ArrayList;


public class Employee {
    private String name;
    private String department;
    private int salary;
    private List<Employee> subordinates;

    public Employee(String name, String department, int salary) {
        this.name = name;
        this.department = department;
        this.salary = salary;
        subordinates = new ArrayList<Employee>();
    }
    public void add(Employee e) {
        subordinates.add(e);
    }

    public void remove(Employee e) {
        subordinates.remove(e);
    }

    public List<Employee> getSubordinates() {
        return subordinates;
    }

    public String toString() {
        return ("Employee :[ Name : " + name + ", dept : " + department + ", salary :" + salary+ " ]");
    }
}
