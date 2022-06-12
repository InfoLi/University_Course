import java.util.Scanner;
public class huiwen {
		public static void main(String [] args) {
		Scanner input = new Scanner(System.in);
		System.out.println("请输入一个整数:");
		int number=input.nextInt();
		int i=0;
		int n=number;
		while(number>0){
			i=i*10+number%10;
			number=number/10;
		}
		if(i==n){
			System.out.println("是回文数");
		}else{
			System.out.println("不是回文数");
		}
    }
}
