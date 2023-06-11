# main.py

'''

CBC parameters: 
    Hemoglobin, Hematocrit, White Blood Cells (WBC), Red Blood Cells (RBC), Platelets.
Lipid Panel parameters: 
    Low-density Lipoprotein (LDL), High-density Lipoprotein (HDL), Triglycerides.
Comprehensive Metabolic Panel (CMP)
    Sugar (glucose) level: High levels may indicate diabetes.
Electrolytes and fluid balance: Electrolytes are minerals in your blood and other body fluids that carry an electric charge, such as Sodium, Potassium, Chloride, and Bicarbonate.
Kidney function: This includes parameters like BUN (Blood Urea Nitrogen) and Creatinine.
Liver function: This includes parameters like Albumin, Bilirubin, ALP (Alkaline Phosphatase), ALT (Alanine Aminotransferase), and AST (Aspartate Aminotransferase).

'''
from parser_1 import Parser
from interpreter import Interpreter

from lexer import Lexer, EOF, IDENT, NUMBER, NEWLINE

def main():
    # Open the file and read the content
    with open('examples/example1.mrd', 'r') as file:
        content = file.read()

    # Pass the content to the lexer
    lexer = Lexer(content)

    # Tokenize the content and print formatted output
    while True:
        token = lexer.get_next_token()
        if token.type == EOF:
            break

        # Determine the separator based on the token type
        separator = ': ' if token.type != NEWLINE else '\n'

        # Print the token value without newline for IDENT and NUMBER tokens
        if token.type in (IDENT, NUMBER):
            print(token.literal, end='')
        else:
            print(token.literal, end=separator)

if __name__ == "__main__":
    main()
