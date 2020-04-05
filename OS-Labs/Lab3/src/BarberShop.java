import java.util.concurrent.Semaphore;

public class BarberShop {

    public static Semaphore lockShop = new Semaphore(5);
    public static Semaphore lockBarber = new Semaphore(1);

    static void customerComesIn() throws InterruptedException {
        // TODO: 3/29/20 Synchronize this method, invoked by a Customer thread

        lockShop.acquire();
        System.out.println("Costumer " + Thread.currentThread().getName() + " enters in BarberShop.");
        lockBarber.acquire();
        barber();
        lockBarber.release();


    }

    static void barber() {
        // TODO: 3/29/20 Synchronize this method, invoked by Barber thread
        System.out.println("Barber gave a haircut to costumer " + Thread.currentThread().getName() + ".");
        lockShop.release();

    }

    public static void main(String[] args) throws InterruptedException {
        // TODO: 3/29/20 Synchronize the scenario

        Thread[] costumers = new Thread[100];
        for (int i = 0; i < 100; i++)
            costumers[i] = new Thread(() -> {
                try {
                    customerComesIn();
                } catch (InterruptedException e) {
                    e.printStackTrace();
                }
            }, "Thread-" + i);

        for (Thread costumer : costumers) {
            costumer.start();
        }

        for (Thread costumer : costumers) {
            costumer.join();
        }

    }
}