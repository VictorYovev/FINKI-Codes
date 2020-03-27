import java.util.Random;
import java.util.concurrent.Semaphore;

class Printer {

    public static void main(String[] args) throws InterruptedException {
        RaceCondition.runTest();
    }
}

class RaceCondition {

    public static Semaphore semaphore = new Semaphore(1);
    Random random = new Random(70);
    int randInt = random.nextInt();

    public static void runTest() throws InterruptedException {


        final RaceCondition raceCondition = new RaceCondition();
        Thread thread1 = new Thread(() -> {
            try {
                raceCondition.printer("Thread1");
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        });
        Thread thread2 = new Thread(() -> {
            try {
                raceCondition.printer("Thread2");
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        });

        thread1.start();
        thread2.start();

        thread1.join();
        thread2.join();
    }

    void printer(String s) throws InterruptedException {

        int i = 100;
        semaphore.acquire();
        while (i != 0) {

            if (randInt % 2 == 0) {
                System.out.println(s + ": " + randInt);
            }
            i--;
        }
        semaphore.release();
    }
}