public class FullTimeWorker extends Worker{
    public int hours_worked;

    public FullTimeWorker(String name, double salary_rate, int hours_worked) {
        super(name, salary_rate);
        this.hours_worked = hours_worked;
    }

    @Override
    public double computePay() {
        if(this.hours_worked > 240){
            return 100/240;
        }
        return 100.0/this.hours_worked;
    }
}
