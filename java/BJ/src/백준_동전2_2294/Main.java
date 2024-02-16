package 백준_동전2_2294;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int target = Integer.parseInt(st.nextToken());
        int[] nums = new int[n];
        int[] dp = new int[target + 1];
        Arrays.fill(dp, 1000000);
        for (int i=0;i<n;i++) {
            int temp = Integer.parseInt(br.readLine());
            nums[i] = temp;
            if (temp <= target) {
                dp[temp] = 1;

            }
        }


        for (int i=1;i<target+1;i++) {
            for(int j=0;j<nums.length;j++) {
                if (i - nums[j] >= 0) {
                    dp[i] = Math.min(dp[i], dp[i - nums[j]] + 1);
                }
            }
        }

        int answer = dp[dp.length - 1];
        if (answer == 1000000) {
            System.out.println(-1);
        } else {
            System.out.println(answer);
        }

    }
}
