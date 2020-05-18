:- use_module(library(clpfd)).
:- use_module(library(clpq)).

feasible(A1, A2, B1, B2) :-
	B1 #> A1,
	B2 #> A2,
	A1 #= A2,
	B1 #= B2,
	A1 #> 1,
	A2 #> 1,
	B1 #> 1,
	B2 #> 1,
	B1 #=< 20,
	B2 #=< 20.

intpp(Aw, Ah, Bw, Bh, Ax, Ay, Bx, By) :-
	feasible(Aw, Ah, Bw, Bh),
	{}(Bx - (Bw / 2) > 0),
	{}(By - (Bh / 2) > 0),
	{}(Bx + (Bw / 2) < 20),
	{}(By + (Bh / 2) < 20),
	abs(Ax - Bx) #< max(Aw//2, Bw//2),
	abs(Ay - By) #< max(Ah//2, Bh//2),
	{}(Bx + (Bw / 2) >= Ax + (Aw / 2)),
	{}(By + (Bh / 2) >= Ay + (Ah / 2)),
	{}(Bx - (Bw / 2) =< Ax - (Aw / 2)),
	{}(By - (Bh / 2) =< Ay - (Ah / 2)).
	
checkintpp(Aw, Ah, Bw, Bh, Ax, Ay, Bx, By) :-
	{}(Ax - (Aw / 2) =\= Bx - (Bw / 2)),
	{}(Ay + (Ah / 2) =\= By + (Bh / 2)),
	{}(Ax + (Aw / 2) =\= Bx + (Bw / 2)),
	{}(Ay - (Ah / 2) =\= By - (Bh / 2)).
		
	
