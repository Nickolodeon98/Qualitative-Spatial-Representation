:- use_module(library(clpfd)).
:- use_module(library(clpq)).

subExconnected(X1, X2, Y1, Y2, A, B, C, D) :-
	(X1 + Y1) // 2 #= abs(A - C),
	{}(B - (X2 / 2) =< D + (Y2 / 2)),
	{}(D - (Y2 / 2) =< B + (X2 / 2)).

singleExconnected(A, B, C, D, E, F, G, H) :-
	(subExconnected(A, B, C, D, E, F, G, H);
	subExconnected(B, A, D, C, F, E, H, G)).
	
doubleExconnected(A, B, C, D, E, F, G, H) :-
	(A + C) // 2 #= abs(E - G),
	(B + D) // 2 #= abs(F - H).

ec(Aw, Ah, Bw, Bh, Ax, Ay, Bx, By) :-
		Aw #> 0,
		Aw #< 20,
		Ah #> 0,
		Ah #< 20,
		Bw #> 0,
		Bw #< 20,
		Bh #> 0,
		Bh #< 20,
		Ax #> 0,
		Ax #< 20,
		Ay #> 0,
		Ay #< 20,
		Bx #> 0,
		Bx #< 20,
		By #> 0,
		By #< 20,
		Aw #= Bw,
		Ah #= Bh,
		Aw #= Ah,
		Bw #= Bh,
		{}(Ax - (Aw / 2) >= 0),
		{}(Ay - (Ah / 2) >= 0),
		{}(Bx - (Bw / 2) >= 0),
		{}(By - (Bh / 2) >= 0),
		{}(Ax + (Aw / 2) =< 20),
		{}(Ay + (Ah / 2) =< 20),
		{}(Bx + (Bw / 2) =< 20),
		{}(By + (Bh / 2) =< 20),
		(singleExconnected(Aw, Ah, Bw, Bh, Ax, Ay, Bx, By);
		doubleExconnected(Aw, Ah, Bw, Bh, Ax, Ay, Bx, By)),
		{}(Bx >= Bw / 2),
		{}(By >= Bh / 2).
