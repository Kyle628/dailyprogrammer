import java.time.*;
import java.util.List;
import java.util.Map;

class RestaurantDemo {

    public static void main(String[] args) {

        Reservation myRes = new Reservation("kyle", 1, LocalTime.now());
        System.out.println(myRes.startTime);

    }

}

class Reservation {
    public String name;
    public int partySize;
    public LocalTime startTime;

    public Reservation(String name, int partySize, LocalTime startTime) {
        this.name = name;
        this.partySize = partySize;
        this.startTime = startTime;
    }
}

class Table {
    public int tableNumber;
    public int maxPartySize;

    public Table(int tableNumber, int maxPartySize) {
        this.tableNumber = tableNumber;
        this.maxPartySize = maxPartySize;
    }
}

class Restaurant {
    public List<Table> tables;
    public LocalTime openTime;
    public LocalTime closeTime;
    public Map<Integer, Duration> reservationDurationsPerPartySize;

    /*public Table bookReservation(Reservation reservation) {
        return Table;
    }*/
}
