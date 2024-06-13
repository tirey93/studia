package org.zpo.a_pesel;

import org.zpo.a_pesel.exceptions.*;

import java.time.LocalDate;
import java.time.format.DateTimeFormatter;
import java.time.format.DateTimeParseException;

public class PeselChecker {
    private final int[] peselArray = new int[11];

    public PeselChecker(String pesel) throws PeselException {
        if (pesel == null){
            throw new NotEnterException();
        }
        if (pesel.length() != 11){
            throw new IncorrectLengthException();
        }

        int i = 0;
        for (char c : pesel.toCharArray()){
            try {
                peselArray[i] = Integer.parseInt(String.valueOf(c));
            }
            catch (NumberFormatException e){
                throw new NotOnlyNumbersException();
            }
            i++;
        }
    }

    public String getGender() {
        if (peselArray[9] % 2 == 1) {
            return "M";
        }
        return "K";
    }

    public boolean checkSum() {
        int sum = peselArray[0] +
                3 * peselArray[1] +
                7 * peselArray[2] +
                9 * peselArray[3] +
                1 * peselArray[4] +
                3 * peselArray[5] +
                7 * peselArray[6] +
                9 * peselArray[7] +
                1 * peselArray[8] +
                3 * peselArray[9];
        sum %= 10;
        sum = 10 - sum;
        sum %= 10;

        return sum == peselArray[10];
    }

    public LocalDate getDate() throws PeselException {
        DateTimeFormatter formatter = DateTimeFormatter.ofPattern("dd-MM-yyyy");
        int year = getBirthYear();
        int month = getBirthMonth();
        int day = getBirthDay();
        try{
        return LocalDate.parse(String.format("%02d-%02d-%d", day, month, year), formatter);
        }
        catch (DateTimeParseException e){
            throw new DateIsIncorrectException();
        }
    }

    private int getBirthYear() {
        int year;
        int month;
        year = 10 * peselArray[0];
        year += peselArray[1];
        month = 10 * peselArray[2];
        month += peselArray[3];
        if (month > 80 && month < 93) {
            year += 1800;
        }
        else if (month > 0 && month < 13) {
            year += 1900;
        }
        else if (month > 20 && month < 33) {
            year += 2000;
        }
        else if (month > 40 && month < 53) {
            year += 2100;
        }
        else if (month > 60 && month < 73) {
            year += 2200;
        }
        return year;
    }

    private int getBirthMonth() {
        int month;
        month = 10 * peselArray[2];
        month += peselArray[3];
        if (month > 80 && month < 93) {
            month -= 80;
        }
        else if (month > 20 && month < 33) {
            month -= 20;
        }
        else if (month > 40 && month < 53) {
            month -= 40;
        }
        else if (month > 60 && month < 73) {
            month -= 60;
        }
        return month;
    }

    private int getBirthDay() {
        int day;
        day = 10 * peselArray[4];
        day += peselArray[5];
        return day;
    }
}
