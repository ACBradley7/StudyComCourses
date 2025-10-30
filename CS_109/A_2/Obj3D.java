import java.util.Scanner;

public abstract class Obj3D {
    public abstract void getDimens(Scanner sc);
    public abstract void calcVolume();
    public abstract void dispVolume();

    public static Obj3D selectOption(Scanner sc) {
        boolean done = false;
        int choice = 0;

        while (done == false) {
            try {
                System.out.print("\nSelect (1) Cylinder, (2) Cube, (3) Sphere: ");
                choice = sc.nextInt();
                if (choice != 1 && choice != 2 && choice != 3) {
                    System.err.println("Enter 1, 2, or 3.");
                } else {
                    done = true;
                }
            } catch (java.util.InputMismatchException err) {
                System.err.println("Enter an integer.");
                sc.nextLine(); 
            }
        }

        if (choice == 1) { return new Cylinder(); }
        else if (choice == 2) { return new Cube(); }
        else if (choice == 3) { return new Sphere(); }
        else { return null; }
    }

    public float getDimen(Scanner sc, String dimen) {
        boolean done = false;
        float dimenVal = 0f;

            while (done == false) {
                try {
                    System.out.print("\n" + dimen + ": ");
                    dimenVal = sc.nextFloat();
                    if (dimenVal < 0) {
                        System.err.println("Value must be positive.");
                    } else {
                        done = true;
                    }
                } catch (java.util.InputMismatchException err) {
                    System.err.println("Enter a decimal or integer.");
                    sc.nextLine(); 
                }
            }

        return dimenVal;
    }
}