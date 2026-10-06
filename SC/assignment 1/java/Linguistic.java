import java.util.Scanner;

public class Linguistic{
    public static void main(String[] args) {
        double[] high = {0, 0.2, 0.4, 0.7, 1.0};
        double[] low = {1, 0.8, 0.6, 0.4, 0.2};

        Scanner sc = new Scanner(System.in);
        System.out.println("Base terms : high, low");
        System.out.println("Hedges: very, fairly, slightly");
        System.out.print("Enter term (e.g. very very high): ");
        String text = sc.nextLine();
        String[] words = text.toLowerCase().split(" ");

        String last = words[words.length - 1];
        if (!last.equals("high") && !last.equals("low") && !last.equals("hot")) {
            System.out.println("Unknown base term: " + last);
            return;
        }

        double power = 1;
        for (int i = 0; i < words.length - 1; i++) {
            if (words[i].equals("very"))
                power = power * 2;
            else if (words[i].equals("fairly"))
                power = power * (2.0 / 3);
            else if (words[i].equals("slightly"))
                power = power * 0.5;
            else {
                System.out.println("Unknown hedge: " + words[i]);
                return;
            }
        }

        System.out.println("\nResult: ");
        for (int j = 0; j < 5; j++) {
            double value;
            if (last.equals("high"))
                value = high[j];
            else 
                value = low[j];
            System.out.printf("%.4f ", Math.pow(value, power));
        }
        System.out.println();
    }
}