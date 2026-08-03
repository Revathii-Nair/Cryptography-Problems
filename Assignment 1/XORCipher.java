public class XORCipher {
    public static void main(String[] args) {
        String str = "Hello World";

        // XOR each character with 0
        System.out.println("XOR with 0:");
        StringBuilder result0 = new StringBuilder();
        for (int i = 0; i < str.length(); i++) {
            char c = str.charAt(i);
            char xored = (char) (c ^ 0);
            result0.append(xored);
            System.out.println("Char: " + c + "  ASCII: " + (int) c
                    + "  XOR 0: " + (int) xored + "  Char: " + xored);
        }
        System.out.println("Resulting string (XOR 0): " + result0.toString());

        System.out.println();

        // XOR each character with 1
        System.out.println("XOR with 1:");
        StringBuilder result1 = new StringBuilder();
        for (int i = 0; i < str.length(); i++) {
            char c = str.charAt(i);
            char xored = (char) (c ^ 1);
            result1.append(xored);
            System.out.println("Char: " + c + "  ASCII: " + (int) c
                    + "  XOR 1: " + (int) xored + "  Char: " + xored);
        }
        System.out.println("Resulting string (XOR 1): " + result1.toString());
    }
}