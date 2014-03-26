package algorithms;

import java.util.Arrays;

/**
 * Sorting algorithms.
 * @author DJohnny
 */
public class Sorts {
    /**
     * Bubble sort.
     * @param array Unsorted array.
     */
    public static void bubbleSort(int[] array) {
        for(int i=0; i<array.length-1; i++) {
            for(int j=0; j<array.length-1-i; j++) {
                if(array[j+1]<array[j]) {
                    swap(array, j, j+1);
                }
            }
        }
    }

    /**
     * Bucket sort.
     * @param array Unsorted array.
     */
    public static void bucketSort(int[] array) {
        int[] bucket=new int[array.length+1];
        for(int i=0; i<array.length; i++) {
            bucket[array[i]]++;
        }

        int position=0;
        for(int i=0; i<bucket.length; i++) {
            for(int j=0; j<bucket[i]; j++) {
                array[position++]=i;
            }
        }
    }

    /**
     * Counting sort.
     * @param array Unsorted array.
     */
    public static void countingSort(int[] array) {
        int[] sortedArray=new int[array.length+1];
        int[] values=new int[array.length+1];
        for(int i=0; i<=array.length; i++) {
            values[i]=0;
        }
        for(int j=0; j<array.length; j++) {
            values[array[j]]=values[array[j]]+1;
        }
        for(int i=1; i<=array.length; i++) {
            values[i]=values[i]+values[i-1];
        }
        for(int j=array.length-1; j>=0; j--) {
            sortedArray[values[array[j]]]=array[j];
            values[array[j]]=values[array[j]]-1;
        }

        for(int k=1; k<=array.length; k++) {
            array[k-1]=sortedArray[k];
        }
    }

    /**
     * Another counting sort.
     * @param array Unsorted array.
     */
    public static void countingSort2(int[] array) {
        int[] counts=new int[array.length+1];
        for(int x:array) { counts[x]++; }

        int current=0;
        for(int i=0; i<counts.length; i++) {
            Arrays.fill(array, current, current+counts[i], i);
            current+=counts[i];
        }
    }

    /**
     * Insertion sort.
     * @param array Unsorted array.
     */
    public static void insertionSort(int[] array) {
        for(int i=1; i<array.length; i++) {
            int tmp=array[i];
            int j=i;
            while(j>0 && array[j-1]>tmp) {
                array[j]=array[j-1];
                j=j-1;
            }
            array[j]=tmp;
        }
    }

    /**
     * Merge sort.
     * @param array Unsorted array.
     */
    public static void mergeSort(int[] array) {
        if(array.length>1) {
            // Split the array in a half.
            int[] left=Arrays.copyOfRange(array, 0, array.length/2);
            int[] right=Arrays.copyOfRange(array, left.length, array.length);

            // Sort each half.
            mergeSort(left);
            mergeSort(right);

            // Merge the halves together.
            System.arraycopy(merge(left, right), 0, array, 0, array.length);
        }
    }

    /**
     * Merges array in the merge sort.
     * @param left Left array.
     * @param right Right array.
     * @return Merged array.
     */
    private static int[] merge(int[] left, int[] right) {
        int[] result=new int[left.length+right.length];
        // Indices of elements to consider in arrays.
        int leftIndex=0, rightIndex=0;
        // Next open position in the result.
        int position=0;

        // As long as neither leftIndex nor rightIndex is past the end, move the smaller element into the result.
        while(leftIndex<left.length&&rightIndex<right.length) {
            if(left[leftIndex]<right[rightIndex]) {
                result[position]=left[leftIndex++];
            } else {
                result[position]=right[rightIndex++];
            }
            position++;
        }

        // Copy what's left.
        System.arraycopy(left, leftIndex, result, position, left.length-leftIndex);
        System.arraycopy(right, rightIndex, result, position, right.length-rightIndex);
        return result;
    }

    /**
     * Selection sort.
     * @param array Unsorted array.
     */
    public static void selectionSort(int[] array) {
        for(int i=0; i<array.length; i++) {
            int min=i;
            for(int j=i; j<array.length; j++) {
                if(array[j]<array[min]) {
                    min=j;
                }
            }
            if(min!=i) {
                swap(array, i, min);
            }
        }
    }

    /**
     * Quick sort.
     * @param array Unsorted array.
     */
    public static void quickSort(int[] array) {
        quickSort(array, 0, array.length-1);
    }

    /**
     * Quick sort.
     * @param array Unsorted array.
     * @param left Index of the leftmost element of the array.
     * @param right Index of the rightmost element of the array.
     */
    public static void quickSort(int[] array, int left, int right) {
        if(left<right) {
            int pivotIndex=partition(array, left, right);
            quickSort(array, left, pivotIndex-1);
            quickSort(array, pivotIndex+1, right);
        }
    }

    /**
     * Finds pivot for the quick sort.
     * @param array Array in which method looks for.
     * @param left Index of the leftmost element of the array.
     * @param right Index of the rightmost element of the array.
     * @return Index of the pivot.
     */
    private static int partition(int[] array, int left, int right) {
        int pivot=array[right];
        int lowerCounter=left-1;
        for(int i=left; i<right; i++) {
            if(array[i]<=pivot) {
                // Lower element from position i swaps with first bigger element.
                swap(array, ++lowerCounter, i);
            }
        }
        // Put pivot to the middle.
        swap(array, lowerCounter+1, right);
        return ++lowerCounter;
    }

    /**
     * Swaps two elements defined by indexes in the array.
     * @param array Array where the method swaps elements.
     * @param index1 Some index in the array.
     * @param index2 Other index in the array.
     */
    private static void swap(int[] array, int index1, int index2) {
        int tmp=array[index1];
        array[index1]=array[index2];
        array[index2]=tmp;
    }

    /**
     * Checks if the array is sorted.
     * @param array Sorted array.
     * @return True if the array is sorted, false otherwise.
     */
    public static boolean isSorted(int[] array) {
        return isSorted(array, 0, array.length-1);
    }

    /**
     * Checks if the array is sorted.
     * @param array Sorted array.
     * @param from From which index method checks sorting.
     * @param to To which index method checks sorting.
     * @return True if the array is sorted, false otherwise.
     */
    public static boolean isSorted(int[] array, int from, int to) {
        for(int i=from+1; i<=to; i++) {
            if(array[i]<array[i-1]) {
                return false;
            }
        }
        return true;
    }
}
