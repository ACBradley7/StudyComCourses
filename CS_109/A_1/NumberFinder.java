import java.util.ArrayList;

// Class with methods to find and print perfect numbers
public class NumberFinder {
    // Class variable that will be an ArrayList of the perfect numbers
    private ArrayList<Integer> perfectNums = new ArrayList<>();

    // Do not need any attributes on instantiation
    public NumberFinder() {
        // Empty
    }

    // Finds the perfect numbers given a maximum of type long
    // Algorithim determined simply by thinking through problem
    public void findPerfectNums(long max) {
        // Our nested loops skip over 1 so we force add it here
        perfectNums.add(1);
        int temp = 0;

        // Loop through every number from one to the maximum
        for (int i = 1; i <= max; i++) {
            // Loops over divisors
            // Only needs to go up to half of i since i / 2 is the largest possible divisor
            for (int j = 1; j <= i / 2; j++) {
                // We define a divisor as any number j that can go into i an even number of times
                if (i % j == 0) {
                    // Add j to a temporary variable that is the sum of the divisors
                    temp += j;
                }
            }

            // If the sum of the divisors equals i then we have a perfect number
            if (temp == i) {
                // Add i to the perfect num ArrayList
                this.perfectNums.add(i);
            }

            temp = 0;
        }
    }

    // Prints out the ArrayList to terminal
    public void dispPerfectNums() {
        // Just outputting as an ArrayList for convenience
        System.out.println("Perfect numbers are: " + this.perfectNums);
    }
}