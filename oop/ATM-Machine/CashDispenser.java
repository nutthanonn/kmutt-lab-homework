public class CashDispenser {
    public int count = 500;

    public double dispenseCash(double amount) {
        int billsRequired = (int) (amount / 20);
        count -= billsRequired;
        return amount;
    }


    public boolean isSufficientCashAvailable(double amount) {
        int billsRequired = (int) (amount / 20);
        if (count >= billsRequired) {
            return true;
        } else {
            return false;
        }
    }
}
