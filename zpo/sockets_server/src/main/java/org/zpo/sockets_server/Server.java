package org.zpo.sockets_server;

import javafx.scene.control.Label;
import javafx.scene.shape.Circle;

import java.io.*;
import java.net.ServerSocket;
import java.net.Socket;

public class Server implements  Runnable {
    private ServerSocket serverSocket;
    private Socket clientSocket;
    private BufferedReader in;

    private final Circle circle;
    public final Label label;
    private final double multiplier;

    public Server(Circle circle, Label label, double multiplier) {
        this.circle = circle;
        this.label = label;
        this.multiplier = multiplier;
    }


    public void start(int port) throws IOException {
        serverSocket = new ServerSocket(port);
        clientSocket = serverSocket.accept();
        in = new BufferedReader(new InputStreamReader(clientSocket.getInputStream()));
    }

    public void stop() throws IOException {
        in.close();
        clientSocket.close();
        serverSocket.close();
    }

    @Override
    public void run() {
        String received;
        while (true){
            try {
                received = in.readLine();
                System.out.println(received);
                double r = Double.parseDouble(received);
                circle.setRadius(r*multiplier);
            } catch (IOException e) {
                throw new RuntimeException(e);
            }
        }
    }
}
