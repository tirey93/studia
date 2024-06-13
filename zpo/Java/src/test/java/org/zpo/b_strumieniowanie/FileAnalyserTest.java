package org.zpo.b_strumieniowanie;

import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.*;

import java.io.IOException;
import java.util.HashMap;
import java.util.Map;

public class FileAnalyserTest {
    @Test
    public void testCount() throws IOException {
        String filePath = "english.200MB.txt";
        int countBeforeFiltering = FileAnalyser.countWords(filePath);

        assertEquals(countBeforeFiltering, 39177225);
    }

    @Test
    public void testCountAfterFiltering() throws IOException {
        String filePath = "english.200MB.txt";
        int k = 100;

        Map<String, Integer> D1 = new HashMap<>();
        Map<String, Integer> D2 = new HashMap<>();

        int wordsCount = FileAnalyser.processSecondPass(FileAnalyser.standarizeFile(filePath), D1, D2);

        assertEquals(wordsCount, 29250532 );
    }

    @Test
    public void testMisraGries() throws IOException {
        String filePath = "english.200MB.txt";
        int k = 100;

        Map<String, Integer> D1 = new HashMap<>();
        Map<String, Integer> D2 = new HashMap<>();

        FileAnalyser.processFirstPass(FileAnalyser.standarizeFile(filePath), D1, k);
        FileAnalyser.processSecondPass(FileAnalyser.standarizeFile(filePath), D1, D2);

        assertEquals(D2.get("the"), 2427360);
        assertEquals(D2.get("and"), 1323210);
        assertEquals(D2.get("that"), 457507);
        assertEquals(D2.get("was"), 405046);
        assertEquals(D2.get("his"), 364337);
        assertEquals(D2.get("with"), 313077);
    }
}
