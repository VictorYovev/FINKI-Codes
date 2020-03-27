import java.util.concurrent.Semaphore;


class BlockingQueue<T> {

    T[] contents;
    int capacity;
    int index;
    Semaphore queueEmpty;
    Semaphore queueLock;

    public BlockingQueue(int capacity) {
        contents = (T[]) new Object[capacity];
        this.capacity = capacity;
        index = 0;
        queueEmpty = new Semaphore(1);
        queueLock = new Semaphore(1);

    }

    public void enqueue(T item) throws InterruptedException {
        queueEmpty.acquire();
        queueLock.acquire();
        if (index < capacity) {
            contents[index++] = item;
            System.out.println("You add " + item + " to queue");
        }
        queueLock.release();


    }

    public T dequeue() throws InterruptedException {
        queueLock.acquire();
        T item = null;
        if (index != 0) {
            T[] newContents = (T[]) new Object[capacity];
            if (index - 1 >= 0)
                System.arraycopy(contents, 1, newContents, 0, index - 1);
            item = contents[0];
            index--;
            contents = newContents; //wrong?
        }
        if (item != null)
            System.out.println("You remove " + item + " from queue");
        queueEmpty.release();
        queueLock.release();
        return item;
    }
}

class ThreadEnqueue implements Runnable {

    BlockingQueue<Integer> queue;

    public ThreadEnqueue(BlockingQueue<Integer> queue) {
        this.queue = queue;
    }

    @Override
    public void run() {

        for (int i = 0; i < 100; i++) {
            try {
                queue.enqueue(i);
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        }
    }
}

class ThreadDequeue implements Runnable {

    BlockingQueue<Integer> queue;

    public ThreadDequeue(BlockingQueue<Integer> queue) {
        this.queue = queue;
    }

    @Override
    public void run() {

        for (int i = 0; i < 100; i++) {
            try {
                queue.dequeue();
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        }
    }
}

public class BlockQueue {

    public static void main(String[] args) throws InterruptedException {
        BlockingQueue<Integer> caton = new BlockingQueue<>(7);
        Thread thread1 = new Thread(new ThreadEnqueue(caton));
        Thread thread2 = new Thread(new ThreadDequeue(caton));

        thread1.start();
        thread2.start();

        thread1.join();
        thread2.join();

    }
}