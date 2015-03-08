package algorithms.math;

import static java.lang.Math.pow;
import static java.lang.Math.sqrt;

/**
 * Math methods.
 * @author DJohnny
 */
public class Math {
    /**
     * Computes quadratic equation (ax^2+bx+c=0).
     * @param a A coefficient.
     * @param b B coefficient.
     * @param c C coefficient.
     * @return Result of quadratic equation, null if discriminant is below zero.
     */
    public static double[] quadratic(int a, int b, int c) {
        double discriminant=pow(b, 2)-4*a*c;

        if(discriminant<0) {
            System.err.print("No result!");
            return null;
        } else {
            double root1=(-b+sqrt(discriminant))/(2*a);
            double root2=(-b-sqrt(discriminant))/(2*a);
            return new double[]{root1, root2};
        }
    }
}
