/**
 * Recursive Java program to calculate the least common multiple of two given numbers.
 *
 * @File = Lcm.java
 * @Date = 2023-04-02
 * @Author = Jannis Metrikat
 * @Version = 1.0
 */

public class Lcm {

    /**
     * calculate greatest common divisor using euclid's algorithm
     */
    public static int gcd(int a, int b) {
        if (b == 0) {
            return a;
        }

        return gcd(b, a % b);
    }

    /**
     * calculates the least common multiple using greatest common divisor
     */
    public static int lcm(int a, int b) {
        return a * b / gcd(a, b);
    }

    /**
     * main method
     */
    public static void main(String[] args) {
        if (args.length != 2) {
            System.out.println("Usage: java Lcm <number1> <number2>");
            System.exit(1);
        }

        int a = Integer.parseInt(args[0]);
        int b = Integer.parseInt(args[1]);

        System.out.println(lcm(Math.abs(a), Math.abs(b)));
        return;
    }
}
