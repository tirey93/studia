package org.zpo.sockets_server;

import javafx.application.Platform;
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
    }

    public void stop() throws IOException {
        if(clientSocket != null)
            clientSocket.close();
        if(in != null)
            in.close();
        serverSocket.close();
    }

    @Override
    public void run() {
        while (true){
            try {
                clientSocket = serverSocket.accept();
                Platform.runLater(() -> label.setText("Serwer działa. Klient podłączony."));
                String received;
                while (true){
                    InputStream inputStream = clientSocket.getInputStream();
                    in = new BufferedReader(new InputStreamReader(inputStream));
                    received = in.readLine();
                    if(received == null) {
                        Platform.runLater(() -> label.setText("Serwer działa."));
                        break;
                    }

                    System.out.println(received);
                    double r = Double.parseDouble(received);
                    circle.setRadius(r*multiplier);
                }
            } catch (IOException e) {
                break;
            }
        }
    }
}
