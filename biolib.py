class BioLib:
    def pattern_count(self, text: str, pattern: str):
        count = 0
        for i in range(len(text)-len(pattern)+1):
            if text[i:i+len(pattern)] == pattern:
                count += 1
        return count

    def frequency_map(self, text: str, pattern_length: int):
        frequency_map = {}
        text_length = len(text)

        for i in range(text_length-pattern_length-1):
            pattern = text[i:i+pattern_length]
            frequency_map[pattern] = frequency_map.get(pattern, 0) + 1
        return frequency_map


    def frequent_words(self, text: str, pattern_length: int):
        words = []
        frequency_map = self.frequency_map(text, pattern_length)
        max_frequency = max(frequency_map.values())
        for pattern, count in frequency_map.items():
            if count == max_frequency:
                words.append(pattern)
        return words