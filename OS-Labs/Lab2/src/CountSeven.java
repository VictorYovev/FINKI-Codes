import java.util.HashSet;
import java.util.Random;
import java.util.Scanner;
import java.util.concurrent.Semaphore;

public class CountSeven {

    public static int NUM_RUNS = 1000;
    /**
     * TODO: definirajte gi potrebnite elementi za sinhronizacija
     */
    public static Semaphore lock;
    /**
     * Promenlivata koja treba da go sodrzi brojot na pojavuvanja na elementot 7
     */
    int count = 0;

    public static void main(String[] args) {
        try {
            CountSeven environment = new CountSeven();
            environment.start();
        } catch (Exception ex) {
            ex.printStackTrace();
        }
    }

    public void init() {
        lock = new Semaphore(1);
    }

    public void start() throws Exception {

        init();

        HashSet<Thread> threads = new HashSet<Thread>();
        Scanner s = new Scanner(System.in);
        int total = s.nextInt();
        Random random = new Random();
        int correct = 0;
        for (int i = 0; i < NUM_RUNS; i++) {
            int[] data = new int[total];
            for (int j = 0; j < total; j++) {
                data[j] = random.nextInt(10);
                if (data[j] == 7)
                    correct++;
            }
            Counter c = new Counter(data);
            threads.add(c);
        }

        for (Thread t : threads) {
            t.start();
        }

        for (Thread t : threads) {
            t.join();
        }
        System.out.println(count);
        System.out.println((correct == count) ? "Great, u made a synchronization" : "Oh buddy u are something wrong");


    }

    class Counter extends Thread {

        private int[] data;

        public Counter(int[] data) {
            this.data = data;
        }

        public void count(int[] data) throws InterruptedException {
            int count1 = 0;
            for (int i = 0; i < data.length; i++) {
                if (data[i] == 7)
                    count1++;
            }
            lock.acquire();
            count += count1;
            lock.release();
        }

        @Override
        public void run() {
            try {
                count(data);
            } catch (Exception e) {
                e.printStackTrace();
            }
        }
    }
}