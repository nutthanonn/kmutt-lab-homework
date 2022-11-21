public class ATM {
    private boolean useAuthenticated = false;

    public boolean isUserAuthenticated() {
        return useAuthenticated;
    }

    public void setUseAuthenticated(boolean useAuthenticated) {
        this.useAuthenticated = useAuthenticated;
    }

    public static void main(String[] args) {
        ATM atm = new ATM();
        atm.run();
    }

    public void run() {
        BankDatabase bankDatabase = new BankDatabase();
        Screen screen = new Screen();
        Keypad keypad = new Keypad();
        boolean userExited = false;
        CashDispenser cashDispenser = new CashDispenser();

        int accountNumber = 0;

        while (!userExited) {
            while (!isUserAuthenticated()) {
                screen.displayMessageLine("Welcome!");
                screen.displayMessage("Please enter your account number: ");
                accountNumber = keypad.getInput();
                screen.displayMessage("Please enter your PIN: ");
                int pin = keypad.getInput();

                BankDatabase user = new BankDatabase();
                boolean authenticated = user.authenticateUser(accountNumber, pin);
                if (authenticated) {
                    setUseAuthenticated(true);
                } else {
                    screen.displayMessageLine("\nInvalid account number or PIN. Please try again.\n");
                }
            }

            String transactionType = displayMainMenu();

            switch (transactionType) {
                case "1":
                    BalanceInquiry balanceInquiry = new BalanceInquiry(accountNumber);
                    balanceInquiry.execute(bankDatabase);
                    break;
                case "2":
                    Withdrawal withdrawal = new Withdrawal(accountNumber);
                    withdrawal.execute(bankDatabase, cashDispenser);
                    break;
                case "3":
                    Deposit deposit = new Deposit(accountNumber);
                    deposit.execute(bankDatabase);
                    break;
                case "4":
                    setUseAuthenticated(false);
                    userExited = true;
                    screen.displayMessageLine("Please take your card.\n");
                    break;
                default:
                    screen.displayMessageLine("Invalid selection. Try again.");
                    break;
            }
            // setUseAuthenticated(false);
        }
    }

    private String displayMainMenu() {
        Screen screen = new Screen();
        Keypad keypad = new Keypad();
        screen.displayMessageLine("\nMain menu:");
        screen.displayMessageLine("1 - View my balance");
        screen.displayMessageLine("2 - Withdraw cash");
        screen.displayMessageLine("3 - Deposit funds");
        screen.displayMessageLine("4 - Exit\n");
        screen.displayMessage("Enter a choice: ");
        return Integer.toString(keypad.getInput());
    }
}