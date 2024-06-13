package org.zpo.threads;

import java.io.*;

public class WriterThread extends AbstractThread {
    private volatile boolean finish = false;

    public WriterThread(String filename) {
        super(filename, 600, 600);
    }

    public void setFinish() {
        this.finish = true;
    }

    @Override
    public void run() {
        try (BufferedWriter writer = new BufferedWriter(new FileWriter(filename))) {
            while (!finish) {
                char c = Main.queue.take();
                writer.write(c);
                appendTextToUI(c);
                this.delay();
            }
        } catch (IOException | InterruptedException e) {
            e.printStackTrace();
        }
    }
}
