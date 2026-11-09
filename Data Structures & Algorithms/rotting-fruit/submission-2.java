class Solution {
    public int orangesRotting(int[][] grid) {

        int n = grid.length;
        int m = grid[0].length;

        Queue<int[]> queue = new LinkedList<>();
        int fresh = 0;
        int timer = 0;

        // Initialize the queue and count fresh oranges
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {

                if (grid[i][j] == 2) {
                    queue.offer(new int[]{i, j});
                } else if (grid[i][j] == 1) {
                    fresh++;
                }
            }
        }

        int[][] directions = {
            {1, 0}, {-1, 0},
            {0, 1}, {0, -1}
        };

        while (!queue.isEmpty() && fresh > 0) {

            int size = queue.size();

            for (int k = 0; k < size; k++) {

                int[] current = queue.poll();

                int i = current[0];
                int j = current[1];

                for (int[] dir : directions) {

                    int ni = i + dir[0];
                    int nj = j + dir[1];

                    if (ni >= 0 && ni < n &&
                        nj >= 0 && nj < m &&
                        grid[ni][nj] == 1) {

                        grid[ni][nj] = 2;
                        fresh--;

                        queue.offer(new int[]{ni, nj});
                    }
                }
            }

            timer++;
        }

        return fresh == 0 ? timer : -1;
    }
}