PUSH    <
POP     <
SP      <
FP      <
TRUE    <
FALSE   <
AND     <
OR      <
NOT     <
GET_FROM_FRAME  <
SET_TO_FRAME    <
GET_FROM_VECT   <
SET_TO_VECT     <
PUSHDOWN_SUM    <
PUSHDOWN_DIF    <
PUSHDOWN_MUL    <
PUSHDOWN_DIV    <
GET_LENGTH      <
IGUAL           <
DIFERENTE       <
MAIOR           <
MAIOR_OU_IGUAL  <
MENOR           <
MENOR_OU_IGUAL  <
K_0000    <
K_0001    <
K_0002    <
K_FFFF    <
WORD_TAM  <
DIM_1     <
DIM_2     <
INIT_HEAP      <
NEW_ARRAY      <
NEW_MATRIX     <

; inicio do codigo
&     /0000
; preparacao do ambiente de execucao
SC    INIT_HEAP
; chama a sub-rotina principal
LD    SP
+     WORD_TAM
MM    FP
SC    main
; termino da execucao do programa
; apos retorno da sub-rotina main
FIM   HM FIM

; declaracao de CONSTANTES
K_0004	K /0004
K_0006	K /0006
; declaracao de FUNCOES
main	$ =1
LD K_0000
SC PUSH  ; var a
LD K_0000
SC PUSH  ; var b
LD    FP
SC    PUSH
LD    K_0002
*     K_FFFF
SC    PUSH
LD    K_0001
SC    PUSH
SC    SET_TO_VECT
LD    FP
SC    PUSH
LD    K_0004
*     K_FFFF
SC    PUSH
LD    K_0006
SC    PUSH
SC    SET_TO_VECT
main_WHILE_1 + K_0000
LD    K_0004
SC    PUSH
SC    GET_FROM_FRAME
SC    PUSH
LD    K_0000
SC    PUSH
SC    MAIOR
SC    POP
JZ main_END_WHILE_1
LD    FP
SC    PUSH
LD    K_0002
*     K_FFFF
SC    PUSH
LD    K_0002
SC    PUSH
SC    GET_FROM_FRAME
SC    PUSH
LD    K_0004
SC    PUSH
SC    GET_FROM_FRAME
SC    PUSH
SC    PUSHDOWN_MUL
SC    SET_TO_VECT
LD    FP
SC    PUSH
LD    K_0004
*     K_FFFF
SC    PUSH
LD    K_0004
SC    PUSH
SC    GET_FROM_FRAME
SC    PUSH
LD    K_0001
SC    PUSH
SC    PUSHDOWN_DIF
SC    SET_TO_VECT
JP main_WHILE_1
main_END_WHILE_1 + K_0000
RET_main	LD  FP
-   WORD_TAM
MM  SP
RS	main
# FIM
