import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        // Gets user input to set the maximum
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter a maximum number: ");
        Long max = sc.nextLong();
        sc.close();

        // Creates a NumberFinder object to find perfect numbers from 1 to a maximum
        NumberFinder finder = new NumberFinder();
        finder.findPerfectNums(max);
        finder.dispPerfectNums();
    }
}