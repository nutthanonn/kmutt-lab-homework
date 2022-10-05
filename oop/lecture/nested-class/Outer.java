class Outer{
    Inner i1 = new Inner();
    private String s  = "outer string";


    public void getS() {
        System.out.println(s);
    }

    public void getInnerS(){
        System.out.println(i1.s);
    }


    class Inner{
        private String s = "inner string";

        public void getS() {
            System.out.println(s);
        }

        public void getOuterS(){
            System.out.println(Outer.this.s);
        }
    }

    public static void main(String[] args) {
        Outer o = new Outer();

        Outer.Inner oi = o.new Inner();

        o.getS();
        oi.getS();
        o.getInnerS();
        oi.getOuterS();
    }
}