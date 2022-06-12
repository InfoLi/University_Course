public class count2_4{
    public static void main(String[] args){
        System.out.println("I\tm(i)");
        for (int i=10;i<=100;i+=10){
            C a = new C();
            System.out.printf("%d\t%.5f\n",i,a.count(i));
        }
    }
}
class C{
    public static double count(double i){
        double sum=0;
        double downdata_1 = 1;
        double downdata_2 = 3;
        double j=1;
        for (j=1;j<=i;j++)
        {
            double left = 1/(downdata_1+(j-1)*4);
            double right = 1/(downdata_2+(j-1)*4);
            sum = sum + (left-right);
        }
        return (sum*4);
    }
}

