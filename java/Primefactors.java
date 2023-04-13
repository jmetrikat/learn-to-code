/**
 * Java program to calculate prime factors of a given number.
 *
 * @File = Primefactors.java
 * @Date = 2023-04-13
 * @Author = Jannis Metrikat
 * @Version = 1.0
 */

public class Primefactors {

    /**
     * calculate prime factors of a given number
     */
    public static void primeFactors(int n) {
        boolean foundFactor = false;

        for (int i = 2; i < n ; i++) {
            boolean isPrime = true;

            for (int j = 2; j < i; j++) {
                if (i % j == 0) {
                    isPrime = false;
                    break;
                }
            }

            if (n % i == 0 && isPrime) {
                System.out.println(i);
                foundFactor = true;
            }
        }

        if (!foundFactor) {
            System.out.println(n + " is prime.");
        }
    }

    /**
     * main method
     */
    public static void main(String[] args) {
        if (args.length != 1) {
            System.out.println("Usage: java Primes <number>");
            System.exit(1);
        }

        int n = Integer.parseInt(args[0]);
        if (n < 2) {
            System.out.println("Number must be greater than 1.");
            System.exit(1);
        }

        primeFactors(n);
        return;
    }
}
