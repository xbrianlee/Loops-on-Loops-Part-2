//Quicksort algorithm for sorting strings in a file. 
//Code cited from Princeton at http://algs4.cs.princeton.edu/23quicksort/Quick.java.html


import java.lang.*;
import java.io.*;
import java.lang.Object;
import java.io.Reader;
import java.io.BufferedReader;

public class quicksort{
	private quicksort() { }
	
	public static void main(String[] args){
        
		 if(args.length!=1){
			System.err.println("inputfile ");
		 }
		 
		 String[] t1 = new String[500];
		 String tempStr;
		try{
			BufferedReader orig = new BufferedReader(new FileReader(args[0]));
		

		
			String s1 = new String(orig.readLine());
			t1 = s1.split(" ");
			orig.close();
		} catch(Exception error){
			System.err.println("Error: message");
		}

		quicksort.sort(t1);
        for(int i=0;i<t1.length;i++){
            System.out.println(t1[i]);
        }
   }
	public static void sort(Comparable[] a) {
       // StdRandom.shuffle(a);
        sort(a, 0, a.length - 1);
        assert isSorted(a);
    }

    private static void sort(Comparable[] a, int lo, int hi) { 
        if (hi <= lo) return;
        int j = partition(a, lo, hi);
        sort(a, lo, j-1);
        sort(a, j+1, hi);
        assert isSorted(a, lo, hi);
    }

    private static int partition(Comparable[] a, int lo, int hi) {
        int i = lo;
        int j = hi + 1;
        Comparable v = a[lo];
        while (true) { 
            while (less(a[++i], v))
                if (i == hi) break;
            while (less(v, a[--j]))
                if (j == lo) break; 
            if (i >= j) break;

            exch(a, i, j);
        }
        exch(a, lo, j);
        return j;
    }

    public static Comparable select(Comparable[] a, int k) {
        if (k < 0 || k >= a.length) {
            throw new IndexOutOfBoundsException("Selected element out of bounds");
        }
      //  StdRandom.shuffle(a);
        int lo = 0, hi = a.length - 1;
        while (hi > lo) {
            int i = partition(a, lo, hi);
            if      (i > k) hi = i - 1;
            else if (i < k) lo = i + 1;
            else return a[i];
        }
        return a[lo];
    }

    private static boolean less(Comparable v, Comparable w) {
        return (v.compareTo(w) < 0);
    }
        
    private static void exch(Object[] a, int i, int j) {
        Object swap = a[i];
        a[i] = a[j];
        a[j] = swap;
    }

    private static boolean isSorted(Comparable[] a) {
        return isSorted(a, 0, a.length - 1);
    }

    private static boolean isSorted(Comparable[] a, int lo, int hi) {
        for (int i = lo + 1; i <= hi; i++)
            if (less(a[i], a[i-1])) return false;
        return true;
    }
}