import java.io.File;
import java.io.FileNotFoundException;
import java.util.Objects;
import java.util.Scanner;

public class LargestFile {
    private static File largestFile = null;

    private static void findLargestFile(File[] files) {
        for (File file : files) {
            if (largestFile == null && !file.isDirectory())
                largestFile = file;

            if (file.isDirectory())
                findLargestFile(Objects.requireNonNull(file.listFiles()));
            else if (largestFile.length() < file.length())
                largestFile = file;
        }
    }

    public static void main(String[] args) throws FileNotFoundException {
        Scanner in = new Scanner(System.in);
        String filePath = in.nextLine();

        File directory = new File(filePath);
        if (!directory.exists() || !directory.isDirectory()) {
            throw new FileNotFoundException();
        }
        File[] files = directory.listFiles();
        if (files == null)
            throw new FileNotFoundException();

        findLargestFile(files);
        long begin = System.currentTimeMillis();
        System.out.println(largestFile.getAbsolutePath());
        System.out.println("Length of file: ~" + Math.ceil(largestFile.length() * 0.00000125) + "MB");
        long end = System.currentTimeMillis();
        System.out.println("Found in: " + (end - begin) / 1000.0 + " seconds");
    }
}
