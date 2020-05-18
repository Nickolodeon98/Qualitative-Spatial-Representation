:- use_module(library(clpfd)).

eq(Aw, Ah, Bw, Bh, Ax, Ay, Bx, By) :-
	Aw #> 1,
	Aw #=< 20,
	Ah #> 1,
	Ah #=< 20,
	Ax #> 0,
	Ax #< 20,
	Ay #> 0,
	Ay #< 20,
	Aw #= Bw,
	Ah #= Bh,
	Ax #= Bx,
	Ay #= By.
