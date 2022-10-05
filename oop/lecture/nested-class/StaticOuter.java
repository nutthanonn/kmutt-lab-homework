
public class StaticOuter {
    String a = "outer string";
    static String b = "static outer string";

    void seeStaticInner(){
        System.out.println(new StaticInner().nonStatic);
        System.out.println(StaticInner.s);
    }

    static class StaticInner {
        String nonStatic = "static inner non static string";
        static String s = "static inner static string";
        public static void main(String[] args) {
            System.out.println(s);
            System.out.println(b);
        }
    }

    public static void main(String[] args) {
        System.out.println(StaticInner.s);
        StaticOuter so = new StaticOuter();
        so.seeStaticInner();
    }
}


class SomeOther{
    public static void main(String[] args) {
        System.out.println(StaticOuter.StaticInner.s);
        StaticOuter.StaticInner soi = new StaticOuter.StaticInner();
        System.out.println(soi.nonStatic);
        System.out.println(soi.s);
    }
}