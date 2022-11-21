import java.text.DecimalFormat;

public class Screen {

    public void displayMessage(String string) {
        System.out.print(string);
    }

    public void displayMessageLine(String string) {
        System.out.println(string);
    }

    public void displayDollarAmount(double availableBalance) {
        DecimalFormat moneyFormat = new DecimalFormat("'$'###,##0.00");
        System.out.println(moneyFormat.format(availableBalance));
    }
}
