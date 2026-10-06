public class MaxMinComp{

    public static void main(String[] args) {

        double[][] R = {
            {0.1,0.6,1},

        };

        double[][] S = {
            {1,0.6,0.3},
            {0.5,0.5,0.3},
            {0.2,0.2,0.2}
        };

        System.out.println("Relation R:");
        for (int i = 0; i < R.length; i++) {
            for (int j = 0; j < R[0].length; j++) {
                System.out.print(R[i][j] + " ");
            }
            System.out.println();
        }


        System.out.println("\nRelation S:");
        for (int i = 0; i < S.length; i++) {
            for (int j = 0; j < S[0].length; j++) {
                System.out.print(S[i][j] + " ");
            }
            System.out.println();
        }

        double[][] maxmin = new double[R.length][S[0].length];
        for (int i = 0; i < R.length; i++) {
            for (int j = 0; j < S[0].length; j++) {
                double max = 0;
                for (int k = 0; k < S.length; k++) {
                    double min = Math.min(R[i][k], S[k][j]);
                    if (min > max) {
                        max = min;
                    }
                }
                maxmin[i][j] = max;
            }
        }

        double[][] maxprod = new double[R.length][S[0].length];

        for (int i = 0; i < R.length; i++) {
            for (int j = 0; j < S[0].length; j++) {
                double max = 0;
                for (int k = 0; k < S.length; k++) {
                    double product = R[i][k] * S[k][j];
                    if (product > max) {
                        max = product;
                    }
                }
                maxprod[i][j] = max;
            }
        }

        System.out.println("\nMax-Min Composition (R o S):");
        for (int i = 0; i < maxmin.length; i++) {
            for (int j = 0; j < maxmin[0].length; j++) {
                System.out.print(maxmin[i][j] + " ");
            }
            System.out.println();
        }

        System.out.println("\nMax-Prod Composition (R o S):");
        for (int i = 0; i < maxprod.length; i++) {
            for (int j = 0; j < maxprod[0].length; j++) {
                System.out.print(maxprod[i][j] + " ");
            }
            System.out.println();
        }
    }
}