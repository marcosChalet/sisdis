import java.rmi.Naming;

public class BrokerClient {
    private static Broker messageMQ = null;

    public static void main(String[] args) {
        try {
            messageMQ = (Broker) Naming.lookup("rmi://127.0.0.1:11099/RMIInterface");
            System.out.println(String.valueOf(messageMQ.addToList("Hello, World")));
            System.out.println(String.valueOf(messageMQ.addToList("Hello, World")));
            System.out.println();
            System.out.println(messageMQ.getList());
            System.out.println();
            System.out.println(messageMQ.getIP());
            System.out.println(messageMQ.getHour());
        }
        catch (Exception e) {
            System.out.println("Trouble: " + e);
        }
    }
}
