package org.zpo.a_pesel.exceptions;

public class NotOnlyNumbersException extends PeselException{

    public NotOnlyNumbersException() {
        super("Pesel musi zawierać wyłącznie cyfry.");
    }
}
