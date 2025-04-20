from biolib.core.genome import Genome, GenomeFactory

1
class BioLib:
    genome: Genome

    def set_genome(self, sequence: str, genome_type: str = 'linear'):
        self.genome = GenomeFactory.create_genome(genome_type, sequence)

    def count_pattern(self, pattern: str) -> int:
        count = 0
        pattern_length = len(pattern)
        for i in range(len(self.genome.get_sequence())-pattern_length+1):
            if self.genome.get_sequence()[i:i+pattern_length] == pattern:
                count += 1
        return count

    def count_approximate_pattern(self, pattern: str, max_difference: int) -> int:
        count = 0
        pattern_length = len(pattern)
        for i in range(len(self.genome.get_sequence())-pattern_length+1):
            if self.calculate_hamming_distance(self.genome.get_sequence()[i:i+pattern_length], pattern) <= max_difference:
                count += 1
        return count

    def match_pattern(self, pattern: str) -> list[int]:
        positions = []
        pattern_length = len(pattern)
        for i in range(len(self.genome.get_sequence())-pattern_length+1):
            if self.genome.get_sequence()[i:i+pattern_length] == pattern:
                positions.append(i)
        return positions

    def match_approximate_pattern(self, pattern: str, max_difference: int) -> list[int]:
        positions = []
        pattern_length = len(pattern)
        for i in range(len(self.genome.get_sequence())-pattern_length+1):
            if self.calculate_hamming_distance(self.genome.get_sequence()[i:i+pattern_length], pattern) <= max_difference:
                positions.append(i)
        return positions

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

    def count_symbol(self, symbol):
        symbol_matches = []
        sequence_length = self.genome.get_sequence_length()
        extended_sequence = self.genome.get_extended_sequence()
        symbol_matches[0] = self.count_pattern(extended_sequence[:sequence_length//2], symbol)

        for i in range(1, sequence_length):
            symbol_matches[i] = symbol_matches[i-1]
            if extended_sequence[i-1] == symbol:
                symbol_matches[i] -= 1
            if extended_sequence[i+(sequence_length//2)-1] == symbol:
                symbol_matches[i] += 1

        return symbol_matches

    def get_skew(self):
        skew = [0]
        modifiers = {
            'C': -1,
            'G': 1,
        }
        for i, nucleotide in enumerate(self.genome.get_sequence()):
            skew.append(skew[i] + modifiers.get(nucleotide, 0))
        return skew

    def get_minimum_skew(self):
        positions = []
        minimum_skew = 0
        skew = self.get_skew()
        for i, skew_value in enumerate(skew):
            if skew_value < minimum_skew:
                minimum_skew = skew_value
                positions = [i]
            elif skew_value == minimum_skew:
                positions.append(i)
        return positions

    def calculate_hamming_distance(self, sequence_1, sequence_2):
        hamming_distance = 0
        for i, nucleotide in enumerate(sequence_1):
            if nucleotide != sequence_2[i]:
                hamming_distance += 1
        return hamming_distance



