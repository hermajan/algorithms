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
        System.out.println(powerLog(2,10));
        System.out.println(powerNegative(2,-3));
        System.out.println(powerRecursive(2,10));     
    }
    
    /**
     * Exponentiation with linear asymptotic complexity (Θ(n)).
     * @param base Real number.
     * @param exp Natural number.
     * @return Result of the exponentiation.
     */
    public static double power(double base,int exp) {
        if(exp<=0) { return 0; }
        double output=1;
        for(int i=exp;i>=1;i--) {
            output=output*base;
        }
        return output;
    }
    /**
     * Exponentiation with logarithmic asymptotic complexity (Θ(log n)).
     * @param base Real number.
     * @param exp Non-negative integer.
     * @return Result of the exponentiation.
     */
    public static double powerLog(double base,int exp) {
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
     * @param base Real number.
     * @param exp Integer.
     * @return Result of the exponentiation.
    */
    public static double powerNegative(double base,int exp) {
        if(exp>0) { return power(base,exp); }
        else { return 1/power(base,-exp); }
    }
    /**
     * Recursive exponentiation.
     * @param base Real number.
     * @param exp Non-negative integer.
     * @return Result of the exponentiation.
     */
    public static double powerRecursive(double base,int exp) {
        if(exp==0) { return 1; }
        else { return base*powerRecursive(base,exp-1); }
    }
}
