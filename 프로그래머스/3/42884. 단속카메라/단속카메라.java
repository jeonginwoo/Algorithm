import java.util.*;

class Solution {
    public int solution(int[][] routes) {
        Arrays.sort(routes, (a, b) -> {
            if (a[1] == b[1]) {
                return a[0]-b[0];
            }
            return a[1]-b[1];
        });
        
        int now = routes[0][1];
        int answer = 1;
        
        for (int i=0; i<routes.length; i++) {
            if (routes[i][0] <= now) {
                continue;
            }
            now = routes[i][1];
            answer++;
        }
        
        return answer;
    }
}