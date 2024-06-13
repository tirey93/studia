package org.zpo.threads;

import java.util.concurrent.Semaphore;

public class SafeBuffer {
    private final Semaphore writePriorityLock;
    private final Semaphore bufferReadLock;
    private final Semaphore bufferWriteLock;
    private volatile char c;

    public SafeBuffer() {
        bufferReadLock = new Semaphore(0);
        bufferWriteLock = new Semaphore(1);
        writePriorityLock = new Semaphore(1);
    }

    public char read() throws InterruptedException {
        bufferReadLock.acquire();
        System.out.println("Locked read.");
        char res = c;
        bufferWriteLock.release();
        System.out.println("Unlocked write.");
        return res;
    }

    public void write(char value) throws InterruptedException {
        bufferWriteLock.acquire();
        System.out.println("Locked write.");
        c = value;
        bufferReadLock.release();
        System.out.println("Unlocked read.");
    }

    public void acquireWritingPriority() throws InterruptedException {
        writePriorityLock.acquire();
        System.out.println("Locked priority.");
    }

    public void releaseWritingPriority() {
        writePriorityLock.release();
        System.out.println("Unlocked priority.");
    }
}
