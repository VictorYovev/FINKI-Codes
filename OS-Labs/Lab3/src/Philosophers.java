import java.util.Random;
import java.util.concurrent.Semaphore;

class Philosophers {

    public static void main(String[] args) throws InterruptedException {
        DiningPhilosophers.runTest();
    }
}

class DiningPhilosophers {

    private static Random random = new Random(System.currentTimeMillis());
    private Semaphore[] forks = new Semaphore[5];
    private Semaphore lock = new Semaphore(1);

    public DiningPhilosophers() {
        forks[0] = new Semaphore(1);
        forks[1] = new Semaphore(1);
        forks[2] = new Semaphore(1);
        forks[3] = new Semaphore(1);
        forks[4] = new Semaphore(1);

    }

    public void lifecycleOfPhilosopher(int id) throws InterruptedException {

        while (true) {
            think();
            eat(id);
        }
    }

    void think() throws InterruptedException {
        Thread.sleep(random.nextInt(50));
    }


    static void runPhilosopher(DiningPhilosophers dp, int id) {
        try {
            dp.lifecycleOfPhilosopher(id);
        } catch (InterruptedException ignored) {

        }
    }

    void eat(int id) throws InterruptedException {
        // TODO: 3/29/20 Synchronize
        lock.acquire();
        forks[id].acquire();
        System.out.println("Philosopher " + (id + 1) + " " + Thread.currentThread().getId() + " picked up the LEFT fork");
        forks[(id + 1) % forks.length].acquire();
        System.out.println("Philosopher " + (id + 1) + " " + Thread.currentThread().getId() + " picked up the RIGHT fork -> eating");
        forks[id].release();
        System.out.println("Philosopher " + (id + 1) + " " + Thread.currentThread().getId() + " put down the LEFT fork");
        forks[(id + 1) % forks.length].release();
        System.out.println("Philosopher " + (id + 1) + " " + Thread.currentThread().getId() + " put down the RIGHT fork -> thinking");
        lock.release();
    }

    public static void runTest() throws InterruptedException {
        final DiningPhilosophers dp = new DiningPhilosophers();

        Thread p1 = new Thread(() -> runPhilosopher(dp, 0));

        Thread p2 = new Thread(() -> runPhilosopher(dp, 1));

        Thread p3 = new Thread(() -> runPhilosopher(dp, 2));

        Thread p4 = new Thread(() -> runPhilosopher(dp, 3));

        Thread p5 = new Thread(() -> runPhilosopher(dp, 4));

        p1.start();
        p2.start();
        p3.start();
        p4.start();
        p5.start();

        p1.join();
        p2.join();
        p3.join();
        p4.join();
        p5.join();
    }
}