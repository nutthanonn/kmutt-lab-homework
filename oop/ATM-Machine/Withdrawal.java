public class Withdrawal {
    public int accountNumber;
    public Double amount;


    public Withdrawal(int accountNumber) {
        this.accountNumber = accountNumber;
    }


    public int withdrawMenu(){
        Screen screen = new Screen();
        screen.displayMessageLine("Withdrawal Menu:");
        screen.displayMessageLine("1 - $20");
        screen.displayMessageLine("2 - $40");
        screen.displayMessageLine("3 - $60");
        screen.displayMessageLine("4 - $100");
        screen.displayMessageLine("5 - $200");
        screen.displayMessageLine("6 - Cancel transaction");
        screen.displayMessage("Choose a withdrawal amount: ");
        Keypad keypad = new Keypad();
        return keypad.getInput();
    }
   
    public void execute(BankDatabase bankDatabase, CashDispenser cashDispenser) {
        Screen screen = new Screen();
        Account account = bankDatabase.getAccount(accountNumber);

        double totalBalance = account.getTotalBalance();
        int choice = withdrawMenu();

        switch (choice) {
            case 1:
                amount = 20.0;
                break;
            case 2:
                amount = 40.0;
                break;
            case 3:
                amount = 60.0;
                break;
            case 4:
                amount = 100.0;
                break;
            case 5:
                amount = 200.0;
                break;
            case 6:
                screen.displayMessageLine("Canceling transaction...");
                return;
            default:
                screen.displayMessageLine("Invalid selection. Try again.");
                return;
        }
        
        if (cashDispenser.isSufficientCashAvailable(amount)) {
            if (totalBalance >= amount) {
                cashDispenser.dispenseCash(amount);
                bankDatabase.debit(accountNumber, amount);
                screen.displayMessageLine("\nWithdrawal " + amount + "$ successful.");
                screen.displayMessageLine("Please take your cash from the cash dispenser.");
            } else {
                screen.displayMessageLine("Insufficient funds in your account.");
            }
        } else {
            screen.displayMessageLine("Insufficient cash available in the ATM.");
        }
    }
}
