/**
 * Java program utilizing memoization to calculate the Fibonacci sequence.
 *
 * @File = Fibonacci.java
 * @Date = 2023-04-02
 * @Author = Jannis Metrikat
 * @Version = 1.0
 */

public class Fibonacci {

    /**
     * calculates the fibonacci sequence of a given number
     */
    public static long fibonacci(int n) {
        long fib[] = new long[n + 2];

        fib[0] = 0;
        fib[1] = 1;

        for (int i = 2; i <= n; i++) {
            fib[i] = fib[i - 1] + fib[i - 2];
        }

        return fib[n];
    }

    /**
     * main method
     */
    public static void main(String[] args) {
        if (args.length != 1) {
            System.out.println("Usage: java Fibonacci <number>");
            System.exit(1);
        }

        int n = Integer.parseInt(args[0]);
        if (n < 0) {
            System.out.println("Number must be positive.");
            System.exit(1);
        }

        System.out.println(fibonacci(n));
        return;
    }
}
