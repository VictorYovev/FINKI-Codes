public class Singleton {

    private static volatile Singleton singleton;

    private Singleton() {

    }

    public synchronized static Singleton getInstance() {
        // TODO: 3/29/20 Synchronize this
        if (singleton == null) {
            singleton = new Singleton();
            System.out.println("Initialized by " + Thread.currentThread().getName());
        }
        return singleton;
    }

    public static void main(String[] args) throws InterruptedException {
        Thread thread1 = new Thread(Singleton::getInstance, "Thread-1");
        Thread thread2 = new Thread(Singleton::getInstance, "Thread-2");
        Thread thread3 = new Thread(Singleton::getInstance, "Thread-3");
        Thread thread4 = new Thread(Singleton::getInstance, "Thread-4");
        Thread thread5 = new Thread(Singleton::getInstance, "Thread-5");

        thread1.start();
        thread2.start();
        thread3.start();
        thread4.start();
        thread5.start();

        thread1.join();
        thread2.join();
        thread3.join();
        thread4.join();
        thread5.join();

    }
}



