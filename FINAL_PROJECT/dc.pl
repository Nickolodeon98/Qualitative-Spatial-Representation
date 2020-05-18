:- use_module(library(clpfd)).
:- use_module(library(clpq)).
	
dc(Aw, Ah, Bw, Bh, Ax, Ay, Bx, By) :-
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
		Bw #>= 2,
		Bh #>= 2,
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
		((Aw + Bw) // 2 #< abs(Ax - Bx); (Ah + Bh) // 2 #< abs(Ay - By)).

