package algorithms;

/**
 * Implementations of the factorial.
 * @author DJohnny
 * @see http://en.wikipedia.org/wiki/Factorial
 */
public class Factorial {
    /**
     * Recursive algorithm for calculating factorial.
     * @param number Non-negative integer.
     * @return Factorial of the number.
     */
    public static long factorialRecursion(long number) {
        if(number==0) { return 1; }
        return number*factorialRecursion(number-1);
    }
    
    /**
     * Iterative algorithm for calculating factorial.
     * @param number Non-negative integer.
     * @return Factorial of the number.
     */
    public static long factorialIterative(long number) {
        if(number==0) { return 1; }
        long output=number;
        for(long i=1;i<number;i++) {
            output=output*(number-i);
        }
        return output;
    }
}
