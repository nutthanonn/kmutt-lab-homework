
public class BalanceInquiry {
    public int accountNumber;

    public BalanceInquiry(int accountNumber) {
        this.accountNumber = accountNumber;
    }

    public int getAccountNumber() {
        return accountNumber;
    }

    public void setAccountNumber(int accountNumber) {
        this.accountNumber = accountNumber;
    }

    public void execute(BankDatabase bankDatabase) {
        double availableBalance = bankDatabase.getAvailableBalance(accountNumber);
        double totalBalance = bankDatabase.getTotalBalance(accountNumber);

        Screen screen = new Screen();
        screen.displayMessageLine("Balance Information:");
        screen.displayMessage(" - Available balance: ");
        screen.displayDollarAmount(availableBalance);
        screen.displayMessage(" - Total balance: ");
        screen.displayDollarAmount(totalBalance);
    }
}
