package org.zpo.sockets_client;

import javafx.application.Application;
import javafx.fxml.FXMLLoader;
import javafx.geometry.Rectangle2D;
import javafx.scene.Scene;
import javafx.stage.Screen;
import javafx.stage.Stage;

import java.io.IOException;

public class CircleApplication extends Application {
    @Override
    public void start(Stage stage) throws IOException {
        FXMLLoader fxmlLoader = new FXMLLoader(CircleApplication.class.getResource("circle-view.fxml"));
        Scene scene = new Scene(fxmlLoader.load(), 600, 400);
        stage.setTitle("Kółko - Klient");
        stage.setResizable(false);
        stage.setScene(scene);
        Rectangle2D primScreenBounds = Screen.getPrimary().getVisualBounds();
        stage.setX(((primScreenBounds.getWidth() - scene.getWidth()) / 2) - 320);
        stage.setY(((primScreenBounds.getHeight() - scene.getHeight()) / 2));
        stage.show();
    }

    public static void main(String[] args) {
        launch();
    }
}