
#import pytest
import function

def gc_content(sequence):
    """Calculate the GC content of a DNA sequence."""
    
    sequence = sequence.upper()
    
    gc = sequence.count("G") + sequence.count("C")
    
    return (gc / len(sequence)) * 100





sequence = "AGCTAGCAGCTAGCTAGC"
result = gc_content(sequence)
print(f"GC content of the sequence is: {result:.2f}%")
