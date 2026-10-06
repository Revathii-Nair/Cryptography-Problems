public class CartesianProduct {
    public static void main(String[] args) {

        double[] A = {0.2, 0.5, 1.0};
        double[] B = {0.3, 0.8};

        double[][] product = new double[A.length][B.length];

        for (int i = 0; i < A.length; i++) {
            for (int j = 0; j < B.length; j++) {
                product[i][j] = Math.min(A[i], B[j]);
            }
        }

        System.out.println("Cartesian Product of A and B:");

        for (int i = 0; i < product.length; i++) {
            for (int j = 0; j < product[i].length; j++) {
                System.out.print(product[i][j] + " ");
            }
            System.out.println();
        }
    }
}