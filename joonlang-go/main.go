// jooncompiler/main.go

package main

import (
	"github.com/printSANO/joonLang/joonlang-go/token"
)

func main() {
	inputCode := `
        # This is a JoonLang program
        변수님이말씀해보세요
        변수님? 42
        언제까지 해보실래요? 5
            변수님? 10
        자러가시는거에요?
        님맥사세요
    `

	token.TokenizeJoonCode(inputCode)
}
