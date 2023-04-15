import COR_Expressions

def simplify(expression):
	if isinstance(expression, COR_Expressions.Converse):
		arg = expression.argument
		if isinstance(arg, COR_Expressions.EmptyRelation):
			return COR_Expressions.EmptyRelation()
		if isinstance(arg, COR_Expressions.UniversalRelation):
			return COR_Expressions.UniversalRelation()
		if isinstance(arg, COR_Expressions.IdentityRelation):
			return COR_Expressions.IdentityRelation()
		if isinstance(arg, COR_Expressions.Complement):
			arg = arg.argument
			if isinstance(arg, COR_Expressions.IdentityRelation):
				return COR_Expressions.Complement(COR_Expressions.IdentityRelation())
		if isinstance(arg, COR_Expressions.Converse):
			arg = arg.argument
			B = arg
			return B
			A = arg
			return A
			C = arg
			return C
		if isinstance(arg, COR_Expressions.Dagger):
			arg1, arg2 = arg.argument1, arg.argument2
			if isinstance(arg1, COR_Expressions.EmptyRelation):
				if isinstance(arg2, COR_Expressions.IdentityRelation):
					return COR_Expressions.Dagger(COR_Expressions.IdentityRelation(), COR_Expressions.EmptyRelation())
			if isinstance(arg1, COR_Expressions.IdentityRelation):
				if isinstance(arg2, COR_Expressions.EmptyRelation):
					return COR_Expressions.Dagger(COR_Expressions.IdentityRelation(), COR_Expressions.EmptyRelation())
				if isinstance(arg2, COR_Expressions.IdentityRelation):
					return COR_Expressions.Dagger(COR_Expressions.IdentityRelation(), COR_Expressions.IdentityRelation())
		if isinstance(arg, COR_Expressions.Intersection):
			arg1, arg2 = arg.argument1, arg.argument2
			if isinstance(arg1, COR_Expressions.IdentityRelation):
				B = arg2
				return COR_Expressions.Intersection(COR_Expressions.IdentityRelation(), B)
				A = arg2
				return COR_Expressions.Intersection(A, COR_Expressions.IdentityRelation())
				C = arg2
				return COR_Expressions.Intersection(C, COR_Expressions.IdentityRelation())
			C = arg1
			if isinstance(arg2, COR_Expressions.IdentityRelation):
				return COR_Expressions.Intersection(COR_Expressions.IdentityRelation(), C)
			B = arg1
			if isinstance(arg2, COR_Expressions.IdentityRelation):
				return COR_Expressions.Intersection(COR_Expressions.IdentityRelation(), B)
			A = arg1
			if isinstance(arg2, COR_Expressions.IdentityRelation):
				return COR_Expressions.Intersection(A, COR_Expressions.IdentityRelation())
	if isinstance(expression, COR_Expressions.Complement):
		arg = expression.argument
		if isinstance(arg, COR_Expressions.UniversalRelation):
			return COR_Expressions.EmptyRelation()
		if isinstance(arg, COR_Expressions.EmptyRelation):
			return COR_Expressions.UniversalRelation()
		if isinstance(arg, COR_Expressions.Complement):
			arg = arg.argument
			if isinstance(arg, COR_Expressions.IdentityRelation):
				return COR_Expressions.IdentityRelation()
			B = arg
			return B
			A = arg
			return A
			C = arg
			return C
		if isinstance(arg, COR_Expressions.Converse):
			arg = arg.argument
			if isinstance(arg, COR_Expressions.Complement):
				arg = arg.argument
				B = arg
				return COR_Expressions.Converse(B)
				C = arg
				return COR_Expressions.Converse(C)
				A = arg
				return COR_Expressions.Converse(A)
	if isinstance(expression, COR_Expressions.Intersection):
		arg1, arg2 = expression.argument1, expression.argument2
		if isinstance(arg1, COR_Expressions.EmptyRelation):
			if isinstance(arg2, COR_Expressions.EmptyRelation):
				return COR_Expressions.EmptyRelation()
			C = arg2
			return COR_Expressions.EmptyRelation()
			A = arg2
			return COR_Expressions.EmptyRelation()
			if isinstance(arg2, COR_Expressions.UniversalRelation):
				return COR_Expressions.EmptyRelation()
			B = arg2
			return COR_Expressions.EmptyRelation()
			if isinstance(arg2, COR_Expressions.IdentityRelation):
				return COR_Expressions.EmptyRelation()
		B = arg1
		if isinstance(arg2, COR_Expressions.UniversalRelation):
			return B
		if isinstance(arg2, COR_Expressions.EmptyRelation):
			return COR_Expressions.EmptyRelation()
		if str(B)==str(arg2):
			return B
		if isinstance(arg2, COR_Expressions.Complement):
			arg = arg2.argument
			if str(B)==str(arg):
				return COR_Expressions.EmptyRelation()
		if isinstance(arg1, COR_Expressions.UniversalRelation):
			A = arg2
			return A
			B = arg2
			return B
			if isinstance(arg2, COR_Expressions.EmptyRelation):
				return COR_Expressions.EmptyRelation()
			C = arg2
			return C
			if isinstance(arg2, COR_Expressions.UniversalRelation):
				return COR_Expressions.UniversalRelation()
			if isinstance(arg2, COR_Expressions.IdentityRelation):
				return COR_Expressions.IdentityRelation()
		if isinstance(arg1, COR_Expressions.IdentityRelation):
			if isinstance(arg2, COR_Expressions.UniversalRelation):
				return COR_Expressions.IdentityRelation()
			if isinstance(arg2, COR_Expressions.EmptyRelation):
				return COR_Expressions.EmptyRelation()
			if isinstance(arg2, COR_Expressions.IdentityRelation):
				return COR_Expressions.IdentityRelation()
			if isinstance(arg2, COR_Expressions.Converse):
				arg = arg2.argument
				A = arg
				return COR_Expressions.Intersection(COR_Expressions.IdentityRelation(), A)
				B = arg
				return COR_Expressions.Intersection(COR_Expressions.IdentityRelation(), B)
				C = arg
				return COR_Expressions.Intersection(COR_Expressions.IdentityRelation(), C)
			if isinstance(arg2, COR_Expressions.Complement):
				arg = arg2.argument
				if isinstance(arg, COR_Expressions.IdentityRelation):
					return COR_Expressions.EmptyRelation()
		A = arg1
		if isinstance(arg2, COR_Expressions.EmptyRelation):
			return COR_Expressions.EmptyRelation()
		if isinstance(arg2, COR_Expressions.UniversalRelation):
			return A
		if str(A)==str(arg2):
			return A
		if isinstance(arg2, COR_Expressions.Complement):
			arg = arg2.argument
			if str(A)==str(arg):
				return COR_Expressions.EmptyRelation()
		C = arg1
		if isinstance(arg2, COR_Expressions.UniversalRelation):
			return C
		if isinstance(arg2, COR_Expressions.EmptyRelation):
			return COR_Expressions.EmptyRelation()
		if str(C)==str(arg2):
			return C
		if isinstance(arg2, COR_Expressions.Complement):
			arg = arg2.argument
			if str(C)==str(arg):
				return COR_Expressions.EmptyRelation()
		if isinstance(arg1, COR_Expressions.Complement):
			arg = arg1.argument
			if isinstance(arg, COR_Expressions.IdentityRelation):
				if isinstance(arg2, COR_Expressions.IdentityRelation):
					return COR_Expressions.EmptyRelation()
			A = arg
			if str(A)==str(arg2):
				return COR_Expressions.EmptyRelation()
			C = arg
			if str(C)==str(arg2):
				return COR_Expressions.EmptyRelation()
			B = arg
			if str(B)==str(arg2):
				return COR_Expressions.EmptyRelation()
		if isinstance(arg1, COR_Expressions.Converse):
			arg = arg1.argument
			B = arg
			if isinstance(arg2, COR_Expressions.IdentityRelation):
				return COR_Expressions.Intersection(B, COR_Expressions.IdentityRelation())
			C = arg
			if isinstance(arg2, COR_Expressions.IdentityRelation):
				return COR_Expressions.Intersection(COR_Expressions.IdentityRelation(), C)
			A = arg
			if isinstance(arg2, COR_Expressions.IdentityRelation):
				return COR_Expressions.Intersection(COR_Expressions.IdentityRelation(), A)
	if isinstance(expression, COR_Expressions.Union):
		arg1, arg2 = expression.argument1, expression.argument2
		if isinstance(arg1, COR_Expressions.EmptyRelation):
			if isinstance(arg2, COR_Expressions.EmptyRelation):
				return COR_Expressions.EmptyRelation()
			if isinstance(arg2, COR_Expressions.UniversalRelation):
				return COR_Expressions.UniversalRelation()
			C = arg2
			return C
			A = arg2
			return A
			if isinstance(arg2, COR_Expressions.IdentityRelation):
				return COR_Expressions.IdentityRelation()
			B = arg2
			return B
		C = arg1
		if str(C)==str(arg2):
			return C
		if isinstance(arg2, COR_Expressions.EmptyRelation):
			return C
		if isinstance(arg2, COR_Expressions.UniversalRelation):
			return COR_Expressions.UniversalRelation()
		if isinstance(arg2, COR_Expressions.Complement):
			arg = arg2.argument
			if str(C)==str(arg):
				return COR_Expressions.UniversalRelation()
		if isinstance(arg1, COR_Expressions.UniversalRelation):
			A = arg2
			return COR_Expressions.UniversalRelation()
			B = arg2
			return COR_Expressions.UniversalRelation()
			if isinstance(arg2, COR_Expressions.UniversalRelation):
				return COR_Expressions.UniversalRelation()
			C = arg2
			return COR_Expressions.UniversalRelation()
			if isinstance(arg2, COR_Expressions.EmptyRelation):
				return COR_Expressions.UniversalRelation()
			if isinstance(arg2, COR_Expressions.IdentityRelation):
				return COR_Expressions.UniversalRelation()
		if isinstance(arg1, COR_Expressions.IdentityRelation):
			if isinstance(arg2, COR_Expressions.IdentityRelation):
				return COR_Expressions.IdentityRelation()
			if isinstance(arg2, COR_Expressions.EmptyRelation):
				return COR_Expressions.IdentityRelation()
			if isinstance(arg2, COR_Expressions.UniversalRelation):
				return COR_Expressions.UniversalRelation()
			if isinstance(arg2, COR_Expressions.Complement):
				arg = arg2.argument
				if isinstance(arg, COR_Expressions.IdentityRelation):
					return COR_Expressions.UniversalRelation()
		A = arg1
		if isinstance(arg2, COR_Expressions.EmptyRelation):
			return A
		if isinstance(arg2, COR_Expressions.UniversalRelation):
			return COR_Expressions.UniversalRelation()
		if str(A)==str(arg2):
			return A
		if isinstance(arg2, COR_Expressions.Complement):
			arg = arg2.argument
			if str(A)==str(arg):
				return COR_Expressions.UniversalRelation()
		B = arg1
		if isinstance(arg2, COR_Expressions.EmptyRelation):
			return B
		if isinstance(arg2, COR_Expressions.UniversalRelation):
			return COR_Expressions.UniversalRelation()
		if str(B)==str(arg2):
			return B
		if isinstance(arg2, COR_Expressions.Complement):
			arg = arg2.argument
			if str(B)==str(arg):
				return COR_Expressions.UniversalRelation()
		if isinstance(arg1, COR_Expressions.Complement):
			arg = arg1.argument
			A = arg
			if str(A)==str(arg2):
				return COR_Expressions.UniversalRelation()
			if isinstance(arg, COR_Expressions.IdentityRelation):
				if isinstance(arg2, COR_Expressions.IdentityRelation):
					return COR_Expressions.UniversalRelation()
			B = arg
			if str(B)==str(arg2):
				return COR_Expressions.UniversalRelation()
			C = arg
			if str(C)==str(arg2):
				return COR_Expressions.UniversalRelation()
	if isinstance(expression, COR_Expressions.Composition):
		arg1, arg2 = expression.argument1, expression.argument2
		A = arg1
		if isinstance(arg2, COR_Expressions.EmptyRelation):
			return COR_Expressions.EmptyRelation()
		if isinstance(arg2, COR_Expressions.IdentityRelation):
			return A
		if isinstance(arg1, COR_Expressions.UniversalRelation):
			if isinstance(arg2, COR_Expressions.IdentityRelation):
				return COR_Expressions.UniversalRelation()
			if isinstance(arg2, COR_Expressions.EmptyRelation):
				return COR_Expressions.EmptyRelation()
			if isinstance(arg2, COR_Expressions.UniversalRelation):
				return COR_Expressions.UniversalRelation()
		if isinstance(arg1, COR_Expressions.EmptyRelation):
			B = arg2
			return COR_Expressions.EmptyRelation()
			if isinstance(arg2, COR_Expressions.EmptyRelation):
				return COR_Expressions.EmptyRelation()
			if isinstance(arg2, COR_Expressions.IdentityRelation):
				return COR_Expressions.EmptyRelation()
			C = arg2
			return COR_Expressions.EmptyRelation()
			if isinstance(arg2, COR_Expressions.UniversalRelation):
				return COR_Expressions.EmptyRelation()
			A = arg2
			return COR_Expressions.EmptyRelation()
		B = arg1
		if isinstance(arg2, COR_Expressions.IdentityRelation):
			return B
		if isinstance(arg2, COR_Expressions.EmptyRelation):
			return COR_Expressions.EmptyRelation()
		if isinstance(arg1, COR_Expressions.IdentityRelation):
			if isinstance(arg2, COR_Expressions.IdentityRelation):
				return COR_Expressions.IdentityRelation()
			C = arg2
			return C
			A = arg2
			return A
			B = arg2
			return B
			if isinstance(arg2, COR_Expressions.UniversalRelation):
				return COR_Expressions.UniversalRelation()
			if isinstance(arg2, COR_Expressions.EmptyRelation):
				return COR_Expressions.EmptyRelation()
		C = arg1
		if isinstance(arg2, COR_Expressions.IdentityRelation):
			return C
		if isinstance(arg2, COR_Expressions.EmptyRelation):
			return COR_Expressions.EmptyRelation()
	if isinstance(expression, COR_Expressions.Dagger):
		arg1, arg2 = expression.argument1, expression.argument2
		if isinstance(arg1, COR_Expressions.IdentityRelation):
			if isinstance(arg2, COR_Expressions.UniversalRelation):
				return COR_Expressions.UniversalRelation()
			if isinstance(arg2, COR_Expressions.Complement):
				arg = arg2.argument
				if isinstance(arg, COR_Expressions.IdentityRelation):
					return COR_Expressions.IdentityRelation()
		if isinstance(arg1, COR_Expressions.UniversalRelation):
			B = arg2
			return COR_Expressions.UniversalRelation()
			C = arg2
			return COR_Expressions.UniversalRelation()
			if isinstance(arg2, COR_Expressions.UniversalRelation):
				return COR_Expressions.UniversalRelation()
			A = arg2
			return COR_Expressions.UniversalRelation()
			if isinstance(arg2, COR_Expressions.EmptyRelation):
				return COR_Expressions.UniversalRelation()
			if isinstance(arg2, COR_Expressions.IdentityRelation):
				return COR_Expressions.UniversalRelation()
		C = arg1
		if isinstance(arg2, COR_Expressions.UniversalRelation):
			return COR_Expressions.UniversalRelation()
		if isinstance(arg2, COR_Expressions.Complement):
			arg = arg2.argument
			if isinstance(arg, COR_Expressions.IdentityRelation):
				return C
		B = arg1
		if isinstance(arg2, COR_Expressions.UniversalRelation):
			return COR_Expressions.UniversalRelation()
		if isinstance(arg2, COR_Expressions.Complement):
			arg = arg2.argument
			if isinstance(arg, COR_Expressions.IdentityRelation):
				return B
		if isinstance(arg1, COR_Expressions.EmptyRelation):
			if isinstance(arg2, COR_Expressions.EmptyRelation):
				return COR_Expressions.EmptyRelation()
			if isinstance(arg2, COR_Expressions.UniversalRelation):
				return COR_Expressions.UniversalRelation()
			if isinstance(arg2, COR_Expressions.Complement):
				arg = arg2.argument
				if isinstance(arg, COR_Expressions.IdentityRelation):
					return COR_Expressions.EmptyRelation()
		A = arg1
		if isinstance(arg2, COR_Expressions.UniversalRelation):
			return COR_Expressions.UniversalRelation()
		if isinstance(arg2, COR_Expressions.Complement):
			arg = arg2.argument
			if isinstance(arg, COR_Expressions.IdentityRelation):
				return A
		if isinstance(arg1, COR_Expressions.Complement):
			arg = arg1.argument
			if isinstance(arg, COR_Expressions.IdentityRelation):
				A = arg2
				return A
				B = arg2
				return B
				C = arg2
				return C
				if isinstance(arg2, COR_Expressions.EmptyRelation):
					return COR_Expressions.EmptyRelation()
				if isinstance(arg2, COR_Expressions.IdentityRelation):
					return COR_Expressions.IdentityRelation()

	return expression # The given expression was unable to be simplified