class BioLib:
    def count_pattern(self, text: str, pattern: str) -> int:
        count = 0
        for i in range(len(text)-len(pattern)+1):
            if text[i:i+len(pattern)] == pattern:
                count += 1
        return count

    def match_pattern(self, text: str, pattern: str) -> list[int]:
        matches = []
        for i in range(len(text)-len(pattern)+1):
            if text[i:i+len(pattern)] == pattern:
                matches.append(i)
        return matches

    def frequency_map(self, text: str, pattern_length: int) -> dict[str, int]:
        frequency_map = {}
        text_length = len(text)

        for i in range(text_length-pattern_length-1):
            pattern = text[i:i+pattern_length]
            frequency_map[pattern] = frequency_map.get(pattern, 0) + 1
        return frequency_map


    def frequent_words(self, text: str, pattern_length: int) -> list[str]:
        words = []
        frequency_map = self.frequency_map(text, pattern_length)
        max_frequency = max(frequency_map.values())
        for pattern, count in frequency_map.items():
            if count == max_frequency:
                words.append(pattern)
        return words

    def complement(self, text: str):
        complements = {
            'A': 'T',
            'T': 'A',
            'C': 'G',
            'G': 'C',
        }
        complemented_text = ''
        for char in text:
            if char in complements.keys():
                complemented_text += complements[char]
            else:
                complemented_text += char

        return complemented_text

    def reverse_complement(self, text: str):
        return self.complement(text[::-1])