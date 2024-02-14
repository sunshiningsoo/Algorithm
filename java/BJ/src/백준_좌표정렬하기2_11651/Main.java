package 백준_좌표정렬하기2_11651;

import java.io.IOException;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Comparator;
import java.util.StringTokenizer;
import java.util.List;
import java.util.ArrayList;
public class Main {

    static class Zum {
        int x;
        int y;

        Zum(int x, int y) {
            this.x = x;
            this.y = y;
        }

        public int getX() {
            return x;
        }

        public int getY() {
            return y;
        }

    }
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        List<Zum> arrs = new ArrayList<>();
        for (int i=0;i<n;i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int x = Integer.parseInt(st.nextToken());
            int y = Integer.parseInt(st.nextToken());
            arrs.add(new Zum(x, y));
        }
        arrs.sort(Comparator.comparing(Zum::getY)
                .thenComparing(Zum::getX));
        for (Zum arr : arrs) {
            System.out.println(arr.getX() + " " + arr.getY());
        }

    }
}
