package 백준_영역구하기_2583;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Comparator;
import java.util.List;
import java.util.StringTokenizer;

public class Main {
    static int R;
    static int C;
    static int num;
    static int[][] world, isVisited;
    static int[] dx = {1, -1, 0, 0};
    static int[] dy = {0, 0, 1, -1};

    static class Node {
        public int x;
        public int y;
        public int size;
        Node(int x, int y, int size) {
            this.x = x;
            this.y = y;
            this.size = size;
        }
    }

    public static int bfs(int cx, int cy) {
        List<Node> q = new ArrayList<>();
        q.add(new Node(cx, cy, 1));
        isVisited[cx][cy] = 1;
        int temp = 1;
        while (q.size() != 0) {
            Node curNode = q.remove(0);
            isVisited[curNode.x][curNode.y] = 1;
//            temp = Math.max(curNode.size, temp);
            for(int i=0;i<4;i++) {
                int nx = curNode.x + dx[i];
                int ny = curNode.y + dy[i];
                if (0<=nx && nx<R && 0<=ny && ny <C && isVisited[nx][ny] == 0 && world[nx][ny] == 0) {
                    q.add(new Node(nx, ny, curNode.size+1));
                    temp += 1;
                    isVisited[nx][ny] = 1;
                }
            }
        }
        return temp;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] arrs = br.readLine().split(" ");
        R = Integer.parseInt(arrs[0]);
        C = Integer.parseInt(arrs[1]);
        world = new int[R][C];
        isVisited = new int[R][C];
        num = Integer.parseInt(arrs[2]);
        for (int i=0;i<num;i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int sx = Integer.parseInt(st.nextToken());
            int sy = Integer.parseInt(st.nextToken());
            int ex = Integer.parseInt(st.nextToken());
            int ey = Integer.parseInt(st.nextToken());
            for (int j=sy;j<ey;j++) {
                for (int k=sx;k<ex;k++) {
                    world[j][k] = 1;
                }
            }
        }

        List<Integer> answers = new ArrayList<>();
        for (int i=0;i<R;i++) {
            for (int j=0;j<C;j++) {
                if (world[i][j] == 0 && isVisited[i][j] == 0) {
                    answers.add(bfs(i, j));
                }
            }
        }
        answers.sort(Comparator.naturalOrder());
        System.out.println(answers.size());
        for(int a: answers) {
            System.out.printf(a+" ");
        }
    }
}
