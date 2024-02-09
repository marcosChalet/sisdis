import java.rmi.Naming;

public class CurrencyConverterClient {
    private static CurrencyConverter converter = null;

    public static void main(String[] args) {
        try {
            converter = (CurrencyConverter) Naming.lookup("rmi://127.0.0.1:11099/RMIInterface");
            System.out.printf("%.2f US$\n", converter.realToDollar(500));
            System.out.printf("%.2f R$\n", converter.dollarToReal(500));
            System.out.printf("%.2f €\n", converter.realToEuro(500));
            System.out.printf("%.2f R$\n", converter.euroToReal(500));
        }
        catch (Exception e) {
            System.out.println("Trouble: " + e);
        }
    }
}
