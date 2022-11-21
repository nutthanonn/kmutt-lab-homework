public class Account {
    public int accountNumber;
    public int pin;
    public double availableBalance;
    public double totalBalance;

    public Account(int theAccountNumber, int thePIN, double theAvailableBalance, double theTotalBalance) {
        accountNumber = theAccountNumber;
        pin = thePIN;
        availableBalance = theAvailableBalance;
        totalBalance = theTotalBalance;
    }

    public boolean validatePIN(int userPIN) {
        if (userPIN == pin) {
            return true;
        } else {
            return false;
        }
    }

    public double getAvailableBalance() {
        return availableBalance;
    }

    public double getTotalBalance() {
        return totalBalance;
    }

    public void credit(double amount) {
        totalBalance += amount;
    }

    public void debit(double amount) {
        totalBalance -= amount;
    }
}
