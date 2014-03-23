package algorithms;

import static org.junit.Assert.assertEquals;
import org.junit.Test;

/**
 * Tests for the Factorial class.
 * @author DJohnny
 */
public class FactorialTest {    
    /**
     * Test of factorialRecursion method, of class Factorial.
     */
    @Test
    public void testFactorialRecursion() {
        System.out.println("factorialRecursion");
        assertEquals(1,Factorial.factorialRecursion(0),0);
        assertEquals(120,Factorial.factorialRecursion(5),0);
    }

    /**
     * Test of factorialIterative method, of class Factorial.
     */
    @Test
    public void testFactorialIterative() {
        System.out.println("factorialIterative");
        assertEquals(1,Factorial.factorialIterative(0),0);
        assertEquals(120,Factorial.factorialIterative(5),0);
    }
}
