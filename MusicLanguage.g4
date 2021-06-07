grammar MusicLanguage;

// start symbol
program: (declaration | play | '\n' )+ EOF ;

declaration: ( tempo | metrum | timbre | note | pause | bar | bars_list | for_loop | check_if ) ;

// declarations and objects

tempo: WS* 'TEMPO' WS* ':' WS* NUMBER ;

metrum: WS* 'METRUM' WS* ':' WS* NUMBER '/' NUMBER ;

timbre: WS* 'TIMBRE' WS* ':' WS* TIMBRE ;

note: WS* 'Note' WS+ NAME WS* ':' WS* pitch=PITCH WS* ',' WS* duration=DURATION ;

pause: WS* 'Pause' WS+ NAME WS* ':' WS* duration=NUMBER ;

bar: WS* 'Bar' WS+ NAME WS* ':' WS* NAME(',' WS* NAME)* ;

bars_list: WS* 'BarsList' WS* NAME WS* ':' WS* NAME(',' WS* NAME)* ;

// instructions

play: WS* 'play' WS+ metrum WS+ ',' WS+ NAME(',' WS* NAME)*;

// terminals

TIMBRE: ('Flute' | 'Piano' | 'Guitar') ;

PITCH: ('c' | 'cis' | 'd' | 'dis' | 'e' | 'eis' | 'f' | 'fis' | 'g' | 'gis' | 'a' | 'b' | 'h' ) [1-2] ;

DURATION: ('1' | '2' | '4' | '8' | '16');

// non-terminals

NUMBER: [0-9]+ ;

NAME: [a-zA-Z0-9_]+ ;

WS : ' ' | '\t' ;

CR: [\r\n]+ -> skip ;

// statements

phrase : WS* play '\n' ;
phrases : (phrase)* ;

// operators

arithmetic : ADD | SUBSTRACT | MULTIPLY | DIVIDE;

ADD: '+';

SUBSTRACT: '-';

MULTIPLY: '*';

DIVIDE: '/';

logic : LOWER | GREATER | LE | GE | NOT | EQUALS | nequals;

LOWER: '<';

GREATER: '>';

LE: '<=';

GE: '>=';

NOT: '!';

EQUALS: '=';

nequals: NOT EQUALS;

// if statement

check_if : WS* 'if' WS+ condition ':\n'
         (declaration | play)+ '\n'
         ('else:\n'
         (declaration | play)+)?
         'endif\n' ;

condition	: NUMBER WS+ logic WS+ NUMBER
			| NAME WS+ logic WS+ NAME
			;

// for loop

for_loop : 'for' WS+ name=NAME WS+ 'from' WS+ start=NUMBER WS+ 'to' WS+ end=NUMBER ':\n'
            phrases WS+
            'endfor';