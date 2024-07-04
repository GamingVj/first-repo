import java.util.*;
class Area
{
    public static void main(String args[])
    {
        float a,r;
        Scanner sc=new Scanner(System.in);
        System.out.println("\n Enter the radius");
        double radius=sc.nextDouble();
        double area=Math.PI * Math.pow(radius, 2);
        System.out.println("Area of circle is: " +area);
    }
}