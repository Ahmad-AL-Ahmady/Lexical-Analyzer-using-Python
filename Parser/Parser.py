class SimpleGrammarParser:
    def __init__(self):
        self.grammar = {}
        self.stack = []
        self.input_string = []
        self.unchecked_string = []

    def input_grammar(self):
        print("\nRecursive Descent Parsing For following grammar")
        print("\tGrammars:")

        try:
            print("Enter rule number 1 for non-terminal 'S':", end=" ")
            rule1_s = input().strip()
            print("Enter rule number 2 for non-terminal 'S':", end=" ")
            rule2_s = input().strip()
            self.grammar['S'] = [rule1_s, rule2_s]

            print("Enter rule number 1 for non-terminal 'B':", end=" ")
            rule1_b = input().strip()
            print("Enter rule number 2 for non-terminal 'B':", end=" ")
            rule2_b = input().strip()
            self.grammar['B'] = [rule1_b, rule2_b]

            return True

        except Exception as e:
            print(f"Error in grammar input: {e}")
            self.grammar.clear()
            return False

    def parse_string(self, input_str):
        if not self.grammar:
            print("Please input valid grammar first!")
            return

        self.input_string = list(input_str.strip())
        self.unchecked_string = self.input_string.copy()
        self.stack = []

        print("The input String:", [char for char in input_str])

        # Start parsing from 'S'
        if self.parse_S(0) == len(self.input_string):
            print("Stack after checking:", self.stack)
            print("The rest of unchecked string:", self.unchecked_string)
            print("Your input String is Accepted.")
        else:
            print("Stack after checking:", self.stack)
            print("The rest of unchecked string:", self.unchecked_string)
            print("Your input String is Rejected.")
        print("=" * 45)

    def parse_S(self, pos):
        if pos >= len(self.input_string):
            return pos

        # Try S -> aSB
        if pos < len(self.input_string) and self.input_string[pos] == 'a':
            self.stack.append('a')
            self.unchecked_string.pop(0)
            new_pos = self.parse_S(pos + 1)
            if new_pos > pos + 1:
                final_pos = self.parse_B(new_pos)
                if final_pos > new_pos:
                    return final_pos
            # Backtrack
            self.stack.pop()
            self.unchecked_string.insert(0, 'a')

        # Try S -> b
        if pos < len(self.input_string) and self.input_string[pos] == 'b':
            self.stack.append('b')
            self.unchecked_string.pop(0)
            return pos + 1

        return pos

    def parse_B(self, pos):
        if pos >= len(self.input_string):
            return pos

        # Try B -> a
        if pos < len(self.input_string) and self.input_string[pos] == 'a':
            self.stack.append('a')
            self.unchecked_string.pop(0)
            return pos + 1

        # Try B -> bBa
        if pos < len(self.input_string) and self.input_string[pos] == 'b':
            self.stack.append('b')
            self.unchecked_string.pop(0)
            new_pos = self.parse_B(pos + 1)
            if new_pos > pos + 1 and new_pos < len(self.input_string) and self.input_string[new_pos] == 'a':
                self.stack.append('a')
                self.unchecked_string.pop(0)
                return new_pos + 1
            # Backtrack
            self.stack.pop()
            self.unchecked_string.insert(0, 'b')

        return pos

    def display_grammar(self):
        if not self.grammar:
            print("\nNo grammar rules defined yet.")
            return

        print("\nCurrent Grammar Rules:")
        for nt in ['S', 'B']:
            rules = self.grammar[nt]
            print(f"{nt} -> {rules[0]} | {rules[1]}")


def main():
    parser = SimpleGrammarParser()

    while True:
        print("\n1-Another Grammar.")
        print("2-Another String.")
        print("3-Display Current Grammar")
        print("4-Exit")

        try:
            choice = input("\nEnter ur choice : ").strip()

            if choice == '1':
                parser.input_grammar()
            elif choice == '2':
                if not parser.grammar:
                    print("Please input grammar first!")
                    continue
                input_str = input("Enter the string want to be checked : ")
                parser.parse_string(input_str)
            elif choice == '3':
                parser.display_grammar()
            elif choice == '4':
                print("Goodbye!")
                break
            else:
                print("Invalid choice! Please try again.")
        except Exception as e:
            print(f"An error occurred: {e}")
            print("Please try again.")


if __name__ == "__main__":
    main()
