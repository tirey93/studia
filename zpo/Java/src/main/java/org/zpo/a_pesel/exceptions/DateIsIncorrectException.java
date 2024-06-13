package org.zpo.a_pesel.exceptions;

public class DateIsIncorrectException extends  PeselException{
    public DateIsIncorrectException() {
        super("Pesel ma niewłaściwą datę.");
    }
}
