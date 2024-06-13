package org.zpo.threads;

import javafx.application.Platform;
import javafx.scene.Scene;
import javafx.scene.control.TextArea;
import javafx.stage.Stage;

public abstract class FxThread extends Thread {
    protected String filename;
    protected SafeBuffer buffer;
    protected TextArea textArea;
    protected double x;
    protected double y;
    protected Stage stage;

    protected FxThread(String filename, SafeBuffer buffer, double x, double y) {
        this.filename = filename;
        this.buffer = buffer;
        this.x = x;
        this.y = y;
        Platform.runLater(this::createAndShowGUI);
    }

    private void createAndShowGUI() {
        stage = new Stage();
        textArea = new TextArea();
        textArea.setEditable(false);
        Scene scene = new Scene(textArea, 400, 300);
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
