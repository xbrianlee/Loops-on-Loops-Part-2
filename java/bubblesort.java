import java.lang.*;
import java.io.*;
import java.lang.Object;
import java.io.Reader;
import java.io.BufferedReader;

public class bubblesort{
	public static void main(String[] args){
        
		 if(args.length!=1){
			System.err.println("inputfile ");
		 }
		 long startTime = System.currentTimeMillis();

		 String[] t1 = new String[50000];
		 String tempStr;
		try{
			BufferedReader orig = new BufferedReader(new FileReader(args[0]));
		

		
			String s1 = new String(orig.readLine());
			t1 = s1.split(" ");
			orig.close();
		} catch(Exception error){
			System.err.println("Error: message");
		}

        for (int t=0; t<t1.length-1; t++)
        {
            for (int i= 0; i < t1.length - t -1; i++) //for(int i = 0; i<t1.length -1; i++)
            {
                if(t1[i+1].compareTo(t1[i])<0)//if(t1[i+1].compareTo(t1[1+1])>0)
                {
                    tempStr = t1[i];
                    t1[i] = t1[i+1];
                    t1[i+1] = tempStr;
                }
            }
        }
		long endTime = System.currentTimeMillis();

		System.out.println(endTime - startTime);
        
   }
}