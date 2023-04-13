/**
 * Java programm to calculate all prime numbers up to a given number.
 *
 * @File = Primes.java
 * @Date = 2023-04-13
 * @Author = Jannis Metrikat
 * @Version = 1.0
 */

public class Primes {

    /**
     * calculate primes using the sieve of eratosthenes
     */
    public static void primes(int n) {
        boolean isPrime[] = new boolean[n + 1];

        for (int i = 2; i <= n; i++) {
            isPrime[i] = true;
        }

        for (int i = 2; i * i <= n; i++) {
            if (isPrime[i]) {
                for (int j = i * i; j <= n; j += i) {
                    isPrime[j] = false;
                }
            }
        }

        for (int i = 2; i <= n; i++) {
            if (isPrime[i]) {
                System.out.println(i);
            }
        }

        return;
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

        primes(n);
        return;
    }
}
