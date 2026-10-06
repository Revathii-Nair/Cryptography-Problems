public class FuzzyIfThenElse {

    public static void main(String[] args) {

        double[] A = {0.2, 0.5, 0.8};
        double[] B = {0.4, 0.7, 0.3};
        double[] C = {0.6, 0.2, 0.9};

        double[] A_complement = new double[A.length];

        for (int i = 0; i < A.length; i++) {
            A_complement[i] = 1 - A[i];
        }

        System.out.println("IF A THEN B ELSE C = (A x B) U (A' x C)\n");

        double[][] AB = new double[A.length][B.length];
        double[][] A_C = new double[A.length][C.length];


        System.out.println("AxB:");
        for (int i = 0; i < A.length; i++) {
            for (int j = 0; j < B.length; j++) {
                AB[i][j] = Math.min(A[i], B[j]);
                System.out.print(AB[i][j] + " ");
            }
            System.out.println();
        }

        System.out.println("\nA'xC:");
        for (int i = 0; i < A.length; i++) {
            for (int j = 0; j < C.length; j++) {
                A_C[i][j] = Math.min(A_complement[i], C[j]);
                System.out.print(A_C[i][j] + " ");
            }
            System.out.println();
        }

        System.out.println("\nResult:");
        for (int i = 0; i < A.length; i++) {
            for (int j = 0; j < B.length; j++) {
                double result = Math.max(AB[i][j], A_C[i][j]);
                System.out.print(result + " ");
            }
            System.out.println();
        }
    }
}