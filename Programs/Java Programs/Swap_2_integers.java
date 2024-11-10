import java.util.*;
class Swap_2_integers
{
    public static void main(String args[])
    {
        int a,b,temp;
        Scanner sc=new Scanner(System.in);
        System.out.println("\nEnter the numbers.");
        a=sc.nextInt();
        b=sc.nextInt();
        System.out.println("Before Swapping: a = "+a+", b = "+b);
        temp=a;
        a=b;
        b=temp;
        System.out.println("After Swapping: a = "+a+", b = "+b);
    }
}