public class BookingFlight {
    public static void main(String[] args) {
        Seats seats = new Seats();
        Amenities amenities = new Amenities();
        int total = seats.EconomyClass() + amenities.WiFi();
        System.out.println("Total: " + total);
    }
}
