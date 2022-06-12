import java.util.Scanner;
import java.util.Random;
public class guessnum {
	public static void main(String [] args) {
	    Random rand = new Random();
        int ran = rand.nextInt(100)+ 1;
        System.out.println("随机产生一个1-100之间的整数,请进行猜测");
        Scanner input = new Scanner(System.in);
        int number=input.nextInt();
        int time = 0;
        while(number!=ran){
            time++;
            if (time<=3){
                System.out.println("没有猜对哦，请继续尝试");
                number=input.nextInt();
            }
            else if(time<=5){
                if (number < ran){
                    System.out.println("小了，请继续尝试");
                    number=input.nextInt();
                }
                else {
                    System.out.println("大了，请继续尝试");
                    number=input.nextInt();
                }
            }
            else {
                System.out.println("答案是"+ran);
                System.exit(0);
            }
        }
        System.out.println("恭喜你，答对了！");
    }    
}        
