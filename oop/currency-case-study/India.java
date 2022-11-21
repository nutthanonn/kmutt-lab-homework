public class India implements Currency {
    @Override
    public String getCurrency() {
        return "Rupe";
    }

    @Override
    public String getSymbol() {
        return "Rs";
    }

    public static void main(String[] args) {
        India i = new India();
        System.out.println(i.getCurrency());
        System.out.println(i.getSymbol());
    }
}
