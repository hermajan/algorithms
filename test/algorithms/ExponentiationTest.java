package algorithms;

import static org.junit.Assert.assertEquals;
import org.junit.Test;

/**
 * Tests for the Exponentiation class.
 * @author DJohnny
 */
public class ExponentiationTest {
    /**
     * Test of power method, of class Exponentiation.
     */
    @Test
    public void testPower() {
        System.out.println("power");
        assertEquals(1,Exponentiation.power(0.0,0),0.0);
        assertEquals(1024,Exponentiation.power(2,10),0.0);
        assertEquals(15.625,Exponentiation.power(2.5,3),0.0);
        assertEquals(81129638414606681695789005144064.0,Exponentiation.power(2,106),0.0);
    }

    /**
     * Test of powerLog method, of class Exponentiation.
     */
    @Test
    public void testPowerLog() {
        System.out.println("powerLog");
        assertEquals(1,Exponentiation.powerLog(0.0,0),0.0);
        assertEquals(1024,Exponentiation.powerLog(2,10),0.0);
        assertEquals(15.625,Exponentiation.powerLog(2.5,3),0.0);
        assertEquals(81129638414606681695789005144064.0,Exponentiation.powerLog(2,106),0.0);
    }

    /**
     * Test of powerNegative method, of class Exponentiation.
     */
    @Test
    public void testPowerNegative() {
        System.out.println("powerNegative");
        assertEquals(1,Exponentiation.powerNegative(0.0,0),0.0);
        assertEquals(1024,Exponentiation.powerNegative(2,10),0.0);
        assertEquals(15.625,Exponentiation.powerNegative(2.5,3),0.0);
        assertEquals(81129638414606681695789005144064.0,Exponentiation.powerNegative(2,106),0.0);
        
        assertEquals(0.125,Exponentiation.powerNegative(2,-3),0.0);
    }

    /**
     * Test of powerRecursive method, of class Exponentiation.
     */
    @Test
    public void testPowerRecursive() {
        System.out.println("powerRecursive");
        assertEquals(1,Exponentiation.powerRecursive(0.0,0),0.0);
        assertEquals(1024,Exponentiation.powerRecursive(2,10),0.0);
        assertEquals(15.625,Exponentiation.powerRecursive(2.5,3),0.0);
        assertEquals(81129638414606681695789005144064.0,Exponentiation.powerRecursive(2,106),0.0);
    }
}
