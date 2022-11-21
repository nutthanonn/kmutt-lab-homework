public class CurrencyFactory {
    
    public static Currency getCurrencyByCountry(String country) throws Exception {
        if (country.equalsIgnoreCase("India")) {
            return new India();
        } else if (country.equalsIgnoreCase("USA")) {
            return new USA();
        } else {
            return null;
        }
    }

    public static void main(String[] args) throws Exception {
        Currency c = CurrencyFactory.getCurrencyByCountry("India");
        System.out.println(c.getCurrency());
        System.out.println(c.getSymbol());
    }
}
