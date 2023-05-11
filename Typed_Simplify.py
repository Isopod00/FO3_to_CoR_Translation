import Typed_COR_Expressions

def simplify(expression):
	if isinstance(expression, Typed_COR_Expressions.Typed_Union):
		lhs1, rhs1 = expression.argument1, expression.argument2
		A = lhs1
		if str(A)==str(rhs1):
			return ("(A[P*P]) ∪ (A[P*P]) = A[P*P]", A)
		if isinstance(rhs1, Typed_COR_Expressions.Typed_Intersection):
			lhs2, rhs2 = rhs1.argument1, rhs1.argument2
			B = lhs2
			if str(A)==str(rhs2):
				return ("(A[P*P]) ∪ ((B[P*P]) ∩ (A[P*P])) = A[P*P]", A)
			if isinstance(rhs2, Typed_COR_Expressions.Typed_Complement):
				arg = rhs2.argument
				if str(A)==str(arg):
					return ("(A[P*P]) ∪ ((B[P*P]) ∩ ((A[P*P])⁻)) = (A[P*P]) ∪ (B[P*P])", Typed_COR_Expressions.Typed_Union(A, B))
			if isinstance(rhs2, Typed_COR_Expressions.Typed_Union):
				lhs3, rhs3 = rhs2.argument1, rhs2.argument2
				if str(A)==str(lhs3):
					C = rhs3
					return ("(A[P*P]) ∪ ((B[P*P]) ∩ ((A[P*P]) ∪ (C[P*P]))) = (A[P*P]) ∪ ((C[P*P]) ∩ (B[P*P]))", Typed_COR_Expressions.Typed_Union(A, Typed_COR_Expressions.Typed_Intersection(C, B)))
				C = lhs3
				if str(A)==str(rhs3):
					return ("(A[P*P]) ∪ ((B[P*P]) ∩ ((C[P*P]) ∪ (A[P*P]))) = (A[P*P]) ∪ ((B[P*P]) ∩ (C[P*P]))", Typed_COR_Expressions.Typed_Union(A, Typed_COR_Expressions.Typed_Intersection(B, C)))
			if isinstance(rhs2, Typed_COR_Expressions.Typed_Intersection):
				lhs3, rhs3 = rhs2.argument1, rhs2.argument2
				C = lhs3
				if str(A)==str(rhs3):
					return ("(A[P*P]) ∪ ((B[P*P]) ∩ ((C[P*P]) ∩ (A[P*P]))) = A[P*P]", A)
				if str(A)==str(lhs3):
					C = rhs3
					return ("(A[P*P]) ∪ ((B[P*P]) ∩ ((A[P*P]) ∩ (C[P*P]))) = A[P*P]", A)
			if str(A)==str(lhs2):
				B = rhs2
				return ("(A[P*P]) ∪ ((A[P*P]) ∩ (B[P*P])) = A[P*P]", A)
			if isinstance(lhs2, Typed_COR_Expressions.Typed_Union):
				lhs3, rhs3 = lhs2.argument1, lhs2.argument2
				if str(A)==str(lhs3):
					B = rhs3
					C = rhs2
					return ("(A[P*P]) ∪ (((A[P*P]) ∪ (B[P*P])) ∩ (C[P*P])) = (A[P*P]) ∪ ((B[P*P]) ∩ (C[P*P]))", Typed_COR_Expressions.Typed_Union(A, Typed_COR_Expressions.Typed_Intersection(B, C)))
				B = lhs3
				if str(A)==str(rhs3):
					C = rhs2
					return ("(A[P*P]) ∪ (((B[P*P]) ∪ (A[P*P])) ∩ (C[P*P])) = ((B[P*P]) ∩ (C[P*P])) ∪ (A[P*P])", Typed_COR_Expressions.Typed_Union(Typed_COR_Expressions.Typed_Intersection(B, C), A))
			if isinstance(lhs2, Typed_COR_Expressions.Typed_Intersection):
				lhs3, rhs3 = lhs2.argument1, lhs2.argument2
				B = lhs3
				if str(A)==str(rhs3):
					C = rhs2
					return ("(A[P*P]) ∪ (((B[P*P]) ∩ (A[P*P])) ∩ (C[P*P])) = A[P*P]", A)
				if str(A)==str(lhs3):
					B = rhs3
					C = rhs2
					return ("(A[P*P]) ∪ (((A[P*P]) ∩ (B[P*P])) ∩ (C[P*P])) = A[P*P]", A)
			if isinstance(lhs2, Typed_COR_Expressions.Typed_Complement):
				arg = lhs2.argument
				if str(A)==str(arg):
					B = rhs2
					return ("(A[P*P]) ∪ (((A[P*P])⁻) ∩ (B[P*P])) = (B[P*P]) ∪ (A[P*P])", Typed_COR_Expressions.Typed_Union(B, A))
		if isinstance(rhs1, Typed_COR_Expressions.Typed_UniversalRelation):
			return ("(A[P*P]) ∪ (T[P*P]) = T[P*P]", Typed_COR_Expressions.Typed_UniversalRelation(expression.type()[0], expression.type()[1]))
		if isinstance(rhs1, Typed_COR_Expressions.Typed_Union):
			lhs2, rhs2 = rhs1.argument1, rhs1.argument2
			if str(A)==str(lhs2):
				B = rhs2
				return ("(A[P*P]) ∪ ((A[P*P]) ∪ (B[P*P])) = (A[P*P]) ∪ (B[P*P])", Typed_COR_Expressions.Typed_Union(A, B))
			B = lhs2
			if str(A)==str(rhs2):
				return ("(A[P*P]) ∪ ((B[P*P]) ∪ (A[P*P])) = (B[P*P]) ∪ (A[P*P])", Typed_COR_Expressions.Typed_Union(B, A))
			if isinstance(rhs2, Typed_COR_Expressions.Typed_Union):
				lhs3, rhs3 = rhs2.argument1, rhs2.argument2
				C = lhs3
				if str(A)==str(rhs3):
					return ("(A[P*P]) ∪ ((B[P*P]) ∪ ((C[P*P]) ∪ (A[P*P]))) = (C[P*P]) ∪ ((A[P*P]) ∪ (B[P*P]))", Typed_COR_Expressions.Typed_Union(C, Typed_COR_Expressions.Typed_Union(A, B)))
				if str(A)==str(lhs3):
					C = rhs3
					return ("(A[P*P]) ∪ ((B[P*P]) ∪ ((A[P*P]) ∪ (C[P*P]))) = (C[P*P]) ∪ ((B[P*P]) ∪ (A[P*P]))", Typed_COR_Expressions.Typed_Union(C, Typed_COR_Expressions.Typed_Union(B, A)))
			if isinstance(rhs2, Typed_COR_Expressions.Typed_Intersection):
				lhs3, rhs3 = rhs2.argument1, rhs2.argument2
				if str(A)==str(lhs3):
					C = rhs3
					return ("(A[P*P]) ∪ ((B[P*P]) ∪ ((A[P*P]) ∩ (C[P*P]))) = (B[P*P]) ∪ (A[P*P])", Typed_COR_Expressions.Typed_Union(B, A))
				C = lhs3
				if str(A)==str(rhs3):
					return ("(A[P*P]) ∪ ((B[P*P]) ∪ ((C[P*P]) ∩ (A[P*P]))) = (A[P*P]) ∪ (B[P*P])", Typed_COR_Expressions.Typed_Union(A, B))
			if isinstance(rhs2, Typed_COR_Expressions.Typed_Complement):
				arg = rhs2.argument
				if str(A)==str(arg):
					return ("(A[P*P]) ∪ ((B[P*P]) ∪ ((A[P*P])⁻)) = T[P*P]", Typed_COR_Expressions.Typed_UniversalRelation(expression.type()[0], expression.type()[1]))
			if isinstance(lhs2, Typed_COR_Expressions.Typed_Union):
				lhs3, rhs3 = lhs2.argument1, lhs2.argument2
				B = lhs3
				if str(A)==str(rhs3):
					C = rhs2
					return ("(A[P*P]) ∪ (((B[P*P]) ∪ (A[P*P])) ∪ (C[P*P])) = (C[P*P]) ∪ ((B[P*P]) ∪ (A[P*P]))", Typed_COR_Expressions.Typed_Union(C, Typed_COR_Expressions.Typed_Union(B, A)))
				if str(A)==str(lhs3):
					B = rhs3
					C = rhs2
					return ("(A[P*P]) ∪ (((A[P*P]) ∪ (B[P*P])) ∪ (C[P*P])) = (B[P*P]) ∪ ((C[P*P]) ∪ (A[P*P]))", Typed_COR_Expressions.Typed_Union(B, Typed_COR_Expressions.Typed_Union(C, A)))
			if isinstance(lhs2, Typed_COR_Expressions.Typed_Intersection):
				lhs3, rhs3 = lhs2.argument1, lhs2.argument2
				if str(A)==str(lhs3):
					B = rhs3
					C = rhs2
					return ("(A[P*P]) ∪ (((A[P*P]) ∩ (B[P*P])) ∪ (C[P*P])) = (C[P*P]) ∪ (A[P*P])", Typed_COR_Expressions.Typed_Union(C, A))
				B = lhs3
				if str(A)==str(rhs3):
					C = rhs2
					return ("(A[P*P]) ∪ (((B[P*P]) ∩ (A[P*P])) ∪ (C[P*P])) = (C[P*P]) ∪ (A[P*P])", Typed_COR_Expressions.Typed_Union(C, A))
			if isinstance(lhs2, Typed_COR_Expressions.Typed_Complement):
				arg = lhs2.argument
				if str(A)==str(arg):
					B = rhs2
					return ("(A[P*P]) ∪ (((A[P*P])⁻) ∪ (B[P*P])) = T[P*P]", Typed_COR_Expressions.Typed_UniversalRelation(expression.type()[0], expression.type()[1]))
		if isinstance(rhs1, Typed_COR_Expressions.Typed_Complement):
			arg = rhs1.argument
			if str(A)==str(arg):
				return ("(A[P*P]) ∪ ((A[P*P])⁻) = T[P*P]", Typed_COR_Expressions.Typed_UniversalRelation(expression.type()[0], expression.type()[1]))
			if isinstance(arg, Typed_COR_Expressions.Typed_Union):
				lhs3, rhs3 = arg.argument1, arg.argument2
				if str(A)==str(lhs3):
					B = rhs3
					return ("(A[P*P]) ∪ (((A[P*P]) ∪ (B[P*P]))⁻) = (A[P*P]) ∪ ((B[P*P])⁻)", Typed_COR_Expressions.Typed_Union(A, Typed_COR_Expressions.Typed_Complement(B)))
				B = lhs3
				if str(A)==str(rhs3):
					return ("(A[P*P]) ∪ (((B[P*P]) ∪ (A[P*P]))⁻) = (A[P*P]) ∪ ((B[P*P])⁻)", Typed_COR_Expressions.Typed_Union(A, Typed_COR_Expressions.Typed_Complement(B)))
			if isinstance(arg, Typed_COR_Expressions.Typed_Intersection):
				lhs3, rhs3 = arg.argument1, arg.argument2
				if str(A)==str(lhs3):
					B = rhs3
					return ("(A[P*P]) ∪ (((A[P*P]) ∩ (B[P*P]))⁻) = T[P*P]", Typed_COR_Expressions.Typed_UniversalRelation(expression.type()[0], expression.type()[1]))
				B = lhs3
				if str(A)==str(rhs3):
					return ("(A[P*P]) ∪ (((B[P*P]) ∩ (A[P*P]))⁻) = T[P*P]", Typed_COR_Expressions.Typed_UniversalRelation(expression.type()[0], expression.type()[1]))
		if isinstance(rhs1, Typed_COR_Expressions.Typed_EmptyRelation):
			return ("(A[P*P]) ∪ (𝟎[P*P]) = A[P*P]", A)
		if isinstance(rhs1, Typed_COR_Expressions.Typed_Composition):
			lhs2, rhs2 = rhs1.argument1, rhs1.argument2
			if str(A)==str(lhs2):
				if isinstance(rhs2, Typed_COR_Expressions.Typed_UniversalRelation):
					return ("(A[P*P]) ∪ ((A[P*P]) ∘ (T[P*P])) = (A[P*P]) ∘ (T[P*P])", Typed_COR_Expressions.Typed_Composition(A, Typed_COR_Expressions.Typed_UniversalRelation(A.type()[1], expression.type()[1])))
			if isinstance(lhs2, Typed_COR_Expressions.Typed_UniversalRelation):
				if str(A)==str(rhs2):
					return ("(A[P*P]) ∪ ((T[P*P]) ∘ (A[P*P])) = (T[P*P]) ∘ (A[P*P])", Typed_COR_Expressions.Typed_Composition(Typed_COR_Expressions.Typed_UniversalRelation(expression.type()[0], A.type()[0]), A))
		if isinstance(rhs1, Typed_COR_Expressions.Typed_Dagger):
			lhs2, rhs2 = rhs1.argument1, rhs1.argument2
			if isinstance(lhs2, Typed_COR_Expressions.Typed_EmptyRelation):
				if str(A)==str(rhs2):
					return ("(A[P*P]) ∪ ((𝟎[P*P]) † (A[P*P])) = A[P*P]", A)
			if str(A)==str(lhs2):
				if isinstance(rhs2, Typed_COR_Expressions.Typed_EmptyRelation):
					return ("(A[P*P]) ∪ ((A[P*P]) † (𝟎[P*P])) = A[P*P]", A)
		if isinstance(lhs1, Typed_COR_Expressions.Typed_Union):
			lhs2, rhs2 = lhs1.argument1, lhs1.argument2
			A = lhs2
			B = rhs2
			if str(B)==str(rhs1):
				return ("((A[P*P]) ∪ (B[P*P])) ∪ (B[P*P]) = (B[P*P]) ∪ (A[P*P])", Typed_COR_Expressions.Typed_Union(B, A))
			if str(A)==str(rhs1):
				return ("((A[P*P]) ∪ (B[P*P])) ∪ (A[P*P]) = (A[P*P]) ∪ (B[P*P])", Typed_COR_Expressions.Typed_Union(A, B))
			if isinstance(rhs1, Typed_COR_Expressions.Typed_Union):
				lhs3, rhs3 = rhs1.argument1, rhs1.argument2
				if str(A)==str(lhs3):
					C = rhs3
					return ("((A[P*P]) ∪ (B[P*P])) ∪ ((A[P*P]) ∪ (C[P*P])) = ((A[P*P]) ∪ (B[P*P])) ∪ (C[P*P])", Typed_COR_Expressions.Typed_Union(Typed_COR_Expressions.Typed_Union(A, B), C))
				if str(B)==str(lhs3):
					C = rhs3
					return ("((A[P*P]) ∪ (B[P*P])) ∪ ((B[P*P]) ∪ (C[P*P])) = (C[P*P]) ∪ ((B[P*P]) ∪ (A[P*P]))", Typed_COR_Expressions.Typed_Union(C, Typed_COR_Expressions.Typed_Union(B, A)))
				C = lhs3
				if str(B)==str(rhs3):
					return ("((A[P*P]) ∪ (B[P*P])) ∪ ((C[P*P]) ∪ (B[P*P])) = ((A[P*P]) ∪ (C[P*P])) ∪ (B[P*P])", Typed_COR_Expressions.Typed_Union(Typed_COR_Expressions.Typed_Union(A, C), B))
				if str(A)==str(rhs3):
					return ("((A[P*P]) ∪ (B[P*P])) ∪ ((C[P*P]) ∪ (A[P*P])) = (B[P*P]) ∪ ((A[P*P]) ∪ (C[P*P]))", Typed_COR_Expressions.Typed_Union(B, Typed_COR_Expressions.Typed_Union(A, C)))
			if isinstance(rhs1, Typed_COR_Expressions.Typed_Complement):
				arg = rhs1.argument
				if str(B)==str(arg):
					return ("((A[P*P]) ∪ (B[P*P])) ∪ ((B[P*P])⁻) = T[P*P]", Typed_COR_Expressions.Typed_UniversalRelation(expression.type()[0], expression.type()[1]))
				if str(A)==str(arg):
					return ("((A[P*P]) ∪ (B[P*P])) ∪ ((A[P*P])⁻) = T[P*P]", Typed_COR_Expressions.Typed_UniversalRelation(expression.type()[0], expression.type()[1]))
			if isinstance(rhs1, Typed_COR_Expressions.Typed_Intersection):
				lhs3, rhs3 = rhs1.argument1, rhs1.argument2
				if str(B)==str(lhs3):
					C = rhs3
					return ("((A[P*P]) ∪ (B[P*P])) ∪ ((B[P*P]) ∩ (C[P*P])) = (A[P*P]) ∪ (B[P*P])", Typed_COR_Expressions.Typed_Union(A, B))
				if str(A)==str(lhs3):
					C = rhs3
					return ("((A[P*P]) ∪ (B[P*P])) ∪ ((A[P*P]) ∩ (C[P*P])) = (A[P*P]) ∪ (B[P*P])", Typed_COR_Expressions.Typed_Union(A, B))
				C = lhs3
				if str(A)==str(rhs3):
					return ("((A[P*P]) ∪ (B[P*P])) ∪ ((C[P*P]) ∩ (A[P*P])) = (B[P*P]) ∪ (A[P*P])", Typed_COR_Expressions.Typed_Union(B, A))
				if str(B)==str(rhs3):
					return ("((A[P*P]) ∪ (B[P*P])) ∪ ((C[P*P]) ∩ (B[P*P])) = (B[P*P]) ∪ (A[P*P])", Typed_COR_Expressions.Typed_Union(B, A))
			if isinstance(rhs2, Typed_COR_Expressions.Typed_Union):
				lhs3, rhs3 = rhs2.argument1, rhs2.argument2
				B = lhs3
				C = rhs3
				if str(C)==str(rhs1):
					return ("((A[P*P]) ∪ ((B[P*P]) ∪ (C[P*P]))) ∪ (C[P*P]) = (B[P*P]) ∪ ((A[P*P]) ∪ (C[P*P]))", Typed_COR_Expressions.Typed_Union(B, Typed_COR_Expressions.Typed_Union(A, C)))
				if str(B)==str(rhs1):
					return ("((A[P*P]) ∪ ((B[P*P]) ∪ (C[P*P]))) ∪ (B[P*P]) = (A[P*P]) ∪ ((C[P*P]) ∪ (B[P*P]))", Typed_COR_Expressions.Typed_Union(A, Typed_COR_Expressions.Typed_Union(C, B)))
			if isinstance(rhs2, Typed_COR_Expressions.Typed_Intersection):
				lhs3, rhs3 = rhs2.argument1, rhs2.argument2
				B = lhs3
				C = rhs3
				if str(B)==str(rhs1):
					return ("((A[P*P]) ∪ ((B[P*P]) ∩ (C[P*P]))) ∪ (B[P*P]) = (A[P*P]) ∪ (B[P*P])", Typed_COR_Expressions.Typed_Union(A, B))
				if str(C)==str(rhs1):
					return ("((A[P*P]) ∪ ((B[P*P]) ∩ (C[P*P]))) ∪ (C[P*P]) = (C[P*P]) ∪ (A[P*P])", Typed_COR_Expressions.Typed_Union(C, A))
			if isinstance(rhs2, Typed_COR_Expressions.Typed_Complement):
				arg = rhs2.argument
				B = arg
				if str(B)==str(rhs1):
					return ("((A[P*P]) ∪ ((B[P*P])⁻)) ∪ (B[P*P]) = T[P*P]", Typed_COR_Expressions.Typed_UniversalRelation(expression.type()[0], expression.type()[1]))
			if isinstance(lhs2, Typed_COR_Expressions.Typed_Union):
				lhs3, rhs3 = lhs2.argument1, lhs2.argument2
				A = lhs3
				B = rhs3
				C = rhs2
				if str(B)==str(rhs1):
					return ("(((A[P*P]) ∪ (B[P*P])) ∪ (C[P*P])) ∪ (B[P*P]) = (A[P*P]) ∪ ((C[P*P]) ∪ (B[P*P]))", Typed_COR_Expressions.Typed_Union(A, Typed_COR_Expressions.Typed_Union(C, B)))
				if str(A)==str(rhs1):
					return ("(((A[P*P]) ∪ (B[P*P])) ∪ (C[P*P])) ∪ (A[P*P]) = (C[P*P]) ∪ ((A[P*P]) ∪ (B[P*P]))", Typed_COR_Expressions.Typed_Union(C, Typed_COR_Expressions.Typed_Union(A, B)))
			if isinstance(lhs2, Typed_COR_Expressions.Typed_Complement):
				arg = lhs2.argument
				A = arg
				B = rhs2
				if str(A)==str(rhs1):
					return ("(((A[P*P])⁻) ∪ (B[P*P])) ∪ (A[P*P]) = T[P*P]", Typed_COR_Expressions.Typed_UniversalRelation(expression.type()[0], expression.type()[1]))
			if isinstance(lhs2, Typed_COR_Expressions.Typed_Intersection):
				lhs3, rhs3 = lhs2.argument1, lhs2.argument2
				A = lhs3
				B = rhs3
				C = rhs2
				if str(B)==str(rhs1):
					return ("(((A[P*P]) ∩ (B[P*P])) ∪ (C[P*P])) ∪ (B[P*P]) = (C[P*P]) ∪ (B[P*P])", Typed_COR_Expressions.Typed_Union(C, B))
				if str(A)==str(rhs1):
					return ("(((A[P*P]) ∩ (B[P*P])) ∪ (C[P*P])) ∪ (A[P*P]) = (C[P*P]) ∪ (A[P*P])", Typed_COR_Expressions.Typed_Union(C, A))
		if isinstance(lhs1, Typed_COR_Expressions.Typed_Complement):
			arg = lhs1.argument
			A = arg
			if str(A)==str(rhs1):
				return ("((A[P*P])⁻) ∪ (A[P*P]) = T[P*P]", Typed_COR_Expressions.Typed_UniversalRelation(expression.type()[0], expression.type()[1]))
			if isinstance(rhs1, Typed_COR_Expressions.Typed_Union):
				lhs3, rhs3 = rhs1.argument1, rhs1.argument2
				B = lhs3
				if str(A)==str(rhs3):
					return ("((A[P*P])⁻) ∪ ((B[P*P]) ∪ (A[P*P])) = T[P*P]", Typed_COR_Expressions.Typed_UniversalRelation(expression.type()[0], expression.type()[1]))
				if str(A)==str(lhs3):
					B = rhs3
					return ("((A[P*P])⁻) ∪ ((A[P*P]) ∪ (B[P*P])) = T[P*P]", Typed_COR_Expressions.Typed_UniversalRelation(expression.type()[0], expression.type()[1]))
			if isinstance(rhs1, Typed_COR_Expressions.Typed_Complement):
				arg = rhs1.argument
				B = arg
				return ("((A[P*P])⁻) ∪ ((B[P*P])⁻) = ((A[P*P]) ∩ (B[P*P]))⁻", Typed_COR_Expressions.Typed_Complement(Typed_COR_Expressions.Typed_Intersection(A, B)))
			if isinstance(rhs1, Typed_COR_Expressions.Typed_Intersection):
				lhs3, rhs3 = rhs1.argument1, rhs1.argument2
				if str(A)==str(lhs3):
					B = rhs3
					return ("((A[P*P])⁻) ∪ ((A[P*P]) ∩ (B[P*P])) = (B[P*P]) ∪ ((A[P*P])⁻)", Typed_COR_Expressions.Typed_Union(B, Typed_COR_Expressions.Typed_Complement(A)))
				B = lhs3
				if str(A)==str(rhs3):
					return ("((A[P*P])⁻) ∪ ((B[P*P]) ∩ (A[P*P])) = (B[P*P]) ∪ ((A[P*P])⁻)", Typed_COR_Expressions.Typed_Union(B, Typed_COR_Expressions.Typed_Complement(A)))
			if isinstance(arg, Typed_COR_Expressions.Typed_Union):
				lhs3, rhs3 = arg.argument1, arg.argument2
				A = lhs3
				B = rhs3
				if str(B)==str(rhs1):
					return ("(((A[P*P]) ∪ (B[P*P]))⁻) ∪ (B[P*P]) = ((A[P*P])⁻) ∪ (B[P*P])", Typed_COR_Expressions.Typed_Union(Typed_COR_Expressions.Typed_Complement(A), B))
				if str(A)==str(rhs1):
					return ("(((A[P*P]) ∪ (B[P*P]))⁻) ∪ (A[P*P]) = ((B[P*P])⁻) ∪ (A[P*P])", Typed_COR_Expressions.Typed_Union(Typed_COR_Expressions.Typed_Complement(B), A))
			if isinstance(arg, Typed_COR_Expressions.Typed_Intersection):
				lhs3, rhs3 = arg.argument1, arg.argument2
				A = lhs3
				B = rhs3
				if str(B)==str(rhs1):
					return ("(((A[P*P]) ∩ (B[P*P]))⁻) ∪ (B[P*P]) = T[P*P]", Typed_COR_Expressions.Typed_UniversalRelation(expression.type()[0], expression.type()[1]))
				if str(A)==str(rhs1):
					return ("(((A[P*P]) ∩ (B[P*P]))⁻) ∪ (A[P*P]) = T[P*P]", Typed_COR_Expressions.Typed_UniversalRelation(expression.type()[0], expression.type()[1]))
		if isinstance(lhs1, Typed_COR_Expressions.Typed_UniversalRelation):
			A = rhs1
			return ("(T[P*P]) ∪ (A[P*P]) = T[P*P]", Typed_COR_Expressions.Typed_UniversalRelation(expression.type()[0], expression.type()[1]))
		if isinstance(lhs1, Typed_COR_Expressions.Typed_Intersection):
			lhs2, rhs2 = lhs1.argument1, lhs1.argument2
			A = lhs2
			B = rhs2
			if str(A)==str(rhs1):
				return ("((A[P*P]) ∩ (B[P*P])) ∪ (A[P*P]) = A[P*P]", A)
			if str(B)==str(rhs1):
				return ("((A[P*P]) ∩ (B[P*P])) ∪ (B[P*P]) = B[P*P]", B)
			if isinstance(rhs1, Typed_COR_Expressions.Typed_Intersection):
				lhs3, rhs3 = rhs1.argument1, rhs1.argument2
				if str(B)==str(lhs3):
					C = rhs3
					return ("((A[P*P]) ∩ (B[P*P])) ∪ ((B[P*P]) ∩ (C[P*P])) = ((C[P*P]) ∪ (A[P*P])) ∩ (B[P*P])", Typed_COR_Expressions.Typed_Intersection(Typed_COR_Expressions.Typed_Union(C, A), B))
				if str(A)==str(lhs3):
					C = rhs3
					return ("((A[P*P]) ∩ (B[P*P])) ∪ ((A[P*P]) ∩ (C[P*P])) = ((B[P*P]) ∪ (C[P*P])) ∩ (A[P*P])", Typed_COR_Expressions.Typed_Intersection(Typed_COR_Expressions.Typed_Union(B, C), A))
				C = lhs3
				if str(B)==str(rhs3):
					return ("((A[P*P]) ∩ (B[P*P])) ∪ ((C[P*P]) ∩ (B[P*P])) = (B[P*P]) ∩ ((C[P*P]) ∪ (A[P*P]))", Typed_COR_Expressions.Typed_Intersection(B, Typed_COR_Expressions.Typed_Union(C, A)))
				if str(A)==str(rhs3):
					return ("((A[P*P]) ∩ (B[P*P])) ∪ ((C[P*P]) ∩ (A[P*P])) = (A[P*P]) ∩ ((B[P*P]) ∪ (C[P*P]))", Typed_COR_Expressions.Typed_Intersection(A, Typed_COR_Expressions.Typed_Union(B, C)))
			if isinstance(rhs1, Typed_COR_Expressions.Typed_Union):
				lhs3, rhs3 = rhs1.argument1, rhs1.argument2
				C = lhs3
				if str(B)==str(rhs3):
					return ("((A[P*P]) ∩ (B[P*P])) ∪ ((C[P*P]) ∪ (B[P*P])) = (B[P*P]) ∪ (C[P*P])", Typed_COR_Expressions.Typed_Union(B, C))
				if str(A)==str(rhs3):
					return ("((A[P*P]) ∩ (B[P*P])) ∪ ((C[P*P]) ∪ (A[P*P])) = (A[P*P]) ∪ (C[P*P])", Typed_COR_Expressions.Typed_Union(A, C))
				if str(B)==str(lhs3):
					C = rhs3
					return ("((A[P*P]) ∩ (B[P*P])) ∪ ((B[P*P]) ∪ (C[P*P])) = (B[P*P]) ∪ (C[P*P])", Typed_COR_Expressions.Typed_Union(B, C))
				if str(A)==str(lhs3):
					C = rhs3
					return ("((A[P*P]) ∩ (B[P*P])) ∪ ((A[P*P]) ∪ (C[P*P])) = (C[P*P]) ∪ (A[P*P])", Typed_COR_Expressions.Typed_Union(C, A))
			if isinstance(rhs1, Typed_COR_Expressions.Typed_Complement):
				arg = rhs1.argument
				if str(B)==str(arg):
					return ("((A[P*P]) ∩ (B[P*P])) ∪ ((B[P*P])⁻) = ((B[P*P])⁻) ∪ (A[P*P])", Typed_COR_Expressions.Typed_Union(Typed_COR_Expressions.Typed_Complement(B), A))
				if str(A)==str(arg):
					return ("((A[P*P]) ∩ (B[P*P])) ∪ ((A[P*P])⁻) = ((A[P*P])⁻) ∪ (B[P*P])", Typed_COR_Expressions.Typed_Union(Typed_COR_Expressions.Typed_Complement(A), B))
			if isinstance(rhs2, Typed_COR_Expressions.Typed_Union):
				lhs3, rhs3 = rhs2.argument1, rhs2.argument2
				B = lhs3
				C = rhs3
				if str(B)==str(rhs1):
					return ("((A[P*P]) ∩ ((B[P*P]) ∪ (C[P*P]))) ∪ (B[P*P]) = (B[P*P]) ∪ ((C[P*P]) ∩ (A[P*P]))", Typed_COR_Expressions.Typed_Union(B, Typed_COR_Expressions.Typed_Intersection(C, A)))
				if str(C)==str(rhs1):
					return ("((A[P*P]) ∩ ((B[P*P]) ∪ (C[P*P]))) ∪ (C[P*P]) = ((B[P*P]) ∩ (A[P*P])) ∪ (C[P*P])", Typed_COR_Expressions.Typed_Union(Typed_COR_Expressions.Typed_Intersection(B, A), C))
			if isinstance(rhs2, Typed_COR_Expressions.Typed_Complement):
				arg = rhs2.argument
				B = arg
				if str(B)==str(rhs1):
					return ("((A[P*P]) ∩ ((B[P*P])⁻)) ∪ (B[P*P]) = (B[P*P]) ∪ (A[P*P])", Typed_COR_Expressions.Typed_Union(B, A))
			if isinstance(rhs2, Typed_COR_Expressions.Typed_Intersection):
				lhs3, rhs3 = rhs2.argument1, rhs2.argument2
				B = lhs3
				C = rhs3
				if str(B)==str(rhs1):
					return ("((A[P*P]) ∩ ((B[P*P]) ∩ (C[P*P]))) ∪ (B[P*P]) = B[P*P]", B)
				if str(C)==str(rhs1):
					return ("((A[P*P]) ∩ ((B[P*P]) ∩ (C[P*P]))) ∪ (C[P*P]) = C[P*P]", C)
			if isinstance(lhs2, Typed_COR_Expressions.Typed_Union):
				lhs3, rhs3 = lhs2.argument1, lhs2.argument2
				A = lhs3
				B = rhs3
				C = rhs2
				if str(B)==str(rhs1):
					return ("(((A[P*P]) ∪ (B[P*P])) ∩ (C[P*P])) ∪ (B[P*P]) = (B[P*P]) ∪ ((A[P*P]) ∩ (C[P*P]))", Typed_COR_Expressions.Typed_Union(B, Typed_COR_Expressions.Typed_Intersection(A, C)))
				if str(A)==str(rhs1):
					return ("(((A[P*P]) ∪ (B[P*P])) ∩ (C[P*P])) ∪ (A[P*P]) = ((B[P*P]) ∩ (C[P*P])) ∪ (A[P*P])", Typed_COR_Expressions.Typed_Union(Typed_COR_Expressions.Typed_Intersection(B, C), A))
			if isinstance(lhs2, Typed_COR_Expressions.Typed_Intersection):
				lhs3, rhs3 = lhs2.argument1, lhs2.argument2
				A = lhs3
				B = rhs3
				C = rhs2
				if str(B)==str(rhs1):
					return ("(((A[P*P]) ∩ (B[P*P])) ∩ (C[P*P])) ∪ (B[P*P]) = B[P*P]", B)
				if str(A)==str(rhs1):
					return ("(((A[P*P]) ∩ (B[P*P])) ∩ (C[P*P])) ∪ (A[P*P]) = A[P*P]", A)
			if isinstance(lhs2, Typed_COR_Expressions.Typed_Complement):
				arg = lhs2.argument
				A = arg
				B = rhs2
				if str(A)==str(rhs1):
					return ("(((A[P*P])⁻) ∩ (B[P*P])) ∪ (A[P*P]) = (A[P*P]) ∪ (B[P*P])", Typed_COR_Expressions.Typed_Union(A, B))
		if isinstance(lhs1, Typed_COR_Expressions.Typed_EmptyRelation):
			A = rhs1
			return ("(𝟎[P*P]) ∪ (A[P*P]) = A[P*P]", A)
		if isinstance(lhs1, Typed_COR_Expressions.Typed_Composition):
			lhs2, rhs2 = lhs1.argument1, lhs1.argument2
			A = lhs2
			B = rhs2
			if isinstance(rhs1, Typed_COR_Expressions.Typed_Composition):
				lhs3, rhs3 = rhs1.argument1, rhs1.argument2
				if str(A)==str(lhs3):
					C = rhs3
					return ("((A[P*P]) ∘ (B[P*P])) ∪ ((A[P*P]) ∘ (C[P*P])) = (A[P*P]) ∘ ((B[P*P]) ∪ (C[P*P]))", Typed_COR_Expressions.Typed_Composition(A, Typed_COR_Expressions.Typed_Union(B, C)))
				C = lhs3
				if str(B)==str(rhs3):
					return ("((A[P*P]) ∘ (B[P*P])) ∪ ((C[P*P]) ∘ (B[P*P])) = ((C[P*P]) ∪ (A[P*P])) ∘ (B[P*P])", Typed_COR_Expressions.Typed_Composition(Typed_COR_Expressions.Typed_Union(C, A), B))
			if isinstance(rhs2, Typed_COR_Expressions.Typed_UniversalRelation):
				if str(A)==str(rhs1):
					return ("((A[P*P]) ∘ (T[P*P])) ∪ (A[P*P]) = (A[P*P]) ∘ (T[P*P])", Typed_COR_Expressions.Typed_Composition(A, Typed_COR_Expressions.Typed_UniversalRelation(A.type()[1], expression.type()[1])))
			if isinstance(lhs2, Typed_COR_Expressions.Typed_UniversalRelation):
				A = rhs2
				if str(A)==str(rhs1):
					return ("((T[P*P]) ∘ (A[P*P])) ∪ (A[P*P]) = (T[P*P]) ∘ (A[P*P])", Typed_COR_Expressions.Typed_Composition(Typed_COR_Expressions.Typed_UniversalRelation(expression.type()[0], A.type()[0]), A))
		if isinstance(lhs1, Typed_COR_Expressions.Typed_Dagger):
			lhs2, rhs2 = lhs1.argument1, lhs1.argument2
			A = lhs2
			if isinstance(rhs2, Typed_COR_Expressions.Typed_EmptyRelation):
				if str(A)==str(rhs1):
					return ("((A[P*P]) † (𝟎[P*P])) ∪ (A[P*P]) = A[P*P]", A)
			if isinstance(lhs2, Typed_COR_Expressions.Typed_EmptyRelation):
				A = rhs2
				if str(A)==str(rhs1):
					return ("((𝟎[P*P]) † (A[P*P])) ∪ (A[P*P]) = A[P*P]", A)
		if isinstance(lhs1, Typed_COR_Expressions.Typed_Converse):
			arg = lhs1.argument
			A = arg
			if isinstance(rhs1, Typed_COR_Expressions.Typed_Converse):
				arg = rhs1.argument
				B = arg
				return ("((A[P*P])⁻¹) ∪ ((B[P*P])⁻¹) = ((A[P*P]) ∪ (B[P*P]))⁻¹", Typed_COR_Expressions.Typed_Converse(Typed_COR_Expressions.Typed_Union(A, B)))
	if isinstance(expression, Typed_COR_Expressions.Typed_Intersection):
		lhs1, rhs1 = expression.argument1, expression.argument2
		A = lhs1
		if str(A)==str(rhs1):
			return ("(A[P*P]) ∩ (A[P*P]) = A[P*P]", A)
		if isinstance(rhs1, Typed_COR_Expressions.Typed_Complement):
			arg = rhs1.argument
			if str(A)==str(arg):
				return ("(A[P*P]) ∩ ((A[P*P])⁻) = 𝟎[P*P]", Typed_COR_Expressions.Typed_EmptyRelation(expression.type()[0], expression.type()[1]))
			if isinstance(arg, Typed_COR_Expressions.Typed_Intersection):
				lhs3, rhs3 = arg.argument1, arg.argument2
				if str(A)==str(lhs3):
					B = rhs3
					return ("(A[P*P]) ∩ (((A[P*P]) ∩ (B[P*P]))⁻) = (A[P*P]) ∩ ((B[P*P])⁻)", Typed_COR_Expressions.Typed_Intersection(A, Typed_COR_Expressions.Typed_Complement(B)))
				B = lhs3
				if str(A)==str(rhs3):
					return ("(A[P*P]) ∩ (((B[P*P]) ∩ (A[P*P]))⁻) = (A[P*P]) ∩ ((B[P*P])⁻)", Typed_COR_Expressions.Typed_Intersection(A, Typed_COR_Expressions.Typed_Complement(B)))
			if isinstance(arg, Typed_COR_Expressions.Typed_Union):
				lhs3, rhs3 = arg.argument1, arg.argument2
				if str(A)==str(lhs3):
					B = rhs3
					return ("(A[P*P]) ∩ (((A[P*P]) ∪ (B[P*P]))⁻) = 𝟎[P*P]", Typed_COR_Expressions.Typed_EmptyRelation(expression.type()[0], expression.type()[1]))
				B = lhs3
				if str(A)==str(rhs3):
					return ("(A[P*P]) ∩ (((B[P*P]) ∪ (A[P*P]))⁻) = 𝟎[P*P]", Typed_COR_Expressions.Typed_EmptyRelation(expression.type()[0], expression.type()[1]))
		if isinstance(rhs1, Typed_COR_Expressions.Typed_UniversalRelation):
			return ("(A[P*P]) ∩ (T[P*P]) = A[P*P]", A)
		if isinstance(rhs1, Typed_COR_Expressions.Typed_Intersection):
			lhs2, rhs2 = rhs1.argument1, rhs1.argument2
			B = lhs2
			if str(A)==str(rhs2):
				return ("(A[P*P]) ∩ ((B[P*P]) ∩ (A[P*P])) = (B[P*P]) ∩ (A[P*P])", Typed_COR_Expressions.Typed_Intersection(B, A))
			if isinstance(rhs2, Typed_COR_Expressions.Typed_Intersection):
				lhs3, rhs3 = rhs2.argument1, rhs2.argument2
				C = lhs3
				if str(A)==str(rhs3):
					return ("(A[P*P]) ∩ ((B[P*P]) ∩ ((C[P*P]) ∩ (A[P*P]))) = ((B[P*P]) ∩ (A[P*P])) ∩ (C[P*P])", Typed_COR_Expressions.Typed_Intersection(Typed_COR_Expressions.Typed_Intersection(B, A), C))
				if str(A)==str(lhs3):
					C = rhs3
					return ("(A[P*P]) ∩ ((B[P*P]) ∩ ((A[P*P]) ∩ (C[P*P]))) = ((B[P*P]) ∩ (C[P*P])) ∩ (A[P*P])", Typed_COR_Expressions.Typed_Intersection(Typed_COR_Expressions.Typed_Intersection(B, C), A))
			if isinstance(rhs2, Typed_COR_Expressions.Typed_Union):
				lhs3, rhs3 = rhs2.argument1, rhs2.argument2
				C = lhs3
				if str(A)==str(rhs3):
					return ("(A[P*P]) ∩ ((B[P*P]) ∩ ((C[P*P]) ∪ (A[P*P]))) = (A[P*P]) ∩ (B[P*P])", Typed_COR_Expressions.Typed_Intersection(A, B))
				if str(A)==str(lhs3):
					C = rhs3
					return ("(A[P*P]) ∩ ((B[P*P]) ∩ ((A[P*P]) ∪ (C[P*P]))) = (A[P*P]) ∩ (B[P*P])", Typed_COR_Expressions.Typed_Intersection(A, B))
			if isinstance(rhs2, Typed_COR_Expressions.Typed_Complement):
				arg = rhs2.argument
				if str(A)==str(arg):
					return ("(A[P*P]) ∩ ((B[P*P]) ∩ ((A[P*P])⁻)) = 𝟎[P*P]", Typed_COR_Expressions.Typed_EmptyRelation(expression.type()[0], expression.type()[1]))
			if str(A)==str(lhs2):
				B = rhs2
				return ("(A[P*P]) ∩ ((A[P*P]) ∩ (B[P*P])) = (A[P*P]) ∩ (B[P*P])", Typed_COR_Expressions.Typed_Intersection(A, B))
			if isinstance(lhs2, Typed_COR_Expressions.Typed_Intersection):
				lhs3, rhs3 = lhs2.argument1, lhs2.argument2
				B = lhs3
				if str(A)==str(rhs3):
					C = rhs2
					return ("(A[P*P]) ∩ (((B[P*P]) ∩ (A[P*P])) ∩ (C[P*P])) = ((A[P*P]) ∩ (C[P*P])) ∩ (B[P*P])", Typed_COR_Expressions.Typed_Intersection(Typed_COR_Expressions.Typed_Intersection(A, C), B))
				if str(A)==str(lhs3):
					B = rhs3
					C = rhs2
					return ("(A[P*P]) ∩ (((A[P*P]) ∩ (B[P*P])) ∩ (C[P*P])) = ((A[P*P]) ∩ (B[P*P])) ∩ (C[P*P])", Typed_COR_Expressions.Typed_Intersection(Typed_COR_Expressions.Typed_Intersection(A, B), C))
			if isinstance(lhs2, Typed_COR_Expressions.Typed_Union):
				lhs3, rhs3 = lhs2.argument1, lhs2.argument2
				B = lhs3
				if str(A)==str(rhs3):
					C = rhs2
					return ("(A[P*P]) ∩ (((B[P*P]) ∪ (A[P*P])) ∩ (C[P*P])) = (C[P*P]) ∩ (A[P*P])", Typed_COR_Expressions.Typed_Intersection(C, A))
				if str(A)==str(lhs3):
					B = rhs3
					C = rhs2
					return ("(A[P*P]) ∩ (((A[P*P]) ∪ (B[P*P])) ∩ (C[P*P])) = (C[P*P]) ∩ (A[P*P])", Typed_COR_Expressions.Typed_Intersection(C, A))
			if isinstance(lhs2, Typed_COR_Expressions.Typed_Complement):
				arg = lhs2.argument
				if str(A)==str(arg):
					B = rhs2
					return ("(A[P*P]) ∩ (((A[P*P])⁻) ∩ (B[P*P])) = 𝟎[P*P]", Typed_COR_Expressions.Typed_EmptyRelation(expression.type()[0], expression.type()[1]))
		if isinstance(rhs1, Typed_COR_Expressions.Typed_Union):
			lhs2, rhs2 = rhs1.argument1, rhs1.argument2
			B = lhs2
			if str(A)==str(rhs2):
				return ("(A[P*P]) ∩ ((B[P*P]) ∪ (A[P*P])) = A[P*P]", A)
			if isinstance(rhs2, Typed_COR_Expressions.Typed_Intersection):
				lhs3, rhs3 = rhs2.argument1, rhs2.argument2
				C = lhs3
				if str(A)==str(rhs3):
					return ("(A[P*P]) ∩ ((B[P*P]) ∪ ((C[P*P]) ∩ (A[P*P]))) = ((C[P*P]) ∪ (B[P*P])) ∩ (A[P*P])", Typed_COR_Expressions.Typed_Intersection(Typed_COR_Expressions.Typed_Union(C, B), A))
				if str(A)==str(lhs3):
					C = rhs3
					return ("(A[P*P]) ∩ ((B[P*P]) ∪ ((A[P*P]) ∩ (C[P*P]))) = ((B[P*P]) ∪ (C[P*P])) ∩ (A[P*P])", Typed_COR_Expressions.Typed_Intersection(Typed_COR_Expressions.Typed_Union(B, C), A))
			if isinstance(rhs2, Typed_COR_Expressions.Typed_Union):
				lhs3, rhs3 = rhs2.argument1, rhs2.argument2
				if str(A)==str(lhs3):
					C = rhs3
					return ("(A[P*P]) ∩ ((B[P*P]) ∪ ((A[P*P]) ∪ (C[P*P]))) = A[P*P]", A)
				C = lhs3
				if str(A)==str(rhs3):
					return ("(A[P*P]) ∩ ((B[P*P]) ∪ ((C[P*P]) ∪ (A[P*P]))) = A[P*P]", A)
			if isinstance(rhs2, Typed_COR_Expressions.Typed_Complement):
				arg = rhs2.argument
				if str(A)==str(arg):
					return ("(A[P*P]) ∩ ((B[P*P]) ∪ ((A[P*P])⁻)) = (B[P*P]) ∩ (A[P*P])", Typed_COR_Expressions.Typed_Intersection(B, A))
			if str(A)==str(lhs2):
				B = rhs2
				return ("(A[P*P]) ∩ ((A[P*P]) ∪ (B[P*P])) = A[P*P]", A)
			if isinstance(lhs2, Typed_COR_Expressions.Typed_Intersection):
				lhs3, rhs3 = lhs2.argument1, lhs2.argument2
				B = lhs3
				if str(A)==str(rhs3):
					C = rhs2
					return ("(A[P*P]) ∩ (((B[P*P]) ∩ (A[P*P])) ∪ (C[P*P])) = ((C[P*P]) ∪ (B[P*P])) ∩ (A[P*P])", Typed_COR_Expressions.Typed_Intersection(Typed_COR_Expressions.Typed_Union(C, B), A))
				if str(A)==str(lhs3):
					B = rhs3
					C = rhs2
					return ("(A[P*P]) ∩ (((A[P*P]) ∩ (B[P*P])) ∪ (C[P*P])) = ((C[P*P]) ∪ (B[P*P])) ∩ (A[P*P])", Typed_COR_Expressions.Typed_Intersection(Typed_COR_Expressions.Typed_Union(C, B), A))
			if isinstance(lhs2, Typed_COR_Expressions.Typed_Complement):
				arg = lhs2.argument
				if str(A)==str(arg):
					B = rhs2
					return ("(A[P*P]) ∩ (((A[P*P])⁻) ∪ (B[P*P])) = (A[P*P]) ∩ (B[P*P])", Typed_COR_Expressions.Typed_Intersection(A, B))
			if isinstance(lhs2, Typed_COR_Expressions.Typed_Union):
				lhs3, rhs3 = lhs2.argument1, lhs2.argument2
				if str(A)==str(lhs3):
					B = rhs3
					C = rhs2
					return ("(A[P*P]) ∩ (((A[P*P]) ∪ (B[P*P])) ∪ (C[P*P])) = A[P*P]", A)
				B = lhs3
				if str(A)==str(rhs3):
					C = rhs2
					return ("(A[P*P]) ∩ (((B[P*P]) ∪ (A[P*P])) ∪ (C[P*P])) = A[P*P]", A)
		if isinstance(rhs1, Typed_COR_Expressions.Typed_EmptyRelation):
			return ("(A[P*P]) ∩ (𝟎[P*P]) = 𝟎[P*P]", Typed_COR_Expressions.Typed_EmptyRelation(expression.type()[0], expression.type()[1]))
		if isinstance(rhs1, Typed_COR_Expressions.Typed_Dagger):
			lhs2, rhs2 = rhs1.argument1, rhs1.argument2
			if str(A)==str(lhs2):
				if isinstance(rhs2, Typed_COR_Expressions.Typed_IdentityRelation):
					return ("(A[P*P]) ∩ ((A[P*P]) † (𝟏[P*P])) = (A[P*P]) † (𝟎[P*P])", Typed_COR_Expressions.Typed_Dagger(A, Typed_COR_Expressions.Typed_EmptyRelation(A.type()[1], expression.type()[1])))
				if isinstance(rhs2, Typed_COR_Expressions.Typed_EmptyRelation):
					return ("(A[P*P]) ∩ ((A[P*P]) † (𝟎[P*P])) = (A[P*P]) † (𝟎[P*P])", Typed_COR_Expressions.Typed_Dagger(A, Typed_COR_Expressions.Typed_EmptyRelation(A.type()[1], expression.type()[1])))
			if isinstance(lhs2, Typed_COR_Expressions.Typed_EmptyRelation):
				if str(A)==str(rhs2):
					return ("(A[P*P]) ∩ ((𝟎[P*P]) † (A[P*P])) = (𝟎[P*P]) † (A[P*P])", Typed_COR_Expressions.Typed_Dagger(Typed_COR_Expressions.Typed_EmptyRelation(expression.type()[0], A.type()[0]), A))
			if isinstance(lhs2, Typed_COR_Expressions.Typed_IdentityRelation):
				if str(A)==str(rhs2):
					return ("(A[P*P]) ∩ ((𝟏[P*P]) † (A[P*P])) = (𝟎[P*P]) † (A[P*P])", Typed_COR_Expressions.Typed_Dagger(Typed_COR_Expressions.Typed_EmptyRelation(expression.type()[0], A.type()[0]), A))
		if isinstance(rhs1, Typed_COR_Expressions.Typed_Composition):
			lhs2, rhs2 = rhs1.argument1, rhs1.argument2
			if str(A)==str(lhs2):
				if isinstance(rhs2, Typed_COR_Expressions.Typed_UniversalRelation):
					return ("(A[P*P]) ∩ ((A[P*P]) ∘ (T[P*P])) = A[P*P]", A)
			if isinstance(lhs2, Typed_COR_Expressions.Typed_UniversalRelation):
				if str(A)==str(rhs2):
					return ("(A[P*P]) ∩ ((T[P*P]) ∘ (A[P*P])) = A[P*P]", A)
		if isinstance(lhs1, Typed_COR_Expressions.Typed_Intersection):
			lhs2, rhs2 = lhs1.argument1, lhs1.argument2
			A = lhs2
			B = rhs2
			if str(B)==str(rhs1):
				return ("((A[P*P]) ∩ (B[P*P])) ∩ (B[P*P]) = (A[P*P]) ∩ (B[P*P])", Typed_COR_Expressions.Typed_Intersection(A, B))
			if str(A)==str(rhs1):
				return ("((A[P*P]) ∩ (B[P*P])) ∩ (A[P*P]) = (B[P*P]) ∩ (A[P*P])", Typed_COR_Expressions.Typed_Intersection(B, A))
			if isinstance(rhs1, Typed_COR_Expressions.Typed_Intersection):
				lhs3, rhs3 = rhs1.argument1, rhs1.argument2
				C = lhs3
				if str(B)==str(rhs3):
					return ("((A[P*P]) ∩ (B[P*P])) ∩ ((C[P*P]) ∩ (B[P*P])) = ((C[P*P]) ∩ (B[P*P])) ∩ (A[P*P])", Typed_COR_Expressions.Typed_Intersection(Typed_COR_Expressions.Typed_Intersection(C, B), A))
				if str(A)==str(rhs3):
					return ("((A[P*P]) ∩ (B[P*P])) ∩ ((C[P*P]) ∩ (A[P*P])) = ((C[P*P]) ∩ (B[P*P])) ∩ (A[P*P])", Typed_COR_Expressions.Typed_Intersection(Typed_COR_Expressions.Typed_Intersection(C, B), A))
				if str(B)==str(lhs3):
					C = rhs3
					return ("((A[P*P]) ∩ (B[P*P])) ∩ ((B[P*P]) ∩ (C[P*P])) = ((A[P*P]) ∩ (C[P*P])) ∩ (B[P*P])", Typed_COR_Expressions.Typed_Intersection(Typed_COR_Expressions.Typed_Intersection(A, C), B))
				if str(A)==str(lhs3):
					C = rhs3
					return ("((A[P*P]) ∩ (B[P*P])) ∩ ((A[P*P]) ∩ (C[P*P])) = ((A[P*P]) ∩ (B[P*P])) ∩ (C[P*P])", Typed_COR_Expressions.Typed_Intersection(Typed_COR_Expressions.Typed_Intersection(A, B), C))
			if isinstance(rhs1, Typed_COR_Expressions.Typed_Union):
				lhs3, rhs3 = rhs1.argument1, rhs1.argument2
				C = lhs3
				if str(A)==str(rhs3):
					return ("((A[P*P]) ∩ (B[P*P])) ∩ ((C[P*P]) ∪ (A[P*P])) = (B[P*P]) ∩ (A[P*P])", Typed_COR_Expressions.Typed_Intersection(B, A))
				if str(B)==str(rhs3):
					return ("((A[P*P]) ∩ (B[P*P])) ∩ ((C[P*P]) ∪ (B[P*P])) = (B[P*P]) ∩ (A[P*P])", Typed_COR_Expressions.Typed_Intersection(B, A))
				if str(B)==str(lhs3):
					C = rhs3
					return ("((A[P*P]) ∩ (B[P*P])) ∩ ((B[P*P]) ∪ (C[P*P])) = (A[P*P]) ∩ (B[P*P])", Typed_COR_Expressions.Typed_Intersection(A, B))
				if str(A)==str(lhs3):
					C = rhs3
					return ("((A[P*P]) ∩ (B[P*P])) ∩ ((A[P*P]) ∪ (C[P*P])) = (B[P*P]) ∩ (A[P*P])", Typed_COR_Expressions.Typed_Intersection(B, A))
			if isinstance(rhs1, Typed_COR_Expressions.Typed_Complement):
				arg = rhs1.argument
				if str(B)==str(arg):
					return ("((A[P*P]) ∩ (B[P*P])) ∩ ((B[P*P])⁻) = 𝟎[P*P]", Typed_COR_Expressions.Typed_EmptyRelation(expression.type()[0], expression.type()[1]))
				if str(A)==str(arg):
					return ("((A[P*P]) ∩ (B[P*P])) ∩ ((A[P*P])⁻) = 𝟎[P*P]", Typed_COR_Expressions.Typed_EmptyRelation(expression.type()[0], expression.type()[1]))
			if isinstance(rhs2, Typed_COR_Expressions.Typed_Intersection):
				lhs3, rhs3 = rhs2.argument1, rhs2.argument2
				B = lhs3
				C = rhs3
				if str(C)==str(rhs1):
					return ("((A[P*P]) ∩ ((B[P*P]) ∩ (C[P*P]))) ∩ (C[P*P]) = ((B[P*P]) ∩ (A[P*P])) ∩ (C[P*P])", Typed_COR_Expressions.Typed_Intersection(Typed_COR_Expressions.Typed_Intersection(B, A), C))
				if str(B)==str(rhs1):
					return ("((A[P*P]) ∩ ((B[P*P]) ∩ (C[P*P]))) ∩ (B[P*P]) = ((C[P*P]) ∩ (A[P*P])) ∩ (B[P*P])", Typed_COR_Expressions.Typed_Intersection(Typed_COR_Expressions.Typed_Intersection(C, A), B))
			if isinstance(rhs2, Typed_COR_Expressions.Typed_Union):
				lhs3, rhs3 = rhs2.argument1, rhs2.argument2
				B = lhs3
				C = rhs3
				if str(B)==str(rhs1):
					return ("((A[P*P]) ∩ ((B[P*P]) ∪ (C[P*P]))) ∩ (B[P*P]) = (B[P*P]) ∩ (A[P*P])", Typed_COR_Expressions.Typed_Intersection(B, A))
				if str(C)==str(rhs1):
					return ("((A[P*P]) ∩ ((B[P*P]) ∪ (C[P*P]))) ∩ (C[P*P]) = (C[P*P]) ∩ (A[P*P])", Typed_COR_Expressions.Typed_Intersection(C, A))
			if isinstance(rhs2, Typed_COR_Expressions.Typed_Complement):
				arg = rhs2.argument
				B = arg
				if str(B)==str(rhs1):
					return ("((A[P*P]) ∩ ((B[P*P])⁻)) ∩ (B[P*P]) = 𝟎[P*P]", Typed_COR_Expressions.Typed_EmptyRelation(expression.type()[0], expression.type()[1]))
			if isinstance(lhs2, Typed_COR_Expressions.Typed_Intersection):
				lhs3, rhs3 = lhs2.argument1, lhs2.argument2
				A = lhs3
				B = rhs3
				C = rhs2
				if str(B)==str(rhs1):
					return ("(((A[P*P]) ∩ (B[P*P])) ∩ (C[P*P])) ∩ (B[P*P]) = (B[P*P]) ∩ ((A[P*P]) ∩ (C[P*P]))", Typed_COR_Expressions.Typed_Intersection(B, Typed_COR_Expressions.Typed_Intersection(A, C)))
				if str(A)==str(rhs1):
					return ("(((A[P*P]) ∩ (B[P*P])) ∩ (C[P*P])) ∩ (A[P*P]) = ((C[P*P]) ∩ (A[P*P])) ∩ (B[P*P])", Typed_COR_Expressions.Typed_Intersection(Typed_COR_Expressions.Typed_Intersection(C, A), B))
			if isinstance(lhs2, Typed_COR_Expressions.Typed_Union):
				lhs3, rhs3 = lhs2.argument1, lhs2.argument2
				A = lhs3
				B = rhs3
				C = rhs2
				if str(B)==str(rhs1):
					return ("(((A[P*P]) ∪ (B[P*P])) ∩ (C[P*P])) ∩ (B[P*P]) = (C[P*P]) ∩ (B[P*P])", Typed_COR_Expressions.Typed_Intersection(C, B))
				if str(A)==str(rhs1):
					return ("(((A[P*P]) ∪ (B[P*P])) ∩ (C[P*P])) ∩ (A[P*P]) = (C[P*P]) ∩ (A[P*P])", Typed_COR_Expressions.Typed_Intersection(C, A))
			if isinstance(lhs2, Typed_COR_Expressions.Typed_Complement):
				arg = lhs2.argument
				A = arg
				B = rhs2
				if str(A)==str(rhs1):
					return ("(((A[P*P])⁻) ∩ (B[P*P])) ∩ (A[P*P]) = 𝟎[P*P]", Typed_COR_Expressions.Typed_EmptyRelation(expression.type()[0], expression.type()[1]))
		if isinstance(lhs1, Typed_COR_Expressions.Typed_Union):
			lhs2, rhs2 = lhs1.argument1, lhs1.argument2
			A = lhs2
			B = rhs2
			if str(B)==str(rhs1):
				return ("((A[P*P]) ∪ (B[P*P])) ∩ (B[P*P]) = B[P*P]", B)
			if str(A)==str(rhs1):
				return ("((A[P*P]) ∪ (B[P*P])) ∩ (A[P*P]) = A[P*P]", A)
			if isinstance(rhs1, Typed_COR_Expressions.Typed_Union):
				lhs3, rhs3 = rhs1.argument1, rhs1.argument2
				C = lhs3
				if str(A)==str(rhs3):
					return ("((A[P*P]) ∪ (B[P*P])) ∩ ((C[P*P]) ∪ (A[P*P])) = (A[P*P]) ∪ ((C[P*P]) ∩ (B[P*P]))", Typed_COR_Expressions.Typed_Union(A, Typed_COR_Expressions.Typed_Intersection(C, B)))
				if str(B)==str(rhs3):
					return ("((A[P*P]) ∪ (B[P*P])) ∩ ((C[P*P]) ∪ (B[P*P])) = (B[P*P]) ∪ ((A[P*P]) ∩ (C[P*P]))", Typed_COR_Expressions.Typed_Union(B, Typed_COR_Expressions.Typed_Intersection(A, C)))
				if str(B)==str(lhs3):
					C = rhs3
					return ("((A[P*P]) ∪ (B[P*P])) ∩ ((B[P*P]) ∪ (C[P*P])) = ((C[P*P]) ∩ (A[P*P])) ∪ (B[P*P])", Typed_COR_Expressions.Typed_Union(Typed_COR_Expressions.Typed_Intersection(C, A), B))
				if str(A)==str(lhs3):
					C = rhs3
					return ("((A[P*P]) ∪ (B[P*P])) ∩ ((A[P*P]) ∪ (C[P*P])) = (A[P*P]) ∪ ((B[P*P]) ∩ (C[P*P]))", Typed_COR_Expressions.Typed_Union(A, Typed_COR_Expressions.Typed_Intersection(B, C)))
			if isinstance(rhs1, Typed_COR_Expressions.Typed_Intersection):
				lhs3, rhs3 = rhs1.argument1, rhs1.argument2
				C = lhs3
				if str(A)==str(rhs3):
					return ("((A[P*P]) ∪ (B[P*P])) ∩ ((C[P*P]) ∩ (A[P*P])) = (A[P*P]) ∩ (C[P*P])", Typed_COR_Expressions.Typed_Intersection(A, C))
				if str(B)==str(rhs3):
					return ("((A[P*P]) ∪ (B[P*P])) ∩ ((C[P*P]) ∩ (B[P*P])) = (C[P*P]) ∩ (B[P*P])", Typed_COR_Expressions.Typed_Intersection(C, B))
				if str(B)==str(lhs3):
					C = rhs3
					return ("((A[P*P]) ∪ (B[P*P])) ∩ ((B[P*P]) ∩ (C[P*P])) = (C[P*P]) ∩ (B[P*P])", Typed_COR_Expressions.Typed_Intersection(C, B))
				if str(A)==str(lhs3):
					C = rhs3
					return ("((A[P*P]) ∪ (B[P*P])) ∩ ((A[P*P]) ∩ (C[P*P])) = (C[P*P]) ∩ (A[P*P])", Typed_COR_Expressions.Typed_Intersection(C, A))
			if isinstance(rhs1, Typed_COR_Expressions.Typed_Complement):
				arg = rhs1.argument
				if str(A)==str(arg):
					return ("((A[P*P]) ∪ (B[P*P])) ∩ ((A[P*P])⁻) = ((A[P*P])⁻) ∩ (B[P*P])", Typed_COR_Expressions.Typed_Intersection(Typed_COR_Expressions.Typed_Complement(A), B))
				if str(B)==str(arg):
					return ("((A[P*P]) ∪ (B[P*P])) ∩ ((B[P*P])⁻) = ((B[P*P])⁻) ∩ (A[P*P])", Typed_COR_Expressions.Typed_Intersection(Typed_COR_Expressions.Typed_Complement(B), A))
			if isinstance(rhs2, Typed_COR_Expressions.Typed_Complement):
				arg = rhs2.argument
				B = arg
				if str(B)==str(rhs1):
					return ("((A[P*P]) ∪ ((B[P*P])⁻)) ∩ (B[P*P]) = (A[P*P]) ∩ (B[P*P])", Typed_COR_Expressions.Typed_Intersection(A, B))
			if isinstance(rhs2, Typed_COR_Expressions.Typed_Intersection):
				lhs3, rhs3 = rhs2.argument1, rhs2.argument2
				B = lhs3
				C = rhs3
				if str(B)==str(rhs1):
					return ("((A[P*P]) ∪ ((B[P*P]) ∩ (C[P*P]))) ∩ (B[P*P]) = (B[P*P]) ∩ ((C[P*P]) ∪ (A[P*P]))", Typed_COR_Expressions.Typed_Intersection(B, Typed_COR_Expressions.Typed_Union(C, A)))
				if str(C)==str(rhs1):
					return ("((A[P*P]) ∪ ((B[P*P]) ∩ (C[P*P]))) ∩ (C[P*P]) = ((B[P*P]) ∪ (A[P*P])) ∩ (C[P*P])", Typed_COR_Expressions.Typed_Intersection(Typed_COR_Expressions.Typed_Union(B, A), C))
			if isinstance(rhs2, Typed_COR_Expressions.Typed_Union):
				lhs3, rhs3 = rhs2.argument1, rhs2.argument2
				B = lhs3
				C = rhs3
				if str(B)==str(rhs1):
					return ("((A[P*P]) ∪ ((B[P*P]) ∪ (C[P*P]))) ∩ (B[P*P]) = B[P*P]", B)
				if str(C)==str(rhs1):
					return ("((A[P*P]) ∪ ((B[P*P]) ∪ (C[P*P]))) ∩ (C[P*P]) = C[P*P]", C)
			if isinstance(lhs2, Typed_COR_Expressions.Typed_Intersection):
				lhs3, rhs3 = lhs2.argument1, lhs2.argument2
				A = lhs3
				B = rhs3
				C = rhs2
				if str(A)==str(rhs1):
					return ("(((A[P*P]) ∩ (B[P*P])) ∪ (C[P*P])) ∩ (A[P*P]) = (A[P*P]) ∩ ((C[P*P]) ∪ (B[P*P]))", Typed_COR_Expressions.Typed_Intersection(A, Typed_COR_Expressions.Typed_Union(C, B)))
				if str(B)==str(rhs1):
					return ("(((A[P*P]) ∩ (B[P*P])) ∪ (C[P*P])) ∩ (B[P*P]) = (B[P*P]) ∩ ((A[P*P]) ∪ (C[P*P]))", Typed_COR_Expressions.Typed_Intersection(B, Typed_COR_Expressions.Typed_Union(A, C)))
			if isinstance(lhs2, Typed_COR_Expressions.Typed_Complement):
				arg = lhs2.argument
				A = arg
				B = rhs2
				if str(A)==str(rhs1):
					return ("(((A[P*P])⁻) ∪ (B[P*P])) ∩ (A[P*P]) = (A[P*P]) ∩ (B[P*P])", Typed_COR_Expressions.Typed_Intersection(A, B))
			if isinstance(lhs2, Typed_COR_Expressions.Typed_Union):
				lhs3, rhs3 = lhs2.argument1, lhs2.argument2
				A = lhs3
				B = rhs3
				C = rhs2
				if str(A)==str(rhs1):
					return ("(((A[P*P]) ∪ (B[P*P])) ∪ (C[P*P])) ∩ (A[P*P]) = A[P*P]", A)
				if str(B)==str(rhs1):
					return ("(((A[P*P]) ∪ (B[P*P])) ∪ (C[P*P])) ∩ (B[P*P]) = B[P*P]", B)
		if isinstance(lhs1, Typed_COR_Expressions.Typed_EmptyRelation):
			A = rhs1
			return ("(𝟎[P*P]) ∩ (A[P*P]) = 𝟎[P*P]", Typed_COR_Expressions.Typed_EmptyRelation(expression.type()[0], expression.type()[1]))
		if isinstance(lhs1, Typed_COR_Expressions.Typed_UniversalRelation):
			A = rhs1
			return ("(T[P*P]) ∩ (A[P*P]) = A[P*P]", A)
		if isinstance(lhs1, Typed_COR_Expressions.Typed_Complement):
			arg = lhs1.argument
			A = arg
			if str(A)==str(rhs1):
				return ("((A[P*P])⁻) ∩ (A[P*P]) = 𝟎[P*P]", Typed_COR_Expressions.Typed_EmptyRelation(expression.type()[0], expression.type()[1]))
			if isinstance(rhs1, Typed_COR_Expressions.Typed_Intersection):
				lhs3, rhs3 = rhs1.argument1, rhs1.argument2
				if str(A)==str(lhs3):
					B = rhs3
					return ("((A[P*P])⁻) ∩ ((A[P*P]) ∩ (B[P*P])) = 𝟎[P*P]", Typed_COR_Expressions.Typed_EmptyRelation(expression.type()[0], expression.type()[1]))
				B = lhs3
				if str(A)==str(rhs3):
					return ("((A[P*P])⁻) ∩ ((B[P*P]) ∩ (A[P*P])) = 𝟎[P*P]", Typed_COR_Expressions.Typed_EmptyRelation(expression.type()[0], expression.type()[1]))
			if isinstance(rhs1, Typed_COR_Expressions.Typed_Union):
				lhs3, rhs3 = rhs1.argument1, rhs1.argument2
				B = lhs3
				if str(A)==str(rhs3):
					return ("((A[P*P])⁻) ∩ ((B[P*P]) ∪ (A[P*P])) = (B[P*P]) ∩ ((A[P*P])⁻)", Typed_COR_Expressions.Typed_Intersection(B, Typed_COR_Expressions.Typed_Complement(A)))
				if str(A)==str(lhs3):
					B = rhs3
					return ("((A[P*P])⁻) ∩ ((A[P*P]) ∪ (B[P*P])) = ((A[P*P])⁻) ∩ (B[P*P])", Typed_COR_Expressions.Typed_Intersection(Typed_COR_Expressions.Typed_Complement(A), B))
			if isinstance(rhs1, Typed_COR_Expressions.Typed_Complement):
				arg = rhs1.argument
				B = arg
				return ("((A[P*P])⁻) ∩ ((B[P*P])⁻) = ((B[P*P]) ∪ (A[P*P]))⁻", Typed_COR_Expressions.Typed_Complement(Typed_COR_Expressions.Typed_Union(B, A)))
			if isinstance(arg, Typed_COR_Expressions.Typed_Intersection):
				lhs3, rhs3 = arg.argument1, arg.argument2
				A = lhs3
				B = rhs3
				if str(A)==str(rhs1):
					return ("(((A[P*P]) ∩ (B[P*P]))⁻) ∩ (A[P*P]) = ((B[P*P])⁻) ∩ (A[P*P])", Typed_COR_Expressions.Typed_Intersection(Typed_COR_Expressions.Typed_Complement(B), A))
				if str(B)==str(rhs1):
					return ("(((A[P*P]) ∩ (B[P*P]))⁻) ∩ (B[P*P]) = (B[P*P]) ∩ ((A[P*P])⁻)", Typed_COR_Expressions.Typed_Intersection(B, Typed_COR_Expressions.Typed_Complement(A)))
			if isinstance(arg, Typed_COR_Expressions.Typed_Union):
				lhs3, rhs3 = arg.argument1, arg.argument2
				A = lhs3
				B = rhs3
				if str(A)==str(rhs1):
					return ("(((A[P*P]) ∪ (B[P*P]))⁻) ∩ (A[P*P]) = 𝟎[P*P]", Typed_COR_Expressions.Typed_EmptyRelation(expression.type()[0], expression.type()[1]))
				if str(B)==str(rhs1):
					return ("(((A[P*P]) ∪ (B[P*P]))⁻) ∩ (B[P*P]) = 𝟎[P*P]", Typed_COR_Expressions.Typed_EmptyRelation(expression.type()[0], expression.type()[1]))
		if isinstance(lhs1, Typed_COR_Expressions.Typed_Dagger):
			lhs2, rhs2 = lhs1.argument1, lhs1.argument2
			A = lhs2
			B = rhs2
			if isinstance(rhs1, Typed_COR_Expressions.Typed_Dagger):
				lhs3, rhs3 = rhs1.argument1, rhs1.argument2
				C = lhs3
				if str(B)==str(rhs3):
					return ("((A[P*P]) † (B[P*P])) ∩ ((C[P*P]) † (B[P*P])) = ((A[P*P]) ∩ (C[P*P])) † (B[P*P])", Typed_COR_Expressions.Typed_Dagger(Typed_COR_Expressions.Typed_Intersection(A, C), B))
				if str(A)==str(lhs3):
					C = rhs3
					return ("((A[P*P]) † (B[P*P])) ∩ ((A[P*P]) † (C[P*P])) = (A[P*P]) † ((B[P*P]) ∩ (C[P*P]))", Typed_COR_Expressions.Typed_Dagger(A, Typed_COR_Expressions.Typed_Intersection(B, C)))
			if isinstance(rhs2, Typed_COR_Expressions.Typed_IdentityRelation):
				if str(A)==str(rhs1):
					return ("((A[P*P]) † (𝟏[P*P])) ∩ (A[P*P]) = (A[P*P]) † (𝟎[P*P])", Typed_COR_Expressions.Typed_Dagger(A, Typed_COR_Expressions.Typed_EmptyRelation(A.type()[1], expression.type()[1])))
			if isinstance(rhs2, Typed_COR_Expressions.Typed_EmptyRelation):
				if str(A)==str(rhs1):
					return ("((A[P*P]) † (𝟎[P*P])) ∩ (A[P*P]) = (A[P*P]) † (𝟎[P*P])", Typed_COR_Expressions.Typed_Dagger(A, Typed_COR_Expressions.Typed_EmptyRelation(A.type()[1], expression.type()[1])))
			if isinstance(lhs2, Typed_COR_Expressions.Typed_IdentityRelation):
				A = rhs2
				if str(A)==str(rhs1):
					return ("((𝟏[P*P]) † (A[P*P])) ∩ (A[P*P]) = (𝟎[P*P]) † (A[P*P])", Typed_COR_Expressions.Typed_Dagger(Typed_COR_Expressions.Typed_EmptyRelation(expression.type()[0], A.type()[0]), A))
			if isinstance(lhs2, Typed_COR_Expressions.Typed_EmptyRelation):
				A = rhs2
				if str(A)==str(rhs1):
					return ("((𝟎[P*P]) † (A[P*P])) ∩ (A[P*P]) = (𝟎[P*P]) † (A[P*P])", Typed_COR_Expressions.Typed_Dagger(Typed_COR_Expressions.Typed_EmptyRelation(expression.type()[0], A.type()[0]), A))
		if isinstance(lhs1, Typed_COR_Expressions.Typed_Converse):
			arg = lhs1.argument
			A = arg
			if isinstance(rhs1, Typed_COR_Expressions.Typed_Converse):
				arg = rhs1.argument
				B = arg
				return ("((A[P*P])⁻¹) ∩ ((B[P*P])⁻¹) = ((A[P*P]) ∩ (B[P*P]))⁻¹", Typed_COR_Expressions.Typed_Converse(Typed_COR_Expressions.Typed_Intersection(A, B)))
			if isinstance(rhs1, Typed_COR_Expressions.Typed_IdentityRelation):
				return ("((A[P*P])⁻¹) ∩ (𝟏[P*P]) = (A[P*P]) ∩ (𝟏[P*P])", Typed_COR_Expressions.Typed_Intersection(A, Typed_COR_Expressions.Typed_IdentityRelation(expression.type()[0], expression.type()[1])))
		if isinstance(lhs1, Typed_COR_Expressions.Typed_IdentityRelation):
			if isinstance(rhs1, Typed_COR_Expressions.Typed_Converse):
				arg = rhs1.argument
				A = arg
				return ("(𝟏[P*P]) ∩ ((A[P*P])⁻¹) = (A[P*P]) ∩ (𝟏[P*P])", Typed_COR_Expressions.Typed_Intersection(A, Typed_COR_Expressions.Typed_IdentityRelation(expression.type()[0], expression.type()[1])))
		if isinstance(lhs1, Typed_COR_Expressions.Typed_Composition):
			lhs2, rhs2 = lhs1.argument1, lhs1.argument2
			A = lhs2
			if isinstance(rhs2, Typed_COR_Expressions.Typed_UniversalRelation):
				if str(A)==str(rhs1):
					return ("((A[P*P]) ∘ (T[P*P])) ∩ (A[P*P]) = A[P*P]", A)
			if isinstance(lhs2, Typed_COR_Expressions.Typed_UniversalRelation):
				A = rhs2
				if str(A)==str(rhs1):
					return ("((T[P*P]) ∘ (A[P*P])) ∩ (A[P*P]) = A[P*P]", A)
	if isinstance(expression, Typed_COR_Expressions.Typed_Converse):
		arg = expression.argument
		if isinstance(arg, Typed_COR_Expressions.Typed_IdentityRelation):
			return ("(𝟏[P*P])⁻¹ = 𝟏[P*P]", Typed_COR_Expressions.Typed_IdentityRelation(expression.type()[0], expression.type()[1]))
		if isinstance(arg, Typed_COR_Expressions.Typed_Converse):
			arg = arg.argument
			A = arg
			return ("((A[P*P])⁻¹)⁻¹ = A[P*P]", A)
		if isinstance(arg, Typed_COR_Expressions.Typed_EmptyRelation):
			return ("(𝟎[P*P])⁻¹ = 𝟎[P*P]", Typed_COR_Expressions.Typed_EmptyRelation(expression.type()[0], expression.type()[1]))
		if isinstance(arg, Typed_COR_Expressions.Typed_UniversalRelation):
			return ("(T[P*P])⁻¹ = T[P*P]", Typed_COR_Expressions.Typed_UniversalRelation(expression.type()[0], expression.type()[1]))
		if isinstance(arg, Typed_COR_Expressions.Typed_Union):
			lhs2, rhs2 = arg.argument1, arg.argument2
			A = lhs2
			if isinstance(rhs2, Typed_COR_Expressions.Typed_Converse):
				arg = rhs2.argument
				B = arg
				return ("((A[P*P]) ∪ ((B[P*P])⁻¹))⁻¹ = ((A[P*P])⁻¹) ∪ (B[P*P])", Typed_COR_Expressions.Typed_Union(Typed_COR_Expressions.Typed_Converse(A), B))
			if isinstance(lhs2, Typed_COR_Expressions.Typed_Converse):
				arg = lhs2.argument
				A = arg
				B = rhs2
				return ("(((A[P*P])⁻¹) ∪ (B[P*P]))⁻¹ = ((B[P*P])⁻¹) ∪ (A[P*P])", Typed_COR_Expressions.Typed_Union(Typed_COR_Expressions.Typed_Converse(B), A))
		if isinstance(arg, Typed_COR_Expressions.Typed_Intersection):
			lhs2, rhs2 = arg.argument1, arg.argument2
			A = lhs2
			if isinstance(rhs2, Typed_COR_Expressions.Typed_IdentityRelation):
				return ("((A[P*P]) ∩ (𝟏[P*P]))⁻¹ = (𝟏[P*P]) ∩ (A[P*P])", Typed_COR_Expressions.Typed_Intersection(Typed_COR_Expressions.Typed_IdentityRelation(expression.type()[0], expression.type()[1]), A))
			if isinstance(rhs2, Typed_COR_Expressions.Typed_Converse):
				arg = rhs2.argument
				B = arg
				return ("((A[P*P]) ∩ ((B[P*P])⁻¹))⁻¹ = ((A[P*P])⁻¹) ∩ (B[P*P])", Typed_COR_Expressions.Typed_Intersection(Typed_COR_Expressions.Typed_Converse(A), B))
			if isinstance(lhs2, Typed_COR_Expressions.Typed_Converse):
				arg = lhs2.argument
				A = arg
				B = rhs2
				return ("(((A[P*P])⁻¹) ∩ (B[P*P]))⁻¹ = ((B[P*P])⁻¹) ∩ (A[P*P])", Typed_COR_Expressions.Typed_Intersection(Typed_COR_Expressions.Typed_Converse(B), A))
			if isinstance(lhs2, Typed_COR_Expressions.Typed_IdentityRelation):
				A = rhs2
				return ("((𝟏[P*P]) ∩ (A[P*P]))⁻¹ = (A[P*P]) ∩ (𝟏[P*P])", Typed_COR_Expressions.Typed_Intersection(A, Typed_COR_Expressions.Typed_IdentityRelation(expression.type()[0], expression.type()[1])))
		if isinstance(arg, Typed_COR_Expressions.Typed_Complement):
			arg = arg.argument
			if isinstance(arg, Typed_COR_Expressions.Typed_IdentityRelation):
				return ("((𝟏[P*P])⁻)⁻¹ = (𝟏[P*P])⁻", Typed_COR_Expressions.Typed_Complement(Typed_COR_Expressions.Typed_IdentityRelation(expression.type()[0], expression.type()[1])))
			if isinstance(arg, Typed_COR_Expressions.Typed_Converse):
				arg = arg.argument
				A = arg
				return ("(((A[P*P])⁻¹)⁻)⁻¹ = (A[P*P])⁻", Typed_COR_Expressions.Typed_Complement(A))
	if isinstance(expression, Typed_COR_Expressions.Typed_Composition):
		lhs1, rhs1 = expression.argument1, expression.argument2
		A = lhs1
		if isinstance(rhs1, Typed_COR_Expressions.Typed_EmptyRelation):
			return ("(A[P*P]) ∘ (𝟎[P*P]) = 𝟎[P*P]", Typed_COR_Expressions.Typed_EmptyRelation(expression.type()[0], expression.type()[1]))
		if isinstance(rhs1, Typed_COR_Expressions.Typed_IdentityRelation):
			return ("(A[P*P]) ∘ (𝟏[P*P]) = A[P*P]", A)
		if isinstance(rhs1, Typed_COR_Expressions.Typed_Dagger):
			lhs2, rhs2 = rhs1.argument1, rhs1.argument2
			if isinstance(lhs2, Typed_COR_Expressions.Typed_EmptyRelation):
				if str(A)==str(rhs2):
					return ("(A[P*P]) ∘ ((𝟎[P*P]) † (A[P*P])) = (𝟎[P*P]) † (A[P*P])", Typed_COR_Expressions.Typed_Dagger(Typed_COR_Expressions.Typed_EmptyRelation(expression.type()[0], A.type()[0]), A))
		if isinstance(lhs1, Typed_COR_Expressions.Typed_IdentityRelation):
			A = rhs1
			return ("(𝟏[P*P]) ∘ (A[P*P]) = A[P*P]", A)
		if isinstance(lhs1, Typed_COR_Expressions.Typed_EmptyRelation):
			A = rhs1
			return ("(𝟎[P*P]) ∘ (A[P*P]) = 𝟎[P*P]", Typed_COR_Expressions.Typed_EmptyRelation(expression.type()[0], expression.type()[1]))
		if isinstance(lhs1, Typed_COR_Expressions.Typed_Dagger):
			lhs2, rhs2 = lhs1.argument1, lhs1.argument2
			A = lhs2
			if isinstance(rhs2, Typed_COR_Expressions.Typed_EmptyRelation):
				if str(A)==str(rhs1):
					return ("((A[P*P]) † (𝟎[P*P])) ∘ (A[P*P]) = (A[P*P]) † (𝟎[P*P])", Typed_COR_Expressions.Typed_Dagger(A, Typed_COR_Expressions.Typed_EmptyRelation(A.type()[1], expression.type()[1])))
		if isinstance(lhs1, Typed_COR_Expressions.Typed_Converse):
			arg = lhs1.argument
			A = arg
			if isinstance(rhs1, Typed_COR_Expressions.Typed_Converse):
				arg = rhs1.argument
				B = arg
				return ("((A[P*P])⁻¹) ∘ ((B[P*P])⁻¹) = ((B[P*P]) ∘ (A[P*P]))⁻¹", Typed_COR_Expressions.Typed_Converse(Typed_COR_Expressions.Typed_Composition(B, A)))
		if isinstance(lhs1, Typed_COR_Expressions.Typed_Complement):
			arg = lhs1.argument
			A = arg
			if isinstance(rhs1, Typed_COR_Expressions.Typed_Complement):
				arg = rhs1.argument
				B = arg
				return ("((A[P*P])⁻) ∘ ((B[P*P])⁻) = ((A[P*P]) † (B[P*P]))⁻", Typed_COR_Expressions.Typed_Complement(Typed_COR_Expressions.Typed_Dagger(A, B)))
		if isinstance(lhs1, Typed_COR_Expressions.Typed_UniversalRelation):
			if isinstance(rhs1, Typed_COR_Expressions.Typed_UniversalRelation):
				return ("(T[P*P]) ∘ (T[P*P]) = T[P*P]", Typed_COR_Expressions.Typed_UniversalRelation(expression.type()[0], expression.type()[1]))
	if isinstance(expression, Typed_COR_Expressions.Typed_Dagger):
		lhs1, rhs1 = expression.argument1, expression.argument2
		A = lhs1
		if isinstance(rhs1, Typed_COR_Expressions.Typed_UniversalRelation):
			return ("(A[P*P]) † (T[P*P]) = T[P*P]", Typed_COR_Expressions.Typed_UniversalRelation(expression.type()[0], expression.type()[1]))
		if isinstance(rhs1, Typed_COR_Expressions.Typed_Composition):
			lhs2, rhs2 = rhs1.argument1, rhs1.argument2
			if isinstance(lhs2, Typed_COR_Expressions.Typed_UniversalRelation):
				if str(A)==str(rhs2):
					return ("(A[P*P]) † ((T[P*P]) ∘ (A[P*P])) = (T[P*P]) ∘ (A[P*P])", Typed_COR_Expressions.Typed_Composition(Typed_COR_Expressions.Typed_UniversalRelation(expression.type()[0], A.type()[0]), A))
		if isinstance(rhs1, Typed_COR_Expressions.Typed_Complement):
			arg = rhs1.argument
			if isinstance(arg, Typed_COR_Expressions.Typed_IdentityRelation):
				return ("(A[P*P]) † ((𝟏[P*P])⁻) = A[P*P]", A)
		if isinstance(lhs1, Typed_COR_Expressions.Typed_UniversalRelation):
			A = rhs1
			return ("(T[P*P]) † (A[P*P]) = T[P*P]", Typed_COR_Expressions.Typed_UniversalRelation(expression.type()[0], expression.type()[1]))
		if isinstance(lhs1, Typed_COR_Expressions.Typed_Complement):
			arg = lhs1.argument
			if isinstance(arg, Typed_COR_Expressions.Typed_IdentityRelation):
				A = rhs1
				return ("((𝟏[P*P])⁻) † (A[P*P]) = A[P*P]", A)
			A = arg
			if isinstance(rhs1, Typed_COR_Expressions.Typed_Complement):
				arg = rhs1.argument
				B = arg
				return ("((A[P*P])⁻) † ((B[P*P])⁻) = ((A[P*P]) ∘ (B[P*P]))⁻", Typed_COR_Expressions.Typed_Complement(Typed_COR_Expressions.Typed_Composition(A, B)))
		if isinstance(lhs1, Typed_COR_Expressions.Typed_Converse):
			arg = lhs1.argument
			A = arg
			if isinstance(rhs1, Typed_COR_Expressions.Typed_Converse):
				arg = rhs1.argument
				B = arg
				return ("((A[P*P])⁻¹) † ((B[P*P])⁻¹) = ((B[P*P]) † (A[P*P]))⁻¹", Typed_COR_Expressions.Typed_Converse(Typed_COR_Expressions.Typed_Dagger(B, A)))
		if isinstance(lhs1, Typed_COR_Expressions.Typed_EmptyRelation):
			if isinstance(rhs1, Typed_COR_Expressions.Typed_EmptyRelation):
				return ("(𝟎[P*P]) † (𝟎[P*P]) = 𝟎[P*P]", Typed_COR_Expressions.Typed_EmptyRelation(expression.type()[0], expression.type()[1]))
		if isinstance(lhs1, Typed_COR_Expressions.Typed_Composition):
			lhs2, rhs2 = lhs1.argument1, lhs1.argument2
			A = lhs2
			if isinstance(rhs2, Typed_COR_Expressions.Typed_UniversalRelation):
				if str(A)==str(rhs1):
					return ("((A[P*P]) ∘ (T[P*P])) † (A[P*P]) = (A[P*P]) ∘ (T[P*P])", Typed_COR_Expressions.Typed_Composition(A, Typed_COR_Expressions.Typed_UniversalRelation(A.type()[1], expression.type()[1])))
	if isinstance(expression, Typed_COR_Expressions.Typed_Complement):
		arg = expression.argument
		if isinstance(arg, Typed_COR_Expressions.Typed_UniversalRelation):
			return ("(T[P*P])⁻ = 𝟎[P*P]", Typed_COR_Expressions.Typed_EmptyRelation(expression.type()[0], expression.type()[1]))
		if isinstance(arg, Typed_COR_Expressions.Typed_EmptyRelation):
			return ("(𝟎[P*P])⁻ = T[P*P]", Typed_COR_Expressions.Typed_UniversalRelation(expression.type()[0], expression.type()[1]))
		if isinstance(arg, Typed_COR_Expressions.Typed_Complement):
			arg = arg.argument
			A = arg
			return ("((A[P*P])⁻)⁻ = A[P*P]", A)
		if isinstance(arg, Typed_COR_Expressions.Typed_Union):
			lhs2, rhs2 = arg.argument1, arg.argument2
			A = lhs2
			if isinstance(rhs2, Typed_COR_Expressions.Typed_Complement):
				arg = rhs2.argument
				B = arg
				return ("((A[P*P]) ∪ ((B[P*P])⁻))⁻ = ((A[P*P])⁻) ∩ (B[P*P])", Typed_COR_Expressions.Typed_Intersection(Typed_COR_Expressions.Typed_Complement(A), B))
			if isinstance(lhs2, Typed_COR_Expressions.Typed_Complement):
				arg = lhs2.argument
				A = arg
				B = rhs2
				return ("(((A[P*P])⁻) ∪ (B[P*P]))⁻ = (A[P*P]) ∩ ((B[P*P])⁻)", Typed_COR_Expressions.Typed_Intersection(A, Typed_COR_Expressions.Typed_Complement(B)))
		if isinstance(arg, Typed_COR_Expressions.Typed_Converse):
			arg = arg.argument
			if isinstance(arg, Typed_COR_Expressions.Typed_Complement):
				arg = arg.argument
				A = arg
				return ("(((A[P*P])⁻)⁻¹)⁻ = (A[P*P])⁻¹", Typed_COR_Expressions.Typed_Converse(A))
		if isinstance(arg, Typed_COR_Expressions.Typed_Intersection):
			lhs2, rhs2 = arg.argument1, arg.argument2
			if isinstance(lhs2, Typed_COR_Expressions.Typed_Complement):
				arg = lhs2.argument
				A = arg
				B = rhs2
				return ("(((A[P*P])⁻) ∩ (B[P*P]))⁻ = ((B[P*P])⁻) ∪ (A[P*P])", Typed_COR_Expressions.Typed_Union(Typed_COR_Expressions.Typed_Complement(B), A))
			A = lhs2
			if isinstance(rhs2, Typed_COR_Expressions.Typed_Complement):
				arg = rhs2.argument
				B = arg
				return ("((A[P*P]) ∩ ((B[P*P])⁻))⁻ = (B[P*P]) ∪ ((A[P*P])⁻)", Typed_COR_Expressions.Typed_Union(B, Typed_COR_Expressions.Typed_Complement(A)))
		if isinstance(arg, Typed_COR_Expressions.Typed_Composition):
			lhs2, rhs2 = arg.argument1, arg.argument2
			if isinstance(lhs2, Typed_COR_Expressions.Typed_Complement):
				arg = lhs2.argument
				A = arg
				B = rhs2
				return ("(((A[P*P])⁻) ∘ (B[P*P]))⁻ = (A[P*P]) † ((B[P*P])⁻)", Typed_COR_Expressions.Typed_Dagger(A, Typed_COR_Expressions.Typed_Complement(B)))
			A = lhs2
			if isinstance(rhs2, Typed_COR_Expressions.Typed_Complement):
				arg = rhs2.argument
				B = arg
				return ("((A[P*P]) ∘ ((B[P*P])⁻))⁻ = ((A[P*P])⁻) † (B[P*P])", Typed_COR_Expressions.Typed_Dagger(Typed_COR_Expressions.Typed_Complement(A), B))
		if isinstance(arg, Typed_COR_Expressions.Typed_Dagger):
			lhs2, rhs2 = arg.argument1, arg.argument2
			if isinstance(lhs2, Typed_COR_Expressions.Typed_Complement):
				arg = lhs2.argument
				A = arg
				B = rhs2
				return ("(((A[P*P])⁻) † (B[P*P]))⁻ = (A[P*P]) ∘ ((B[P*P])⁻)", Typed_COR_Expressions.Typed_Composition(A, Typed_COR_Expressions.Typed_Complement(B)))
			A = lhs2
			if isinstance(rhs2, Typed_COR_Expressions.Typed_Complement):
				arg = rhs2.argument
				B = arg
				return ("((A[P*P]) † ((B[P*P])⁻))⁻ = ((A[P*P])⁻) ∘ (B[P*P])", Typed_COR_Expressions.Typed_Composition(Typed_COR_Expressions.Typed_Complement(A), B))

	return (None, expression) # The given expression was unable to be simplified