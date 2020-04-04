import java.util.concurrent.Semaphore;

class H2OMachine {

    String[] molecule;
    int count;
    public static Semaphore initO = new Semaphore(1);
    public static Semaphore initH = new Semaphore(2);
    public static Semaphore oHere = new Semaphore(0);
    public static Semaphore hHere = new Semaphore(0);
    public static Semaphore ready = new Semaphore(0);
    public static Semaphore lock = new Semaphore(1);

    public H2OMachine() {
        molecule = new String[3];
        count = 0;
    }

    public void hydrogen() throws InterruptedException {
        initH.acquire(1);
        oHere.acquire();
        hHere.release();
        ready.acquire();
        count++;
        if (count == 3)
            System.out.println("The molecule is formed");
        lock.release();
        initH.release();
    }

    public void oxygen() throws InterruptedException {
        initO.acquire();
        oHere.release(2);
        hHere.acquire(2);
        ready.release(2);
        lock.acquire();
        count++;
        if (count == 3)
            System.out.println("The molecule is formed");
        lock.release();
        initO.release();
    }
}

class H2OThread extends Thread {

    H2OMachine molecule;
    String atom;

    public H2OThread(H2OMachine molecule, String atom) {
        this.molecule = molecule;
        this.atom = atom;
    }

    public void run() {
        if ("H".equals(atom)) {
            try {
                molecule.hydrogen();
            } catch (Exception e) {
            }
        } else if ("O".equals(atom)) {
            try {
                molecule.oxygen();
            } catch (Exception e) {
            }
        }
    }
}

public class H2O {
    public static void main(String[] args) {

        // TODO: 3/29/20 Simulate with multiple scenarios 
        H2OMachine molecule = new H2OMachine();

        Thread t1 = new H2OThread(molecule, "H");
        Thread t2 = new H2OThread(molecule, "O");
        Thread t3 = new H2OThread(molecule, "H");
        Thread t4 = new H2OThread(molecule, "O");

        t2.start();
        t1.start();
        t4.start();
        t3.start();
    }
}