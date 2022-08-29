class BicycleRegistration {
    public static void main(String[] args) {
        Bicycle bike1, bike2;
        String owner1, owner2;


        bike1 = new Bicycle();
        bike1.setOwnerName("Nutthanon");
        bike1.setTagNo("2004-134R");
        String tag1 = bike1.getTagNo();

        bike2 = new Bicycle();
        bike2.setOwnerName("Tho");
        bike2.setTagNo("2004-123L");
        String tag2 = bike2.getTagNo();

        owner1 = bike1.getOwnerName();
        owner2 = bike2.getOwnerName();

        System.out.println(owner1 + " owns a bicycle.");
        System.out.println("Tag Number : " + tag1);
        System.out.println(owner2 + " also owns a bicycle.");
        System.out.println("Tag Number : " + tag2);
    }
}