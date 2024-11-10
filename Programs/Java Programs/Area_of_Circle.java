import java.util.*;
class Area_of_Circle
{
    public static void main(String args[])
    {
        Scanner sc=new Scanner(System.in);
        System.out.println("\n Enter the radius");
        double radius=sc.nextDouble();
        double area=Math.PI * Math.pow(radius, 2);
        System.out.println("Area of circle is: " +area);
    }
}