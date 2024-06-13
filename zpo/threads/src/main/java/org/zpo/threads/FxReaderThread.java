package org.zpo.threads;

import java.io.*;

public class FxReaderThread extends FxThread {
    private ReadMode mode;

    public FxReaderThread(String filename, SafeBuffer buffer, double x, double y, ReadMode mode) {
        super(filename, buffer, x, y);
        this.mode = mode;
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
                buffer.write((char) ch);
                appendTextToUI((char) ch);
                this.delay();
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
                        buffer.write(ch);
                        appendTextToUI(ch);
                        this.delay();
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
                    buffer.write(ch);
                    appendTextToUI(ch);
                    this.delay();
                }

                buffer.releaseWritingPriority();
            }

        } catch (IOException | InterruptedException e) {
            e.printStackTrace();
        }
    }
}