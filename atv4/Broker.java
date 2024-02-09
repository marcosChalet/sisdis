import java.rmi.Remote;
import java.rmi.RemoteException;

public interface Broker extends Remote {
    public String addToList(String msg) throws RemoteException;
    public String getList() throws RemoteException;
    public String getIP() throws RemoteException;
    public String getHour() throws RemoteException;
}