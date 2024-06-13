module org.zpo.threads {
    requires javafx.controls;
    requires javafx.fxml;

    requires org.kordamp.bootstrapfx.core;

    opens org.zpo.threads to javafx.fxml;
    exports org.zpo.threads;
}