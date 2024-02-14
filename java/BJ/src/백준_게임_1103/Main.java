package 백준_게임_1103;

import java.io.IOException;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {

    public static String[][] world = new String[50][50];
    public static int[][] isVisited;
    public static int[][] cache = new int[50][50];
    public static int R;
    public static int C;
    public static int answer;
    public static int[] dx = {1, -1, 0, 0};
    public static int[] dy = {0, 0, -1, 1};

    public static boolean inRange(int x, int y) {
        if (0<=x && x<R && 0<=y && y<C) return true;
        return false;
    }

    public static void back(int cx, int cy, int cnt) {
        cache[cx][cy] = cnt;
        if (cnt > answer) {
            answer = cnt;
        }

        for (int i=0;i<4;i++) {
            int nx = cx + dx[i] * Integer.parseInt(world[cx][cy]);
            int ny = cy + dy[i] * Integer.parseInt(world[cx][cy]);
            if (inRange(nx, ny) && !world[nx][ny].equals("H") && !world[nx][ny].equals("0")) {
                if (isVisited[nx][ny] == 1) {
                    answer = -1;
                    return;
                }
                // 더 작은 경우로 오면 큰 값을 구하는 것이기에 더 안봐도 됨
                if (cnt < cache[nx][ny]) continue;
                isVisited[nx][ny] = 1;
                back(nx, ny, cnt + 1);
                if (answer == -1) return;
                isVisited[nx][ny] = 0;
            }
        }
    }


    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        String[] arrs = br.readLine().split(" ");
        R = Integer.parseInt(arrs[0]);
        C = Integer.parseInt(arrs[1]);
        isVisited = new int[R][C];
        isVisited[0][0] = 1;
        for (int i = 0;i<R;i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            String s = st.nextToken();
            for (int j = 0;j<C;j++) {
                world[i][j] = String.valueOf(s.charAt(j));
                cache[i][j] = Integer.MIN_VALUE;
            }
        }

        back(0, 0, 0);
        if (answer == -1) {
            System.out.println(answer);
        } else {
            System.out.println(answer+1);
        }


    }
}
