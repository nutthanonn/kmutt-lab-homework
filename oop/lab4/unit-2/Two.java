public class Two {
    public static void main(String[] args) {
        int first_val = 3;
        int sec_val = 30;
        if(first_val > sec_val){
            System.out.printf("Greatest: %d\n", first_val);
            System.out.printf("lesser: %d\n", sec_val);
        }else{
            System.out.printf("Greatest: %d\n", sec_val);
            System.out.printf("lesser: %d\n", first_val);
        }


        char case_val = 'A';
        switch (case_val) {
            case 'A':
                System.out.println('A');
                break;
            case 'B':
                System.out.println('B');
                break;
            case 'C':
                System.out.println('C');
                break;
            default:
                System.out.println(case_val);
                break;
        }

        int aa = 10;
        int count = 0;
        for(int i=0;i<aa+1;i++){
            count += i;
        }
        System.out.println(count);


        int ii = 0;
        while(ii <= 5){
            System.out.println(ii);
            ii++;
        }

        int iii = 0;
        do {
            System.out.println(iii);
            iii++;
        } while (iii<=5);
    }
}
