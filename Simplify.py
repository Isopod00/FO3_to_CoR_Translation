import COR_Expressions

def simplify(expression):
	if isinstance(expression, COR_Expressions.Intersection):
		lhs1, rhs1 = expression.argument1, expression.argument2
		if isinstance(lhs1, COR_Expressions.Complement):
			arg = lhs1.argument
			A = arg
			if str(A)==str(rhs1):
				return ("((A)⁻) ∩ (A) = 𝟎", COR_Expressions.EmptyRelation())
		if isinstance(lhs1, COR_Expressions.Intersection):
			lhs2, rhs2 = lhs1.argument1, lhs1.argument2
			A = lhs2
			if str(A)==str(rhs2):
				if str(A)==str(rhs1):
					return ("((A) ∩ (A)) ∩ (A) = (A) ∪ (A)", COR_Expressions.Union(A, A))
				B = rhs1
				return ("((A) ∩ (A)) ∩ (B) = (A) ∩ (B)", COR_Expressions.Intersection(A, B))
			B = rhs2
			if str(A)==str(rhs1):
				return ("((A) ∩ (B)) ∩ (A) = (B) ∩ (A)", COR_Expressions.Intersection(B, A))
			if str(B)==str(rhs1):
				return ("((A) ∩ (B)) ∩ (B) = (A) ∩ (B)", COR_Expressions.Intersection(A, B))
		if isinstance(lhs1, COR_Expressions.EmptyRelation):
			A = rhs1
			return ("(𝟎) ∩ (A) = 𝟎", COR_Expressions.EmptyRelation())
		if isinstance(lhs1, COR_Expressions.Union):
			lhs2, rhs2 = lhs1.argument1, lhs1.argument2
			A = lhs2
			if str(A)==str(rhs2):
				B = rhs1
				return ("((A) ∪ (A)) ∩ (B) = (B) ∩ (A)", COR_Expressions.Intersection(B, A))
			B = rhs2
			if str(A)==str(rhs1):
				return ("((A) ∪ (B)) ∩ (A) = A", A)
			if str(B)==str(rhs1):
				return ("((A) ∪ (B)) ∩ (B) = B", B)
		A = lhs1
		if isinstance(rhs1, COR_Expressions.UniversalRelation):
			return ("(A) ∩ (T) = A", A)
		if isinstance(rhs1, COR_Expressions.Intersection):
			lhs2, rhs2 = rhs1.argument1, rhs1.argument2
			B = lhs2
			if str(A)==str(rhs2):
				return ("(A) ∩ ((B) ∩ (A)) = (B) ∩ (A)", COR_Expressions.Intersection(B, A))
			if str(B)==str(rhs2):
				return ("(A) ∩ ((B) ∩ (B)) = (B) ∩ (A)", COR_Expressions.Intersection(B, A))
			if str(A)==str(lhs2):
				if str(A)==str(rhs2):
					return ("(A) ∩ ((A) ∩ (A)) = (A) ∩ (A)", COR_Expressions.Intersection(A, A))
				B = rhs2
				return ("(A) ∩ ((A) ∩ (B)) = (A) ∩ (B)", COR_Expressions.Intersection(A, B))
		if isinstance(rhs1, COR_Expressions.Union):
			lhs2, rhs2 = rhs1.argument1, rhs1.argument2
			if str(A)==str(lhs2):
				B = rhs2
				return ("(A) ∩ ((A) ∪ (B)) = A", A)
			B = lhs2
			if str(A)==str(rhs2):
				return ("(A) ∩ ((B) ∪ (A)) = A", A)
			if str(B)==str(rhs2):
				return ("(A) ∩ ((B) ∪ (B)) = (B) ∩ (A)", COR_Expressions.Intersection(B, A))
		if isinstance(rhs1, COR_Expressions.Complement):
			arg = rhs1.argument
			if str(A)==str(arg):
				return ("(A) ∩ ((A)⁻) = 𝟎", COR_Expressions.EmptyRelation())
		if isinstance(rhs1, COR_Expressions.EmptyRelation):
			return ("(A) ∩ (𝟎) = 𝟎", COR_Expressions.EmptyRelation())
		if isinstance(lhs1, COR_Expressions.UniversalRelation):
			A = rhs1
			return ("(T) ∩ (A) = A", A)
	if isinstance(expression, COR_Expressions.Composition):
		lhs1, rhs1 = expression.argument1, expression.argument2
		if isinstance(lhs1, COR_Expressions.Intersection):
			lhs2, rhs2 = lhs1.argument1, lhs1.argument2
			A = lhs2
			if str(A)==str(rhs2):
				B = rhs1
				return ("((A) ∩ (A)) ∘ (B) = (A) ∘ (B)", COR_Expressions.Composition(A, B))
		if isinstance(lhs1, COR_Expressions.EmptyRelation):
			A = rhs1
			return ("(𝟎) ∘ (A) = 𝟎", COR_Expressions.EmptyRelation())
		A = lhs1
		if isinstance(rhs1, COR_Expressions.EmptyRelation):
			return ("(A) ∘ (𝟎) = 𝟎", COR_Expressions.EmptyRelation())
		if isinstance(rhs1, COR_Expressions.IdentityRelation):
			return ("(A) ∘ (𝟏) = A", A)
		if isinstance(rhs1, COR_Expressions.Union):
			lhs2, rhs2 = rhs1.argument1, rhs1.argument2
			if str(A)==str(lhs2):
				if str(A)==str(rhs2):
					return ("(A) ∘ ((A) ∪ (A)) = (A) ∘ (A)", COR_Expressions.Composition(A, A))
			B = lhs2
			if str(B)==str(rhs2):
				return ("(A) ∘ ((B) ∪ (B)) = (A) ∘ (B)", COR_Expressions.Composition(A, B))
		if isinstance(rhs1, COR_Expressions.Intersection):
			lhs2, rhs2 = rhs1.argument1, rhs1.argument2
			B = lhs2
			if str(B)==str(rhs2):
				return ("(A) ∘ ((B) ∩ (B)) = (A) ∘ (B)", COR_Expressions.Composition(A, B))
			if str(A)==str(lhs2):
				if str(A)==str(rhs2):
					return ("(A) ∘ ((A) ∩ (A)) = (A) ∘ (A)", COR_Expressions.Composition(A, A))
		if isinstance(lhs1, COR_Expressions.IdentityRelation):
			A = rhs1
			return ("(𝟏) ∘ (A) = A", A)
		if isinstance(lhs1, COR_Expressions.Union):
			lhs2, rhs2 = lhs1.argument1, lhs1.argument2
			A = lhs2
			if str(A)==str(rhs2):
				B = rhs1
				return ("((A) ∪ (A)) ∘ (B) = (A) ∘ (B)", COR_Expressions.Composition(A, B))
	if isinstance(expression, COR_Expressions.Union):
		lhs1, rhs1 = expression.argument1, expression.argument2
		if isinstance(lhs1, COR_Expressions.Union):
			lhs2, rhs2 = lhs1.argument1, lhs1.argument2
			A = lhs2
			if str(A)==str(rhs2):
				if str(A)==str(rhs1):
					return ("((A) ∪ (A)) ∪ (A) = A", A)
				B = rhs1
				return ("((A) ∪ (A)) ∪ (B) = (B) ∪ (A)", COR_Expressions.Union(B, A))
			B = rhs2
			if str(B)==str(rhs1):
				return ("((A) ∪ (B)) ∪ (B) = (B) ∪ (A)", COR_Expressions.Union(B, A))
			if str(A)==str(rhs1):
				return ("((A) ∪ (B)) ∪ (A) = (B) ∪ (A)", COR_Expressions.Union(B, A))
		A = lhs1
		if isinstance(rhs1, COR_Expressions.Intersection):
			lhs2, rhs2 = rhs1.argument1, rhs1.argument2
			B = lhs2
			if str(B)==str(rhs2):
				return ("(A) ∪ ((B) ∩ (B)) = (B) ∪ (A)", COR_Expressions.Union(B, A))
			if str(A)==str(rhs2):
				return ("(A) ∪ ((B) ∩ (A)) = A", A)
			if str(A)==str(lhs2):
				if str(A)==str(rhs2):
					return ("(A) ∪ ((A) ∩ (A)) = (A) ∪ (A)", COR_Expressions.Union(A, A))
				B = rhs2
				return ("(A) ∪ ((A) ∩ (B)) = A", A)
		if isinstance(rhs1, COR_Expressions.Complement):
			arg = rhs1.argument
			if str(A)==str(arg):
				return ("(A) ∪ ((A)⁻) = T", COR_Expressions.UniversalRelation())
		if isinstance(rhs1, COR_Expressions.UniversalRelation):
			return ("(A) ∪ (T) = T", COR_Expressions.UniversalRelation())
		if isinstance(rhs1, COR_Expressions.Union):
			lhs2, rhs2 = rhs1.argument1, rhs1.argument2
			B = lhs2
			if str(B)==str(rhs2):
				return ("(A) ∪ ((B) ∪ (B)) = (A) ∪ (B)", COR_Expressions.Union(A, B))
			if str(A)==str(rhs2):
				return ("(A) ∪ ((B) ∪ (A)) = (B) ∪ (A)", COR_Expressions.Union(B, A))
			if str(A)==str(lhs2):
				if str(A)==str(rhs2):
					return ("(A) ∪ ((A) ∪ (A)) = (A) ∩ (A)", COR_Expressions.Intersection(A, A))
				B = rhs2
				return ("(A) ∪ ((A) ∪ (B)) = (A) ∪ (B)", COR_Expressions.Union(A, B))
		if isinstance(lhs1, COR_Expressions.Complement):
			arg = lhs1.argument
			A = arg
			if str(A)==str(rhs1):
				return ("((A)⁻) ∪ (A) = T", COR_Expressions.UniversalRelation())
		if isinstance(lhs1, COR_Expressions.Intersection):
			lhs2, rhs2 = lhs1.argument1, lhs1.argument2
			A = lhs2
			B = rhs2
			if str(A)==str(rhs1):
				return ("((A) ∩ (B)) ∪ (A) = (A) ∪ (A)", COR_Expressions.Union(A, A))
			if str(B)==str(rhs1):
				return ("((A) ∩ (B)) ∪ (B) = (B) ∩ (B)", COR_Expressions.Intersection(B, B))
			if str(A)==str(rhs2):
				B = rhs1
				return ("((A) ∩ (A)) ∪ (B) = (B) ∪ (A)", COR_Expressions.Union(B, A))
		if isinstance(lhs1, COR_Expressions.UniversalRelation):
			A = rhs1
			return ("(T) ∪ (A) = T", COR_Expressions.UniversalRelation())
	if isinstance(expression, COR_Expressions.Converse):
		arg = expression.argument
		if isinstance(arg, COR_Expressions.IdentityRelation):
			return ("(𝟏)⁻¹ = 𝟏", COR_Expressions.IdentityRelation())
		if isinstance(arg, COR_Expressions.Converse):
			arg = arg.argument
			A = arg
			return ("((A)⁻¹)⁻¹ = A", A)
		if isinstance(arg, COR_Expressions.UniversalRelation):
			return ("(T)⁻¹ = T", COR_Expressions.UniversalRelation())
		if isinstance(arg, COR_Expressions.Union):
			lhs2, rhs2 = arg.argument1, arg.argument2
			A = lhs2
			if str(A)==str(rhs2):
				return ("((A) ∪ (A))⁻¹ = (A)⁻¹", COR_Expressions.Converse(A))
		if isinstance(arg, COR_Expressions.EmptyRelation):
			return ("(𝟎)⁻¹ = 𝟎", COR_Expressions.EmptyRelation())
		if isinstance(arg, COR_Expressions.Intersection):
			lhs2, rhs2 = arg.argument1, arg.argument2
			A = lhs2
			if str(A)==str(rhs2):
				return ("((A) ∩ (A))⁻¹ = (A)⁻¹", COR_Expressions.Converse(A))
	if isinstance(expression, COR_Expressions.Dagger):
		lhs1, rhs1 = expression.argument1, expression.argument2
		if isinstance(lhs1, COR_Expressions.Union):
			lhs2, rhs2 = lhs1.argument1, lhs1.argument2
			A = lhs2
			if str(A)==str(rhs2):
				if str(A)==str(rhs1):
					return ("((A) ∪ (A)) † (A) = (A) † (A)", COR_Expressions.Dagger(A, A))
				B = rhs1
				return ("((A) ∪ (A)) † (B) = (A) † (B)", COR_Expressions.Dagger(A, B))
		if isinstance(lhs1, COR_Expressions.UniversalRelation):
			A = rhs1
			return ("(T) † (A) = T", COR_Expressions.UniversalRelation())
		A = lhs1
		if isinstance(rhs1, COR_Expressions.UniversalRelation):
			return ("(A) † (T) = T", COR_Expressions.UniversalRelation())
		if isinstance(rhs1, COR_Expressions.Union):
			lhs2, rhs2 = rhs1.argument1, rhs1.argument2
			B = lhs2
			if str(B)==str(rhs2):
				return ("(A) † ((B) ∪ (B)) = (A) † (B)", COR_Expressions.Dagger(A, B))
			if str(A)==str(lhs2):
				if str(A)==str(rhs2):
					return ("(A) † ((A) ∪ (A)) = (A) † (A)", COR_Expressions.Dagger(A, A))
		if isinstance(rhs1, COR_Expressions.Intersection):
			lhs2, rhs2 = rhs1.argument1, rhs1.argument2
			if str(A)==str(lhs2):
				if str(A)==str(rhs2):
					return ("(A) † ((A) ∩ (A)) = (A) † (A)", COR_Expressions.Dagger(A, A))
			B = lhs2
			if str(B)==str(rhs2):
				return ("(A) † ((B) ∩ (B)) = (A) † (B)", COR_Expressions.Dagger(A, B))
		if isinstance(lhs1, COR_Expressions.Intersection):
			lhs2, rhs2 = lhs1.argument1, lhs1.argument2
			A = lhs2
			if str(A)==str(rhs2):
				if str(A)==str(rhs1):
					return ("((A) ∩ (A)) † (A) = (A) † (A)", COR_Expressions.Dagger(A, A))
				B = rhs1
				return ("((A) ∩ (A)) † (B) = (A) † (B)", COR_Expressions.Dagger(A, B))
	if isinstance(expression, COR_Expressions.Complement):
		arg = expression.argument
		if isinstance(arg, COR_Expressions.Union):
			lhs2, rhs2 = arg.argument1, arg.argument2
			A = lhs2
			if str(A)==str(rhs2):
				return ("((A) ∪ (A))⁻ = (A)⁻", COR_Expressions.Complement(A))
		if isinstance(arg, COR_Expressions.Intersection):
			lhs2, rhs2 = arg.argument1, arg.argument2
			A = lhs2
			if str(A)==str(rhs2):
				return ("((A) ∩ (A))⁻ = (A)⁻", COR_Expressions.Complement(A))
		if isinstance(arg, COR_Expressions.EmptyRelation):
			return ("(𝟎)⁻ = T", COR_Expressions.UniversalRelation())
		if isinstance(arg, COR_Expressions.UniversalRelation):
			return ("(T)⁻ = 𝟎", COR_Expressions.EmptyRelation())

	return (None, expression) # The given expression was unable to be simplified