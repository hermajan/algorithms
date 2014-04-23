package algorithms.time;

/**
 * Handling with a year.
 * @author DJohnny
 */
public class Year {
    /**
     * Checks if the year is leap.
     * @param year Input year.
     * @return True if the year is leap, false otherwise.
     */
    public static boolean leapYear(int year) {
        if(year%4!=0) {
            return false;
        } else if((year%100)!=0) {
            return true;
        } else if(year%400==0) {
            return true;
        } else {
            return false;
        }
    }
}
