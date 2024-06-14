package org.zpo.sockets_client;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.net.Socket;

public class Client {
    private Socket clientSocket;
    private PrintWriter out;

    public void startConnection(String ip, int port) throws IOException {
        clientSocket = new Socket(ip, port);
        out = new PrintWriter(clientSocket.getOutputStream(), true);
    }

    public void sendMessage(String msg) throws IOException {
        if(out != null)
            out.println(msg);
    }

    public void stopConnection() throws IOException {
        out.close();
        clientSocket.close();
    }
}
