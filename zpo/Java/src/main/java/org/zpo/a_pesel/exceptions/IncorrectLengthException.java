package org.zpo.a_pesel.exceptions;

public class IncorrectLengthException extends  PeselException{
    public IncorrectLengthException() {
        super("Pesel musi mieć dokładnie 11 znaków.");
    }
}
