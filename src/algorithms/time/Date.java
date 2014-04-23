package algorithms.time;

import static algorithms.time.Year.leapYear;

/**
 * Handling with a date.
 * @author DJohnny
 */
public class Date {
    /**
     * Converts a Gregorian calendar date to the Julian calendar date.
     * @param day Day.
     * @param month Month.
     * @param year Year.
     * @return Array with the Julian calendar date in the format [day, month, year].
     */
    public static int[] gregorianToJulian(int day, int month, int year) {
        int century=year/100;
        int difference=century-century/4-2;
        int newDay=day-difference;
        int months[]=new int[]{31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};
        if(leapYear(year)) {
            months[1]=29;
        }

        if(newDay<0) {
            newDay+=months[month-1]-1;
            month--;
        } else if(newDay==0) {
            month--;
            newDay+=months[month-1];
        }

        return new int[]{newDay, month, year};
    }
    
    /**
     * Converts a Julian calendar date to the Gregorian calendar date.
     * @param day Day.
     * @param month Month.
     * @param year Year.
     * @return Array with the Gregorian calendar date in the format [day, month, year].
     */
    public static int[] julianToGregorian(int day, int month, int year) {
        int century=year/100;
        int difference=century-century/4-2;
        int newDay=day+difference;
        int months[]=new int[]{31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};
        if(leapYear(year)) {
            months[1]=29;
        }

        if(newDay>months[month-1]) {
            newDay-=months[month-1];
            month++;
        }

        return new int[]{newDay, month, year};
    }
}
