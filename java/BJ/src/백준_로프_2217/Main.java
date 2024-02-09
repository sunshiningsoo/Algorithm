package 백준_로프_2217;

import java.util.ArrayList;
import java.util.Comparator;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);
        int num = sc.nextInt();
        ArrayList<Integer> lists = new ArrayList<>();
        for (int i=0;i<num;i++) {
            lists.add(sc.nextInt());
        }
        lists.sort(Comparator.reverseOrder());

        int temp = 0;
        ArrayList<Integer> arr = new ArrayList<>();

        for(int i=0;i<num;i++) {
            temp = Math.max(temp, lists.get(i) * (i+1));
        }

        System.out.println(temp);
    }
}
