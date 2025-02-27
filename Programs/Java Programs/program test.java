import java.util.*;

public class MyClass
{

    public static void main(String args[])
    {
        int x, y, sum;
        Scanner MyObj = new Scanner(System.in);
        System.out.println("Type a number: ");
        x = MyObj.nextInt();
        
        System.out.println("Type another number: ");
        y = MyObj.nextInt();

        sum = x + y;
        System.out.println("Sum is: " + sum);

    }
}