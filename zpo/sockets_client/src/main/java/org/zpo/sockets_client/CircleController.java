package org.zpo.sockets_client;

import javafx.event.ActionEvent;
import javafx.fxml.FXML;
import javafx.scene.control.Label;
import javafx.scene.control.Slider;
import javafx.scene.input.MouseEvent;
import javafx.scene.layout.Pane;
import javafx.scene.shape.Circle;

public class CircleController {
    @FXML
    public Slider slider;
    @FXML
    public Circle circle;
    @FXML
    public Pane pane;
    @FXML
    public Label label;

    private int maxRadius;

    public void initialize() {
        maxRadius = (int)pane.getPrefHeight()/2;
    }

    public void onSliderChanged(MouseEvent mouseEvent) {
        circle.setRadius(maxRadius*slider.getValue()/slider.getMax());
    }

    public void connect(ActionEvent actionEvent) {

    }
}