// Write a program to display volume of sphere and hemisphere make use of interface.

interface Volume {
    // Method to calculate volume
    double calculateVolume();
}

class Sphere implements Volume {
    private double radius;

    // Constructor
    public Sphere(double radius) {
        this.radius = radius;
    }

    // Implementing the calculateVolume method
    @Override
    public double calculateVolume() {
        return (4.0 / 3.0) * Math.PI * Math.pow(radius, 3);
    }
}

class Hemisphere implements Volume {
    private double radius;

    // Constructor
    public Hemisphere(double radius) {
        this.radius = radius;
    }

    // Implementing the calculateVolume method
    @Override
    public double calculateVolume() {
        return (2.0 / 3.0) * Math.PI * Math.pow(radius, 3);
    }
}

public class VolumeCalculator {
    public static void main(String[] args) {
        // Creating instances of Sphere and Hemisphere
        Volume sphere = new Sphere(5);
        Volume hemisphere = new Hemisphere(5);

        // Displaying the volumes
        System.out.println("Volume of Sphere: " + sphere.calculateVolume());
        System.out.println("Volume of Hemisphere: " + hemisphere.calculateVolume());
    }
}