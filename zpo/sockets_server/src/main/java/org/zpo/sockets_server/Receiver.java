package org.zpo.sockets_server;

import javafx.scene.shape.Circle;

import java.io.IOException;

public class Receiver implements Runnable{

    private final Server server;
    private final Circle circle;

    public Receiver(Server server, Circle circle) {
        this.server = server;
        this.circle = circle;
    }

    @Override
    public void run() {
        String received;
        while (true){
            try {
                received = server.in.readLine();
                System.out.println(received);
                double r = Double.parseDouble(received);
                circle.setRadius(r*1.75);
            } catch (IOException e) {
                throw new RuntimeException(e);
            }
        }
    }
}
