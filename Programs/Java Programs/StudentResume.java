// Write a program with various string components to design a java application to accept student resumes.


import java.util.*;

public class StudentResume {
    public static void main(String[] args) {
        Scanner Scanner = new Scanner(System.in);

        System.out.print("\nEnter student's name: ");
        String name = Scanner.nextLine();

        System.out.print("Enter student's email: ");
        String email = Scanner.nextLine();

        System.out.print("Enter student's phone number: ");
        String phoneNumber = Scanner.nextLine();

        System.out.print("Enter student's education: ");
        String education = Scanner.nextLine();

        System.out.print("Enter student's skills: ");
        String skills = Scanner.nextLine();

        System.out.print("Enter student's experience: ");
        String experience = Scanner.nextLine();

        System.out.println("\n--- Student Resume ---");
        System.out.println("Name: " + name);
        System.out.println("Email: " + email);
        System.out.println("Phone Number: " + phoneNumber);
        System.out.println("Education: " + education);
        System.out.println("Skills: " + skills);
        System.out.println("Experience: " + experience);
    }
}