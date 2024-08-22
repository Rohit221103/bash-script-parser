# Yacc example

import ply.yacc as yacc

# Get the token map from the lexer.  This is required.
from lex_example import MyLexer
tokens=MyLexer.tokens
literals=MyLexer.literals
#print(tokens)


# To specify the grammar rules we have to define functions in our yacc file. 
# The syntax for the same is as follows: 
def p_program(p):
    'program : statements'
    p[0] = p[1]
def p_statements(p):
    '''statements : statement 
                  | statement statements
    '''
    if len(p)==2:
        p[0]=p[1]
    else:
        p[0]=(p[1],p[2])
def p_declaration(p):
    '''statement : ID '=' NUMBER 
                 | ID '=' STRING 
                 | ID '=' DECIMAL
                 | ECHO X
                 | ECHO STRING
                 | IF_START LPAREN LPAREN expression RPAREN RPAREN ';' THEN statements IF_CLOSED
                 | ID '=' LPAREN tuple RPAREN
                 | FOR ID IN STRING ';' DO statements DONE
                 | ID LPAREN RPAREN LCURLY statements RCURLY
                 | ID tuple
                 | ID LSQR NUMBER RSQR '=' STRING
                 | ID LSQR NUMBER RSQR '=' NUMBER
                 | ID LSQR NUMBER RSQR '=' DECIMAL
        X : '$' ID 
          | '$' ID ',' X
        tuple : STRING
              | STRING tuple
    '''
    print(len(p))
    for i in p:
        print(i)
    if len(p)==4 and p[2]=='=':
        p[0] = ('declaration',p[1],p[3])
    if p[1]=='echo':
        print(p[1])
        p[0]=['print']+[i for i in p[1::] ]
        #print(p[0])
    if p[1]=='if':
        p[0]=(p[1],p[4])
    if len(p)>=5 and p[2]=='=' and p[3]=='(':
        p[0]=(p[1],p[2],p[3],p[4])

def p_expression(p):
    '''expression : expression '+' expression
                  | expression '-' expression
                  | expression '*' expression
                  | expression '/' expression
                  | expression LT expression
                  | expression LTE expression
                  | expression GT expression
                  | expression GTE expression
                  | expression NE expression
                  | expression EQUIVALENCE expression
                  | '$' ID
                  | ID
                  | NUMBER
    '''
    if len(p)==4:
        if p[1]=='$':
            p[0]=(p[2],p[3],p[5])
        else:
            p[0]=(p[1],p[2],p[3])
    else:
        if p[1]=='$':
            p[0]=p[2]
        else:
            p[0]=p[1]

# Error rule for syntax errors
def p_error(p):
    print("Syntax error in input!")
    raise SyntaxError
# Build the parser
parser = yacc.yacc()
'''while True:
   try:
       s = input('calc > ')
   except EOFError:
       break
   if not s: continue
   result = parser.parse(s)
   print(result)'''
s='''
CASE1=1 CASE2=4.5 CASE3="hello" #variable declaration
echo $CASE1,$CASE2
if (( $CASE1 < 2 )) ; then #if statement
     echo "hello"
fi
CASE4=2
fruits=('apple' 'banana')
fruits[0]='apple'
for i in '{arrayname[@]}'; do
  echo "hello $i"
done
myfuc() {
   echo "hello $1"
}
myfuc "John"
'''
r=parser.parse(s)
print(r)
if r: 
    print('accepted')
