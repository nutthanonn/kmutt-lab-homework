public class U2_4_1{
    public static void main(String[] args) {
        int arr[] = {234,6,846,85,96,198,545,12,60,34,4,87,7,1};

        for(int i=0;i<arr.length;i++){
            for(int j=0;j<arr.length;j++){
                if(arr[j] > arr[i]) {
                    int temp = arr[i];
                    arr[i] = arr[j];
                    arr[j] = temp;
                }
            }
        }

        for(int i=0;i<arr.length;i++){
            System.out.print(arr[i] + " ");
        }

    }
}