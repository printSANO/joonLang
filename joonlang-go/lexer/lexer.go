package lexer

import (
	"unicode"
)

// TokenType represents the type of a token.
type TokenType int

const (
	TokenTypeInvalid TokenType = iota
	TokenTypeVariable
	TokenTypeKeyword
	TokenTypeNumber
	TokenTypeWhitespace
)

// Token represents a token in JoonLang.
type Token struct {
	TokenType TokenType
	Value     string
}

// Lexer represents the JoonLang lexer.
type Lexer struct {
	input  string
	pos    int
	tokens []Token
}

// NewLexer creates a new JoonLang lexer.
func NewLexer(input string) *Lexer {
	return &Lexer{
		input:  input,
		pos:    0,
		tokens: make([]Token, 0),
	}
}

// Tokenize performs lexical analysis and tokenization.
func (l *Lexer) Tokenize() ([]Token, error) {
	for l.pos < len(l.input) {
		ch := rune(l.input[l.pos])
		if unicode.IsSpace(ch) {
			l.consumeWhitespace()
		} else if ch == '#' {
			l.consumeComment()
		} else if unicode.IsLetter(ch) {
			l.consumeVariable()
		} else if unicode.IsDigit(ch) {
			l.consumeNumber()
		} else {
			// Handle other token types like keywords and operators
			// based on the JoonLang syntax
			// Example: if ch == '님이말씀해보세요', l.consumeKeyword()
			// ...
		}
	}
	return l.tokens, nil
}

// Helper functions for consuming different types of tokens

func (l *Lexer) consumeWhitespace() {
	// Consume whitespace characters
	start := l.pos
	for l.pos < len(l.input) && unicode.IsSpace(rune(l.input[l.pos])) {
		l.pos++
	}
	l.tokens = append(l.tokens, Token{TokenType: TokenTypeWhitespace, Value: l.input[start:l.pos]})
}

func (l *Lexer) consumeComment() {
	// Consume comments (lines starting with '#')
	start := l.pos
	for l.pos < len(l.input) && l.input[l.pos] != '\n' {
		l.pos++
	}
	l.tokens = append(l.tokens, Token{TokenType: TokenTypeWhitespace, Value: l.input[start:l.pos]})
}

func (l *Lexer) consumeVariable() {
	// Consume variable names
	start := l.pos
	for l.pos < len(l.input) && (unicode.IsLetter(rune(l.input[l.pos])) || unicode.IsDigit(rune(l.input[l.pos]))) {
		l.pos++
	}
	l.tokens = append(l.tokens, Token{TokenType: TokenTypeVariable, Value: l.input[start:l.pos]})
}

func (l *Lexer) consumeNumber() {
	// Consume numbers
	start := l.pos
	for l.pos < len(l.input) && unicode.IsDigit(rune(l.input[l.pos])) {
		l.pos++
	}
	l.tokens = append(l.tokens, Token{TokenType: TokenTypeNumber, Value: l.input[start:l.pos]})
}

// Other functions for consuming keywords, operators, etc., can be added similarly.
