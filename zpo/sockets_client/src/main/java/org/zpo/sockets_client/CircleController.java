package org.zpo.sockets_client;

import javafx.event.ActionEvent;
import javafx.fxml.FXML;
import javafx.scene.control.CheckMenuItem;
import javafx.scene.control.Label;
import javafx.scene.control.Slider;
import javafx.scene.input.MouseEvent;
import javafx.scene.layout.Pane;
import javafx.scene.shape.Circle;

import java.io.IOException;
import java.net.ServerSocket;

public class CircleController {
    @FXML
    public Slider slider;
    @FXML
    public Circle circle;
    @FXML
    public Pane pane;
    @FXML
    public Label label;
    @FXML
    public CheckMenuItem connect;

    private boolean isConnectedToServer;

    private int maxRadius;

    private Client client;

    public void initialize() {
        maxRadius = (int)pane.getPrefHeight()/2;
        client = new Client();
    }

    public void onSliderChanged(MouseEvent mouseEvent) throws IOException {
        circle.setRadius(maxRadius*slider.getValue()/slider.getMax());
        client.sendMessage(String.valueOf(slider.getValue()));
    }

    public void connect(ActionEvent actionEvent) {
        if (isConnectedToServer) {
            handleDisconnect();
        }
        else {

            handleConnect();
        }
        isConnectedToServer = !isConnectedToServer;
    }

    private void handleDisconnect() {
        try {
            client.stopConnection();
        } catch (IOException e) {
            throw new RuntimeException(e);
        }
        connect.setText("Połącz");
    }

    private void handleConnect() {
        try {
            client.startConnection("127.0.0.1", 6666);
        } catch (IOException e) {
            throw new RuntimeException(e);
        }

        connect.setText("Rozłącz");
    }
}