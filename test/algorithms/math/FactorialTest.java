package algorithms;

import static org.junit.Assert.assertEquals;
import org.junit.Test;

/**
 * Tests for the Factorial class.
 * @author DJohnny
 */
public class FactorialTest {
    /**
     * Test of factorialIterative method, of class Factorial.
     */
    @Test
    public void testFactorialIterative() {
        System.out.println("factorialIterative");
        assertEquals(1, Factorial.factorialIterative(0), 0);
        assertEquals(120, Factorial.factorialIterative(5), 0);
    }

    /**
     * Test of factorialRecursive method, of class Factorial.
     */
    @Test
    public void testFactorialRecursive() {
        System.out.println("factorialRecursive");
        assertEquals(1, Factorial.factorialRecursive(0), 0);
        assertEquals(120, Factorial.factorialRecursive(5), 0);
    }
}
