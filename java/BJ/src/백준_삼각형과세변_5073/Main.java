package 백준_삼각형과세변_5073;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    public static void main(String[] args) {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        while (true) {
            try {
                String[] arrs = br.readLine().split(" ");
                if ((arrs[0].equals("0")) && (arrs[1].equals("0")) && (arrs[2].equals("0"))) {
                    break;
                }
                Set<Integer> seta = new HashSet<>();
                ArrayList<Integer> arr = new ArrayList<>();
                int a = Integer.parseInt(arrs[0]);
                int b = Integer.parseInt(arrs[1]);
                int c = Integer.parseInt(arrs[2]);
                arr.add(a);
                arr.add(b);
                arr.add(c);
                arr.sort(Comparator.naturalOrder());

                if (arr.get(0)+arr.get(1) <= arr.get(2)) {
                    System.out.println("Invalid");
                } else {
                    seta.addAll(arr);
                    if (seta.size() == 1) {
                        System.out.println("Equilateral");
                    } else if (seta.size() == 2) {
                        System.out.println("Isosceles");
                    } else {
                        System.out.println("Scalene");
                    }
                }
            } catch (IOException e) {

            }

        }

    }
}
