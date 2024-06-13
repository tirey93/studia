package org.zpo.a_pesel;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvFileSource;
import org.junit.jupiter.params.provider.CsvSource;
import org.junit.jupiter.params.provider.ValueSource;
import org.zpo.a_pesel.exceptions.PeselException;

import java.time.LocalDate;
import java.time.format.DateTimeFormatter;

import static org.junit.jupiter.api.Assertions.*;

class PeselCheckerTest {

    @ParameterizedTest
    @CsvFileSource(resources = "/getgender.csv",numLinesToSkip = 1)
    void getGender(String pesel, String gender) throws PeselException {
        PeselChecker peselChecker = new PeselChecker(pesel);
        assertEquals(gender, peselChecker.getGender());
    }

    @ParameterizedTest
    @CsvFileSource(resources = "/checksum.csv",numLinesToSkip = 1)
    void checkSum(String pesel, boolean correctSum) throws PeselException {
        PeselChecker peselChecker = new PeselChecker(pesel);
        assertEquals(correctSum, peselChecker.checkSum());
    }


    @ParameterizedTest
    @CsvFileSource(resources = "/getdate.csv",numLinesToSkip = 1)
    void getDate(String pesel, String dateStr) throws PeselException {
        PeselChecker peselChecker = new PeselChecker(pesel);
        DateTimeFormatter formatter = DateTimeFormatter.ofPattern("yyyy-MM-dd");

        assertEquals(LocalDate.parse(dateStr, formatter), peselChecker.getDate());
    }
}