package algorithms.math;

/**
 * Implementations of the factorial.
 */
public class Factorial {
	/**
	 * Iterative algorithm for calculating factorial.
	 * @param number Non-negative integer.
	 * @return Factorial of the number.
	 */
	public static long factorialIterative(long number) {
		if(number == 0) { return 1; }
		long output = 1;
		for(long i = number; i > 1; i--) {
			output *= i;
		}
		return output;
	}

	/**
	 * Iterative algorithm for calculating factorial forwardly.
	 * @param number Non-negative integer.
	 * @return Factorial of the number.
	 */
	public static long factorialIterativeForward(long number) {
		if(number == 0) { return 1; }
		long output = number;
		for(long i=1; i<number; i++) {
			output *= number-i;
		}
		return output;
	}
	
	/**
	 * Recursive algorithm for calculating factorial.
	 * @param number Non-negative integer.
	 * @return Factorial of the number.
	 */
	public static long factorialRecursive(long number) {
		if(number==0) { return 1; }
		return number*factorialRecursive(number-1);
	}
}
