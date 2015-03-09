package algorithms.math;

import static org.junit.Assert.assertEquals;
import org.junit.Test;

/**
 * Tests for the Fibonacci class.
 * @author DJohnny
 */
public class FibonacciTest {
	/**
	 * Test of fibIterative method, of class Fibonacci.
	 */
	@Test
	public void testFibIterative() {
		System.out.println("fibIterative");
		assertEquals(1, Fibonacci.fibIterative(1));
		assertEquals(1, Fibonacci.fibIterative(2));
		assertEquals(8, Fibonacci.fibIterative(6));
		assertEquals(55, Fibonacci.fibIterative(10));
		assertEquals(144, Fibonacci.fibIterative(12));
	}
	
	/**
	 * Test of fibRecursive method, of class Fibonacci.
	 */
    @Test
    public void testFibRecursive() {
        System.out.println("fibRecursive");
        assertEquals(1, Fibonacci.fibRecursive(1));
        assertEquals(1, Fibonacci.fibRecursive(2));
        assertEquals(8, Fibonacci.fibRecursive(6));
        assertEquals(55, Fibonacci.fibRecursive(10));
        assertEquals(144, Fibonacci.fibRecursive(12));
    }

    /**
     * Test of fibBinet method, of class Fibonacci.
     */
    @Test
    public void testFibBinet() {
        System.out.println("fibBinet");
        assertEquals(1, Fibonacci.fibBinet(1));
        assertEquals(1, Fibonacci.fibBinet(2));
        assertEquals(8, Fibonacci.fibBinet(6));
        assertEquals(55, Fibonacci.fibBinet(10));
        assertEquals(144, Fibonacci.fibBinet(12));
    }
}

