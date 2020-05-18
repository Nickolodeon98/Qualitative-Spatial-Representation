:- use_module(library(clpfd)).
:- use_module(library(clpq)).

check(A1, B1, A2, B2) :-
	A1 #> 1,
	B1 #> 1,
	A1 #= B1,
	A2 #> 0,
	X is (B1 rdiv 2),
	{}(B2 - X > 0),
	{}(B2 + X < 20),
	B2 #> 0,
	A2 #< 20,
	B2 #< 20.


hPartOf(Aw, Bw, Ax, Bx) :- 
	check(Aw, Bw, Ax, Bx),
	X is (Aw rdiv 2),
	Y is (Bw rdiv 2),
	{}(Ax - X < Bx + Y),
	{}(Bx - Y < Ax + X).

vPartOf(Ah, Bh, Ay, By) :-
	check(Ah, Bh, Ay, By),
	X is (Ah rdiv 2),
	Y is (Bh rdiv 2),
	{}(Ay - X < By + Y),
	{}(By - Y < Ay + X).

aPartOf(Aw, Ah, Bw, Bh, Ax, Ay, Bx, By) :-
	{}(Ay + Ah / 2 = By + Bh / 2),
	hPartOf(Aw, Bw, Ax, Bx).
	
bPartOf(Aw, Ah, Bw, Bh, Ax, Ay, Bx, By) :-
	{}(Ax + Aw / 2 = Bx + Bw / 2),
	vPartOf(Ah, Bh, Ay, By).

hvPartOf(Aw, Ah, Bw, Bh, Ax, Ay, Bx, By) :-
	(hPartOf(Aw, Bw, Ax, Bx),
	vPartOf(Ah, Bh, Ay, By)).
	
abPartOf(Aw, Ah, Bw, Bh, Ax, Ay, Bx, By) :-
	(aPartOf(Aw, Ah, Bw, Bh, Ax, Ay, Bx, By);
	bPartOf(Aw, Ah, Bw, Bh, Ax, Ay, Bx, By)).

po(Aw, Ah, Bw, Bh, Ax, Ay, Bx, By) :-
	check(Aw, Bw, Ax, Bx),
	check(Ah, Bh, Ay, By),
	((Bx #=< By);
	(Bx #>= By)),
	(Ax #\= Bx;
	Ay #\= By),
	(hvPartOf(Aw, Ah, Bw, Bh, Ax, Ay, Bx, By);
	abPartOf(Aw, Ah, Bw, Bh, Ax, Ay, Bx, By)).
