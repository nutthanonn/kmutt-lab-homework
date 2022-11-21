import java.util.List;

public class BankDatabase {
    public List<Account> accounts;


    public BankDatabase() {
        accounts = List.of(
                new Account(12345, 54321, 1000.0, 1200.0),
                new Account(98765, 56789, 200.0, 200.0)
        );
    }

    public Account getAccount(int accountNumber) {
        for (Account account : accounts) {
            if (account.accountNumber == accountNumber) {
                return account;
            }
        }
        return null;
    }

    public boolean authenticateUser(int userAccountNumber, int userPIN) {
        Account userAccount = getAccount(userAccountNumber);
        if (userAccount != null) {
            return userAccount.validatePIN(userPIN);
        } else {
            return false;
        }
    }

    public double getAvailableBalance(int userAccountNumber) {
        return getAccount(userAccountNumber).getAvailableBalance();
    }

    public double getTotalBalance(int userAccountNumber) {
        return getAccount(userAccountNumber).getTotalBalance();
    }

    public void credit(int userAccountNumber, double amount) {
        getAccount(userAccountNumber).credit(amount);
    }

    public void debit(int userAccountNumber, double amount) {
        getAccount(userAccountNumber).debit(amount);
    }
}
