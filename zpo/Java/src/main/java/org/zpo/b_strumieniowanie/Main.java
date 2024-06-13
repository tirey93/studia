package org.zpo.b_strumieniowanie;

import java.io.IOException;
import java.util.*;


public class Main {
    public static void main(String[] args) {
        String filePath = "english.200MB.txt";
        int k = 100;

        try {
            long startTime = System.currentTimeMillis();

            Map<String, Integer> D1 = new HashMap<>();
            Map<String, Integer> D2 = new HashMap<>();

            FileAnalyser.processFirstPass(FileAnalyser.standarizeFile(filePath), D1, k);
            int wordsCount = FileAnalyser.processSecondPass(FileAnalyser.standarizeFile(filePath), D1, D2);

            long executionTime = System.currentTimeMillis() - startTime;

            D2.entrySet().stream()
                    .filter(entry -> entry.getValue() > wordsCount / k)
                    .sorted((e1, e2) -> e2.getValue().compareTo(e1.getValue()))
                    .forEach(entry -> System.out.println(entry.getKey() + ": " + entry.getValue()));
            System.out.println("Execution time: " + executionTime / 1000.0);
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}