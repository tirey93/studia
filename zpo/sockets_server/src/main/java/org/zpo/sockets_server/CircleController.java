package org.zpo.sockets_server;

import javafx.event.ActionEvent;
import javafx.fxml.FXML;
import javafx.scene.control.CheckMenuItem;
import javafx.scene.control.Label;
import javafx.scene.control.Slider;
import javafx.scene.input.MouseEvent;
import javafx.scene.layout.Pane;
import javafx.scene.shape.Circle;

import java.io.IOException;

public class CircleController {
    @FXML
    public Circle circle;
    @FXML
    public Pane pane;
    @FXML
    public Label label;
    public CheckMenuItem connect;

    private boolean isConnected;
    Server server;
    Receiver receiver;

    public void initialize() {
        server = new Server();
    }
    public void connect(ActionEvent actionEvent) {
        if (isConnected) {
            handleDisconnect();
        }
        else {

            handleConnect();
        }
        isConnected = !isConnected;
    }

    private void handleDisconnect() {
        try {
            server.stop();
        } catch (IOException e) {
            throw new RuntimeException(e);
        }
        connect.setText("Uruchom");
    }

    private void handleConnect() {
        try {
            server.start(6666);
            receiver = new Receiver(server, circle);
            Thread t = new Thread(receiver);
            t.start();
        } catch (IOException e) {
            throw new RuntimeException(e);
        }
        connect.setText("Wyłącz");
    }
}