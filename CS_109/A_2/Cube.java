import java.util.Scanner;

public class Cube extends Obj3D{
    float volume = 0f;
    float length = 0f, width = 0f, height = 0f;

    public Cube() {
        // Empty
    }

    public void getDimens(Scanner sc) {
        this.length = super.getDimen(sc, "Length");
        this.width = super.getDimen(sc, "Width");
        this.height = super.getDimen(sc, "Height");
    }

    public void calcVolume() {
        this.volume = this.length * this.width * this.height;
    }

    public void dispVolume() {
        System.out.println("\nThe volume is " + this.volume + ".");
    }
}