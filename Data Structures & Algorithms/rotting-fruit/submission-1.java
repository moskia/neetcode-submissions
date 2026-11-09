class Solution {
    public int orangesRotting(int[][] grid) {
        int n = grid.length;
        int m = grid[0].length;
        int timer = 0;
        boolean[][] visited = new boolean[n][m];

        Queue<int[]> queue = new LinkedList<>();

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j ++) {
                if (grid[i][j] == 2) {
                    queue.offer(new int[]{i, j});
                    visited[i][j] = true;
                } else if (grid[i][j] == 0) {
                    visited[i][j] = true;
                }
            }
        }

        int[][] directions = {
            {1, 0},
            {-1, 0},
            {0, 1},
            {0, -1}
        };

        while (!queue.isEmpty()) {
            boolean rotted = false;
            int size = queue.size();
            

            for (int k = 0; k < size; k++){
                int[] current = queue.poll();

                int i = current[0];
                int j = current[1];
                for (int[] dir: directions) {
                    int ni = i + dir[0];
                    int nj = j + dir[1];

                    if (ni < n && ni >= 0 && 
                    nj < m && nj >= 0 && 
                    !visited[ni][nj] &&
                    grid[ni][nj] == 1) {

                        visited[ni][nj] = true;
                        queue.offer(new int[]{ni, nj});

                        rotted = true;
                    }
                }
            }
             
            if (rotted) {
                timer++;
            }
        }

        boolean allTrue = Arrays.stream(visited).allMatch(row -> {
            for (boolean value : row) {
                if (!value) return false;
            }
            return true;
        });

        if (allTrue) {
            return timer;
        } else {
            return -1;
        }

    }
}