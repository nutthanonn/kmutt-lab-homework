public class U2_5_2 {
    public static void main(String[] args) {
        int rows = 3;
        int cols = 3;
        int a[][] ={{1,2,3},{4,5,6},{2,3,4}};
        int b[][] ={{1,2,3},{4,5,6},{2,3,4}};
        int c[][] = new int[rows][cols];
        for(int i=0;i<3;i++){    
            for(int j=0;j<3;j++){     
                c[i][j]=0;      
                for(int k=0;k<3;k++) {      
                    c[i][j] += a[i][k] * b[k][j];
                }
                System.out.print(c[i][j] + " ");
            }
                System.out.println();
            }  
    }
}
