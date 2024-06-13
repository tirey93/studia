package org.zpo.sockets_client;

import javafx.event.ActionEvent;
import javafx.fxml.FXML;
import javafx.scene.control.Label;
import javafx.scene.control.Slider;
import javafx.scene.input.MouseEvent;
import javafx.scene.layout.Pane;
import javafx.scene.shape.Circle;

public class HelloController {
    @FXML
    public Slider slider;
    @FXML
    public Circle circle;
    @FXML
    public Pane pane;

    private int maxRadius;

    public void initialize() {
        maxRadius = (int)pane.getPrefHeight()/2;
    }

    public void onSliderChanged(MouseEvent mouseEvent) {
        circle.setRadius(maxRadius*slider.getValue()/slider.getMax());
        System.out.println(slider.getValue());
    }

    public void connect(ActionEvent actionEvent) {

    }
}