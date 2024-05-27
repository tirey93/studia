package org.zpo.b_strumieniowanie;

import java.io.IOException;
import java.nio.charset.StandardCharsets;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.*;
import java.util.concurrent.atomic.AtomicInteger;
import java.util.stream.Stream;

public class FileAnalyser {
    public static Stream<String> standarizeFile(String fn) throws IOException {
        return Files
                .lines(Paths.get(fn), StandardCharsets.UTF_8)
                .map(String::toLowerCase)
                .map(s -> s.replaceAll("[^a-z]+", " "))
                .flatMap(l -> Arrays.stream(l.split(" ")))
                .filter(w -> w.length() >= 3);
    }

    public static int countWords(String fn) throws IOException {
        Stream<String> lines = Files.lines(Paths.get(fn), StandardCharsets.UTF_8);
        int totalWords = 0;

        for (String line : (Iterable<String>) lines::iterator) {
            totalWords += line.split(" ").length;
        }

        return totalWords;
    }

    public static void processFirstPass(Stream<String> wordsStream, Map<String, Integer> D1, int k) {
        wordsStream.forEach(word -> {
            if (D1.size() < k - 1) {
                D1.put(word, D1.getOrDefault(word, 0) + 1);
            } else {
                if (D1.containsKey(word)) {
                    D1.put(word, D1.get(word) + 1);
                } else {
                    Iterator<Map.Entry<String, Integer>> iterator = D1.entrySet().iterator();
                    while (iterator.hasNext()) {
                        Map.Entry<String, Integer> entry = iterator.next();
                        entry.setValue(entry.getValue() - 1);
                        if (entry.getValue() == 0) {
                            iterator.remove();
                        }
                    }
                }
            }
        });
    }

    public static int processSecondPass(Stream<String> wordsStream, Map<String, Integer> D1, Map<String, Integer> D2) {
        AtomicInteger wordsCount = new AtomicInteger(0);

        wordsStream.peek(word -> wordsCount.incrementAndGet())
                .filter(D1::containsKey)
                .forEach(word -> D2.put(word, D2.getOrDefault(word, 0) + 1));

        return wordsCount.get();
    }
}
