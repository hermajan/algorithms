<?php
namespace algorithms\math\binary;

/**
 * Converting to binary number.
 * @author DJohnny
 */
class Binary {
	/**
	 * Converts decimal number to binary.
	 * @param int $number Number to convert.
	 * @return string String with binary number.
	 */
	public static function dec2bin($number) {
		return decbin($number);
	}
}
?>
