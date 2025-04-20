import cmd
from biolib import BioLib


class BioLibCLI(cmd.Cmd):
    prompt = "BioLib>> "
    intro = "Welcome to BioLib! Type help to learn more."

    def __init__(self):
        super().__init__()
        self.app = BioLib()

    def do_set_genome(self, line):
        """
        Set a genome sequence.
        Alias: sg
        """
        sequence = input('Input genome sequence: ')
        self.app.set_genome(sequence)
        print("Genome sequence set successfully")

    def do_sg(self, line):
        """Alias for set_genome"""
        return self.do_set_genome(line)

    def do_count_pattern(self, line):
        """
        Get count of pattern occurrences in a text
        Alias: cp
        """
        pattern = input('Input pattern: ')
        result = self.app.count_pattern(pattern)
        print(f"Pattern count: {result}")

    def do_cp(self, line):
        """Alias for count_pattern"""
        return self.do_count_pattern(line)

    def do_count_approximate_pattern(self, line):
        """
        Get count of approximate pattern occurrences in a text
        Alias: cap
        """
        pattern = input('Input pattern: ')
        max_difference = input('Input maximum difference: ')
        result = self.app.count_approximate_pattern(pattern, int(max_difference))
        print(f"Approximate pattern count: {result}")

    def do_cap(self, line):
        """Alias for count_approximate_pattern"""
        return self.do_count_approximate_pattern(line)

    def do_match_pattern(self, line):
        """
        Get indexes of matches of pattern occurrences in a text
        Alias: mp
        """
        pattern = input('Input pattern: ')
        result = self.app.match_pattern(pattern)
        print(f"Pattern matches at indexes: {result}")

    def do_mp(self, line):
        """Alias for match_pattern"""
        return self.do_match_pattern(line)

    def do_frequency_map(self, line):
        """
        Get a map every pattern occurrence in a text
        Alias: fm
        """
        text = input('Input text: ')
        pattern_length = input('Input pattern length: ')
        result = self.app.frequency_map(text, int(pattern_length))
        print(f"Frequency map: {result}")

    def do_fm(self, line):
        """Alias for frequency_map"""
        return self.do_frequency_map(line)

    def do_frequent_words(self, line):
        """
        Get a list of the most frequent words in a text
        Alias: fw
        """
        text = input('Input text: ')
        pattern_length = input('Input pattern length: ')
        result = self.app.frequent_words(text, int(pattern_length))
        print(f"Frequent words: {result}")

    def do_fw(self, line):
        """Alias for frequent_words"""
        return self.do_frequent_words(line)

    def do_complement(self, line):
        """
        Get a literal complement of a dna sequence
        Alias: c
        """
        text = input('Input DNA sequence: ')
        result = self.app.complement(text)
        print(f"Complement: {result}")

    def do_c(self, line):
        """Alias for complement"""
        return self.do_complement(line)

    def do_reverse_complement(self, line):
        """
        Get a reverse complement of a dna sequence
        Alias: rc
        """
        text = input('Input DNA sequence: ')
        result = self.app.reverse_complement(text)
        print(f"Reverse complement: {result}")

    def do_rc(self, line):
        """Alias for reverse_complement"""
        return self.do_reverse_complement(line)

    def do_get_minimum_skew(self, line):
        """
        Get minimum skew of a dna sequence.
        Alias: gms
        """
        result = self.app.get_minimum_skew()
        print(f"Minimum skew: {result}")

    def do_gms(self, line):
        """Alias for get_minimum_skew"""
        return self.do_get_minimum_skew(line)

    def do_calculate_hamming_distance(self, line):
        """
        Calculate hamming distance between two sequences.
        Alias: chd
        """
        sequence_1 = input('Input sequence 1: ')
        sequence_2 = input('Input sequence 2: ')
        result = self.app.calculate_hamming_distance(sequence_1, sequence_2)
        print(f"Hamming distance: {result}")

    def do_chd(self, line):
        """Alias for calculate_hamming_distance"""
        return self.do_calculate_hamming_distance(line)

    def do_quit(self, line):
        """
        Quit the CLI.
        Alias: q
        """
        return True

    def do_q(self, line):
        """Alias for quit"""
        return self.do_quit(line)

    def postcmd(self, stop, line):
        print()
        return stop

def main():
    BioLibCLI().cmdloop()

if __name__ == '__main__':
    main()