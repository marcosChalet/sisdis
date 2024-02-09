import java.rmi.Remote;
import java.rmi.RemoteException;

public interface CurrencyConverter extends Remote {
    double euroToReal(double amount) throws RemoteException;
    double realToEuro(double amount) throws RemoteException;
    double dollarToReal(double amount) throws RemoteException;
    double realToDollar(double amount) throws RemoteException;
}