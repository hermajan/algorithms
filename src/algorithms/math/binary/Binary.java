package algorithms.math.binary;

/**
 * Converting to binary number.
 * @author DJohnny
 */
public class Binary {
	/**
	 * Converts binary number to decimal using method from Java language.
	 * @param binary Binary number in string.
	 * @return Decimal integer number.
	 */
	public static int bin2dec(String binary) {
		return Integer.parseUnsignedInt(binary, 2);
	}
	/**
	 * Converts decimal number to binary using method from Java language.
	 * @param number Number to convert.
	 * @return String with binary number.
	 */
	public static String dec2bin(int number) {
		return Integer.toBinaryString(number);
	}
	
	/**
	 * Converts decimal number to binary using string.
	 * @param number Number to convert.
	 * @return String with binary number.
	 */
	public static String dec2bin2(int number) {
		if(number==0) {
			return "0";
		}
		String binary="";
		while(number>0) {
			int bit=number%2;
			binary=bit+binary;
			number=number/2;
		}
		return binary;
	}

	/**
	 * Converts decimal number to binary using integer.
	 * @param number Number to convert.
	 * @return Integer with binary number.
	 */
	public static int dec2bin3(int number) {
		if(number==0) {
			return 0;
		}
		int binary=0;
		int multiplier=1;
		while(number>0) {
			int bit=number%2;
			number=number/2;
			binary=binary+bit*multiplier;
			multiplier=multiplier*10;
		}
		return binary;
	}
}
