class MethodOverloading {

    // Method with no parameters
    public void display() {
        System.out.println("Display method with no parameters");
    }

    // Method with one integer parameter
    public void display(int a) {
        System.out.println("Display method with one integer parameter: " + a);
    }

    // Method with one string parameter
    public void display(String s) {
        System.out.println("Display method with one string parameter: " + s);
    }

    // Method with two parameters
    public void display(int a, String s) {
        System.out.println("Display method with two parameters: " + a + ", " + s);
    }
}

class MethodOverriding extends MethodOverloading {

    // Overriding the display method with one integer parameter
    @Override
    public void display(int a) {
        System.out.println("Overridden display method with one integer parameter: " + a);
    }
}

public class MethodOverloadingAndOverriding {
    public static void main(String[] args) {
        MethodOverloading overloading = new MethodOverloading();
        MethodOverriding overriding = new MethodOverriding();

        // Demonstrating method overloading
        overloading.display();
        overloading.display(10);
        overloading.display("Hello");
        overloading.display(20, "World");

        // Demonstrating method overriding
        overriding.display(10); // This will call the overridden method in MethodOverriding
    }
}