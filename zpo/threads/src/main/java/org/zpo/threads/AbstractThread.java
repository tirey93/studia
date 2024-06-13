package org.zpo.threads;

import javafx.application.Platform;
import javafx.scene.Scene;
import javafx.scene.control.TextArea;
import javafx.stage.Stage;

public abstract class AbstractThread extends Thread {
    protected String filename;
    protected SafeBuffer buffer;
    protected TextArea textArea;
    protected double x;
    protected double y;
    protected Stage stage;

    protected AbstractThread(String filename, SafeBuffer buffer, double x, double y) {
        this.filename = filename;
        this.buffer = buffer;
        this.x = x;
        this.y = y;
        Platform.runLater(this::createAndShowGUI);
    }

    private void createAndShowGUI() {
        stage = new Stage();
        textArea = new TextArea();
        Scene scene = new Scene(textArea, 300, 250);
        stage.setTitle(filename);
        stage.setScene(scene);
        stage.setX(x);
        stage.setY(y);
        stage.show();
    }

     protected void delay() throws InterruptedException {
        Thread.sleep(50);
    }

    protected void appendTextToUI(char ch) {
        Platform.runLater(() -> textArea.appendText(Character.toString(ch)));
    }
}
