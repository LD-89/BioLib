import math

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

    def get_motifs_matrix(self, motifs):
        count = {}
        k = len(motifs[0])
        for symbol in "ACGT":
            count[symbol] = [0 for j in range(k)]

        t = len(motifs)
        for i in range(t):
            for j in range(k):
                symbol = motifs[i][j]
                count[symbol][j] += 1

        return count

    def get_profile_matrix(self, motifs):
        t = len(motifs)
        profile = {}
        motifs_matrix = self.get_motifs_matrix(motifs)
        for nucleotide, counts in motifs_matrix.items():
            profile[nucleotide] = []
            for count in counts:
                profile[nucleotide].append(count / t)

        return profile

    def get_motifs_consensus(self, motifs):
        k = len(motifs[0])
        count = self.get_motifs_matrix(motifs)
        consensus = ""
        for j in range(k):
            m = 0
            frequentSymbol = ""
            for symbol in "ACGT":
                if count[symbol][j] > m:
                    m = count[symbol][j]
                    frequentSymbol = symbol
            consensus += frequentSymbol
        return consensus

    def get_motifs_score(self, motifs):
        consensus = self.get_motifs_consensus(motifs)
        score = 0

        for i, nucleotide in enumerate(consensus):
            for j, motif in enumerate(motifs):
                if motif[i] != nucleotide:
                    score += 1

        return score

    def get_motifs_entropy(self, motifs):
        profile = self.get_profile_matrix(motifs)
        entropy = 0
        for symbol in "ACGT":
            for count in profile[symbol]:
                if count != 0:
                    entropy -= count * math.log2(count)
        return entropy


    def translate_rna_to_amino_acid(self):
        # amino acid code in a format of {codon_1: {codon_2: {codon_3: amino_acid}}}
        amino_acid_code = {
            'A': {
                'A': {
                    'A': 'K',
                    'C': 'N',
                    'G': 'K',
                    'U': 'N',
                },
                'C': {
                    'A': 'T',
                    'C': 'T',
                    'G': 'T',
                    'U': 'T',
                },
                'G': {
                    'A': 'R',
                    'C': 'S',
                    'G': 'R',
                    'U': 'S',
                },
                'U': {
                    'A': 'I',
                    'C': 'I',
                    'G': 'M',
                    'U': 'I',
                },
            },
            'C': {
                'A': {
                    'A': 'Q',
                    'C': 'H',
                    'G': 'Q',
                    'U': 'H',
                },
                'C': {
                    'A': 'P',
                    'C': 'P',
                    'G': 'P',
                    'U': 'P',
                },
                'G': {
                    'A': 'R',
                    'C': 'R',
                    'G': 'R',
                    'U': 'R',
                },
                'U': {
                    'A': 'L',
                    'C': 'L',
                    'G': 'L',
                    'U': 'L',
                },
            },
            'G': {
                'A': {
                    'A': 'E',
                    'C': 'D',
                    'G': 'E',
                    'U': 'D',
                },
                'C': {
                    'A': 'A',
                    'C': 'A',
                    'G': 'A',
                    'U': 'A',
                },
                'G': {
                    'A': 'G',
                    'C': 'G',
                    'G': 'G',
                    'U': 'G',
                },
                'U': {
                    'A': 'V',
                    'C': 'V',
                    'G': 'V',
                    'U': 'V',
                },
            },
            'U': {
                'A': {
                    'A': '*',
                    'C': 'Y',
                    'G': '*',
                    'U': 'Y',
                },
                'C': {
                    'A': 'S',
                    'C': 'S',
                    'G': 'S',
                    'U': 'S',
                },
                'G': {
                    'A': '*',
                    'C': 'C',
                    'G': 'W',
                    'U': 'C',
                },
                'U': {
                    'A': 'L',
                    'C': 'F',
                    'G': 'L',
                    'U': 'F',
                },
            },
        }
        amino_acids = {
            'A': ('Alanine', 'Ala'),
            'C': ('Cysteine', 'Cys'),
            'D': ('Aspartic acid', 'Asp'),
            'E': ('Glutamic acid', 'Glu'),
            'F': ('Phenylalanine', 'Phe'),
            'G': ('Glycine', 'Gly'),
            'H': ('Histodie', 'His'),
            'I': ('Isoleucine', 'Ile'),
            'K': ('Lysine', 'Lys'),
            'L': ('Leucine', 'Leu'),
            'M': ('Methionine', 'Met'),
            'N': ('Asparagine', 'Asn'),
            'P': ('Proline', 'Pro'),
            'Q': ('Glutamine', 'Gln'),
            'R': ('Arginine', 'Arg'),
            'S': ('Serine', 'Ser'),
            'T': ('Threonine', 'Thr'),
            'V': ('Valine', 'Val'),
            'W': ('Tryptophan', 'Trp'),
            'Y': ('Tyrosine', 'Tyr'),
            '*': ('Stop codon', 'Stop'),
        }
        rna_sequence = self.genome.get_sequence().upper()
        amino_acid_sequence = ''
        for i in range(0, len(rna_sequence), 3):
            codon = rna_sequence[i:i+3]
            amino_acid_sequence += amino_acid_code[codon[0]][codon[1]][codon[2]]
        return amino_acid_sequence

    def gibbs_sampler(self):
        pass




