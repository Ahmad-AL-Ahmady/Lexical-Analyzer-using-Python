import re

cpp_keywords = r'\b(alignas|alignof|and|and_eq|asm|atomic_cancel|atomic_commit|atomic_noexcept|auto|bitand|bitor|bool|break|case|catch|char|char8_t|char16_t|char32_t|class|co_await|co_return|co_yield|compl|concept|const|consteval|constexpr|constinit|const_cast|continue|decltype|default|delete|do|double|dynamic_cast|else|enum|explicit|export|extern|false|float|for|friend|goto|if|import|inline|int|long|module|mutable|namespace|new|noexcept|not|not_eq|nullptr|operator|or|or_eq|private|protected|public|reflexpr|register|reinterpret_cast|requires|return|short|signed|sizeof|static|static_assert|static_cast|struct|switch|synchronized|template|this|thread_local|throw|true|try|typedef|typeid|typename|union|unsigned|using|virtual|void|volatile|wchar_t|while|xor|xor_eq)\b'


def tokenize(code):
    # Regex patterns for different token types
    patterns = [
        ('SINGLE_COMMENT', r'//[^\r\n]*'),
        ('MULTI_COMMENT', r'/\\*(.*?)\\*/'),
        ('STRING', r'"([^"\\]|\\.)*"'),
        ('KEYWORD', cpp_keywords),
        ('IDENTIFIER', r'\b[A-Za-z_]\w*\b'),
        ('NUMBER', r'\b\d+(\.\d+)?\b'),
        ('OPERATOR', r'[+\-*/=<>!&|]{1,2}'),
        ('SPECIAL_CHAR', r'[{}()[\],;.#]'),
        ('CHAR', r"'([^'\\]|\\.)'"),
    ]

    # Combine patterns into a single regex
    token_regex = '|'.join(
        f'(?P<{name}>{pattern})' for name, pattern in patterns)

    # Compile the regex
    regex = re.compile(token_regex, re.MULTILINE | re.DOTALL)

    # Find and print tokens
    tokens = []
    for match in regex.finditer(code):
        for name, pattern in patterns:
            if match.group(name):
                token_type = name
                token_value = match.group(name)

                # Skip whitespace if needed
                if token_type not in ['WHITESPACE', '']:
                    print(f'{token_type}: {repr(token_value)}')
                    tokens.append((token_type, token_value))
                break

    return tokens


# Read multiline input from the user
print("Enter C++ code (type 'END' on a new line to finish):")
lines = []
while True:
    line = input()
    if line.strip().upper() == 'END':
        break
    lines.append(line)

# Join all lines into a single string
cpp_code = '\n'.join(lines)

# Run lexical analysis
tokenize(cpp_code)

# Keep the window open until the user presses Enter
input("\nPress Enter to exit...")
