public class FuzzySetOperation {
    public static void main(String[] args) {

        double[] A = {0.2, 0.5, 0.8, 1.0};
        double[] B = {0.4, 0.3, 0.9, 0.6};

        double[] union = new double[A.length];
        double[] intersection = new double[A.length];
        double[] complementA = new double[A.length];
        double[] complementB = new double[A.length];

        for (int i = 0; i < A.length; i++) {
            union[i] = Math.max(A[i], B[i]);
            intersection[i] = Math.min(A[i], B[i]);
            complementA[i] = Math.round((1 - A[i]) * 100.0) / 100.0;
            complementB[i] = Math.round((1 - B[i]) * 100.0) / 100.0;
        }


        System.out.print("Set A: ");
        for (double x : A) {
            System.out.print(x + " ");
        }
        
        System.out.print("\nSet B: ");
        for (double x : B) {
            System.out.print(x + " ");
        }

        System.out.print("\nUnion: ");
        for (double x : union) {
            System.out.print(x + " ");
        }

        System.out.print("\nIntersection: ");
        for (double x : intersection) {
            System.out.print(x + " ");
        }

        System.out.print("\nComplement of A: ");
        for (double x : complementA) {
            System.out.print(x + " ");
        }

        System.out.print("\nComplement of B: ");
        for (double x : complementB) {
            System.out.print(x + " ");
        }
    }
}