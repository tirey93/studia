module org.zpo.sockets_client {
    requires javafx.controls;
    requires javafx.fxml;

    requires org.kordamp.bootstrapfx.core;

    opens org.zpo.sockets_client to javafx.fxml;
    exports org.zpo.sockets_client;
}