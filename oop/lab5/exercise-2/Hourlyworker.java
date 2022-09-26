public class Hourlyworker extends Worker{
    public int hours_worked;

    public Hourlyworker(String name, double salary_rate, int hours_worked) {
        super(name, salary_rate);
        this.hours_worked = hours_worked;
    }


    @Override
    public double computePay() {
        if(this.hours_worked > 60){
            return 50.0/60.0;
        }
        return 50.0/this.hours_worked;
    }
}
