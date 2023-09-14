/**
 *  C programm utilizing memoization to calculate the Fibonacci sequence.
 *
 * @File = fibonacci.c
 * @Date = 2022-12-29
 * @Author = Jannis Metrikat
 * @Version = 1.0
 */

#include <stdio.h>
#include <stdlib.h>

/* calculate the n-th Fibonacci number */
long long fibonacci(int n) {
    long long *fib = (long long *) malloc((n + 2) * sizeof(long long));

    fib[0] = 0;
    fib[1] = 1;

    for (int i = 2; i <= n; i++) {
        fib[i] = fib[i - 1] + fib[i - 2];
    }

    long long result = fib[n];
    free(fib);

    return result;
}

int main(int argc, char *argv[]) {
    if (argc != 2) {
        fprintf(stderr, "Usage: %s <number>\n", argv[0]);
        return 1;
    }

    int n = atoi(argv[1]);
    if (n < 0) {
        fprintf(stderr, "Number must be positive.\n");
        return 1;
    }

    printf("%lld\n", fibonacci(n));
    return 0;
}
