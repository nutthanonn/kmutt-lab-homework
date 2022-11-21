public class Deposit {
    public int accountNumber;
    public Double amount;

    public Deposit(int accountNumber) {
        this.accountNumber = accountNumber;
    }

    public void execute(BankDatabase bankDatabase) {
        Screen screen = new Screen();
        Keypad keypad = new Keypad();

        screen.displayMessage("Please enter a deposit amount: ");
        int input = keypad.getInput();
        amount = (double) input;

        if (amount >= 0) {
            bankDatabase.credit(accountNumber, amount);
            screen.displayMessageLine("Deposit complete. Thank you!");
        } else {
            screen.displayMessageLine("Canceling transaction...");
        }
    }
}
