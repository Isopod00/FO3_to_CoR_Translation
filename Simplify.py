import COR_Expressions

def simplify(expression):
	if isinstance(expression, COR_Expressions.Intersection):
		lhs1, rhs1 = expression.argument1, expression.argument2
		B = lhs1
		if str(B)==str(rhs1):
			return B
		if isinstance(rhs1, COR_Expressions.Intersection):
			lhs2, rhs2 = rhs1.argument1, rhs1.argument2
			C = lhs2
			if str(B)==str(rhs2):
				return COR_Expressions.Intersection(C, B)
			if str(B)==str(lhs2):
				A = rhs2
				return COR_Expressions.Intersection(A, B)
			A = lhs2
			if str(B)==str(rhs2):
				return COR_Expressions.Intersection(B, A)
		if isinstance(rhs1, COR_Expressions.UniversalRelation):
			return B
		if isinstance(rhs1, COR_Expressions.Complement):
			arg = rhs1.argument
			if str(B)==str(arg):
				return COR_Expressions.EmptyRelation()
		if isinstance(rhs1, COR_Expressions.Union):
			lhs2, rhs2 = rhs1.argument1, rhs1.argument2
			A = lhs2
			if str(B)==str(rhs2):
				return B
			if str(B)==str(lhs2):
				C = rhs2
				return B
			C = lhs2
			if str(B)==str(rhs2):
				return B
		if isinstance(rhs1, COR_Expressions.EmptyRelation):
			return COR_Expressions.EmptyRelation()
		A = lhs1
		if str(A)==str(rhs1):
			return A
		if isinstance(rhs1, COR_Expressions.Intersection):
			lhs2, rhs2 = rhs1.argument1, rhs1.argument2
			if str(A)==str(lhs2):
				B = rhs2
				return COR_Expressions.Intersection(B, A)
			B = lhs2
			if str(A)==str(rhs2):
				return COR_Expressions.Intersection(B, A)
			C = lhs2
			if str(A)==str(rhs2):
				return COR_Expressions.Intersection(C, A)
		if isinstance(rhs1, COR_Expressions.Union):
			lhs2, rhs2 = rhs1.argument1, rhs1.argument2
			if str(A)==str(lhs2):
				B = rhs2
				return A
			C = lhs2
			if str(A)==str(rhs2):
				return A
			B = lhs2
			if str(A)==str(rhs2):
				return A
		if isinstance(rhs1, COR_Expressions.Complement):
			arg = rhs1.argument
			if str(A)==str(arg):
				return COR_Expressions.EmptyRelation()
		if isinstance(rhs1, COR_Expressions.EmptyRelation):
			return COR_Expressions.EmptyRelation()
		if isinstance(rhs1, COR_Expressions.UniversalRelation):
			return A
		C = lhs1
		if str(C)==str(rhs1):
			return C
		if isinstance(rhs1, COR_Expressions.Union):
			lhs2, rhs2 = rhs1.argument1, rhs1.argument2
			B = lhs2
			if str(C)==str(rhs2):
				return C
			if str(C)==str(lhs2):
				A = rhs2
				return C
			A = lhs2
			if str(C)==str(rhs2):
				return C
		if isinstance(rhs1, COR_Expressions.Intersection):
			lhs2, rhs2 = rhs1.argument1, rhs1.argument2
			if str(C)==str(lhs2):
				B = rhs2
				return COR_Expressions.Intersection(B, C)
			A = lhs2
			if str(C)==str(rhs2):
				return COR_Expressions.Intersection(C, A)
			B = lhs2
			if str(C)==str(rhs2):
				return COR_Expressions.Intersection(B, C)
		if isinstance(rhs1, COR_Expressions.Complement):
			arg = rhs1.argument
			if str(C)==str(arg):
				return COR_Expressions.EmptyRelation()
		if isinstance(rhs1, COR_Expressions.EmptyRelation):
			return COR_Expressions.EmptyRelation()
		if isinstance(rhs1, COR_Expressions.UniversalRelation):
			return C
		if isinstance(lhs1, COR_Expressions.Intersection):
			lhs2, rhs2 = lhs1.argument1, lhs1.argument2
			A = lhs2
			C = rhs2
			if str(A)==str(rhs1):
				return COR_Expressions.Intersection(C, A)
			if str(C)==str(rhs1):
				return COR_Expressions.Intersection(C, A)
			B = rhs2
			if str(B)==str(rhs1):
				return COR_Expressions.Intersection(B, A)
			if str(A)==str(rhs1):
				return COR_Expressions.Intersection(A, B)
			B = lhs2
			C = rhs2
			if str(C)==str(rhs1):
				return COR_Expressions.Intersection(B, C)
			if str(B)==str(rhs1):
				return COR_Expressions.Intersection(B, C)
			A = rhs2
			if str(B)==str(rhs1):
				return COR_Expressions.Intersection(B, A)
			if str(A)==str(rhs1):
				return COR_Expressions.Intersection(B, A)
			C = lhs2
			A = rhs2
			if str(A)==str(rhs1):
				return COR_Expressions.Intersection(A, C)
			if str(C)==str(rhs1):
				return COR_Expressions.Intersection(C, A)
			B = rhs2
			if str(C)==str(rhs1):
				return COR_Expressions.Intersection(B, C)
			if str(B)==str(rhs1):
				return COR_Expressions.Intersection(B, C)
		if isinstance(lhs1, COR_Expressions.Union):
			lhs2, rhs2 = lhs1.argument1, lhs1.argument2
			B = lhs2
			C = rhs2
			if str(B)==str(rhs1):
				return B
			if str(C)==str(rhs1):
				return C
			A = rhs2
			if str(B)==str(rhs1):
				return B
			if str(A)==str(rhs1):
				return A
			C = lhs2
			B = rhs2
			if str(B)==str(rhs1):
				return B
			if str(C)==str(rhs1):
				return C
			A = rhs2
			if str(A)==str(rhs1):
				return A
			if str(C)==str(rhs1):
				return C
			A = lhs2
			B = rhs2
			if str(B)==str(rhs1):
				return B
			if str(A)==str(rhs1):
				return A
			C = rhs2
			if str(A)==str(rhs1):
				return A
			if str(C)==str(rhs1):
				return C
		if isinstance(lhs1, COR_Expressions.UniversalRelation):
			C = rhs1
			return C
		if isinstance(lhs1, COR_Expressions.Complement):
			arg = lhs1.argument
			B = arg
			if str(B)==str(rhs1):
				return COR_Expressions.EmptyRelation()
			A = arg
			if str(A)==str(rhs1):
				return COR_Expressions.EmptyRelation()
			C = arg
			if str(C)==str(rhs1):
				return COR_Expressions.EmptyRelation()
		if isinstance(lhs1, COR_Expressions.EmptyRelation):
			B = rhs1
			return COR_Expressions.EmptyRelation()
	if isinstance(expression, COR_Expressions.Union):
		lhs1, rhs1 = expression.argument1, expression.argument2
		B = lhs1
		if str(B)==str(rhs1):
			return B
		if isinstance(rhs1, COR_Expressions.UniversalRelation):
			return COR_Expressions.UniversalRelation()
		if isinstance(rhs1, COR_Expressions.Complement):
			arg = rhs1.argument
			if str(B)==str(arg):
				return COR_Expressions.UniversalRelation()
		if isinstance(rhs1, COR_Expressions.Union):
			lhs2, rhs2 = rhs1.argument1, rhs1.argument2
			A = lhs2
			if str(B)==str(rhs2):
				return COR_Expressions.Union(B, A)
			if str(B)==str(lhs2):
				A = rhs2
				return COR_Expressions.Union(A, B)
			C = lhs2
			if str(B)==str(rhs2):
				return COR_Expressions.Union(C, B)
		if isinstance(rhs1, COR_Expressions.Intersection):
			lhs2, rhs2 = rhs1.argument1, rhs1.argument2
			A = lhs2
			if str(B)==str(rhs2):
				return B
			if str(B)==str(lhs2):
				A = rhs2
				return B
			C = lhs2
			if str(B)==str(rhs2):
				return B
		if isinstance(rhs1, COR_Expressions.EmptyRelation):
			return B
		A = lhs1
		if str(A)==str(rhs1):
			return A
		if isinstance(rhs1, COR_Expressions.Union):
			lhs2, rhs2 = rhs1.argument1, rhs1.argument2
			if str(A)==str(lhs2):
				C = rhs2
				return COR_Expressions.Union(A, C)
			B = lhs2
			if str(A)==str(rhs2):
				return COR_Expressions.Union(A, B)
			C = lhs2
			if str(A)==str(rhs2):
				return COR_Expressions.Union(A, C)
		if isinstance(rhs1, COR_Expressions.Intersection):
			lhs2, rhs2 = rhs1.argument1, rhs1.argument2
			C = lhs2
			if str(A)==str(rhs2):
				return A
			if str(A)==str(lhs2):
				B = rhs2
				return A
			B = lhs2
			if str(A)==str(rhs2):
				return A
		if isinstance(rhs1, COR_Expressions.Complement):
			arg = rhs1.argument
			if str(A)==str(arg):
				return COR_Expressions.UniversalRelation()
		if isinstance(rhs1, COR_Expressions.UniversalRelation):
			return COR_Expressions.UniversalRelation()
		if isinstance(rhs1, COR_Expressions.EmptyRelation):
			return A
		C = lhs1
		if str(C)==str(rhs1):
			return C
		if isinstance(rhs1, COR_Expressions.Union):
			lhs2, rhs2 = rhs1.argument1, rhs1.argument2
			if str(C)==str(lhs2):
				A = rhs2
				return COR_Expressions.Union(C, A)
			A = lhs2
			if str(C)==str(rhs2):
				return COR_Expressions.Union(C, A)
			B = lhs2
			if str(C)==str(rhs2):
				return COR_Expressions.Union(C, B)
		if isinstance(rhs1, COR_Expressions.UniversalRelation):
			return COR_Expressions.UniversalRelation()
		if isinstance(rhs1, COR_Expressions.Intersection):
			lhs2, rhs2 = rhs1.argument1, rhs1.argument2
			if str(C)==str(lhs2):
				A = rhs2
				return C
			A = lhs2
			if str(C)==str(rhs2):
				return C
			B = lhs2
			if str(C)==str(rhs2):
				return C
		if isinstance(rhs1, COR_Expressions.Complement):
			arg = rhs1.argument
			if str(C)==str(arg):
				return COR_Expressions.UniversalRelation()
		if isinstance(rhs1, COR_Expressions.EmptyRelation):
			return C
		if isinstance(lhs1, COR_Expressions.Union):
			lhs2, rhs2 = lhs1.argument1, lhs1.argument2
			C = lhs2
			B = rhs2
			if str(C)==str(rhs1):
				return COR_Expressions.Union(C, B)
			if str(B)==str(rhs1):
				return COR_Expressions.Union(B, C)
			A = rhs2
			if str(C)==str(rhs1):
				return COR_Expressions.Union(A, C)
			if str(A)==str(rhs1):
				return COR_Expressions.Union(C, A)
			B = lhs2
			C = rhs2
			if str(C)==str(rhs1):
				return COR_Expressions.Union(B, C)
			if str(B)==str(rhs1):
				return COR_Expressions.Union(C, B)
			A = rhs2
			if str(B)==str(rhs1):
				return COR_Expressions.Union(B, A)
			if str(A)==str(rhs1):
				return COR_Expressions.Union(A, B)
			A = lhs2
			B = rhs2
			if str(B)==str(rhs1):
				return COR_Expressions.Union(B, A)
			if str(A)==str(rhs1):
				return COR_Expressions.Union(B, A)
			C = rhs2
			if str(A)==str(rhs1):
				return COR_Expressions.Union(A, C)
			if str(C)==str(rhs1):
				return COR_Expressions.Union(A, C)
		if isinstance(lhs1, COR_Expressions.Complement):
			arg = lhs1.argument
			C = arg
			if str(C)==str(rhs1):
				return COR_Expressions.UniversalRelation()
			B = arg
			if str(B)==str(rhs1):
				return COR_Expressions.UniversalRelation()
			A = arg
			if str(A)==str(rhs1):
				return COR_Expressions.UniversalRelation()
		if isinstance(lhs1, COR_Expressions.Intersection):
			lhs2, rhs2 = lhs1.argument1, lhs1.argument2
			B = lhs2
			C = rhs2
			if str(C)==str(rhs1):
				return C
			if str(B)==str(rhs1):
				return B
			A = rhs2
			if str(A)==str(rhs1):
				return A
			if str(B)==str(rhs1):
				return B
			A = lhs2
			C = rhs2
			if str(C)==str(rhs1):
				return C
			if str(A)==str(rhs1):
				return A
			B = rhs2
			if str(A)==str(rhs1):
				return A
			if str(B)==str(rhs1):
				return B
			C = lhs2
			A = rhs2
			if str(A)==str(rhs1):
				return A
			if str(C)==str(rhs1):
				return C
			B = rhs2
			if str(C)==str(rhs1):
				return C
			if str(B)==str(rhs1):
				return B
		if isinstance(lhs1, COR_Expressions.EmptyRelation):
			C = rhs1
			return C
		if isinstance(lhs1, COR_Expressions.UniversalRelation):
			C = rhs1
			return COR_Expressions.UniversalRelation()
	if isinstance(expression, COR_Expressions.Composition):
		lhs1, rhs1 = expression.argument1, expression.argument2
		if isinstance(lhs1, COR_Expressions.EmptyRelation):
			C = rhs1
			return COR_Expressions.EmptyRelation()
		if isinstance(lhs1, COR_Expressions.IdentityRelation):
			C = rhs1
			return C
		C = lhs1
		if isinstance(rhs1, COR_Expressions.EmptyRelation):
			return COR_Expressions.EmptyRelation()
		if isinstance(rhs1, COR_Expressions.IdentityRelation):
			return C
		A = lhs1
		if isinstance(rhs1, COR_Expressions.IdentityRelation):
			return A
		if isinstance(rhs1, COR_Expressions.EmptyRelation):
			return COR_Expressions.EmptyRelation()
		B = lhs1
		if isinstance(rhs1, COR_Expressions.IdentityRelation):
			return B
		if isinstance(rhs1, COR_Expressions.EmptyRelation):
			return COR_Expressions.EmptyRelation()
	if isinstance(expression, COR_Expressions.Converse):
		arg = expression.argument
		if isinstance(arg, COR_Expressions.UniversalRelation):
			return COR_Expressions.UniversalRelation()
		if isinstance(arg, COR_Expressions.Converse):
			arg = arg.argument
			A = arg
			return A
		if isinstance(arg, COR_Expressions.EmptyRelation):
			return COR_Expressions.EmptyRelation()
		if isinstance(arg, COR_Expressions.IdentityRelation):
			return COR_Expressions.IdentityRelation()
	if isinstance(expression, COR_Expressions.Complement):
		arg = expression.argument
		if isinstance(arg, COR_Expressions.UniversalRelation):
			return COR_Expressions.EmptyRelation()
		if isinstance(arg, COR_Expressions.Complement):
			arg = arg.argument
			B = arg
			return B
		if isinstance(arg, COR_Expressions.EmptyRelation):
			return COR_Expressions.UniversalRelation()
	if isinstance(expression, COR_Expressions.Dagger):
		lhs1, rhs1 = expression.argument1, expression.argument2
		A = lhs1
		if isinstance(rhs1, COR_Expressions.UniversalRelation):
			return COR_Expressions.UniversalRelation()
		C = lhs1
		if isinstance(rhs1, COR_Expressions.UniversalRelation):
			return COR_Expressions.UniversalRelation()
		B = lhs1
		if isinstance(rhs1, COR_Expressions.UniversalRelation):
			return COR_Expressions.UniversalRelation()
		if isinstance(lhs1, COR_Expressions.UniversalRelation):
			B = rhs1
			return COR_Expressions.UniversalRelation()

	return expression # The given expression was unable to be simplified