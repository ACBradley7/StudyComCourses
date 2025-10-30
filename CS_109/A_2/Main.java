import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        // Rectangle Functions
        System.out.println("\nLet's calculate the area of a rectangle.");
        Rectangle rect = new Rectangle();
        int length = rect.getDimen(sc, "Length");
        int width = rect.getDimen(sc, "Width");
        rect.calcArea(length, width);
        rect.dispArea();

        // Volume Claculation
        System.out.println("\nLet's calculate the volume of a 3D shape.");
        Obj3D shape = Obj3D.selectOption(sc);
        shape.getDimens(sc);
        shape.calcVolume();
        shape.dispVolume();

        sc.close();
    }
}