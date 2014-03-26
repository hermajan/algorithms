package algorithms;

import static org.junit.Assert.assertArrayEquals;
import static org.junit.Assert.assertTrue;
import org.junit.Test;

/**
 * Tests for the Sorts class.
 * @author DJohnny
 */
public class SortsTest {
    int[] sortedArray={0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
    int[] unsortedArray={5, 8, 2, 1, 10, 7, 4, 6, 3, 9, 0};
    int[] sortedArray2={0, 1, 1, 2, 3, 4, 5, 5, 6, 7, 8, 8, 9, 10};
    int[] unsortedArray2={5, 8, 2, 1, 10, 8, 7, 4, 5, 6, 3, 9, 0, 1};

    /**
     * Test of bubbleSort method, of class Sorts.
     */
    @Test
    public void testBubbleSort() {
        System.out.println("bubbleSort");

        int[] array=new int[unsortedArray.length];
        System.arraycopy(unsortedArray, 0, array, 0, unsortedArray.length);
        Sorts.bubbleSort(array);
        assertArrayEquals(sortedArray, array);
        assertTrue(Sorts.isSorted(array));

        array=new int[unsortedArray2.length];
        System.arraycopy(unsortedArray2, 0, array, 0, unsortedArray2.length);
        Sorts.bubbleSort(array);
        assertArrayEquals(sortedArray2, array);
        assertTrue(Sorts.isSorted(array));
    }

    /**
     * Test of bucketSort method, of class Sorts.
     */
    @Test
    public void testBucketSort() {
        System.out.println("bucketSort");

        int[] array=new int[unsortedArray.length];
        System.arraycopy(unsortedArray, 0, array, 0, array.length);
        Sorts.bucketSort(array);
        assertArrayEquals(sortedArray, array);
        assertTrue(Sorts.isSorted(array));

        array=new int[unsortedArray2.length];
        System.arraycopy(unsortedArray2, 0, array, 0, unsortedArray2.length);
        Sorts.bucketSort(array);
        assertArrayEquals(sortedArray2, array);
        assertTrue(Sorts.isSorted(array));
    }

    /**
     * Test of countingSort method, of class Sorts.
     */
    @Test
    public void testCountingSort() {
        System.out.println("countingSort");

        int[] array=new int[unsortedArray.length];
        System.arraycopy(unsortedArray, 0, array, 0, array.length);
        Sorts.countingSort(array);
        assertArrayEquals(sortedArray, array);
        assertTrue(Sorts.isSorted(array));

        array=new int[unsortedArray2.length];
        System.arraycopy(unsortedArray2, 0, array, 0, unsortedArray2.length);
        Sorts.countingSort(array);
        assertArrayEquals(sortedArray2, array);
        assertTrue(Sorts.isSorted(array));
    }

    /**
     * Test of countingSort method, of class Sorts.
     */
    @Test
    public void testCountingSort2() {
        System.out.println("countingSort2");

        int[] array=new int[unsortedArray.length];
        System.arraycopy(unsortedArray, 0, array, 0, array.length);
        Sorts.countingSort2(array);
        assertArrayEquals(sortedArray, array);
        assertTrue(Sorts.isSorted(array));

        array=new int[unsortedArray2.length];
        System.arraycopy(unsortedArray2, 0, array, 0, unsortedArray2.length);
        Sorts.countingSort2(array);
        assertArrayEquals(sortedArray2, array);
        assertTrue(Sorts.isSorted(array));
    }

    /**
     * Test of insertionSort method, of class Sorts.
     */
    @Test
    public void testInsertionSort() {
        System.out.println("insertionSort");

        int[] array=new int[unsortedArray.length];
        System.arraycopy(unsortedArray, 0, array, 0, unsortedArray.length);
        Sorts.insertionSort(array);
        assertArrayEquals(sortedArray, array);
        assertTrue(Sorts.isSorted(array));

        array=new int[unsortedArray2.length];
        System.arraycopy(unsortedArray2, 0, array, 0, unsortedArray2.length);
        Sorts.insertionSort(array);
        assertArrayEquals(sortedArray2, array);
        assertTrue(Sorts.isSorted(array));
    }

    /**
     * Test of mergeSort method, of class Sorts.
     */
    @Test
    public void testMergeSort() {
        System.out.println("mergeSort");

        int[] array=new int[unsortedArray.length];
        System.arraycopy(unsortedArray, 0, array, 0, unsortedArray.length);
        Sorts.mergeSort(array);
        assertArrayEquals(sortedArray, array);
        assertTrue(Sorts.isSorted(array));

        array=new int[unsortedArray2.length];
        System.arraycopy(unsortedArray2, 0, array, 0, unsortedArray2.length);
        Sorts.mergeSort(array);
        assertArrayEquals(sortedArray2, array);
        assertTrue(Sorts.isSorted(array));
    }

    /**
     * Test of selectionionSort method, of class Sorts.
     */
    @Test
    public void testSelectionSort() {
        System.out.println("selectionSort");

        int[] array=new int[unsortedArray.length];
        System.arraycopy(unsortedArray, 0, array, 0, unsortedArray.length);
        Sorts.selectionSort(array);
        assertArrayEquals(sortedArray, array);
        assertTrue(Sorts.isSorted(array));

        array=new int[unsortedArray2.length];
        System.arraycopy(unsortedArray2, 0, array, 0, unsortedArray2.length);
        Sorts.selectionSort(array);
        assertArrayEquals(sortedArray2, array);
        assertTrue(Sorts.isSorted(array));
    }

    /**
     * Test of quickSort method, of class Sorts.
     */
    @Test
    public void testQuickSort() {
        System.out.println("quickSort");

        int[] array=new int[unsortedArray.length];
        System.arraycopy(unsortedArray, 0, array, 0, unsortedArray.length);
        Sorts.quickSort(array);
        assertArrayEquals(sortedArray, array);
        assertTrue(Sorts.isSorted(array));

        array=new int[unsortedArray2.length];
        System.arraycopy(unsortedArray2, 0, array, 0, unsortedArray2.length);
        Sorts.quickSort(array);
        assertArrayEquals(sortedArray2, array);
        assertTrue(Sorts.isSorted(array));
    }
}
