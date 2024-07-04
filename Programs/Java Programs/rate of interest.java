import java.util.*;
class SI
{
    public static void main(String args[])
    {
        float p,n,r,SI;
        Scanner sc=new Scanner(System.in);
        System.out.println("\n Enter the Values");
        p= sc.nextFloat();
        n=sc.nextFloat();
        r=sc.nextFloat();
        SI=(p*n*r)/100;
        System.out.println("\n Simple interest = "+SI);
    }
}