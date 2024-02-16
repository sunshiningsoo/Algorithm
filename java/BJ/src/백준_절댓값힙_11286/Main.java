package 백준_절댓값힙_11286;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Comparator;
import java.util.PriorityQueue;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        long n = Long.parseLong(br.readLine());
        StringBuilder sb = new StringBuilder();
        PriorityQueue<Long> pluspq = new PriorityQueue<>();
        PriorityQueue<Long> minuspq = new PriorityQueue<>(Comparator.reverseOrder());

        for (int i=0;i<n;i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            long a = Long.parseLong(st.nextToken());
            if (a == 0) {
                if (pluspq.isEmpty() && minuspq.isEmpty()) sb.append("0\n");
                else if (pluspq.isEmpty() && !minuspq.isEmpty()) sb.append(minuspq.poll()+"\n");
                else if (!pluspq.isEmpty() && minuspq.isEmpty()) sb.append(pluspq.poll()+"\n");
                else {
                    if (Math.abs(pluspq.peek()) == Math.abs(minuspq.peek())) sb.append(minuspq.poll()+"\n");
                    else if (Math.abs(pluspq.peek()) > Math.abs(minuspq.peek())) sb.append(minuspq.poll()+"\n");
                    else sb.append(pluspq.poll()+"\n");
                }
            } else {
                if (a > 0) pluspq.add(a);
                else minuspq.add(a);
            }
        }

        System.out.println(sb.toString());
    }
}
