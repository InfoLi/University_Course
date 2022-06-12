import java.util.*;

// add insertpos remove getLength show  search
public class test{
    public static void main(String args[]){
        LList<Integer> num = new LList<Integer>();
        num.add(15);
        num.add(6);
        num.add(2);
        num.add(98);
        num.add(43);  
        num.add(2);
        System.out.print("the start list\t");
        num.show();
        System.out.print("insert 100\t");                      
        num.insertpos(3,100);  
        num.show();  
        System.out.print("remove position 2 \t");            
        num.remove(2);
        num.show();
        num.search(2);
    }
}