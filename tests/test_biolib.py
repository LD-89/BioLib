import unittest
from biolib.core.biolib import BioLib
from biolib.core.genome import Genome, LinearGenome, CircularGenome


class TestBioLib(unittest.TestCase):
    def setUp(self):
        """Set up test fixtures before each test method is run."""
        self.biolib = BioLib()
        # Sample DNA sequence for testing
        self.dna_sequence = "ATGCGTAGCATCGATCGATCGATCG"
        # Sample RNA sequence for testing
        self.rna_sequence = "AUGCGUAGCAUCGAUCGAUCGAUCG"
        # Set up a default genome for most tests
        self.biolib.set_genome(self.dna_sequence)

    def test_set_genome(self):
        """Test genome setting with different types."""
        # Test with default (linear) genome
        self.biolib.set_genome(self.dna_sequence)
        self.assertEqual(self.biolib.genome.get_sequence(), self.dna_sequence)
        self.assertIsInstance(self.biolib.genome, Genome)
        self.assertIsInstance(self.biolib.genome, LinearGenome)
        
        # Test with explicit linear genome
        self.biolib.set_genome(self.dna_sequence, "linear")
        self.assertEqual(self.biolib.genome.get_sequence(), self.dna_sequence)
        self.assertIsInstance(self.biolib.genome, LinearGenome)
        
        # Test with circular genome
        self.biolib.set_genome(self.dna_sequence, "circular")
        self.assertEqual(self.biolib.genome.get_sequence(), self.dna_sequence)
        self.assertIsInstance(self.biolib.genome, CircularGenome)

    def test_count_pattern(self):
        """Test counting occurrences of a pattern in a sequence."""
        # Simple pattern that appears once
        self.assertEqual(self.biolib.count_pattern("ATGC"), 1)
        
        # Pattern that appears multiple times
        self.biolib.set_genome("ATGATGATG")
        self.assertEqual(self.biolib.count_pattern("ATG"), 3)
        
        # Pattern that doesn't exist
        self.assertEqual(self.biolib.count_pattern("GGGG"), 0)
        
        # Empty pattern should match entire sequence length
        with self.assertRaises(Exception):
            self.biolib.count_pattern("")

    def test_count_approximate_pattern(self):
        """Test counting patterns with allowed differences."""
        # Test with exact match (0 differences)
        self.assertEqual(self.biolib.count_approximate_pattern("ATGC", 0), 1)
        
        # Test with 1 allowed difference
        self.biolib.set_genome("ATGCATGC")
        # ATGC should match ATGC (itself) and ATGA (one off)
        self.assertEqual(self.biolib.count_approximate_pattern("ATGC", 1), 2)
        
        # Test with 2 allowed differences
        self.assertEqual(self.biolib.count_approximate_pattern("ATGC", 2), 2)

    def test_match_pattern(self):
        """Test finding positions of exact pattern matches."""
        # Test finding a pattern that occurs once
        self.biolib.set_genome("ATCGATCG")
        self.assertEqual(self.biolib.match_pattern("ATC"), [0, 4])
        
        # Test pattern that doesn't exist
        self.assertEqual(self.biolib.match_pattern("AAA"), [])
        
        # Test with a longer sequence and multiple occurrences
        self.biolib.set_genome("ATGATGATGATG")
        self.assertEqual(self.biolib.match_pattern("ATG"), [0, 3, 6, 9])

    def test_match_approximate_pattern(self):
        """Test finding positions of approximate pattern matches."""
        # Test with exact match
        self.biolib.set_genome("ATCGATCG")
        self.assertEqual(self.biolib.match_approximate_pattern("ATC", 0), [0, 4])
        
        # Test with 1 allowed difference - should find more matches
        # ATC matches ATC exactly, and ATG with 1 mismatch
        self.biolib.set_genome("ATCATGATC")
        expected = [0, 3, 6]  # ATC at 0 and 6, ATG at 3 is 1 mismatch away
        self.assertEqual(
            sorted(self.biolib.match_approximate_pattern("ATC", 1)), 
            sorted(expected)
        )

    def test_frequency_map(self):
        """Test creating frequency map of patterns in text."""
        text = "ATGATGATG"
        # Test with pattern length 3
        expected = {"ATG": 3, "TGA": 2, "GAT": 2}
        self.assertEqual(self.biolib.frequency_map(text, 3), expected)
        
        # Test with pattern length 2
        expected = {"AT": 3, "TG": 3, "GA": 2}
        self.assertEqual(self.biolib.frequency_map(text, 2), expected)

    def test_frequent_words(self):
        """Test finding most frequent words of given length."""
        text = "ATGATGATG"
        # ATG is the most frequent 3-mer
        self.assertEqual(self.biolib.frequent_words(text, 3), ["ATG"])
        
        # For 2-mers, both AT and TG appear 3 times
        result = self.biolib.frequent_words(text, 2)
        self.assertIn("AT", result)
        self.assertIn("TG", result)
        self.assertEqual(len(result), 2)

    def test_complement(self):
        """Test DNA/RNA complementation."""
        # Test DNA complement
        self.assertEqual(self.biolib.complement("ATGC"), "TACG")
        
        # Test with lowercase
        self.assertEqual(self.biolib.complement("atgc"), "TACG")
        
        # Test with mixed case
        self.assertEqual(self.biolib.complement("AtGc"), "TACG")
        
        # Test with non-standard characters (should be preserved)
        self.assertEqual(self.biolib.complement("ATGC-N"), "TACG-N")

    def test_reverse_complement(self):
        """Test reverse complement of DNA/RNA."""
        # Test DNA reverse complement
        self.assertEqual(self.biolib.reverse_complement("ATGC"), "GCAT")
        
        # Test with a palindromic sequence
        self.assertEqual(self.biolib.reverse_complement("GGATCC"), "GGATCC")

    def test_get_skew(self):
        """Test calculation of GC skew."""
        # Simple case: G increases skew, C decreases skew
        self.biolib.set_genome("GAGCC")
        self.assertEqual(self.biolib.get_skew(), [0, 1, 1, 2, 1, 0])
        
        # Test with a longer sequence
        self.biolib.set_genome("GGCCGGAA")
        self.assertEqual(self.biolib.get_skew(), [0, 1, 2, 1, 0, 1, 2, 2, 2])

    def test_get_minimum_skew(self):
        """Test finding positions of minimum skew."""
        # Test with a simple case
        self.biolib.set_genome("GAGCC")
        # Minimum skew of 0 occurs at positions 0 and 5
        self.assertEqual(self.biolib.get_minimum_skew(), [0, 5])
        
        # Test with a sequence having unique minimum
        self.biolib.set_genome("AGGCATGC")
        # Skew values: [0, 1, 2, 2, 1, 1, 2, 2, 1]
        # Minimum unique value is 0 at position 0
        self.assertEqual(self.biolib.get_minimum_skew(), [0])

    def test_calculate_hamming_distance(self):
        """Test calculation of Hamming distance between sequences."""
        # Test with identical sequences
        self.assertEqual(self.biolib.calculate_hamming_distance("ATGC", "ATGC"), 0)
        
        # Test with one difference
        self.assertEqual(self.biolib.calculate_hamming_distance("ATGC", "ATCC"), 1)
        
        # Test with multiple differences
        self.assertEqual(self.biolib.calculate_hamming_distance("ATGC", "GCTA"), 4)

    def test_get_motifs_matrix(self):
        """Test generation of motif count matrix."""
        motifs = ["ACGT", "ACCT", "ACGA"]
        expected = {
            'A': [3, 0, 0, 0],
            'C': [0, 3, 1, 0],
            'G': [0, 0, 2, 1],
            'T': [0, 0, 0, 2]
        }
        self.assertEqual(self.biolib.get_motifs_matrix(motifs), expected)

    def test_get_profile_matrix(self):
        """Test generation of motif profile matrix."""
        motifs = ["ACGT", "ACCT", "ACGA"]
        expected = {
            'A': [1.0, 0.0, 0.0, 0.0],
            'C': [0.0, 1.0, 0.33333333333333337, 0.0],
            'G': [0.0, 0.0, 0.6666666666666666, 0.3333333333333333],
            'T': [0.0, 0.0, 0.0, 0.6666666666666666]
        }
        result = self.biolib.get_profile_matrix(motifs)
        
        # Check each element with a small tolerance for floating-point comparison
        for nucleotide in "ACGT":
            for i in range(4):
                self.assertAlmostEqual(
                    result[nucleotide][i],
                    expected[nucleotide][i],
                    places=6
                )

    def test_get_motifs_consensus(self):
        """Test generation of consensus string from motifs."""
        motifs = ["ACGT", "ACCT", "ACGA"]
        # First column: all A (A)
        # Second column: all C (C)
        # Third column: 2 G, 1 C (G)
        # Fourth column: 2 T, 1 A (T)
        self.assertEqual(self.biolib.get_motifs_consensus(motifs), "ACGT")
        
        # Test with a more complex example
        motifs = ["AACGTA", "CCCGTT", "CACCTT", "GGATTA", "TTCCGG"]
        self.assertEqual(self.biolib.get_motifs_consensus(motifs), "CACCTA")

    def test_get_motifs_score(self):
        """Test calculation of motif score."""
        motifs = ["ACGT", "ACCT", "ACGA"]
        # Consensus is ACGT
        # ACGT has 0 differences
        # ACCT has 1 difference
        # ACGA has 1 difference
        # Total score: 2
        self.assertEqual(self.biolib.get_motifs_score(motifs), 2)

    def test_get_motifs_entropy(self):
        """Test calculation of motif entropy."""
        motifs = ["ACGT", "ACCT", "ACGA"]
        # Calculate expected entropy manually for comparison
        # First column: all A (entropy = 0)
        # Second column: all C (entropy = 0)
        # Third column: 2 G (2/3), 1 C (1/3) 
        # Fourth column: 2 T (2/3), 1 A (1/3)
        expected_entropy = -((2/3) * (1.0).bit_length() + (1/3) * (2.0).bit_length()) * 2
        # Allow for floating-point imprecision
        self.assertAlmostEqual(
            self.biolib.get_motifs_entropy(motifs),
            expected_entropy,
            places=6
        )

    def test_translate_rna_to_amino_acid(self):
        """Test translation of RNA sequence to amino acid sequence."""
        # Set up an RNA sequence
        self.biolib.set_genome("AUGCCAUAG")  # AUG (M) CCA (P) UAG (Stop)
        self.assertEqual(self.biolib.translate_rna_to_amino_acid(), "MP*")
        
        # Test with another sequence
        self.biolib.set_genome("AUGGCACCCUGG")  # AUG (M) GCA (A) CCC (P) UGG (W)
        self.assertEqual(self.biolib.translate_rna_to_amino_acid(), "MAPW")


if __name__ == '__main__':
    unittest.main()
