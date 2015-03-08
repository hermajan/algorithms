package algorithms.math;

import static org.junit.Assert.assertArrayEquals;
import org.junit.Test;

/**
 * Tests for the Math class.
 * @author DJohnny
 */
public class MathTest {
    /**
     * Test of quadratic method, of class Math.
     */
    @Test
    public void testQuadratic() {
        System.out.println("quadratic");
        assertArrayEquals(new double[]{0, 0}, Math.quadratic(1, 0, 0), 0);
        assertArrayEquals(new double[]{-2, -2}, Math.quadratic(1, 4, 4), 0);
        assertArrayEquals(new double[]{3, -2}, Math.quadratic(1, -1, -6), 0);
        assertArrayEquals(new double[]{7.7416, 0.2583}, Math.quadratic(2, -16, 4), 0.0001);
    }

}
