public class ConstructorOverloading{

    private int number;
    private String text;

    // Constructor with no parameters
    public ConstructorOverloading() {
        this.number = 0;
        this.text = "Default";
        System.out.println("Constructor with no parameters called");
    }

    // Constructor with one integer parameter
    public ConstructorOverloading(int number) {
        this.number = number;
        this.text = "Default";
        System.out.println("Constructor with one integer parameter called: " + number);
    }

    // Constructor with one string parameter
    public ConstructorOverloading(String text) {
        this.number = 0;
        this.text = text;
        System.out.println("Constructor with one string parameter called: " + text);
    }

    // Constructor with two parameters
    public ConstructorOverloading(int number, String text) {
        this.number = number;
        this.text = text;
        System.out.println("Constructor with two parameters called: " + number + ", " + text);
    }

    public static void main(String[] args) {
        // Creating instances using different constructors
        ConstructorOverloading example1 = new ConstructorOverloading();
        ConstructorOverloading example2 = new ConstructorOverloading(10);
        ConstructorOverloading example3 = new ConstructorOverloading("Hello");
        ConstructorOverloading example4 = new ConstructorOverloading(20, "World");
    }
}