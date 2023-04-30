import Typed_COR_Expressions

def simplify(expression):
	if isinstance(expression, Typed_COR_Expressions.Typed_Intersection):
		lhs1, rhs1 = expression.argument1, expression.argument2
		A = lhs1
		if str(A)==str(rhs1):
			return A
		if isinstance(rhs1, Typed_COR_Expressions.Typed_UniversalRelation):
			return A
		if isinstance(rhs1, Typed_COR_Expressions.Typed_Intersection):
			lhs2, rhs2 = rhs1.argument1, rhs1.argument2
			if str(A)==str(lhs2):
				B = rhs2
				return Typed_COR_Expressions.Typed_Intersection(B, A)
			B = lhs2
			if str(A)==str(rhs2):
				return Typed_COR_Expressions.Typed_Intersection(A, B)
		if isinstance(rhs1, Typed_COR_Expressions.Typed_Union):
			lhs2, rhs2 = rhs1.argument1, rhs1.argument2
			if str(A)==str(lhs2):
				B = rhs2
				return A
			B = lhs2
			if str(A)==str(rhs2):
				return A
		if isinstance(rhs1, Typed_COR_Expressions.Typed_EmptyRelation):
			return Typed_COR_Expressions.Typed_EmptyRelation(expression.type()[0], expression.type()[1])
		if isinstance(rhs1, Typed_COR_Expressions.Typed_Complement):
			arg = rhs1.argument
			if str(A)==str(arg):
				return Typed_COR_Expressions.Typed_EmptyRelation(expression.type()[0], expression.type()[1])
		if isinstance(lhs1, Typed_COR_Expressions.Typed_Union):
			lhs2, rhs2 = lhs1.argument1, lhs1.argument2
			A = lhs2
			B = rhs2
			if str(B)==str(rhs1):
				return B
			if str(A)==str(rhs1):
				return A
		if isinstance(lhs1, Typed_COR_Expressions.Typed_UniversalRelation):
			A = rhs1
			return A
		if isinstance(lhs1, Typed_COR_Expressions.Typed_Intersection):
			lhs2, rhs2 = lhs1.argument1, lhs1.argument2
			A = lhs2
			B = rhs2
			if str(A)==str(rhs1):
				return Typed_COR_Expressions.Typed_Intersection(B, A)
			if str(B)==str(rhs1):
				return Typed_COR_Expressions.Typed_Intersection(B, A)
		if isinstance(lhs1, Typed_COR_Expressions.Typed_EmptyRelation):
			A = rhs1
			return Typed_COR_Expressions.Typed_EmptyRelation(expression.type()[0], expression.type()[1])
		if isinstance(lhs1, Typed_COR_Expressions.Typed_Complement):
			arg = lhs1.argument
			A = arg
			if str(A)==str(rhs1):
				return Typed_COR_Expressions.Typed_EmptyRelation(expression.type()[0], expression.type()[1])
	if isinstance(expression, Typed_COR_Expressions.Typed_Union):
		lhs1, rhs1 = expression.argument1, expression.argument2
		A = lhs1
		if str(A)==str(rhs1):
			return A
		if isinstance(rhs1, Typed_COR_Expressions.Typed_UniversalRelation):
			return Typed_COR_Expressions.Typed_UniversalRelation(expression.type()[0], expression.type()[1])
		if isinstance(rhs1, Typed_COR_Expressions.Typed_Intersection):
			lhs2, rhs2 = rhs1.argument1, rhs1.argument2
			B = lhs2
			if str(A)==str(rhs2):
				return A
			if str(A)==str(lhs2):
				B = rhs2
				return A
		if isinstance(rhs1, Typed_COR_Expressions.Typed_Union):
			lhs2, rhs2 = rhs1.argument1, rhs1.argument2
			if str(A)==str(lhs2):
				B = rhs2
				return Typed_COR_Expressions.Typed_Union(B, A)
			B = lhs2
			if str(A)==str(rhs2):
				return Typed_COR_Expressions.Typed_Union(B, A)
		if isinstance(rhs1, Typed_COR_Expressions.Typed_EmptyRelation):
			return A
		if isinstance(rhs1, Typed_COR_Expressions.Typed_Complement):
			arg = rhs1.argument
			if str(A)==str(arg):
				return Typed_COR_Expressions.Typed_UniversalRelation(expression.type()[0], expression.type()[1])
		if isinstance(lhs1, Typed_COR_Expressions.Typed_UniversalRelation):
			A = rhs1
			return Typed_COR_Expressions.Typed_UniversalRelation(expression.type()[0], expression.type()[1])
		if isinstance(lhs1, Typed_COR_Expressions.Typed_Intersection):
			lhs2, rhs2 = lhs1.argument1, lhs1.argument2
			A = lhs2
			B = rhs2
			if str(B)==str(rhs1):
				return B
			if str(A)==str(rhs1):
				return A
		if isinstance(lhs1, Typed_COR_Expressions.Typed_Union):
			lhs2, rhs2 = lhs1.argument1, lhs1.argument2
			A = lhs2
			B = rhs2
			if str(B)==str(rhs1):
				return Typed_COR_Expressions.Typed_Union(A, B)
			if str(A)==str(rhs1):
				return Typed_COR_Expressions.Typed_Union(B, A)
		if isinstance(lhs1, Typed_COR_Expressions.Typed_Complement):
			arg = lhs1.argument
			A = arg
			if str(A)==str(rhs1):
				return Typed_COR_Expressions.Typed_UniversalRelation(expression.type()[0], expression.type()[1])
		if isinstance(lhs1, Typed_COR_Expressions.Typed_EmptyRelation):
			A = rhs1
			return A
	if isinstance(expression, Typed_COR_Expressions.Typed_Dagger):
		lhs1, rhs1 = expression.argument1, expression.argument2
		if isinstance(lhs1, Typed_COR_Expressions.Typed_UniversalRelation):
			A = rhs1
			return Typed_COR_Expressions.Typed_UniversalRelation(expression.type()[0], expression.type()[1])
		A = lhs1
		if isinstance(rhs1, Typed_COR_Expressions.Typed_UniversalRelation):
			return Typed_COR_Expressions.Typed_UniversalRelation(expression.type()[0], expression.type()[1])
	if isinstance(expression, Typed_COR_Expressions.Typed_Converse):
		arg = expression.argument
		if isinstance(arg, Typed_COR_Expressions.Typed_Converse):
			arg = arg.argument
			A = arg
			return A
		if isinstance(arg, Typed_COR_Expressions.Typed_IdentityRelation):
			return Typed_COR_Expressions.Typed_IdentityRelation(expression.type()[0], expression.type()[1])
		if isinstance(arg, Typed_COR_Expressions.Typed_EmptyRelation):
			return Typed_COR_Expressions.Typed_EmptyRelation(expression.type()[0], expression.type()[1])
		if isinstance(arg, Typed_COR_Expressions.Typed_UniversalRelation):
			return Typed_COR_Expressions.Typed_UniversalRelation(expression.type()[0], expression.type()[1])
	if isinstance(expression, Typed_COR_Expressions.Typed_Composition):
		lhs1, rhs1 = expression.argument1, expression.argument2
		A = lhs1
		if isinstance(rhs1, Typed_COR_Expressions.Typed_IdentityRelation):
			return A
		if isinstance(rhs1, Typed_COR_Expressions.Typed_EmptyRelation):
			return Typed_COR_Expressions.Typed_EmptyRelation(expression.type()[0], expression.type()[1])
		if isinstance(lhs1, Typed_COR_Expressions.Typed_EmptyRelation):
			A = rhs1
			return Typed_COR_Expressions.Typed_EmptyRelation(expression.type()[0], expression.type()[1])
		if isinstance(lhs1, Typed_COR_Expressions.Typed_IdentityRelation):
			A = rhs1
			return A
	if isinstance(expression, Typed_COR_Expressions.Typed_Complement):
		arg = expression.argument
		if isinstance(arg, Typed_COR_Expressions.Typed_EmptyRelation):
			return Typed_COR_Expressions.Typed_UniversalRelation(expression.type()[0], expression.type()[1])
		if isinstance(arg, Typed_COR_Expressions.Typed_UniversalRelation):
			return Typed_COR_Expressions.Typed_EmptyRelation(expression.type()[0], expression.type()[1])
		if isinstance(arg, Typed_COR_Expressions.Typed_Complement):
			arg = arg.argument
			A = arg
			return A

	return expression # The given expression was unable to be simplified