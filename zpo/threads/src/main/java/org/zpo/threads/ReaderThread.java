package org.zpo.threads;

import java.io.*;

public class ReaderThread extends AbstractThread {
    private ReadMode mode = ReadMode.LINE;

    public ReaderThread(String filename, SafeBuffer buffer, double x, double y) {
        super(filename, buffer, x, y);
    }

    @Override
    public void run() {
        try {
            Thread.sleep(2000);
        } catch (InterruptedException e) {
            e.printStackTrace();
        }

        switch (mode) {
           case CHARACTER -> characterMode();
           case WORD -> wordMode();
           case LINE -> lineMode();
       }
    }

    private void characterMode() {
        try (BufferedReader reader = new BufferedReader(new FileReader(filename))) {
            int ch;

            while ((ch = reader.read()) != -1) {
                writeChar((char) ch);
            }

        } catch (IOException | InterruptedException e) {
            e.printStackTrace();
        }
    }

    private void wordMode() {
        try (BufferedReader reader = new BufferedReader(new FileReader(filename))) {
            String line;

            while ((line = reader.readLine()) != null) {
                String[] words = line.concat("\n").split(" ");

                for (String word : words) {
                    word = word.concat(" ");
                    buffer.acquireWritingPriority();

                    for (char ch : word.toCharArray()) {
                        writeChar(ch);
                    }

                    buffer.releaseWritingPriority();
                }
            }

        } catch (IOException | InterruptedException e) {
            e.printStackTrace();
        }
    }

    private void lineMode() {
        try (BufferedReader reader = new BufferedReader(new FileReader(filename))) {
            String line;

            while ((line = reader.readLine()) != null) {
                line = line.concat("\n");
                buffer.acquireWritingPriority();

                for (char ch : line.toCharArray()) {
                    writeChar(ch);
                }

                buffer.releaseWritingPriority();
            }

        } catch (IOException | InterruptedException e) {
            e.printStackTrace();
        }
    }

    private void writeChar(char ch) throws InterruptedException {
        buffer.write(ch);
        appendTextToUI(ch);
        this.delay();
    }
}