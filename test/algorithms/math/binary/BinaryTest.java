package algorithms.math.binary;

import static org.junit.Assert.assertEquals;
import org.junit.Test;

/**
 * Tests for the BinaryTest class.
 * @author DJohnny
 */
public class BinaryTest {
	/**
	 * Test of bin2dec method, of class Binary.
	 */
	@Test
	public void testBin2dec() {
		System.out.println("bin2dec");
		assertEquals(8, Binary.bin2dec("1000"));
	}
	/**
	 * Test of dec2bin method, of class Binary.
	 */
	@Test
	public void testDec2bin() {
		System.out.println("dec2bin");
		assertEquals("0", Binary.dec2bin(0));
		assertEquals("1000", Binary.dec2bin(8));
	}

	/**
	 * Test of dec2bin2 method, of class Binary.
	 */
	@Test
	public void testDec2bin2() {
		System.out.println("dec2bin2");
		assertEquals("0", Binary.dec2bin2(0));
		assertEquals("1000", Binary.dec2bin2(8));
	}

	/**
	 * Test of dec2bin3 method, of class Binary.
	 */
	@Test
	public void testDec2bin3() {
		System.out.println("dec2bin3");
		assertEquals(0, Binary.dec2bin3(0));
		assertEquals(1000, Binary.dec2bin3(8));
	}
}