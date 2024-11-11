abstract class abstract_class {
    // Abstract method to make sound
    abstract void makeSound();

    // Abstract method to move
    abstract void move();
}

class Dog extends abstract_class {
    // Implementing the abstract method makeSound
    @Override
    void makeSound() {
        System.out.println("Dog barks");
    }

    // Implementing the abstract method move
    @Override
    void move() {
        System.out.println("Dog runs");
    }
}

class Bird extends abstract_class {
    // Implementing the abstract method makeSound
    @Override
    void makeSound() {
        System.out.println("Bird chirps");
    }

    // Implementing the abstract method move
    @Override
    void move() {
        System.out.println("Bird flies");
    }
}

public class AbstractClassAndMethods {
    public static void main(String[] args) {
        // Creating instances of Dog and Bird
        abstract_class dog = new Dog();
        abstract_class bird = new Bird();

        // Calling methods on Dog instance
        dog.makeSound();
        dog.move();

        // Calling methods on Bird instance
        bird.makeSound();
        bird.move();
    }
}