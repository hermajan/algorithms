import 'dart:html';

void main() {
    querySelector("#num").onInput.listen(binaryEvent);
}

void binaryEvent(Event e) {
    String num = (e.target as InputElement).value;
    try {
        querySelector('#binDart').text=dec2bin(int.parse(num));
    } on FormatException {
        print("Bad format!");
    }
}

/**
 * Converts decimal number to binary using string.
 * @param number Number to convert.
 * @return String with binary number.
 */
String dec2bin(int number) {
    return number.toRadixString(2);
}
