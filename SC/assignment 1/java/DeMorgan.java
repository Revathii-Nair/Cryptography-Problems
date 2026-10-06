public class DeMorgan {
    public static void main(String[] args) {

        double[] A = {0.2, 0.5, 0.8, 1.0};
        double[] B = {0.4, 0.3, 0.9, 0.6};

        double[] left1 = new double[A.length];
        double[] right1 = new double[A.length];
        double[] left2 = new double[A.length];
        double[] right2 = new double[A.length];

        for (int i = 0; i < A.length; i++) {
            left1[i] = 1 - Math.max(A[i], B[i]);
            right1[i] = Math.min(1 - A[i], 1 - B[i]);
        }

        System.out.print("(AUB)' = ");
        for (double x : left1) {
            System.out.print(x + " ");
        }

        System.out.print("\nA'nB' = ");
        for (double x : right1) {
            System.out.print(x + " ");
        }

        for (int i = 0; i < A.length; i++) {
            left2[i] = 1 - Math.min(A[i], B[i]);
            right2[i] = Math.max(1 - A[i], 1 - B[i]);
        }

        System.out.print("\n\n(A∩B)' = ");
        for (double x : left2) {
            System.out.print(x + " ");
        }

        System.out.print("\nA'UB' = ");
        for (double x : right2) {
            System.out.print(x + " ");
        }
    }
}