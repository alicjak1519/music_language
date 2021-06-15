grammar MusicLanguage;

// start symbol
program: (declaration | play | '\n' )+ EOF ;

declaration: ( tempo | meter | timbre | note | bar | bars_list | for_loop | check_if | integer | string) ;

// declarations and objects

tempo: WS* 'TEMPO' WS* ':' WS* NUMBER ;

meter: WS* NUMBER '/' NUMBER ;

timbre: WS* 'TIMBRE' WS* ':' WS* TIMBRE ;

note: WS* 'Note' WS+ NAME WS* ':' WS* pitch=PITCH WS* ',' WS* duration=NUMBER ;

bar: WS* 'Bar' WS+ NAME WS* ':' WS* NAME(',' WS* NAME)* ;

bars_list: WS* 'BarsList' WS* NAME WS* ':' WS* meter WS* ',' WS* NAME(',' WS* NAME)* ;


// instructions

play: WS* 'play' WS+ NAME(',' WS* NAME)*;

// terminals

TIMBRE: ('Flute' | 'Piano' | 'Guitar') ;

PITCH: ( '0' | 'C' | 'C#' | 'D' | 'D#' | 'E' | 'E#' | 'F' | 'F#' | 'G' | 'G#' | 'A' | 'B' | 'H' ) '-' [1-4] ;


// non-terminals
integer: WS* 'integer' WS+ NAME ':' WS+ NUMBER ;
string: WS* 'string' WS+ NAME ':' WS+ NAME ;

NUMBER: [0-9]+ ;

NAME: [a-zA-Z0-9_]+ ;

WS: ' ' | '\t' ;

CR: [\r\n]+ -> skip ;

// statements

phrase : WS* (play | declaration) '\n' ;
phrases : (phrase)+ ;

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

EQUALS: '==';

nequals: NOT EQUALS;

// if statement

check_if : WS* 'if' WS+ condition ':\n'
         phrases
         (WS* 'else:\n'
         phrases)?
         WS* 'endif' ;

condition: (NAME | NUMBER) WS+ logic WS+ (NAME | NUMBER) ;

// for loop

for_loop: WS* 'for' WS+ name=NAME WS+ 'from' WS+ start_number=NUMBER WS+ 'to' WS+ end_number=NUMBER ':\n'
        WS* phrases
        WS* 'endfor';