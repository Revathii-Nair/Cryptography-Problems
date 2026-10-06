public class IfAThenB {

    public static void main(String[] args) {

        double[] A = {0.2, 0.5, 0.8};
        double[] B = {0.4, 0.7, 0.3};
        double[] Y = {1, 1, 1};

        double[] A_complement = new double[A.length];

        for (int i = 0; i < A.length; i++) {
            A_complement[i] = 1 - A[i];
        }

        System.out.println("Fuzzy Set A:");
        for (double x : A)
            System.out.print(x + " ");

        System.out.println("\n\nFuzzy Set B:");
        for (double x : B)
            System.out.print(x + " ");

        System.out.println("\n\nUniversal Set Y:");
        for (double x : Y)
            System.out.print(x + " ");

        System.out.println("\n\nAxB:");
        double[][] AB = new double[A.length][B.length];

        for (int i = 0; i < A.length; i++) {
            for (int j = 0; j < B.length; j++) {
                AB[i][j] = Math.min(A[i], B[j]);
                System.out.print(AB[i][j] + " ");
            }
            System.out.println();
        }

        System.out.println("\nA' x Y:");
        double[][] A_Y = new double[A.length][Y.length];

        for (int i = 0; i < A.length; i++) {
            for (int j = 0; j < Y.length; j++) {
                A_Y[i][j] = Math.min(A_complement[i], Y[j]);
                System.out.print(A_Y[i][j] + " ");
            }
            System.out.println();
        }

        System.out.println("\nIF A THEN B = (AxB)U(A'xY):");

        for (int i = 0; i < A.length; i++) {
            for (int j = 0; j < B.length; j++) {

                double result = Math.max(AB[i][j], A_Y[i][j]);

                System.out.print(result + " ");
            }
            System.out.println();
        }
    }
}