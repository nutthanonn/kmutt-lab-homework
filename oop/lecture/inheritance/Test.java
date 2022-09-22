class A{
    public int a = 101;
}
class B extends A {
    public int a = 80;
}
class C extends B {
    public int a = 60;
}
class D extends C {
    public int a = 40;
}

class E extends D {
    public int a = 10;

    public void show() {
        int a = 0;
    }    
}


public class Test {
    public static void main(String[] args) {
        new E().show(); //anonymous obj
        B a1 = new E();
        D d1 = (D) a1;
        C c1 = (C) a1;
        System.out.println(a1.a);
        System.out.println(c1.a);
        System.out.println(d1.a);
    }
}