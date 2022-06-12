import java.util.Scanner;

public class money{
    public static void main(String[] args){
        Scanner input = new Scanner(System.in);
        System.out.println("plz enter loan amount");
        int loanamount = input.nextInt();
        System.out.println("plz enter number of years");
        int years = input.nextInt();
        double interestrate = 0.05;
        for(int n=0;n<25;n++)
        {
            double monthlypayment=0.00;
            double updata= loanamount*(interestrate/12);
            double downdata=1-(1/Math.pow(1+(interestrate/12),(years*12)));
            monthlypayment = updata/downdata;
            double totalpayment = monthlypayment*12*years;
            System.out.printf("U should return:%.2f the interestrate is:%.5f  the monthlypayment is:%.2f %n",totalpayment,interestrate,monthlypayment);
            interestrate = interestrate+0.00125;
            updata=0;
            downdata=0;
            totalpayment=0;
        }
        /*
        double monthlypayment=0.00;
        double updata= loanamount*(interestrate/12);
        double downdata=1-(1/Math.pow(1+(interestrate/12),(years*12)));
        monthlypayment = updata/downdata;
        double totalpayment = monthlypayment*12*years;
        System.out.println("U should return:"+totalpayment);
        // System.out.println("loan amount"+loanamount+"number of years"+years);
        */
    }
}