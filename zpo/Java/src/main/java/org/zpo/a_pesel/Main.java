package org.zpo.a_pesel;

import org.zpo.a_pesel.exceptions.PeselException;

//TIP To <b>Run</b> code, press <shortcut actionId="Run"/> or
// click the <icon src="AllIcons.Actions.Execute"/> icon in the gutter.
public class Main {
    public static void main(String[] args) {
        try{
            PeselChecker checker = new PeselChecker(args[0]);
            if(checker.checkSum()){
                System.out.println("Płeć to: " + checker.getGender());
                System.out.println("Data urodzenia to: " + checker.getDate());
                System.out.println("Pesel jest poprawny.");
            }
            else {
                System.out.println("Pesel jest nie poprawny.");
            }
        }
        catch (PeselException e){
            System.out.println("Błąd: " + e.getMessage());
        }
    }
}