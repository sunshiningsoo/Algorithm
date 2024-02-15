package 백준_주유소_13305;

import java.io.IOException;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Stack;
import java.util.StringTokenizer;

public class Main {

    static int N;
    static long[] road;
    static long[] world;

    static long answer;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine());
        StringTokenizer st = new StringTokenizer(br.readLine());
        road = new long[N - 1];
        world = new long[N];
        for(int i=0;i<N-1;i++) {
            road[i] = Integer.parseInt(st.nextToken());
        }
        StringTokenizer st2 = new StringTokenizer(br.readLine());
        for(int i=0;i<N;i++) {
            world[i] = Integer.parseInt(st2.nextToken());
        }

        Stack<Long> stack = new Stack<>();
        int ptr = 0;
        int hap = 0;
        hap += road[ptr];
        stack.add(world[ptr]);
        ptr += 1;

//        while (ptr != road.length) {
//            if (stack.get(0) <= world[ptr]) {
//                stack.add(world[ptr]);
//                hap += road[ptr];
//                ptr += 1;
//            } else {
//                answer += stack.get(0) * hap;
//                stack.clear();
//                stack.add(world[ptr]);
//                hap = 0;
//                hap += road[ptr];
//                ptr += 1;
//            }
//        }
        long minValue = world[0];
        while (ptr != road.length) {
            if (minValue > world[ptr]) minValue = world[ptr];
            answer += minValue * road[ptr];
            ptr += 1;
        }

        if (stack.size()!=0) {
            answer += stack.get(0) * hap;
        }

        System.out.println(answer);

    }
}
