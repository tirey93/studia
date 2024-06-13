package org.zpo.a_pesel.exceptions;

public abstract class PeselException extends  Exception{
    public PeselException(String message) {
        super(message);
    }
}
