import COR_Expressions

def simplify(expression):
	if isinstance(expression, COR_Expressions.Union):
		lhs1, rhs1 = expression.argument1, expression.argument2
		A = lhs1
		if str(A)==str(rhs1):
			return A
		if isinstance(rhs1, COR_Expressions.Intersection):
			lhs2, rhs2 = rhs1.argument1, rhs1.argument2
			B = lhs2
			if str(A)==str(rhs2):
				return A
			if isinstance(rhs2, COR_Expressions.Complement):
				arg = rhs2.argument
				if str(A)==str(arg):
					return COR_Expressions.Union(A, B)
			if isinstance(rhs2, COR_Expressions.Union):
				lhs3, rhs3 = rhs2.argument1, rhs2.argument2
				if str(A)==str(lhs3):
					C = rhs3
					return COR_Expressions.Union(A, COR_Expressions.Intersection(C, B))
				C = lhs3
				if str(A)==str(rhs3):
					return COR_Expressions.Union(A, COR_Expressions.Intersection(B, C))
			if isinstance(rhs2, COR_Expressions.Intersection):
				lhs3, rhs3 = rhs2.argument1, rhs2.argument2
				C = lhs3
				if str(A)==str(rhs3):
					return A
				if str(A)==str(lhs3):
					C = rhs3
					return A
			if str(A)==str(lhs2):
				B = rhs2
				return A
			if isinstance(lhs2, COR_Expressions.Union):
				lhs3, rhs3 = lhs2.argument1, lhs2.argument2
				if str(A)==str(lhs3):
					B = rhs3
					C = rhs2
					return COR_Expressions.Union(A, COR_Expressions.Intersection(B, C))
				B = lhs3
				if str(A)==str(rhs3):
					C = rhs2
					return COR_Expressions.Union(COR_Expressions.Intersection(B, C), A)
			if isinstance(lhs2, COR_Expressions.Intersection):
				lhs3, rhs3 = lhs2.argument1, lhs2.argument2
				B = lhs3
				if str(A)==str(rhs3):
					C = rhs2
					return A
				if str(A)==str(lhs3):
					B = rhs3
					C = rhs2
					return A
			if isinstance(lhs2, COR_Expressions.Complement):
				arg = lhs2.argument
				if str(A)==str(arg):
					B = rhs2
					return COR_Expressions.Union(B, A)
		if isinstance(rhs1, COR_Expressions.UniversalRelation):
			return COR_Expressions.UniversalRelation()
		if isinstance(rhs1, COR_Expressions.Union):
			lhs2, rhs2 = rhs1.argument1, rhs1.argument2
			if str(A)==str(lhs2):
				B = rhs2
				return COR_Expressions.Union(A, B)
			B = lhs2
			if str(A)==str(rhs2):
				return COR_Expressions.Union(B, A)
			if isinstance(rhs2, COR_Expressions.Union):
				lhs3, rhs3 = rhs2.argument1, rhs2.argument2
				C = lhs3
				if str(A)==str(rhs3):
					return COR_Expressions.Union(C, COR_Expressions.Union(A, B))
				if str(A)==str(lhs3):
					C = rhs3
					return COR_Expressions.Union(C, COR_Expressions.Union(B, A))
			if isinstance(rhs2, COR_Expressions.Intersection):
				lhs3, rhs3 = rhs2.argument1, rhs2.argument2
				if str(A)==str(lhs3):
					C = rhs3
					return COR_Expressions.Union(B, A)
				C = lhs3
				if str(A)==str(rhs3):
					return COR_Expressions.Union(A, B)
			if isinstance(rhs2, COR_Expressions.Complement):
				arg = rhs2.argument
				if str(A)==str(arg):
					return COR_Expressions.UniversalRelation()
			if isinstance(lhs2, COR_Expressions.Union):
				lhs3, rhs3 = lhs2.argument1, lhs2.argument2
				B = lhs3
				if str(A)==str(rhs3):
					C = rhs2
					return COR_Expressions.Union(C, COR_Expressions.Union(B, A))
				if str(A)==str(lhs3):
					B = rhs3
					C = rhs2
					return COR_Expressions.Union(B, COR_Expressions.Union(C, A))
			if isinstance(lhs2, COR_Expressions.Intersection):
				lhs3, rhs3 = lhs2.argument1, lhs2.argument2
				if str(A)==str(lhs3):
					B = rhs3
					C = rhs2
					return COR_Expressions.Union(C, A)
				B = lhs3
				if str(A)==str(rhs3):
					C = rhs2
					return COR_Expressions.Union(C, A)
			if isinstance(lhs2, COR_Expressions.Complement):
				arg = lhs2.argument
				if str(A)==str(arg):
					B = rhs2
					return COR_Expressions.UniversalRelation()
		if isinstance(rhs1, COR_Expressions.Complement):
			arg = rhs1.argument
			if str(A)==str(arg):
				return COR_Expressions.UniversalRelation()
			if isinstance(arg, COR_Expressions.Union):
				lhs3, rhs3 = arg.argument1, arg.argument2
				if str(A)==str(lhs3):
					B = rhs3
					return COR_Expressions.Union(A, COR_Expressions.Complement(B))
				B = lhs3
				if str(A)==str(rhs3):
					return COR_Expressions.Union(A, COR_Expressions.Complement(B))
			if isinstance(arg, COR_Expressions.Intersection):
				lhs3, rhs3 = arg.argument1, arg.argument2
				if str(A)==str(lhs3):
					B = rhs3
					return COR_Expressions.UniversalRelation()
				B = lhs3
				if str(A)==str(rhs3):
					return COR_Expressions.UniversalRelation()
		if isinstance(rhs1, COR_Expressions.EmptyRelation):
			return A
		if isinstance(rhs1, COR_Expressions.Composition):
			lhs2, rhs2 = rhs1.argument1, rhs1.argument2
			if str(A)==str(lhs2):
				if isinstance(rhs2, COR_Expressions.UniversalRelation):
					return COR_Expressions.Composition(A, COR_Expressions.UniversalRelation())
			if isinstance(lhs2, COR_Expressions.UniversalRelation):
				if str(A)==str(rhs2):
					return COR_Expressions.Composition(COR_Expressions.UniversalRelation(), A)
		if isinstance(rhs1, COR_Expressions.Dagger):
			lhs2, rhs2 = rhs1.argument1, rhs1.argument2
			if isinstance(lhs2, COR_Expressions.EmptyRelation):
				if str(A)==str(rhs2):
					return A
			if str(A)==str(lhs2):
				if isinstance(rhs2, COR_Expressions.EmptyRelation):
					return A
		if isinstance(lhs1, COR_Expressions.Union):
			lhs2, rhs2 = lhs1.argument1, lhs1.argument2
			A = lhs2
			B = rhs2
			if str(B)==str(rhs1):
				return COR_Expressions.Union(B, A)
			if str(A)==str(rhs1):
				return COR_Expressions.Union(A, B)
			if isinstance(rhs1, COR_Expressions.Union):
				lhs3, rhs3 = rhs1.argument1, rhs1.argument2
				if str(A)==str(lhs3):
					C = rhs3
					return COR_Expressions.Union(COR_Expressions.Union(A, B), C)
				if str(B)==str(lhs3):
					C = rhs3
					return COR_Expressions.Union(C, COR_Expressions.Union(B, A))
				C = lhs3
				if str(B)==str(rhs3):
					return COR_Expressions.Union(COR_Expressions.Union(A, C), B)
				if str(A)==str(rhs3):
					return COR_Expressions.Union(B, COR_Expressions.Union(A, C))
			if isinstance(rhs1, COR_Expressions.Intersection):
				lhs3, rhs3 = rhs1.argument1, rhs1.argument2
				if str(B)==str(lhs3):
					if str(A)==str(rhs3):
						return COR_Expressions.Union(A, B)
					C = rhs3
					return COR_Expressions.Union(A, B)
				if str(A)==str(lhs3):
					if str(B)==str(rhs3):
						return COR_Expressions.Union(B, A)
					C = rhs3
					return COR_Expressions.Union(A, B)
				C = lhs3
				if str(A)==str(rhs3):
					return COR_Expressions.Union(B, A)
				if str(B)==str(rhs3):
					return COR_Expressions.Union(B, A)
			if isinstance(rhs1, COR_Expressions.Complement):
				arg = rhs1.argument
				if str(B)==str(arg):
					return COR_Expressions.UniversalRelation()
				if str(A)==str(arg):
					return COR_Expressions.UniversalRelation()
			if isinstance(rhs2, COR_Expressions.Union):
				lhs3, rhs3 = rhs2.argument1, rhs2.argument2
				B = lhs3
				C = rhs3
				if str(C)==str(rhs1):
					return COR_Expressions.Union(B, COR_Expressions.Union(A, C))
				if str(B)==str(rhs1):
					return COR_Expressions.Union(A, COR_Expressions.Union(C, B))
			if isinstance(rhs2, COR_Expressions.Intersection):
				lhs3, rhs3 = rhs2.argument1, rhs2.argument2
				B = lhs3
				C = rhs3
				if str(B)==str(rhs1):
					return COR_Expressions.Union(A, B)
				if str(C)==str(rhs1):
					return COR_Expressions.Union(C, A)
			if isinstance(rhs2, COR_Expressions.Complement):
				arg = rhs2.argument
				B = arg
				if str(B)==str(rhs1):
					return COR_Expressions.UniversalRelation()
			if isinstance(lhs2, COR_Expressions.Union):
				lhs3, rhs3 = lhs2.argument1, lhs2.argument2
				A = lhs3
				B = rhs3
				C = rhs2
				if str(B)==str(rhs1):
					return COR_Expressions.Union(A, COR_Expressions.Union(C, B))
				if str(A)==str(rhs1):
					return COR_Expressions.Union(C, COR_Expressions.Union(A, B))
			if isinstance(lhs2, COR_Expressions.Complement):
				arg = lhs2.argument
				A = arg
				B = rhs2
				if str(A)==str(rhs1):
					return COR_Expressions.UniversalRelation()
			if isinstance(lhs2, COR_Expressions.Intersection):
				lhs3, rhs3 = lhs2.argument1, lhs2.argument2
				A = lhs3
				B = rhs3
				C = rhs2
				if str(B)==str(rhs1):
					return COR_Expressions.Union(C, B)
				if str(A)==str(rhs1):
					return COR_Expressions.Union(C, A)
		if isinstance(lhs1, COR_Expressions.Complement):
			arg = lhs1.argument
			A = arg
			if str(A)==str(rhs1):
				return COR_Expressions.UniversalRelation()
			if isinstance(rhs1, COR_Expressions.Union):
				lhs3, rhs3 = rhs1.argument1, rhs1.argument2
				B = lhs3
				if str(A)==str(rhs3):
					return COR_Expressions.UniversalRelation()
				if str(A)==str(lhs3):
					B = rhs3
					return COR_Expressions.UniversalRelation()
			if isinstance(rhs1, COR_Expressions.Complement):
				arg = rhs1.argument
				B = arg
				return COR_Expressions.Complement(COR_Expressions.Intersection(A, B))
			if isinstance(rhs1, COR_Expressions.Intersection):
				lhs3, rhs3 = rhs1.argument1, rhs1.argument2
				if str(A)==str(lhs3):
					B = rhs3
					return COR_Expressions.Union(B, COR_Expressions.Complement(A))
				B = lhs3
				if str(A)==str(rhs3):
					return COR_Expressions.Union(B, COR_Expressions.Complement(A))
			if isinstance(arg, COR_Expressions.Union):
				lhs3, rhs3 = arg.argument1, arg.argument2
				A = lhs3
				B = rhs3
				if str(B)==str(rhs1):
					return COR_Expressions.Union(COR_Expressions.Complement(A), B)
				if str(A)==str(rhs1):
					return COR_Expressions.Union(COR_Expressions.Complement(B), A)
			if isinstance(arg, COR_Expressions.Intersection):
				lhs3, rhs3 = arg.argument1, arg.argument2
				A = lhs3
				B = rhs3
				if str(B)==str(rhs1):
					return COR_Expressions.UniversalRelation()
				if str(A)==str(rhs1):
					return COR_Expressions.UniversalRelation()
		if isinstance(lhs1, COR_Expressions.UniversalRelation):
			A = rhs1
			return COR_Expressions.UniversalRelation()
		if isinstance(lhs1, COR_Expressions.Intersection):
			lhs2, rhs2 = lhs1.argument1, lhs1.argument2
			A = lhs2
			B = rhs2
			if str(A)==str(rhs1):
				return A
			if str(B)==str(rhs1):
				return B
			if isinstance(rhs1, COR_Expressions.Intersection):
				lhs3, rhs3 = rhs1.argument1, rhs1.argument2
				if str(B)==str(lhs3):
					C = rhs3
					return COR_Expressions.Intersection(COR_Expressions.Union(C, A), B)
				if str(A)==str(lhs3):
					C = rhs3
					return COR_Expressions.Intersection(COR_Expressions.Union(B, C), A)
				C = lhs3
				if str(B)==str(rhs3):
					return COR_Expressions.Intersection(B, COR_Expressions.Union(C, A))
				if str(A)==str(rhs3):
					return COR_Expressions.Intersection(A, COR_Expressions.Union(B, C))
			if isinstance(rhs1, COR_Expressions.Union):
				lhs3, rhs3 = rhs1.argument1, rhs1.argument2
				if str(A)==str(lhs3):
					if str(B)==str(rhs3):
						return COR_Expressions.Union(B, A)
					C = rhs3
					return COR_Expressions.Union(C, A)
				C = lhs3
				if str(B)==str(rhs3):
					return COR_Expressions.Union(B, C)
				if str(A)==str(rhs3):
					return COR_Expressions.Union(A, C)
				if str(B)==str(lhs3):
					C = rhs3
					return COR_Expressions.Union(B, C)
			if isinstance(rhs1, COR_Expressions.Complement):
				arg = rhs1.argument
				if str(B)==str(arg):
					return COR_Expressions.Union(COR_Expressions.Complement(B), A)
				if str(A)==str(arg):
					return COR_Expressions.Union(COR_Expressions.Complement(A), B)
			if isinstance(rhs2, COR_Expressions.Union):
				lhs3, rhs3 = rhs2.argument1, rhs2.argument2
				B = lhs3
				C = rhs3
				if str(B)==str(rhs1):
					return COR_Expressions.Union(B, COR_Expressions.Intersection(C, A))
				if str(C)==str(rhs1):
					return COR_Expressions.Union(COR_Expressions.Intersection(B, A), C)
			if isinstance(rhs2, COR_Expressions.Complement):
				arg = rhs2.argument
				B = arg
				if str(B)==str(rhs1):
					return COR_Expressions.Union(B, A)
			if isinstance(rhs2, COR_Expressions.Intersection):
				lhs3, rhs3 = rhs2.argument1, rhs2.argument2
				B = lhs3
				C = rhs3
				if str(B)==str(rhs1):
					return B
				if str(C)==str(rhs1):
					return C
			if isinstance(lhs2, COR_Expressions.Union):
				lhs3, rhs3 = lhs2.argument1, lhs2.argument2
				A = lhs3
				B = rhs3
				C = rhs2
				if str(B)==str(rhs1):
					return COR_Expressions.Union(B, COR_Expressions.Intersection(A, C))
				if str(A)==str(rhs1):
					return COR_Expressions.Union(COR_Expressions.Intersection(B, C), A)
			if isinstance(lhs2, COR_Expressions.Intersection):
				lhs3, rhs3 = lhs2.argument1, lhs2.argument2
				A = lhs3
				B = rhs3
				C = rhs2
				if str(B)==str(rhs1):
					return B
				if str(A)==str(rhs1):
					return A
			if isinstance(lhs2, COR_Expressions.Complement):
				arg = lhs2.argument
				A = arg
				B = rhs2
				if str(A)==str(rhs1):
					return COR_Expressions.Union(A, B)
		if isinstance(lhs1, COR_Expressions.EmptyRelation):
			A = rhs1
			return A
		if isinstance(lhs1, COR_Expressions.Composition):
			lhs2, rhs2 = lhs1.argument1, lhs1.argument2
			A = lhs2
			B = rhs2
			if isinstance(rhs1, COR_Expressions.Composition):
				lhs3, rhs3 = rhs1.argument1, rhs1.argument2
				if str(A)==str(lhs3):
					C = rhs3
					return COR_Expressions.Composition(A, COR_Expressions.Union(B, C))
				C = lhs3
				if str(B)==str(rhs3):
					return COR_Expressions.Composition(COR_Expressions.Union(C, A), B)
				if str(B)==str(lhs3):
					if str(B)==str(rhs3):
						return COR_Expressions.Composition(COR_Expressions.Union(A, B), B)
			if str(A)==str(rhs2):
				if isinstance(rhs1, COR_Expressions.Composition):
					lhs4, rhs4 = rhs1.argument1, rhs1.argument2
					if str(A)==str(lhs4):
						B = rhs4
						return COR_Expressions.Composition(A, COR_Expressions.Union(A, B))
					B = lhs4
					if str(A)==str(rhs4):
						return COR_Expressions.Composition(COR_Expressions.Union(B, A), A)
			if isinstance(rhs2, COR_Expressions.UniversalRelation):
				if str(A)==str(rhs1):
					return COR_Expressions.Composition(A, COR_Expressions.UniversalRelation())
			if isinstance(lhs2, COR_Expressions.UniversalRelation):
				A = rhs2
				if str(A)==str(rhs1):
					return COR_Expressions.Composition(COR_Expressions.UniversalRelation(), A)
		if isinstance(lhs1, COR_Expressions.Dagger):
			lhs2, rhs2 = lhs1.argument1, lhs1.argument2
			A = lhs2
			if isinstance(rhs2, COR_Expressions.EmptyRelation):
				if str(A)==str(rhs1):
					return A
			if isinstance(lhs2, COR_Expressions.EmptyRelation):
				A = rhs2
				if str(A)==str(rhs1):
					return A
		if isinstance(lhs1, COR_Expressions.Converse):
			arg = lhs1.argument
			A = arg
			if isinstance(rhs1, COR_Expressions.Converse):
				arg = rhs1.argument
				B = arg
				return COR_Expressions.Converse(COR_Expressions.Union(A, B))
	if isinstance(expression, COR_Expressions.Intersection):
		lhs1, rhs1 = expression.argument1, expression.argument2
		A = lhs1
		if str(A)==str(rhs1):
			return A
		if isinstance(rhs1, COR_Expressions.Complement):
			arg = rhs1.argument
			if str(A)==str(arg):
				return COR_Expressions.EmptyRelation()
			if isinstance(arg, COR_Expressions.Intersection):
				lhs3, rhs3 = arg.argument1, arg.argument2
				if str(A)==str(lhs3):
					B = rhs3
					return COR_Expressions.Intersection(A, COR_Expressions.Complement(B))
				B = lhs3
				if str(A)==str(rhs3):
					return COR_Expressions.Intersection(A, COR_Expressions.Complement(B))
			if isinstance(arg, COR_Expressions.Union):
				lhs3, rhs3 = arg.argument1, arg.argument2
				if str(A)==str(lhs3):
					B = rhs3
					return COR_Expressions.EmptyRelation()
				B = lhs3
				if str(A)==str(rhs3):
					return COR_Expressions.EmptyRelation()
		if isinstance(rhs1, COR_Expressions.UniversalRelation):
			return A
		if isinstance(rhs1, COR_Expressions.Intersection):
			lhs2, rhs2 = rhs1.argument1, rhs1.argument2
			B = lhs2
			if str(A)==str(rhs2):
				return COR_Expressions.Intersection(B, A)
			if isinstance(rhs2, COR_Expressions.Intersection):
				lhs3, rhs3 = rhs2.argument1, rhs2.argument2
				C = lhs3
				if str(A)==str(rhs3):
					return COR_Expressions.Intersection(COR_Expressions.Intersection(B, A), C)
				if str(A)==str(lhs3):
					C = rhs3
					return COR_Expressions.Intersection(COR_Expressions.Intersection(B, C), A)
			if isinstance(rhs2, COR_Expressions.Union):
				lhs3, rhs3 = rhs2.argument1, rhs2.argument2
				C = lhs3
				if str(A)==str(rhs3):
					return COR_Expressions.Intersection(A, B)
				if str(A)==str(lhs3):
					C = rhs3
					return COR_Expressions.Intersection(A, B)
			if isinstance(rhs2, COR_Expressions.Complement):
				arg = rhs2.argument
				if str(A)==str(arg):
					return COR_Expressions.EmptyRelation()
			if str(A)==str(lhs2):
				B = rhs2
				return COR_Expressions.Intersection(A, B)
			if isinstance(lhs2, COR_Expressions.Intersection):
				lhs3, rhs3 = lhs2.argument1, lhs2.argument2
				B = lhs3
				if str(A)==str(rhs3):
					C = rhs2
					return COR_Expressions.Intersection(COR_Expressions.Intersection(A, C), B)
				if str(A)==str(lhs3):
					B = rhs3
					C = rhs2
					return COR_Expressions.Intersection(COR_Expressions.Intersection(A, B), C)
			if isinstance(lhs2, COR_Expressions.Union):
				lhs3, rhs3 = lhs2.argument1, lhs2.argument2
				B = lhs3
				if str(A)==str(rhs3):
					C = rhs2
					return COR_Expressions.Intersection(C, A)
				if str(A)==str(lhs3):
					B = rhs3
					C = rhs2
					return COR_Expressions.Intersection(C, A)
			if isinstance(lhs2, COR_Expressions.Complement):
				arg = lhs2.argument
				if str(A)==str(arg):
					B = rhs2
					return COR_Expressions.EmptyRelation()
		if isinstance(rhs1, COR_Expressions.Union):
			lhs2, rhs2 = rhs1.argument1, rhs1.argument2
			B = lhs2
			if str(A)==str(rhs2):
				return A
			if isinstance(rhs2, COR_Expressions.Intersection):
				lhs3, rhs3 = rhs2.argument1, rhs2.argument2
				C = lhs3
				if str(A)==str(rhs3):
					return COR_Expressions.Intersection(COR_Expressions.Union(C, B), A)
				if str(A)==str(lhs3):
					C = rhs3
					return COR_Expressions.Intersection(COR_Expressions.Union(B, C), A)
			if isinstance(rhs2, COR_Expressions.Union):
				lhs3, rhs3 = rhs2.argument1, rhs2.argument2
				if str(A)==str(lhs3):
					C = rhs3
					return A
				C = lhs3
				if str(A)==str(rhs3):
					return A
			if isinstance(rhs2, COR_Expressions.Complement):
				arg = rhs2.argument
				if str(A)==str(arg):
					return COR_Expressions.Intersection(B, A)
			if str(A)==str(lhs2):
				B = rhs2
				return A
			if isinstance(lhs2, COR_Expressions.Intersection):
				lhs3, rhs3 = lhs2.argument1, lhs2.argument2
				B = lhs3
				if str(A)==str(rhs3):
					C = rhs2
					return COR_Expressions.Intersection(COR_Expressions.Union(C, B), A)
				if str(A)==str(lhs3):
					B = rhs3
					C = rhs2
					return COR_Expressions.Intersection(COR_Expressions.Union(C, B), A)
			if isinstance(lhs2, COR_Expressions.Complement):
				arg = lhs2.argument
				if str(A)==str(arg):
					B = rhs2
					return COR_Expressions.Intersection(A, B)
			if isinstance(lhs2, COR_Expressions.Union):
				lhs3, rhs3 = lhs2.argument1, lhs2.argument2
				if str(A)==str(lhs3):
					B = rhs3
					C = rhs2
					return A
				B = lhs3
				if str(A)==str(rhs3):
					C = rhs2
					return A
		if isinstance(rhs1, COR_Expressions.EmptyRelation):
			return COR_Expressions.EmptyRelation()
		if isinstance(rhs1, COR_Expressions.Dagger):
			lhs2, rhs2 = rhs1.argument1, rhs1.argument2
			if str(A)==str(lhs2):
				if isinstance(rhs2, COR_Expressions.IdentityRelation):
					return COR_Expressions.Dagger(A, COR_Expressions.EmptyRelation())
				if isinstance(rhs2, COR_Expressions.EmptyRelation):
					return COR_Expressions.Dagger(A, COR_Expressions.EmptyRelation())
			if isinstance(lhs2, COR_Expressions.EmptyRelation):
				if str(A)==str(rhs2):
					return COR_Expressions.Dagger(COR_Expressions.EmptyRelation(), A)
			if isinstance(lhs2, COR_Expressions.IdentityRelation):
				if str(A)==str(rhs2):
					return COR_Expressions.Dagger(COR_Expressions.EmptyRelation(), A)
		if isinstance(rhs1, COR_Expressions.Composition):
			lhs2, rhs2 = rhs1.argument1, rhs1.argument2
			if str(A)==str(lhs2):
				if isinstance(rhs2, COR_Expressions.UniversalRelation):
					return A
			if isinstance(lhs2, COR_Expressions.UniversalRelation):
				if str(A)==str(rhs2):
					return A
		if isinstance(lhs1, COR_Expressions.Intersection):
			lhs2, rhs2 = lhs1.argument1, lhs1.argument2
			A = lhs2
			B = rhs2
			if str(B)==str(rhs1):
				return COR_Expressions.Intersection(A, B)
			if str(A)==str(rhs1):
				return COR_Expressions.Intersection(B, A)
			if isinstance(rhs1, COR_Expressions.Intersection):
				lhs3, rhs3 = rhs1.argument1, rhs1.argument2
				C = lhs3
				if str(B)==str(rhs3):
					return COR_Expressions.Intersection(COR_Expressions.Intersection(C, B), A)
				if str(A)==str(rhs3):
					return COR_Expressions.Intersection(COR_Expressions.Intersection(C, B), A)
				if str(B)==str(lhs3):
					C = rhs3
					return COR_Expressions.Intersection(COR_Expressions.Intersection(A, C), B)
				if str(A)==str(lhs3):
					C = rhs3
					return COR_Expressions.Intersection(COR_Expressions.Intersection(A, B), C)
			if isinstance(rhs1, COR_Expressions.Union):
				lhs3, rhs3 = rhs1.argument1, rhs1.argument2
				if str(B)==str(lhs3):
					if str(A)==str(rhs3):
						return COR_Expressions.Intersection(A, B)
					C = rhs3
					return COR_Expressions.Intersection(A, B)
				C = lhs3
				if str(A)==str(rhs3):
					return COR_Expressions.Intersection(B, A)
				if str(B)==str(rhs3):
					return COR_Expressions.Intersection(B, A)
				if str(A)==str(lhs3):
					if str(B)==str(rhs3):
						return COR_Expressions.Intersection(A, B)
					C = rhs3
					return COR_Expressions.Intersection(B, A)
			if isinstance(rhs1, COR_Expressions.Complement):
				arg = rhs1.argument
				if str(B)==str(arg):
					return COR_Expressions.EmptyRelation()
				if str(A)==str(arg):
					return COR_Expressions.EmptyRelation()
			if isinstance(rhs2, COR_Expressions.Intersection):
				lhs3, rhs3 = rhs2.argument1, rhs2.argument2
				B = lhs3
				C = rhs3
				if str(C)==str(rhs1):
					return COR_Expressions.Intersection(COR_Expressions.Intersection(B, A), C)
				if str(B)==str(rhs1):
					return COR_Expressions.Intersection(COR_Expressions.Intersection(C, A), B)
			if isinstance(rhs2, COR_Expressions.Union):
				lhs3, rhs3 = rhs2.argument1, rhs2.argument2
				B = lhs3
				C = rhs3
				if str(B)==str(rhs1):
					return COR_Expressions.Intersection(B, A)
				if str(C)==str(rhs1):
					return COR_Expressions.Intersection(C, A)
			if isinstance(rhs2, COR_Expressions.Complement):
				arg = rhs2.argument
				B = arg
				if str(B)==str(rhs1):
					return COR_Expressions.EmptyRelation()
			if isinstance(lhs2, COR_Expressions.Intersection):
				lhs3, rhs3 = lhs2.argument1, lhs2.argument2
				A = lhs3
				B = rhs3
				C = rhs2
				if str(B)==str(rhs1):
					return COR_Expressions.Intersection(B, COR_Expressions.Intersection(A, C))
				if str(A)==str(rhs1):
					return COR_Expressions.Intersection(COR_Expressions.Intersection(C, A), B)
			if isinstance(lhs2, COR_Expressions.Union):
				lhs3, rhs3 = lhs2.argument1, lhs2.argument2
				A = lhs3
				B = rhs3
				C = rhs2
				if str(B)==str(rhs1):
					return COR_Expressions.Intersection(C, B)
				if str(A)==str(rhs1):
					return COR_Expressions.Intersection(C, A)
			if isinstance(lhs2, COR_Expressions.Complement):
				arg = lhs2.argument
				A = arg
				B = rhs2
				if str(A)==str(rhs1):
					return COR_Expressions.EmptyRelation()
		if isinstance(lhs1, COR_Expressions.Union):
			lhs2, rhs2 = lhs1.argument1, lhs1.argument2
			A = lhs2
			B = rhs2
			if str(B)==str(rhs1):
				return B
			if str(A)==str(rhs1):
				return A
			if isinstance(rhs1, COR_Expressions.Union):
				lhs3, rhs3 = rhs1.argument1, rhs1.argument2
				C = lhs3
				if str(A)==str(rhs3):
					return COR_Expressions.Union(A, COR_Expressions.Intersection(C, B))
				if str(B)==str(rhs3):
					return COR_Expressions.Union(B, COR_Expressions.Intersection(A, C))
				if str(B)==str(lhs3):
					if str(A)==str(rhs3):
						return COR_Expressions.Union(B, A)
					C = rhs3
					return COR_Expressions.Union(COR_Expressions.Intersection(C, A), B)
				if str(A)==str(lhs3):
					C = rhs3
					return COR_Expressions.Union(A, COR_Expressions.Intersection(B, C))
			if isinstance(rhs1, COR_Expressions.Intersection):
				lhs3, rhs3 = rhs1.argument1, rhs1.argument2
				if str(B)==str(lhs3):
					if str(A)==str(rhs3):
						return COR_Expressions.Intersection(A, B)
					C = rhs3
					return COR_Expressions.Intersection(C, B)
				C = lhs3
				if str(A)==str(rhs3):
					return COR_Expressions.Intersection(A, C)
				if str(B)==str(rhs3):
					return COR_Expressions.Intersection(C, B)
				if str(A)==str(lhs3):
					if str(B)==str(rhs3):
						return COR_Expressions.Intersection(B, A)
					C = rhs3
					return COR_Expressions.Intersection(C, A)
			if isinstance(rhs1, COR_Expressions.Complement):
				arg = rhs1.argument
				if str(A)==str(arg):
					return COR_Expressions.Intersection(COR_Expressions.Complement(A), B)
				if str(B)==str(arg):
					return COR_Expressions.Intersection(COR_Expressions.Complement(B), A)
			if isinstance(rhs2, COR_Expressions.Complement):
				arg = rhs2.argument
				B = arg
				if str(B)==str(rhs1):
					return COR_Expressions.Intersection(A, B)
			if isinstance(rhs2, COR_Expressions.Intersection):
				lhs3, rhs3 = rhs2.argument1, rhs2.argument2
				B = lhs3
				C = rhs3
				if str(B)==str(rhs1):
					return COR_Expressions.Intersection(B, COR_Expressions.Union(C, A))
				if str(C)==str(rhs1):
					return COR_Expressions.Intersection(COR_Expressions.Union(B, A), C)
			if isinstance(rhs2, COR_Expressions.Union):
				lhs3, rhs3 = rhs2.argument1, rhs2.argument2
				B = lhs3
				C = rhs3
				if str(B)==str(rhs1):
					return B
				if str(C)==str(rhs1):
					return C
			if isinstance(lhs2, COR_Expressions.Intersection):
				lhs3, rhs3 = lhs2.argument1, lhs2.argument2
				A = lhs3
				B = rhs3
				C = rhs2
				if str(A)==str(rhs1):
					return COR_Expressions.Intersection(A, COR_Expressions.Union(C, B))
				if str(B)==str(rhs1):
					return COR_Expressions.Intersection(B, COR_Expressions.Union(A, C))
			if isinstance(lhs2, COR_Expressions.Complement):
				arg = lhs2.argument
				A = arg
				B = rhs2
				if str(A)==str(rhs1):
					return COR_Expressions.Intersection(A, B)
			if isinstance(lhs2, COR_Expressions.Union):
				lhs3, rhs3 = lhs2.argument1, lhs2.argument2
				A = lhs3
				B = rhs3
				C = rhs2
				if str(A)==str(rhs1):
					return A
				if str(B)==str(rhs1):
					return B
		if isinstance(lhs1, COR_Expressions.EmptyRelation):
			A = rhs1
			return COR_Expressions.EmptyRelation()
		if isinstance(lhs1, COR_Expressions.UniversalRelation):
			A = rhs1
			return A
		if isinstance(lhs1, COR_Expressions.Complement):
			arg = lhs1.argument
			A = arg
			if str(A)==str(rhs1):
				return COR_Expressions.EmptyRelation()
			if isinstance(rhs1, COR_Expressions.Intersection):
				lhs3, rhs3 = rhs1.argument1, rhs1.argument2
				if str(A)==str(lhs3):
					B = rhs3
					return COR_Expressions.EmptyRelation()
				B = lhs3
				if str(A)==str(rhs3):
					return COR_Expressions.EmptyRelation()
			if isinstance(rhs1, COR_Expressions.Union):
				lhs3, rhs3 = rhs1.argument1, rhs1.argument2
				B = lhs3
				if str(A)==str(rhs3):
					return COR_Expressions.Intersection(B, COR_Expressions.Complement(A))
				if str(A)==str(lhs3):
					B = rhs3
					return COR_Expressions.Intersection(COR_Expressions.Complement(A), B)
			if isinstance(rhs1, COR_Expressions.Complement):
				arg = rhs1.argument
				B = arg
				return COR_Expressions.Complement(COR_Expressions.Union(B, A))
			if isinstance(arg, COR_Expressions.Intersection):
				lhs3, rhs3 = arg.argument1, arg.argument2
				A = lhs3
				B = rhs3
				if str(A)==str(rhs1):
					return COR_Expressions.Intersection(COR_Expressions.Complement(B), A)
				if str(B)==str(rhs1):
					return COR_Expressions.Intersection(B, COR_Expressions.Complement(A))
			if isinstance(arg, COR_Expressions.Union):
				lhs3, rhs3 = arg.argument1, arg.argument2
				A = lhs3
				B = rhs3
				if str(A)==str(rhs1):
					return COR_Expressions.EmptyRelation()
				if str(B)==str(rhs1):
					return COR_Expressions.EmptyRelation()
		if isinstance(lhs1, COR_Expressions.Dagger):
			lhs2, rhs2 = lhs1.argument1, lhs1.argument2
			A = lhs2
			B = rhs2
			if isinstance(rhs1, COR_Expressions.Dagger):
				lhs3, rhs3 = rhs1.argument1, rhs1.argument2
				C = lhs3
				if str(B)==str(rhs3):
					return COR_Expressions.Dagger(COR_Expressions.Intersection(A, C), B)
				if str(A)==str(lhs3):
					if str(A)==str(rhs3):
						return COR_Expressions.Dagger(A, COR_Expressions.Intersection(B, A))
					C = rhs3
					return COR_Expressions.Dagger(A, COR_Expressions.Intersection(B, C))
				if str(B)==str(lhs3):
					if str(B)==str(rhs3):
						return COR_Expressions.Dagger(COR_Expressions.Intersection(A, B), B)
			if str(A)==str(rhs2):
				if isinstance(rhs1, COR_Expressions.Dagger):
					lhs4, rhs4 = rhs1.argument1, rhs1.argument2
					B = lhs4
					if str(A)==str(rhs4):
						return COR_Expressions.Dagger(COR_Expressions.Intersection(B, A), A)
					if str(A)==str(lhs4):
						B = rhs4
						return COR_Expressions.Dagger(A, COR_Expressions.Intersection(B, A))
			if isinstance(rhs2, COR_Expressions.IdentityRelation):
				if str(A)==str(rhs1):
					return COR_Expressions.Dagger(A, COR_Expressions.EmptyRelation())
			if isinstance(rhs2, COR_Expressions.EmptyRelation):
				if str(A)==str(rhs1):
					return COR_Expressions.Dagger(A, COR_Expressions.EmptyRelation())
			if isinstance(lhs2, COR_Expressions.IdentityRelation):
				A = rhs2
				if str(A)==str(rhs1):
					return COR_Expressions.Dagger(COR_Expressions.EmptyRelation(), A)
			if isinstance(lhs2, COR_Expressions.EmptyRelation):
				A = rhs2
				if str(A)==str(rhs1):
					return COR_Expressions.Dagger(COR_Expressions.EmptyRelation(), A)
		if isinstance(lhs1, COR_Expressions.Converse):
			arg = lhs1.argument
			A = arg
			if isinstance(rhs1, COR_Expressions.Converse):
				arg = rhs1.argument
				B = arg
				return COR_Expressions.Converse(COR_Expressions.Intersection(A, B))
			if isinstance(rhs1, COR_Expressions.IdentityRelation):
				return COR_Expressions.Intersection(A, COR_Expressions.IdentityRelation())
		if isinstance(lhs1, COR_Expressions.IdentityRelation):
			if isinstance(rhs1, COR_Expressions.Converse):
				arg = rhs1.argument
				A = arg
				return COR_Expressions.Intersection(A, COR_Expressions.IdentityRelation())
		if isinstance(lhs1, COR_Expressions.Composition):
			lhs2, rhs2 = lhs1.argument1, lhs1.argument2
			A = lhs2
			if isinstance(rhs2, COR_Expressions.UniversalRelation):
				if str(A)==str(rhs1):
					return A
			if isinstance(lhs2, COR_Expressions.UniversalRelation):
				A = rhs2
				if str(A)==str(rhs1):
					return A
	if isinstance(expression, COR_Expressions.Converse):
		arg = expression.argument
		if isinstance(arg, COR_Expressions.IdentityRelation):
			return COR_Expressions.IdentityRelation()
		if isinstance(arg, COR_Expressions.Converse):
			arg = arg.argument
			A = arg
			return A
		if isinstance(arg, COR_Expressions.EmptyRelation):
			return COR_Expressions.EmptyRelation()
		if isinstance(arg, COR_Expressions.UniversalRelation):
			return COR_Expressions.UniversalRelation()
		if isinstance(arg, COR_Expressions.Union):
			lhs2, rhs2 = arg.argument1, arg.argument2
			if isinstance(lhs2, COR_Expressions.Converse):
				arg = lhs2.argument
				A = arg
				if str(A)==str(rhs2):
					return COR_Expressions.Union(A, COR_Expressions.Converse(A))
				B = rhs2
				return COR_Expressions.Union(COR_Expressions.Converse(B), A)
			A = lhs2
			if isinstance(rhs2, COR_Expressions.Converse):
				arg = rhs2.argument
				B = arg
				return COR_Expressions.Union(COR_Expressions.Converse(A), B)
		if isinstance(arg, COR_Expressions.Intersection):
			lhs2, rhs2 = arg.argument1, arg.argument2
			A = lhs2
			if isinstance(rhs2, COR_Expressions.IdentityRelation):
				return COR_Expressions.Intersection(COR_Expressions.IdentityRelation(), A)
			if isinstance(rhs2, COR_Expressions.Converse):
				arg = rhs2.argument
				B = arg
				return COR_Expressions.Intersection(COR_Expressions.Converse(A), B)
			if isinstance(lhs2, COR_Expressions.Converse):
				arg = lhs2.argument
				A = arg
				if str(A)==str(rhs2):
					return COR_Expressions.Intersection(COR_Expressions.Converse(A), A)
				B = rhs2
				return COR_Expressions.Intersection(COR_Expressions.Converse(B), A)
			if isinstance(lhs2, COR_Expressions.IdentityRelation):
				A = rhs2
				return COR_Expressions.Intersection(A, COR_Expressions.IdentityRelation())
		if isinstance(arg, COR_Expressions.Dagger):
			lhs2, rhs2 = arg.argument1, arg.argument2
			A = lhs2
			if isinstance(rhs2, COR_Expressions.Converse):
				arg = rhs2.argument
				B = arg
				return COR_Expressions.Dagger(B, COR_Expressions.Converse(A))
			if isinstance(lhs2, COR_Expressions.Converse):
				arg = lhs2.argument
				A = arg
				B = rhs2
				return COR_Expressions.Dagger(COR_Expressions.Converse(B), A)
		if isinstance(arg, COR_Expressions.Complement):
			arg = arg.argument
			if isinstance(arg, COR_Expressions.IdentityRelation):
				return COR_Expressions.Complement(COR_Expressions.IdentityRelation())
			if isinstance(arg, COR_Expressions.Converse):
				arg = arg.argument
				A = arg
				return COR_Expressions.Complement(A)
		if isinstance(arg, COR_Expressions.Composition):
			lhs2, rhs2 = arg.argument1, arg.argument2
			A = lhs2
			if isinstance(rhs2, COR_Expressions.Converse):
				arg = rhs2.argument
				B = arg
				return COR_Expressions.Composition(B, COR_Expressions.Converse(A))
			if isinstance(lhs2, COR_Expressions.Converse):
				arg = lhs2.argument
				A = arg
				if str(A)==str(rhs2):
					return COR_Expressions.Composition(COR_Expressions.Converse(A), A)
				B = rhs2
				return COR_Expressions.Composition(COR_Expressions.Converse(B), A)
	if isinstance(expression, COR_Expressions.Composition):
		lhs1, rhs1 = expression.argument1, expression.argument2
		A = lhs1
		if isinstance(rhs1, COR_Expressions.EmptyRelation):
			return COR_Expressions.EmptyRelation()
		if isinstance(rhs1, COR_Expressions.IdentityRelation):
			return A
		if isinstance(rhs1, COR_Expressions.Union):
			lhs2, rhs2 = rhs1.argument1, rhs1.argument2
			if isinstance(lhs2, COR_Expressions.IdentityRelation):
				B = rhs2
				return COR_Expressions.Union(A, COR_Expressions.Composition(A, B))
			B = lhs2
			if isinstance(rhs2, COR_Expressions.IdentityRelation):
				return COR_Expressions.Union(COR_Expressions.Composition(A, B), A)
			if str(A)==str(lhs2):
				if isinstance(rhs2, COR_Expressions.IdentityRelation):
					return COR_Expressions.Union(COR_Expressions.Composition(A, A), A)
		if isinstance(rhs1, COR_Expressions.Dagger):
			lhs2, rhs2 = rhs1.argument1, rhs1.argument2
			if isinstance(lhs2, COR_Expressions.EmptyRelation):
				if str(A)==str(rhs2):
					return COR_Expressions.Dagger(COR_Expressions.EmptyRelation(), A)
		if isinstance(lhs1, COR_Expressions.IdentityRelation):
			A = rhs1
			return A
		if isinstance(lhs1, COR_Expressions.EmptyRelation):
			A = rhs1
			return COR_Expressions.EmptyRelation()
		if isinstance(lhs1, COR_Expressions.Dagger):
			lhs2, rhs2 = lhs1.argument1, lhs1.argument2
			A = lhs2
			if isinstance(rhs2, COR_Expressions.EmptyRelation):
				if str(A)==str(rhs1):
					return COR_Expressions.Dagger(A, COR_Expressions.EmptyRelation())
		if isinstance(lhs1, COR_Expressions.Converse):
			arg = lhs1.argument
			A = arg
			if isinstance(rhs1, COR_Expressions.Converse):
				arg = rhs1.argument
				B = arg
				return COR_Expressions.Converse(COR_Expressions.Composition(B, A))
		if isinstance(lhs1, COR_Expressions.Union):
			lhs2, rhs2 = lhs1.argument1, lhs1.argument2
			A = lhs2
			if isinstance(rhs2, COR_Expressions.IdentityRelation):
				B = rhs1
				return COR_Expressions.Union(COR_Expressions.Composition(A, B), B)
			if isinstance(lhs2, COR_Expressions.IdentityRelation):
				A = rhs2
				B = rhs1
				return COR_Expressions.Union(B, COR_Expressions.Composition(A, B))
		if isinstance(lhs1, COR_Expressions.Complement):
			arg = lhs1.argument
			A = arg
			if isinstance(rhs1, COR_Expressions.Complement):
				arg = rhs1.argument
				if str(A)==str(arg):
					return COR_Expressions.Complement(COR_Expressions.Dagger(A, A))
				B = arg
				return COR_Expressions.Complement(COR_Expressions.Dagger(A, B))
		if isinstance(lhs1, COR_Expressions.UniversalRelation):
			if isinstance(rhs1, COR_Expressions.UniversalRelation):
				return COR_Expressions.UniversalRelation()
	if isinstance(expression, COR_Expressions.Dagger):
		lhs1, rhs1 = expression.argument1, expression.argument2
		A = lhs1
		if isinstance(rhs1, COR_Expressions.UniversalRelation):
			return COR_Expressions.UniversalRelation()
		if isinstance(rhs1, COR_Expressions.Composition):
			lhs2, rhs2 = rhs1.argument1, rhs1.argument2
			if isinstance(lhs2, COR_Expressions.UniversalRelation):
				if str(A)==str(rhs2):
					return COR_Expressions.Composition(COR_Expressions.UniversalRelation(), A)
		if isinstance(rhs1, COR_Expressions.Complement):
			arg = rhs1.argument
			if isinstance(arg, COR_Expressions.IdentityRelation):
				return A
		if isinstance(lhs1, COR_Expressions.UniversalRelation):
			A = rhs1
			return COR_Expressions.UniversalRelation()
		if isinstance(lhs1, COR_Expressions.Complement):
			arg = lhs1.argument
			if isinstance(arg, COR_Expressions.IdentityRelation):
				A = rhs1
				return A
			A = arg
			if isinstance(rhs1, COR_Expressions.Complement):
				arg = rhs1.argument
				B = arg
				return COR_Expressions.Complement(COR_Expressions.Composition(A, B))
		if isinstance(lhs1, COR_Expressions.Converse):
			arg = lhs1.argument
			A = arg
			if isinstance(rhs1, COR_Expressions.Converse):
				arg = rhs1.argument
				B = arg
				return COR_Expressions.Converse(COR_Expressions.Dagger(B, A))
		if isinstance(lhs1, COR_Expressions.EmptyRelation):
			if isinstance(rhs1, COR_Expressions.EmptyRelation):
				return COR_Expressions.EmptyRelation()
		if isinstance(lhs1, COR_Expressions.Composition):
			lhs2, rhs2 = lhs1.argument1, lhs1.argument2
			A = lhs2
			if isinstance(rhs2, COR_Expressions.UniversalRelation):
				if str(A)==str(rhs1):
					return COR_Expressions.Composition(A, COR_Expressions.UniversalRelation())
	if isinstance(expression, COR_Expressions.Complement):
		arg = expression.argument
		if isinstance(arg, COR_Expressions.UniversalRelation):
			return COR_Expressions.EmptyRelation()
		if isinstance(arg, COR_Expressions.EmptyRelation):
			return COR_Expressions.UniversalRelation()
		if isinstance(arg, COR_Expressions.Complement):
			arg = arg.argument
			A = arg
			return A
		if isinstance(arg, COR_Expressions.Union):
			lhs2, rhs2 = arg.argument1, arg.argument2
			A = lhs2
			if isinstance(rhs2, COR_Expressions.Complement):
				arg = rhs2.argument
				B = arg
				return COR_Expressions.Intersection(COR_Expressions.Complement(A), B)
			if isinstance(lhs2, COR_Expressions.Complement):
				arg = lhs2.argument
				A = arg
				B = rhs2
				return COR_Expressions.Intersection(A, COR_Expressions.Complement(B))
		if isinstance(arg, COR_Expressions.Composition):
			lhs2, rhs2 = arg.argument1, arg.argument2
			A = lhs2
			if isinstance(rhs2, COR_Expressions.Complement):
				arg = rhs2.argument
				if str(A)==str(arg):
					return COR_Expressions.Dagger(COR_Expressions.Complement(A), A)
				B = arg
				return COR_Expressions.Dagger(COR_Expressions.Complement(A), B)
			if isinstance(lhs2, COR_Expressions.Complement):
				arg = lhs2.argument
				A = arg
				if str(A)==str(rhs2):
					return COR_Expressions.Dagger(A, COR_Expressions.Complement(A))
				B = rhs2
				return COR_Expressions.Dagger(A, COR_Expressions.Complement(B))
		if isinstance(arg, COR_Expressions.Converse):
			arg = arg.argument
			if isinstance(arg, COR_Expressions.Complement):
				arg = arg.argument
				A = arg
				return COR_Expressions.Converse(A)
		if isinstance(arg, COR_Expressions.Intersection):
			lhs2, rhs2 = arg.argument1, arg.argument2
			if isinstance(lhs2, COR_Expressions.Complement):
				arg = lhs2.argument
				A = arg
				B = rhs2
				return COR_Expressions.Union(COR_Expressions.Complement(B), A)
			A = lhs2
			if isinstance(rhs2, COR_Expressions.Complement):
				arg = rhs2.argument
				B = arg
				return COR_Expressions.Union(B, COR_Expressions.Complement(A))
		if isinstance(arg, COR_Expressions.Dagger):
			lhs2, rhs2 = arg.argument1, arg.argument2
			A = lhs2
			if isinstance(rhs2, COR_Expressions.Complement):
				arg = rhs2.argument
				if str(A)==str(arg):
					return COR_Expressions.Composition(COR_Expressions.Complement(A), A)
				B = arg
				return COR_Expressions.Composition(COR_Expressions.Complement(A), B)
			if isinstance(lhs2, COR_Expressions.Complement):
				arg = lhs2.argument
				A = arg
				B = rhs2
				return COR_Expressions.Composition(A, COR_Expressions.Complement(B))

	return expression # The given expression was unable to be simplified