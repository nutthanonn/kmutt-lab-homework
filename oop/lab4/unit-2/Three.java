
public class Three {
    public static void main(String[] args) {
        int a1[] = new int[10];
        int a2[] = {3, 5, 7, 1, 8, 99 , 44, -10}; 
        int a3[] = {4, 3, 2, 1};

        System.out.println(a1.length);
        System.out.println(a2.length);
        System.out.println(a3.length);


        int matrix1[][] = new int[3][3];
        int count = 0;
        for(int i=0;i<3;i++){
            for(int j=0;j<3;j++){
                matrix1[i][j] = count;
                count++;
            }
        }
        for(int i=0;i<3;i++){
            for(int j=0;j<3;j++){
                System.out.println(matrix1[i][j]);
            }
        }
    }
}
