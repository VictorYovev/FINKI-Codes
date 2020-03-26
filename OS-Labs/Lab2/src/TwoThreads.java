import java.util.Arrays;

//Првото извршување на код нема да можеме да го предвидиме, тие се две инстанци од две различни класи Thread1, Thread2.
//По модифицирањето останува исто, односно кодот е следниов:
public class TwoThreads {
    public static class ThreadAB implements Runnable {
        Object [] objects;
        public ThreadAB(Object[] objects){
           this.objects = objects.clone();
        }
        @Override
        public void run() {
            Arrays.stream(objects).forEach(System.out::println);
        }
    }
    public static void main(String[] args) {
        Integer [] numbers = {1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26};
        Character [] letters = {'A','B','C','D','E','F','G','H','I','J','K','L','M','O','P','Q','R','S','T','U','V','W','X','Y','Z'};
        new Thread(new ThreadAB(numbers)).start();
        new Thread(new ThreadAB(letters)).start();
    }

}