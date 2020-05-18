:- use_module(library(clpfd)).
:- use_module(library(clpq)).
	
itpp(Aw, Ah, Bw, Bh, Ax, Ay, Bx, By) :-
	Bw #> Aw,
	Bh #> Ah,
	Aw #= Ah,
	Bw #= Bh,
	Aw #> 1,
	Ah #> 1,
	Bw #> 1,
	Bh #> 1,
	Bw #=< 20,
	Bh #=< 20,
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

checkitpp(Aw, Ah, Bw, Bh, Ax, Ay, Bx, By) :-
	(({}(Ax - (Aw / 2) = Bx - (Bw / 2));
	{}(Ay + (Ah / 2) = By + (Bh / 2)));
	({}(Ax + (Aw / 2) = Bx + (Bw / 2));
	{}(Ay - (Ah / 2) = By - (Bh / 2)))).
	
	
