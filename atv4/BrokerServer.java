import java.rmi.Naming;
import java.rmi.RemoteException;
import java.rmi.server.UnicastRemoteObject;
import java.time.LocalTime;
import java.time.format.DateTimeFormatter;
import java.util.ArrayList;

public class BrokerServer extends UnicastRemoteObject implements Broker {

  ArrayList<String> repository;

  public BrokerServer() throws RemoteException {
      super();
      this.repository = new ArrayList<String>();
  }

  @Override
  public String addToList(String msg) throws RemoteException {
    this.repository.add(msg);
    return "Mensagem armazenada...";
  }

  @Override
  public String getList() throws RemoteException {
    String jsonResponse = "";
    jsonResponse += "{\n  data: [\n";

    for (String msg : repository) {
      if (msg != "") {
        jsonResponse += "    \"" + msg + "\",\n";
      }
    }

    jsonResponse += "  ]\n}";
    return jsonResponse;
  }

  @Override
  public String getIP() throws RemoteException {
    return "IP: 127.0.0.1";
  }

  @Override
  public String getHour() throws RemoteException {
    LocalTime currentTime = LocalTime.now();
    DateTimeFormatter formatter = DateTimeFormatter.ofPattern("HH:mm:ss");
    String formattedTime = currentTime.format(formatter);
    return "Hora: " + formattedTime;
  }

  public static void main(String[] args) {
      try {
          System.out.println("BrokerServer is running...");
          Naming.rebind("rmi://127.0.0.1:11099/RMIInterface", new BrokerServer());
      } catch (Exception e) {
          System.out.println("Trouble: " + e);
      }
  }
}