public class TestWorker {
    public static void main(String[] args) {
        FullTimeWorker ftw = new FullTimeWorker("John", 10000, 30);
        System.out.println(ftw.computePay());


        Hourlyworker hw = new Hourlyworker("Doe", 11500, 25);
        System.out.println(hw.computePay());
    }
}
