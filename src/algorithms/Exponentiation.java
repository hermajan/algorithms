package algorithms;

/**
 * Implementations of exponentiation.
 * @author DJohnny
 * @see http://en.wikipedia.org/wiki/Exponentiation
 */
public class Exponentiation {
    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        System.out.println(power(2,10));
        System.out.println(power2(2,10));
        System.out.println(power3(2,-3));
        
        /**
         * Time measurement.
         * @see http://stackoverflow.com/questions/1770010/how-do-i-measure-time-elapsed-in-java
        */
        //System.out.println(System.nanoTime()+" ns");
    }
    
    public static double power(double base, int exp) {
        //System.out.println(System.nanoTime()+" ns");
        if(exp<=0) { return 0; }
        double output=1;
        for(int i=exp;i>=1;i--) {
            output=output*base;
        }
        return output;
    }
    public static double power2(double base, int exp) {
        double output=1;
        while(exp>0) {
            if(exp%2==1) { output=output*base; }
            base=base*base;
            exp=exp/2;
        }
        return output;
    }
    /**
     * Exponentiation, which works with negative numbers.
     * @param base
     * @param exp
     * @return 
    */
    public static double power3(double base, int exp) {
        if(exp>0) { return power(base,exp); }
        else { return 1/power(base,-exp); }
    }
}
