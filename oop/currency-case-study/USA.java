public class USA implements Currency{
    @Override
    public String getCurrency() {
        return "Dollar";
    }

    @Override
    public String getSymbol() {
        return "$";
    }

    public static void main(String[] args) {
        USA u = new USA();
        System.out.println(u.getCurrency());
        System.out.println(u.getSymbol());
    }
}