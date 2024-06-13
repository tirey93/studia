package org.zpo.threads;

import java.io.*;

public class FxWriterThread extends FxThread {
    private volatile boolean done = false;

    public FxWriterThread(String filename, SafeBuffer buffer, double x, double y) {
        super(filename, buffer, x, y);
    }

    public void setDone() {
        this.done = true;
    }

    @Override
    public void run() {
        try (BufferedWriter writer = new BufferedWriter(new FileWriter(filename))) {
            while (!done) {
                char ch = buffer.read();
                writer.write(ch);
                appendTextToUI(ch);
                this.delay();
            }
        } catch (IOException | InterruptedException e) {
            e.printStackTrace();
        }
    }
}
