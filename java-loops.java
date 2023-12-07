import java.util.*;
import java.io.*;

class Solution{
    public static void main(String []argh){
        Scanner in = new Scanner(System.in);
        int t=in.nextInt();
        for(int i=0;i<t;i++){
            int a = in.nextInt();
            int b = in.nextInt();
            int n = in.nextInt();
            System.out.print(a+b);
            int val = a+b;
            int p2 = 1;
            for (int j = 1; j <= n-1; ++j)
            {
                p2 *= 2;
                val += p2*b;
                System.out.print(" "+val);
            }
            System.out.println();
        }
        in.close();
    }
}
