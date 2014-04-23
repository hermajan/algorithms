package algorithms.time;

import static org.junit.Assert.assertArrayEquals;
import org.junit.Test;

/**
 * Tests for the DateTest class.
 * @author DJohnny
 */
public class DateTest {
    /**
     * Test of gregorianToJulian method, of class Date.
     */
    @Test
    public void testGregorianToJulian() {
        System.out.println("gregorianToJulian");
        assertArrayEquals(new int[]{7, 4, 2014}, Date.gregorianToJulian(20, 4, 2014));
        assertArrayEquals(new int[]{31, 3, 2014}, Date.gregorianToJulian(13, 4, 2014));
        assertArrayEquals(new int[]{18, 4, 2014}, Date.gregorianToJulian(1, 5, 2014));
    }
    
    /**
     * Test of julianToGregorian method, of class Date.
     */
    @Test
    public void testJulianToGregorian() {
        System.out.println("julianToGregorian");
        assertArrayEquals(new int[]{20, 4, 2014}, Date.julianToGregorian(7, 4, 2014));
        assertArrayEquals(new int[]{13, 4, 2014}, Date.julianToGregorian(31, 3, 2014));
        assertArrayEquals(new int[]{1, 5, 2014}, Date.julianToGregorian(18, 4, 2014));
    }
}