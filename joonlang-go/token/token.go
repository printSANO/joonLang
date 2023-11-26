package token

import (
	"fmt"

	"github.com/printSANO/joonLang/joonlang-go/lexer"
)

// TokenizeJoonCode tokenizes JoonLang code using the lexer package.
func TokenizeJoonCode(code string) {
	lexer := lexer.NewLexer(code)
	tokens, err := lexer.Tokenize()
	if err != nil {
		fmt.Println("Lexer error:", err)
		return
	}

	for _, token := range tokens {
		fmt.Printf("Token Type: %v, Value: %v\n", token.TokenType, token.Value)
	}
}
