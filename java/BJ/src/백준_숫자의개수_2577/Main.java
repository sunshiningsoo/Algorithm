package 백준_숫자의개수_2577;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        int[] arrs = new int[10];
        try {
            int a = Integer.parseInt(br.readLine());
            int b = Integer.parseInt(br.readLine());
            int c = Integer.parseInt(br.readLine());
            String hap = String.valueOf(a * b * c);
            for(int i=0;i<hap.length();i++) {
                arrs[Integer.parseInt(String.valueOf(hap.charAt(i)))] += 1;
            }

            for (int i=0;i<arrs.length;i++) {
                sb.append(arrs[i]).append("\n");
            }
            System.out.println(sb.toString());
        } catch (Exception e) {

        }
    }

}
