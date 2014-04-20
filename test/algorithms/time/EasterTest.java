package algorithms.time;

import static org.junit.Assert.assertArrayEquals;
import org.junit.Test;

/**
 * Tests for the EasterTest class.
 * @author DJohnny
 */
public class EasterTest {
    /**
     * Test of easterSundayButcher method, of class Easter.
     */
    @Test
    public void testEasterSundayButcher() {
        System.out.println("easterSundayButcher");
        assertArrayEquals(new int[]{1, 4, 1888}, Easter.easterSundayButcher(1888));
        assertArrayEquals(new int[]{8, 4, 2012}, Easter.easterSundayButcher(2012));
        assertArrayEquals(new int[]{20, 4, 2014}, Easter.easterSundayButcher(2014));
        assertArrayEquals(new int[]{29, 3, 2111}, Easter.easterSundayButcher(2111));
    }

    /**
     * Test of easterSundayOudin method, of class Easter.
     */
    @Test
    public void testEasterSundayOudin() {
        System.out.println("easterSundayOudin");
        assertArrayEquals(new int[]{1, 4, 1888}, Easter.easterSundayOudin(1888));
        assertArrayEquals(new int[]{8, 4, 2012}, Easter.easterSundayOudin(2012));
        assertArrayEquals(new int[]{20, 4, 2014}, Easter.easterSundayOudin(2014));
        assertArrayEquals(new int[]{29, 3, 2111}, Easter.easterSundayOudin(2111));
    }

    /**
     * Test of easterSundayMeeus method, of class Easter.
     */
    @Test
    public void testEasterSundayMeeus() {
        System.out.println("easterSundayMeeus");
        assertArrayEquals(new int[]{24, 4, 1888}, Easter.easterSundayMeeus(1888));
        assertArrayEquals(new int[]{2, 4, 2012}, Easter.easterSundayMeeus(2012));
        assertArrayEquals(new int[]{7, 4, 2014}, Easter.easterSundayMeeus(2014));
        assertArrayEquals(new int[]{19, 4, 2111}, Easter.easterSundayMeeus(2111));
    }
}
