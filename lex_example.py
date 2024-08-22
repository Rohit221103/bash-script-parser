import ply.lex as lex
import os
from os import path
class MyLexer(object):
    l=[]
    reserved = {
       'echo' : 'ECHO',
       'if' : 'IF_START',
       'fi' : 'IF_CLOSED',
       'then' : 'THEN',
       'else' : 'ELSE',
       'in' : 'IN',
       'elif' : 'elif',
       'while' : 'WHILE',
       'for' : 'FOR',
       'do' : 'DO',
       'done' : 'DONE',
       'case' : 'SWITCH_START',
       'esac' : 'SWITCH_CLOSED',
       }

    tokens = [
            'NUMBER',
            'DECIMAL',
            'STRING',
            'PLUS',
            'MINUS',
            'TIMES',
            'DIVIDE',
            'LPAREN',
            'RPAREN',
            'LCURLY',
            'RCURLY',
            'LSQR',
            'RSQR',
            'ID',
            'EQUIVALENCE',
            'LT',
            'GT',
            'LTE',
            'GTE',
            'NE',
            'COMMENT',
            ]+ list(reserved.values())
    # Regular expression rules for simple tokens
    #t_PLUS    = r'\+'
    #t_MINUS   = r'-'
    #t_TIMES   = r'\*'
    #t_DIVIDE  = r'/'
    t_LPAREN  = r'\('
    t_RPAREN  = r'\)'
    t_EQUIVALENCE = r'=='
    t_LCURLY = r'\{'
    t_RCURLY = r'\}'
    t_LSQR = r'\['
    t_RSQR = r'\]'
    t_LT=r'<'
    t_GT=r'>'
    t_LTE=r'<='
    t_GTE=r'>='
    t_NE=r'!='
    literals = ['+','-','*','/','$','=',';',',']
    # A regular expression rule with some action code
    

    def t_STRING(self,t):
        r'(\'[^\']*\')|(\"[^\"]*\")'
        t.value=t.value[1:-1:]
        return t
    def t_COMMENT(self,t):
        r'\#.*'
        pass
    def t_DECIMAL(self,t):
        r'[0-9][0-9]*\.[0-9]*'
        t.value=float(t.value)
        return t
    def t_NUMBER(self,t):
        r'\d+'
        t.value = int(t.value)    
        return t
    def t_ID(self,t):
        r'[a-zA-Z_][a-zA-Z_0-9]*'
        t.type = self.reserved.get(t.value,'ID')    # Check for reserved words
        return t
    # Define a rule so we can track line numbers
    def t_newline(self,t):
        r'\n+'
        t.lexer.lineno += len(t.value)
        print()
        #print(self.l[t.lexer.lineno-1]) 
        
    # A string containing ignored characters (spaces and tabs)
    t_ignore  = ' \t'

    # Error handling rule
    def t_error(self,t):
        print("Illegal character '%s'" % t.value[0])
        t.lexer.skip(1)

        # Give the lexer some input

    def build(self,**kwargs):
        self.lexer = lex.lex(module=self, **kwargs)

    # Test it output
    def test(self,data):
        self.lexer.input(data)
        self.l=data.split('\n')
        print('\n'+str(self.l)+'\n\n'+self.l[0])
        while True:
             tok = self.lexer.token()
             if not tok: 
                 break
             print(tok)   

data1 = '''ehdad
3 + 4 * 10
+ -20 *2 - ab + forget
if else 
a==b a=b () 
for '''

data='''CASE1=223;CASE2=412.521  #variable declaration
echo=2.2
echo $echo
echo $CASE1,$CASE2
a='as'
b="bas"
function f()
{
  as="as"
}
'''

m = MyLexer()
m.build()
#m.test(data)

#a=open(r'/home/rohit/.bashrc','r')
a=open('b.sh','r')
m.test(a.read())
a.close()
