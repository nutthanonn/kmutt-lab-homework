class Manager extends Employee {
    private String dept;

    public Manager(String dept, String name, Double salary) {
        super(name, salary);
        this.dept = dept;
    }

    public String getDept() {
        return dept;
    }

    public void setDept(String dept) {
        this.dept = dept;
    }

    @Override
    public String toString() {
        return "Name: " + getName() + " Department: " + getDept() +" Salary: " + getSalary();
    }
}