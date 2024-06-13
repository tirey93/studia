module org.zpo.sockets_server {
    requires javafx.controls;
    requires javafx.fxml;

    requires org.kordamp.bootstrapfx.core;

    opens org.zpo.sockets_server to javafx.fxml;
    exports org.zpo.sockets_server;
}