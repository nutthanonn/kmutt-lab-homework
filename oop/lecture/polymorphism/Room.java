class Room {
    double length, breadth, height;
    Room(){
        length -= 1;
        breadth -=1;
        height-= 1;
    }


    Room(double l, double b, double h){
        length = l;
        breadth = b;
        height = h;
    }

    Room(double len){
        length = breadth = height = len;
    }

    double volume(){
        return length*breadth*height;
    }
}