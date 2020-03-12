import java.io.File;
import java.io.FileNotFoundException;
import java.util.Objects;
import java.util.Scanner;
import java.util.concurrent.TimeUnit;

public class JpgOrPng {

    private static void printFiles(File[] files) {
        long weekAgo = System.currentTimeMillis() - TimeUnit.DAYS.toMillis(7);
        for (File file : files) {
            if (file.isDirectory() && file.length() > 0)
                printFiles(Objects.requireNonNull(file.listFiles()));
            else if (file.lastModified() >= weekAgo && (file.getName().endsWith(".jpg") || file.getName().endsWith(".bmp")))
                System.out.println(file.getAbsolutePath());
        }
    }

    public static void main(String[] args) throws FileNotFoundException {
        Scanner input = new Scanner(System.in);
        String filePath = input.nextLine();

        File directory = new File(filePath);
        if (!directory.exists() || !directory.isDirectory()) {
            throw new FileNotFoundException();
        }
        File[] files = directory.listFiles();
        if (files == null)
            throw new FileNotFoundException();
        printFiles(files);
    }
}
