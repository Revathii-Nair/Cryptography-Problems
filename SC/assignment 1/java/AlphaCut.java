public class AlphaCut {
    static boolean sameRow(int[] a, int[] b) {
        for (int k = 0; k < a.length; k++) {
            if (a[k] != b[k])
                return false;
        }
        return true;
    }

    public static void main(String[] args) {
        double[][] R = {
            {1,   0.7, 0.4, 0.4},
            {0.7, 1,   0.4, 0.4},
            {0.4, 0.4, 1,   0.5},
            {0.4, 0.4, 0.5, 1}
        };
        double alpha = 0.7;
        int n = R.length;

        int[][] cut = new int[n][n];
        System.out.println("Alpha-Cut Matrix:");
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (R[i][j] >= alpha)
                    cut[i][j] = 1;
                System.out.print(cut[i][j] + " ");
            }
            System.out.println();
        }

        boolean[] done = new boolean[n];
        boolean firstClass = true;
        System.out.print("\nR" + alpha + " = ");

        for (int i = 0; i < n; i++) {
            if (done[i]) continue;
            
            if (!firstClass) System.out.print(",");
            System.out.print("{");

            boolean firstElement = true;
            for (int j = 0; j < n; j++) {
                if (sameRow(cut[i], cut[j])) {  
                    if (!firstElement) System.out.print(",");
                    System.out.print("x" + (j + 1));
                    done[j] = true;
                    firstElement = false;
                }
            }
            System.out.print("}");
            firstClass = false;
        }
        System.out.println();
    }
}