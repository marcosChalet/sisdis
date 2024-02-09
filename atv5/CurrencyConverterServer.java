import java.rmi.Naming;
import java.rmi.RemoteException;
import java.rmi.server.UnicastRemoteObject;

public class CurrencyConverterServer extends UnicastRemoteObject implements CurrencyConverter {

    protected CurrencyConverterServer() throws RemoteException {
        super();
    }

    @Override
    public double euroToReal(double amount) throws RemoteException {
        return amount * 5.34;
    }
    
    @Override
    public double realToEuro(double amount) throws RemoteException {
        return amount / 5.34;
    }
    
    @Override
    public double dollarToReal(double amount) throws RemoteException {
        return amount * 4.95;
    }
    
    @Override
    public double realToDollar(double amount) throws RemoteException {
        return amount / 4.95;
    }

  public static void main(String[] args) {
      try {
          System.out.println("BrokerServer is running...");
          Naming.rebind("rmi://127.0.0.1:11099/RMIInterface", new CurrencyConverterServer());
      } catch (Exception e) {
          System.out.println("Trouble: " + e);
      }
  }
}