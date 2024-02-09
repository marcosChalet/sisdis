import java.rmi.Naming;
import java.rmi.RemoteException;
import java.rmi.server.UnicastRemoteObject;
import java.time.LocalDateTime;
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
       LocalDateTime currentDateTime = LocalDateTime.now();
        int year = currentDateTime.getYear();
        int month = currentDateTime.getMonthValue();
        int day = currentDateTime.getDayOfMonth();
        int hour = currentDateTime.getHour();
        int minute = currentDateTime.getMinute();
        String formattedDateTime = String.format("%04d-%02d-%02d %02d:%02d", year, month, day, hour, minute);
    return "Hour: " + formattedDateTime;
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