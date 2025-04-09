import cmd

from biolib import BioLib


class BioLibCLI(cmd.Cmd):
    prompt = "BioLib>> "
    intro = "Welcome to BioLib! Type help to learn more."

    def __init__(self):
        super().__init__()
        self.app = BioLib()

    def do_count_pattern(self, text: str, pattern: str):
        """
        Get count of pattern occurrences in a text
        """
        self.app.count_pattern(text, pattern)

    def do_match_pattern(self, text: str, pattern: str):
        """
        Get indexes of matches of pattern occurrences in a text
        """
        self.app.match_pattern(text, pattern)

    def do_frequency_map(self, text: str, pattern_length: str):
        """
        Get a map every pattern occurrence in a text
        """
        self.app.frequency_map(text, int(pattern_length))

    def do_frequent_words(self, text: str, pattern_length: str):
        """
        Get a list of the most frequent words in a text
        """
        self.app.frequent_words(text, int(pattern_length))

    def do_complement(self, text: str):
        """
        Get a literal complement of a dna sequence
        """
        self.app.complement(text)

    def do_reverse_complement(self, text: str):
        """
        Get a reverse complement of a dna sequence
        """
        self.app.reverse_complement(text)

    def do_quit(self, line):
        """Quit the CLI."""
        return True

    def postcmd(self, stop, line):
        print()
        return stop


if __name__ == '__main__':
        BioLibCLI().cmdloop()