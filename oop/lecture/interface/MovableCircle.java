public class MovableCircle extends MovablePoint {
    
    private MovablePoint center;
    
    private int radius;

    public MovableCircle(int x, int y, int xSpeed, int ySpeed, int radius) {
        super(x, y, xSpeed, ySpeed);
        center = new MovablePoint(x, y, xSpeed, ySpeed);
        this.radius = radius;
    }
    
    public void moveUp(){
        center.y -= center.ySpeed;
    }

    public void moveDown(){
        center.y += center.ySpeed;
    }

    public void moveLeft(){
        center.x -= center.xSpeed;
    }

    public void moveRight(){
        center.x += center.xSpeed;
    }


    @Override
    public String toString() {
        return String.format("Point at (%d,%d)", center.x, center.y);
    }
}
