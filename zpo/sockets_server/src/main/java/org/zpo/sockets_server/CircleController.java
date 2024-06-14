package org.zpo.sockets_server;

import javafx.application.Platform;
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

    public void initialize() {
        var multiplier = pane.getPrefHeight() / 2 / 100;
        server = new Server(circle, label, multiplier);
    }
    public void connect(ActionEvent actionEvent) {
        if (isConnected) {
            handleDisconnect();
        }
        else {

            handleConnect();
        }
    }

    private void handleDisconnect() {
        try {
            server.stop();
        } catch (IOException e) {
            throw new RuntimeException(e);
        }
        connect.setText("Uruchom");
        label.setText("Serwer nie działa.");
        isConnected = !isConnected;
    }

    private void handleConnect() {
        try {
            server.start(6666);
            Thread t = new Thread(server);
            t.start();
        } catch (IOException e) {
            throw new RuntimeException(e);
        }
        connect.setText("Wyłącz");
        label.setText("Serwer działa.");
        isConnected = !isConnected;
    }
}