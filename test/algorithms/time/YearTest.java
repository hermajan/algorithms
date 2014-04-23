package algorithms.time;

import static org.junit.Assert.assertEquals;
import org.junit.Test;

/**
 * Tests for the YearTest class.
 * @author DJohnny
 */
public class YearTest {
    /**
     * Test of leapYear method, of class Year.
     */
    @Test
    public void testLeapYear() {
        System.out.println("leapYear");
        assertEquals(true, Year.leapYear(2000));
        assertEquals(true, Year.leapYear(2012));
        assertEquals(false, Year.leapYear(2014));
    }
}
