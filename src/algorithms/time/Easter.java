package algorithms.time;

/**
 * Algorithms for the calculation of the date of Easter in a calendar.
 * @author DJohnny
 */
public class Easter {
    /**
     * Butcher's algorithm for calculating the date of Easter in the Gregorian calendar.
     * @param year Input year for calculating.
     * @return Array with date of the Easter Sunday in format [day, month, year].
     */
    public static int[] easterSundayButcher(int year) {
        int a=year%19;
        int b=year/100;
        int c=year%100;
        int d=b/4;
        int e=b%4;
        int f=(b+8)/25;
        int g=(b-f+1)/3;
        int h=(19*a+b-d-g+15)%30;
        int i=c/4;
        int k=c%4;
        int L=(32+2*e+2*i-h-k)%7;
        int m=(a+11*h+22*L)/451;
        int month=(h+L-7*m+114)/31;
        int day=((h+L-7*m+114)%31)+1;
        
        return new int[]{day, month, year};
    }

    /**
     * Oudin's algorithm for calculating the date of Easter in the Gregorian calendar.
     * @param year Input year for calculating.
     * @return Array with date of the Easter Sunday in format [day, month, year].
     */
    public static int[] easterSundayOudin(int year) {
        int century=year/100;
        int G=year%19;
        int K=(century-17)/25;
        int I=(century-century/4-(century-K)/3+19*G+15)%30;
        I=I-(I/28)*(1-(I/28)*(29/(I+1))*((21-G)/11));
        int J=(year+year/4+I+2-century+century/4)%7;
        int L=I-J;
        int month=3+(L+40)/44;
        int day=L+28-31*(month/4);
        
        return new int[]{day, month, year};
    }

    /**
     * Meeus's algorithm for calculating the date of Easter in the Julian calendar.
     * @param year Input year for calculating.
     * @return Array with date of the Easter Sunday in format [day, month, year].
     */
    public static int[] easterSundayMeeus(int year) {
        int a=year%4;
        int b=year%7;
        int c=year%19;
        int d=(19*c+15)%30;
        int e=(2*a+4*b-d+34)%7;
        int month=(d+e+114)/31;
        int day=((d+e+114)%31)+1;

        return new int[]{day, month, year};
    }
}
