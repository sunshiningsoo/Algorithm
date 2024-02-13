package 백준_사다리조작_15684;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;

public class Main {
    static int answer = 4;
    static int C, R, H;
    static int world[][];
    public static void main(String[] args) {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        try {
            String[] arrs = br.readLine().split(" ");
            C = Integer.parseInt(arrs[0]);
            R = Integer.parseInt(arrs[1]);
            H = Integer.parseInt(arrs[2]);
            world = new int[H][C];
            for (int i=0;i<R;i++) {
                String[] k = br.readLine().split(" ");
                int r = Integer.parseInt(k[0]);
                int c = Integer.parseInt(k[1]);
                world[r-1][c-1] = 1;
            }
            DFS(0, 0, 0);
            if (answer > 3) {
                System.out.println("-1");
            } else {
                System.out.println(answer);
            }

        } catch (Exception e) {
            System.out.println("e = " + e.getLocalizedMessage());
        }
    }

    public static boolean checker() {
        List<Integer> arrs = new ArrayList<>();
        List<Integer> arrss = new ArrayList<>();
        for(int i=0;i<C;i++) {
            arrs.add(i);
            arrss.add(i);
        }
        for(int i=0;i<H;i++) {
            for (int j=0;j<C;j++) {
                if (world[i][j] == 1) {
                    int temp = arrs.get(j);
                    int newInt = arrs.get(j + 1);
                    arrs.set(j, newInt);
                    arrs.set(j + 1, temp);
                }
            }
        }

        if (arrss.equals(arrs)) return true;

        return false;
    }

    public static boolean boundCheck(int x, int y) {
        if (y == 0 && world[x][y+1] == 0) return true;
        if (y-1>=0 && world[x][y-1] == 0 && y+1 < C && world[x][y+1] == 0) return true;
        return false;
    }

    public static void DFS(int cnt, int x, int y) {
        if (cnt >= answer) return;
        if (checker()) {
            answer = cnt < answer ? cnt : answer;
            return;
        }
        if (cnt >= 3) return;

        for (int i=x;i<H;i++) {
            int cur = i == x ? y : 0;
            for (int j = cur;j<C;j++) {
                if (world[i][j] == 0 && boundCheck(i, j)) {
                    world[i][j] = 1;
                    DFS(cnt+1, i, j+2);
                    world[i][j] = 0;
                }
            }
        }
    }

}
