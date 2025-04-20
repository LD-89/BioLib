from abc import ABC, abstractmethod


class Genome(ABC):
    __sequence: str
    __sequence_length: int
    def __init__(self, sequence: str):
        self.__sequence = sequence
        self.__sequence_length = len(sequence)

    def get_sequence(self):
        return self.__sequence

    def get_sequence_length(self):
        return self.__sequence_length

    @abstractmethod
    def get_extended_sequence(self):
        pass

class LinearGenome(Genome):
    def get_extended_sequence(self):
        return self.__sequence

class CircularGenome(Genome):
    def get_extended_sequence(self):
        return self.__sequence+self.__sequence[:self.__sequence_length//2]


class GenomeFactory:
    @staticmethod
    def create_genome(genome_type: str, sequence: str) -> None | CircularGenome | LinearGenome:
        if genome_type == "linear":
            return LinearGenome(sequence)
        elif genome_type == "circular":
            return CircularGenome(sequence)