import java.util.Scanner;

public class Rectangle {
    int area = 0;

    public Rectangle() {
        // Empty
    }

    public int getDimen(Scanner sc, String dimen) {
        boolean done = false;
        int dimenVal = 0;

        while (done == false) {
            try {
                System.out.print("\n" + dimen + ": ");
                dimenVal = sc.nextInt();
                if (dimenVal < 0) {
                    System.err.println("Value must be positive.");
                } else {
                    done = true;
                }
            } catch (java.util.InputMismatchException err) {
                System.err.println("Enter an integer.");
                sc.nextLine(); 
            }
        }

        return dimenVal;
    }

    public void calcArea(int l, int w) {
        this.area = l * w;
    }

    public void dispArea() {
        System.out.println("\nThe area is " + this.area + ".");
    }
}