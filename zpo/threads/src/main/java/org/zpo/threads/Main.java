package org.zpo.threads;

import javafx.application.Application;
import javafx.application.Platform;
import javafx.stage.Stage;

import java.util.concurrent.*;

public class Main extends Application {
    private static final int NUM_PRODUCERS = 3;
    private static final SafeBuffer buffer = new SafeBuffer();

    public static void main(String[] args) {
        launch(args);
    }

    @Override
    public void start(Stage primaryStage) {
        run(ReadMode.LINE);
    }

    private void run(ReadMode mode) {
        String[] filenames = {"plik1.txt", "plik2.txt", "plik3.txt"};
        int y = 100;
        int x = 100;
        int frameWidth = 410;

        CompletableFuture[] futures = new CompletableFuture[NUM_PRODUCERS];

        for (int i = 0; i < filenames.length; i++) {
            FxReaderThread readerThread = new FxReaderThread(filenames[i], buffer, x, y, mode);
            futures[i] = CompletableFuture.runAsync(readerThread::run);

            x += frameWidth;
        }

        FxWriterThread consumer = new FxWriterThread("wynik.txt", buffer, 510, 450);
        consumer.start();

        CompletableFuture.allOf(futures).thenRun(() -> {
            consumer.setDone();

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