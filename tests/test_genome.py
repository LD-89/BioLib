import unittest
from biolib.core.genome import Genome, LinearGenome, CircularGenome, GenomeFactory


class TestGenome(unittest.TestCase):
    def test_linear_genome(self):
        """Test LinearGenome class functionality."""
        sequence = "ATGCATGC"
        genome = LinearGenome(sequence)
        
        # Test basic properties
        self.assertEqual(genome.get_sequence(), sequence)
        self.assertEqual(genome.get_sequence_length(), len(sequence))
        
        # Test extended sequence (for linear genome, should be the same as original)
        self.assertEqual(genome.get_extended_sequence(), sequence)
    
    def test_circular_genome(self):
        """Test CircularGenome class functionality."""
        sequence = "ATGCATGC"
        genome = CircularGenome(sequence)
        
        # Test basic properties
        self.assertEqual(genome.get_sequence(), sequence)
        self.assertEqual(genome.get_sequence_length(), len(sequence))
        
        # Test extended sequence (for circular, should include half the sequence repeated)
        expected_extended = sequence + sequence[:len(sequence)//2]
        self.assertEqual(genome.get_extended_sequence(), expected_extended)
        
        # Test with odd length sequence
        odd_sequence = "ATGCATG"
        odd_genome = CircularGenome(odd_sequence)
        expected_extended = odd_sequence + odd_sequence[:len(odd_sequence)//2]
        self.assertEqual(odd_genome.get_extended_sequence(), expected_extended)

    def test_genome_factory(self):
        """Test GenomeFactory class functionality."""
        sequence = "ATGCATGC"
        
        # Test creating linear genome
        linear_genome = GenomeFactory.create_genome("linear", sequence)
        self.assertIsInstance(linear_genome, LinearGenome)
        self.assertEqual(linear_genome.get_sequence(), sequence)
        
        # Test creating circular genome
        circular_genome = GenomeFactory.create_genome("circular", sequence)
        self.assertIsInstance(circular_genome, CircularGenome)
        self.assertEqual(circular_genome.get_sequence(), sequence)
        
        # Test with invalid genome type
        invalid_genome = GenomeFactory.create_genome("invalid", sequence)
        self.assertIsNone(invalid_genome)


if __name__ == '__main__':
    unittest.main()
