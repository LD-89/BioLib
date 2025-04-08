import cmd


class BioLib:
    def pattern_count(self, text: str, pattern: str):
        count = 0
        for i in range(len(text)-len(pattern)+1):
            if text[i:i+len(pattern)] == pattern:
                count += 1
        return count


class BioLibCLI(cmd.Cmd):
    prompt = "BioLib>> "
    intro = "Welcome to BioLib! Type help to learn more."

    def __init__(self):
        super().__init__()
        self.app = BioLib()

    def do_pattern_count(self, text: str, pattern: str):
        """
        Find pattern in text
        """
        self.app.pattern_count(text, pattern)

    def do_quit(self, line):
        """Quit the CLI."""
        return True

    def postcmd(self, stop, line):
        print()
        return stop


if __name__ == '__main__':
        BioLibCLI().cmdloop()