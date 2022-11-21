public class Seats implements SeatsType {

    @Override
    public int EconomyClass() {
        return 2500;
    }

    @Override
    public int PremiumEconomyClass() {
        return 3500;
    }

    @Override
    public int BusinessClass() {
        return 4500;
    }

    @Override
    public int FirstClass() {
        return 5500;
    }
}
