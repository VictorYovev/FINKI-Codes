import java.io.*;
import java.nio.file.Paths;

public class Vowels {
    private static int countVowels(char[] array) {
        int counter = 0;
        for (char c : array) {
            switch (c) {
                case 'А':
                case 'а':
                case 'Е':
                case 'е':
                case 'И':
                case 'и':
                case 'О':
                case 'о':
                case 'У':
                case 'у':
                    counter++;
                    break;
            }
        }
        return counter;
    }

    public static void main(String[] args) throws IOException {

        BufferedReader in = new BufferedReader(new InputStreamReader(new FileInputStream(Paths.get(".") + "/izvor")));
        BufferedWriter out = new BufferedWriter(new OutputStreamWriter(new FileOutputStream(Paths.get(".") + "/destinacija")));

        String line;
        while ((line = in.readLine()) != null) {
            out.write(String.valueOf(countVowels(line.toCharArray())) + '\n');
        }
        in.close();
        out.flush();
        out.close();

    }
}
