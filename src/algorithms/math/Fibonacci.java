package algorithms.math;

import static java.lang.Math.pow;
import static java.lang.Math.sqrt;

/**
 * Implementations of the Fibonacci number.
 * @author DJohnny
 */
public class Fibonacci {
	/**
	 * Iterative algorithm for calculating the Fibonacci number.
	 * @param index Index of a number in the Fibonacci sequence.
	 * @return Fibonacci number.
	 */
	public static int fibIterative(int index) {
		int lower=0;
		int higher=1;
		for(int i=1; i<index; i++) {
			int tmp=lower+higher;
			lower=higher;
			higher=tmp;
		}
		return higher;
	}
	
    /**
     * Recursive algorithm for calculating the Fibonacci number.
     * @param index Index of a number in the Fibonacci sequence.
     * @return Fibonacci number.
     */
    public static int fibRecursive(int index) {
        if(index<=1) { return index; }
        else { return fibRecursive(index-1)+fibRecursive(index-2); }
    }

    /**
     * Algorithm for calculating the Fibonacci number with Binet's formula.
     * @param index Index of a number in the Fibonacci sequence.
     * @return Fibonacci number.
     */
    public static int fibBinet(int index) {
        double f=(1+sqrt(5))/2;
        return (int)((pow(f, index)-pow(-f, -index))/sqrt(5));
    }
}

