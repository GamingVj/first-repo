// Write a program to display Exceptional Handling.

public class ExceptionHandling {

    // Method to perform division
    public static int divide(int numerator, int denominator) {
        try {
            return numerator / denominator;
        } catch (ArithmeticException e) {
            System.out.println("Exception caught: Division by zero is not allowed.");
            return 0; // Return a default value or handle it appropriately
        }
    }

    public static void main(String[] args) {
        // Test cases
        int result1 = divide(10, 2);
        System.out.println("Result of 10 / 2: " + result1);

        int result2 = divide(10, 0);
        System.out.println("Result of 10 / 0: " + result2);

        int result3 = divide(10, 5);
        System.out.println("Result of 10 / 5: " + result3);
    }
}