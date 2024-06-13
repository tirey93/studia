package org.zpo.threads;

import javafx.application.Application;
import javafx.application.Platform;
import javafx.stage.Stage;

import java.util.concurrent.*;

public class Main extends Application {
    private static final int NUM_PRODUCERS = 3;

    public  static BlockingQueue<Character> queue = new LinkedBlockingQueue<>(1);
    public static Semaphore semaphore = new Semaphore(1);

    public static void main(String[] args) {
        launch(args);
    }

    @Override
    public void start(Stage primaryStage) {
        run();
    }

    private void run() {
        String[] filenames = {"plik1.txt", "plik2.txt", "plik3.txt"};
        int y = 250;
        int x = 250;
        int frameWidth = 350;

        CompletableFuture[] futures = new CompletableFuture[NUM_PRODUCERS];

        for (int i = 0; i < filenames.length; i++) {
            ReaderThread readerThread = new ReaderThread(filenames[i], x, y);
            futures[i] = CompletableFuture.runAsync(readerThread::run);
            x += frameWidth;
        }

        WriterThread consumer = new WriterThread("wynik.txt");
        consumer.start();

        CompletableFuture.allOf(futures).thenRun(() -> {
            consumer.setFinish();
            try {
                consumer.join();
            } catch (InterruptedException e) {
                System.out.println(e.getMessage());
            } finally {
                Platform.exit();
            }
        });
    }
}