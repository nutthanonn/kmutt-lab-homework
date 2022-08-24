
public class U2_3_2 {
    public static void main(String[] args) {
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
                System.out.print(matrix1[i][j] + " ");
            }
            System.out.println();
        }
    }   
}
