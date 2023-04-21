import COR_Expressions

def simplify(expression):
	if isinstance(expression, COR_Expressions.Intersection):
		lhs1, rhs1 = expression.argument1, expression.argument2
		A = lhs1
		if str(A)==str(rhs1):
			return A
		if isinstance(rhs1, COR_Expressions.UniversalRelation):
			return A
		if isinstance(rhs1, COR_Expressions.Intersection):
			lhs2, rhs2 = rhs1.argument1, rhs1.argument2
			if str(A)==str(lhs2):
				B = rhs2
				return COR_Expressions.Intersection(B, A)
			B = lhs2
			if str(A)==str(rhs2):
				return COR_Expressions.Intersection(A, B)
		if isinstance(rhs1, COR_Expressions.Union):
			lhs2, rhs2 = rhs1.argument1, rhs1.argument2
			if str(A)==str(lhs2):
				B = rhs2
				return A
			B = lhs2
			if str(A)==str(rhs2):
				return A
		if isinstance(rhs1, COR_Expressions.EmptyRelation):
			return COR_Expressions.EmptyRelation()
		if isinstance(rhs1, COR_Expressions.Complement):
			arg = rhs1.argument
			if str(A)==str(arg):
				return COR_Expressions.EmptyRelation()
		if isinstance(lhs1, COR_Expressions.Union):
			lhs2, rhs2 = lhs1.argument1, lhs1.argument2
			A = lhs2
			B = rhs2
			if str(B)==str(rhs1):
				return B
			if str(A)==str(rhs1):
				return A
		if isinstance(lhs1, COR_Expressions.UniversalRelation):
			A = rhs1
			return A
		if isinstance(lhs1, COR_Expressions.Intersection):
			lhs2, rhs2 = lhs1.argument1, lhs1.argument2
			A = lhs2
			B = rhs2
			if str(A)==str(rhs1):
				return COR_Expressions.Intersection(B, A)
			if str(B)==str(rhs1):
				return COR_Expressions.Intersection(B, A)
		if isinstance(lhs1, COR_Expressions.EmptyRelation):
			A = rhs1
			return COR_Expressions.EmptyRelation()
		if isinstance(lhs1, COR_Expressions.Complement):
			arg = lhs1.argument
			A = arg
			if str(A)==str(rhs1):
				return COR_Expressions.EmptyRelation()
	if isinstance(expression, COR_Expressions.Union):
		lhs1, rhs1 = expression.argument1, expression.argument2
		A = lhs1
		if str(A)==str(rhs1):
			return A
		if isinstance(rhs1, COR_Expressions.UniversalRelation):
			return COR_Expressions.UniversalRelation()
		if isinstance(rhs1, COR_Expressions.Intersection):
			lhs2, rhs2 = rhs1.argument1, rhs1.argument2
			B = lhs2
			if str(A)==str(rhs2):
				return A
			if str(A)==str(lhs2):
				B = rhs2
				return A
		if isinstance(rhs1, COR_Expressions.Union):
			lhs2, rhs2 = rhs1.argument1, rhs1.argument2
			if str(A)==str(lhs2):
				B = rhs2
				return COR_Expressions.Union(B, A)
			B = lhs2
			if str(A)==str(rhs2):
				return COR_Expressions.Union(B, A)
		if isinstance(rhs1, COR_Expressions.EmptyRelation):
			return A
		if isinstance(rhs1, COR_Expressions.Complement):
			arg = rhs1.argument
			if str(A)==str(arg):
				return COR_Expressions.UniversalRelation()
		if isinstance(lhs1, COR_Expressions.UniversalRelation):
			A = rhs1
			return COR_Expressions.UniversalRelation()
		if isinstance(lhs1, COR_Expressions.Intersection):
			lhs2, rhs2 = lhs1.argument1, lhs1.argument2
			A = lhs2
			B = rhs2
			if str(B)==str(rhs1):
				return B
			if str(A)==str(rhs1):
				return A
		if isinstance(lhs1, COR_Expressions.Union):
			lhs2, rhs2 = lhs1.argument1, lhs1.argument2
			A = lhs2
			B = rhs2
			if str(B)==str(rhs1):
				return COR_Expressions.Union(A, B)
			if str(A)==str(rhs1):
				return COR_Expressions.Union(B, A)
		if isinstance(lhs1, COR_Expressions.Complement):
			arg = lhs1.argument
			A = arg
			if str(A)==str(rhs1):
				return COR_Expressions.UniversalRelation()
		if isinstance(lhs1, COR_Expressions.EmptyRelation):
			A = rhs1
			return A
	if isinstance(expression, COR_Expressions.Dagger):
		lhs1, rhs1 = expression.argument1, expression.argument2
		if isinstance(lhs1, COR_Expressions.UniversalRelation):
			A = rhs1
			return COR_Expressions.UniversalRelation()
		A = lhs1
		if isinstance(rhs1, COR_Expressions.UniversalRelation):
			return COR_Expressions.UniversalRelation()
	if isinstance(expression, COR_Expressions.Converse):
		arg = expression.argument
		if isinstance(arg, COR_Expressions.Converse):
			arg = arg.argument
			A = arg
			return A
		if isinstance(arg, COR_Expressions.IdentityRelation):
			return COR_Expressions.IdentityRelation()
		if isinstance(arg, COR_Expressions.EmptyRelation):
			return COR_Expressions.EmptyRelation()
		if isinstance(arg, COR_Expressions.UniversalRelation):
			return COR_Expressions.UniversalRelation()
	if isinstance(expression, COR_Expressions.Composition):
		lhs1, rhs1 = expression.argument1, expression.argument2
		A = lhs1
		if isinstance(rhs1, COR_Expressions.IdentityRelation):
			return A
		if isinstance(rhs1, COR_Expressions.EmptyRelation):
			return COR_Expressions.EmptyRelation()
		if isinstance(lhs1, COR_Expressions.EmptyRelation):
			A = rhs1
			return COR_Expressions.EmptyRelation()
		if isinstance(lhs1, COR_Expressions.IdentityRelation):
			A = rhs1
			return A
	if isinstance(expression, COR_Expressions.Complement):
		arg = expression.argument
		if isinstance(arg, COR_Expressions.EmptyRelation):
			return COR_Expressions.UniversalRelation()
		if isinstance(arg, COR_Expressions.UniversalRelation):
			return COR_Expressions.EmptyRelation()
		if isinstance(arg, COR_Expressions.Complement):
			arg = arg.argument
			A = arg
			return A

	return expression # The given expression was unable to be simplified