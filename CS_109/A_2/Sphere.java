import java.util.Scanner;
import java.lang.Math;

public class Sphere extends Obj3D {
    float volume = 0f;
    float radius = 0f;

    public Sphere() {
        // Empty
    }

    public void getDimens(Scanner sc) {
        this.radius = super.getDimen(sc, "Radius");
    }

    public void calcVolume() {
        this.volume = (float)(4f / 3f * Math.PI * this.radius * this.radius * this.radius);
    }

    public void dispVolume() {
        System.out.println("\nThe volume is about " + this.volume + ".");
    }
}