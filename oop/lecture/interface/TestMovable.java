public class TestMovable {
    public static void main(String[] args) {
        Movable m1 = new MovablePoint(5, 6, 10, 0);
        System.out.println(m1);
        m1.moveLeft();
        System.out.println(m1);
        
        Movable m2 = new MovableCircle(2, 1, 2, 20, 1);
        System.out.println(m2);
        m2.moveLeft();
        System.out.println(m2);
    }    
}
