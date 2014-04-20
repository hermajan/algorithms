package algorithms.math;

import static java.lang.Math.pow;
import static java.lang.Math.sqrt;

/**
 * Implementations of the Fibonacci number.
 * @author DJohnny
 */
public class Fibonacci {
    /**
     * Recursive algorithm for calculating the Fibonacci number.
     * @param n Index of a number in the Fibonacci sequence.
     * @return Fibonacci number.
     */
    public static int fibRecursive(int n) {
        if(n<=1) { return n; }
        else { return fibRecursive(n-1)+fibRecursive(n-2); }
    }

    /**
     * Iterative algorithm for calculating the Fibonacci number.
     * @param n Index of a number in the Fibonacci sequence.
     * @return Fibonacci number.
     */
    public static int fibIterative(int n) {
        int lower=0;
        int higher=1;
        for(int i=1; i<n; i++) {
            int tmp=lower+higher;
            lower=higher;
            higher=tmp;
        }
        return higher;
    }

    /**
     * Algorithm for calculating the Fibonacci number with Binet's formula.
     * @param n Index of a number in the Fibonacci sequence.
     * @return Fibonacci number.
     */
    public static int fibBinet(int n) {
        double f=(1+sqrt(5))/2;
        return (int)((pow(f, n)-pow(-f, -n))/sqrt(5));
    }
}
