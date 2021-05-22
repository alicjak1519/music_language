grammar MusicLanguage;


// declarations and objects

tempo: WS* 'TEMPO' WS* ':' WS* NUMBER ;

metrum: WS* 'METRUM' WS* ':' WS* NUMBER '/' NUMBER ;

timbre: WS* 'TIMBRE' WS* ':' WS* TIMBRE ;

note: WS* 'Note' WS+ NAME WS* ':' WS* pitch=NUMBER WS* ',' WS* duration=NUMBER ;

pause: WS* 'Pause' WS+ NAME WS* ':' WS* duration=NUMBER ;

bar: WS* 'Bar' WS+ NAME WS* ':' WS* (note | pause)+ ;

bars_list: WS* 'BarsList' WS* NAME WS* (bar)+ ;

// instructions

play: WS* 'play' WS+ metrum WS+ ',' WS+ bars_list;

// terminals

TIMBRE: ('Flute' | 'Piano' | 'Guitar') ;

PITCH: ('c' | 'cis' | 'd' | 'dis' | 'e' | 'eis' | 'f' | 'fis' | 'g' | 'gis' | 'a' | 'b' | 'h' ) [1-2] ;

DURATION: ('1' | '2' | '4' | '8' | '16');

// non-terminals

NUMBER: [1-9] [0-9]* ;

NAME : [A-Z][a-zA-Z0-9_]* ;

WS: [ \t\r\n]+ -> skip ;

// statements

phrase : WS* play '\n' ;
phrases : (phrase)* ;

for_loop : 'for' WS+ name=NAME WS+ 'from' WS+ from=NUMBER WS+ 'to' WS+ to=NUMBER '\n' phrases WS* 'end for';

//condition : ?? ;
//
//if : WS* 'if' WS+ condition  ?? ;

// operators