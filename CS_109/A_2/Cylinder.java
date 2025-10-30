import java.util.Scanner;
import java.lang.Math;

public class Cylinder extends Obj3D{
    float volume = 0f;
    float radius = 0f, height = 0f;

    public Cylinder() {
        // Empty
    }

    public void getDimens(Scanner sc) {
        this.radius = super.getDimen(sc, "Radius");
        this.height = super.getDimen(sc, "Height");
    }

    public void calcVolume() {
        this.volume = (float)(Math.PI * this.height * this.radius * this.radius);
    }

    public void dispVolume() {
        System.out.println("\nThe volume is about " + this.volume + ".");
    }
}