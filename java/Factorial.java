/**
 * Recursive Java program to calculate the factorial of a given number.
 *
 * @File = Factorial.java
 * @Date = 2022-12-28
 * @Author = Jannis Metrikat
 * @Version = 1.0
 *
 */

public class Factorial {

    /**
     * calculate the factorial of a given number
     */
    public static long factorial(int n) {
        if (n == 0) {
            return 1;
        } else {
            return n * factorial(n - 1);
        }
    }

    /**
     * main method
     */
    public static void main(String[] args) {
        if (args.length != 1) {
            System.out.println("Usage: java Factorial <number>");
            System.exit(1);
        }

        int n = Integer.parseInt(args[0]);
        if (n < 0) {
            System.out.println("Number must be positive.");
            System.exit(1);
        }

        System.out.println(factorial(n));
        return;
    }
}
