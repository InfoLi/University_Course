import java.util.Scanner;
public class countscore{
    public static void main(String[] args){
        Scanner input = new Scanner(System.in);
        int score[] = new int[99];
        int temp = 0;
        double aver = 0;
        int num = 0;
        int sum = 0;
        System.out.println("Plz enter score(<=100),stop at '101'");
        temp = input.nextInt();
        while (temp!=101){
            score[num] = temp;
            temp = input.nextInt();
            num++;
        } 
        for (int j=0;j<num;j++){
            sum = sum + score[j];
        }
        aver = sum/num;
        System.out.println("the average score is"+aver);
        System.out.println("the score which is higher than aver:");
        for (int j=0;j<num;j++){
            if(score[j]>=aver){
                System.out.printf("%d ",score[j]);
            }
        }
    }
}