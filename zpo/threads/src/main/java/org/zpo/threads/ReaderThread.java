package org.zpo.threads;

import java.io.*;

public class ReaderThread extends AbstractThread {
    private ReadMode mode = ReadMode.CHARACTER;

    public ReaderThread(String filename, double x, double y) {
        super(filename, x, y);
    }

    @Override
    public void run() {
        switch (mode) {
           case CHARACTER -> characterMode();
           case WORD -> wordMode();
           case LINE -> lineMode();
       }
    }

    private void characterMode() {
        try (BufferedReader reader = new BufferedReader(new FileReader(filename))) {
            int c;

            while ((c = reader.read()) != -1) {
                writeChar((char) c);
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
                    Main.semaphore.acquire();
                    word = word.concat(" ");
                    for (char c : word.toCharArray()) {
                        writeChar(c);
                    }
                    Main.semaphore.release();
                    this.delay();
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
                Main.semaphore.acquire();
                for (char c : line.toCharArray()) {
                    writeChar(c);
                }
                Main.semaphore.release();
                this.delay();
            }

        } catch (IOException | InterruptedException e) {
            e.printStackTrace();
        }
    }

    private void writeChar(char c) throws InterruptedException {
        Main.queue.put(c);
        appendTextToUI(c);
    }
}