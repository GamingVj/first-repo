public class MethodOverloading{

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

    public static void main(String[] args) {
        MethodOverloading example = new MethodOverloading();

        // Calling overloaded methods
        example.display();
        example.display(10);
        example.display("Hello");
        example.display(20, "World");
    }
}