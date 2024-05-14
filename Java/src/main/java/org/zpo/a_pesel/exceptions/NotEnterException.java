package org.zpo.a_pesel.exceptions;

import org.zpo.a_pesel.PeselChecker;

public class NotEnterException extends PeselException {
    public NotEnterException() throws PeselException {
        super("Pesel musi zostać podany.");
    }
}
