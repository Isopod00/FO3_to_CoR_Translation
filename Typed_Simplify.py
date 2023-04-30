import Typed_COR_Expressions

def simplify(expression):
	if isinstance(expression, Typed_COR_Expressions.Typed_Intersection):
		lhs1, rhs1 = expression.argument1, expression.argument2
		A = lhs1
		if str(A)==str(rhs1) and A.type() == rhs1.type():
			return A
		if isinstance(rhs1, Typed_COR_Expressions.Typed_UniversalRelation) and rhs1.set1=='P' and rhs1.set2=='P':
			return A
		if isinstance(rhs1, Typed_COR_Expressions.Typed_UniversalRelation) and rhs1.set1=='P' and rhs1.set2=='Q':
			return A
		if isinstance(rhs1, Typed_COR_Expressions.Typed_UniversalRelation) and rhs1.set1=='P' and rhs1.set2=='R':
			return A
		if isinstance(rhs1, Typed_COR_Expressions.Typed_UniversalRelation) and rhs1.set1=='P' and rhs1.set2=='S':
			return A
		if isinstance(rhs1, Typed_COR_Expressions.Typed_UniversalRelation) and rhs1.set1=='Q' and rhs1.set2=='P':
			return A
		if isinstance(rhs1, Typed_COR_Expressions.Typed_UniversalRelation) and rhs1.set1=='Q' and rhs1.set2=='Q':
			return A
		if isinstance(rhs1, Typed_COR_Expressions.Typed_UniversalRelation) and rhs1.set1=='Q' and rhs1.set2=='R':
			return A
		if isinstance(rhs1, Typed_COR_Expressions.Typed_UniversalRelation) and rhs1.set1=='Q' and rhs1.set2=='S':
			return A
		if isinstance(rhs1, Typed_COR_Expressions.Typed_UniversalRelation) and rhs1.set1=='R' and rhs1.set2=='P':
			return A
		if isinstance(rhs1, Typed_COR_Expressions.Typed_UniversalRelation) and rhs1.set1=='R' and rhs1.set2=='Q':
			return A
		if isinstance(rhs1, Typed_COR_Expressions.Typed_UniversalRelation) and rhs1.set1=='R' and rhs1.set2=='R':
			return A
		if isinstance(rhs1, Typed_COR_Expressions.Typed_UniversalRelation) and rhs1.set1=='R' and rhs1.set2=='S':
			return A
		if isinstance(rhs1, Typed_COR_Expressions.Typed_UniversalRelation) and rhs1.set1=='S' and rhs1.set2=='P':
			return A
		if isinstance(rhs1, Typed_COR_Expressions.Typed_UniversalRelation) and rhs1.set1=='S' and rhs1.set2=='Q':
			return A
		if isinstance(rhs1, Typed_COR_Expressions.Typed_UniversalRelation) and rhs1.set1=='S' and rhs1.set2=='R':
			return A
		if isinstance(rhs1, Typed_COR_Expressions.Typed_UniversalRelation) and rhs1.set1=='S' and rhs1.set2=='S':
			return A
		if isinstance(rhs1, Typed_COR_Expressions.Typed_Intersection):
			lhs2, rhs2 = rhs1.argument1, rhs1.argument2
			if str(A)==str(lhs2) and A.type() == lhs2.type():
				B = rhs2
				return Typed_COR_Expressions.Typed_Intersection(B, A)
			B = lhs2
			if str(A)==str(rhs2) and A.type() == rhs2.type():
				return Typed_COR_Expressions.Typed_Intersection(A, B)
		if isinstance(rhs1, Typed_COR_Expressions.Typed_Union):
			lhs2, rhs2 = rhs1.argument1, rhs1.argument2
			if str(A)==str(lhs2) and A.type() == lhs2.type():
				B = rhs2
				return A
			B = lhs2
			if str(A)==str(rhs2) and A.type() == rhs2.type():
				return A
		if isinstance(rhs1, Typed_COR_Expressions.Typed_EmptyRelation) and rhs1.set1=='P' and rhs1.set2=='P':
			return Typed_COR_Expressions.Typed_EmptyRelation('P', 'P')
		if isinstance(rhs1, Typed_COR_Expressions.Typed_EmptyRelation) and rhs1.set1=='P' and rhs1.set2=='Q':
			return Typed_COR_Expressions.Typed_EmptyRelation('P', 'Q')
		if isinstance(rhs1, Typed_COR_Expressions.Typed_EmptyRelation) and rhs1.set1=='P' and rhs1.set2=='R':
			return Typed_COR_Expressions.Typed_EmptyRelation('P', 'R')
		if isinstance(rhs1, Typed_COR_Expressions.Typed_EmptyRelation) and rhs1.set1=='P' and rhs1.set2=='S':
			return Typed_COR_Expressions.Typed_EmptyRelation('P', 'S')
		if isinstance(rhs1, Typed_COR_Expressions.Typed_EmptyRelation) and rhs1.set1=='Q' and rhs1.set2=='P':
			return Typed_COR_Expressions.Typed_EmptyRelation('Q', 'P')
		if isinstance(rhs1, Typed_COR_Expressions.Typed_EmptyRelation) and rhs1.set1=='Q' and rhs1.set2=='Q':
			return Typed_COR_Expressions.Typed_EmptyRelation('Q', 'Q')
		if isinstance(rhs1, Typed_COR_Expressions.Typed_EmptyRelation) and rhs1.set1=='Q' and rhs1.set2=='R':
			return Typed_COR_Expressions.Typed_EmptyRelation('Q', 'R')
		if isinstance(rhs1, Typed_COR_Expressions.Typed_EmptyRelation) and rhs1.set1=='Q' and rhs1.set2=='S':
			return Typed_COR_Expressions.Typed_EmptyRelation('Q', 'S')
		if isinstance(rhs1, Typed_COR_Expressions.Typed_EmptyRelation) and rhs1.set1=='R' and rhs1.set2=='P':
			return Typed_COR_Expressions.Typed_EmptyRelation('R', 'P')
		if isinstance(rhs1, Typed_COR_Expressions.Typed_EmptyRelation) and rhs1.set1=='R' and rhs1.set2=='Q':
			return Typed_COR_Expressions.Typed_EmptyRelation('R', 'Q')
		if isinstance(rhs1, Typed_COR_Expressions.Typed_EmptyRelation) and rhs1.set1=='R' and rhs1.set2=='R':
			return Typed_COR_Expressions.Typed_EmptyRelation('R', 'R')
		if isinstance(rhs1, Typed_COR_Expressions.Typed_EmptyRelation) and rhs1.set1=='R' and rhs1.set2=='S':
			return Typed_COR_Expressions.Typed_EmptyRelation('R', 'S')
		if isinstance(rhs1, Typed_COR_Expressions.Typed_EmptyRelation) and rhs1.set1=='S' and rhs1.set2=='P':
			return Typed_COR_Expressions.Typed_EmptyRelation('S', 'P')
		if isinstance(rhs1, Typed_COR_Expressions.Typed_EmptyRelation) and rhs1.set1=='S' and rhs1.set2=='Q':
			return Typed_COR_Expressions.Typed_EmptyRelation('S', 'Q')
		if isinstance(rhs1, Typed_COR_Expressions.Typed_EmptyRelation) and rhs1.set1=='S' and rhs1.set2=='R':
			return Typed_COR_Expressions.Typed_EmptyRelation('S', 'R')
		if isinstance(rhs1, Typed_COR_Expressions.Typed_EmptyRelation) and rhs1.set1=='S' and rhs1.set2=='S':
			return Typed_COR_Expressions.Typed_EmptyRelation('S', 'S')
		if isinstance(rhs1, Typed_COR_Expressions.Typed_Complement):
			arg = rhs1.argument
			if str(A)==str(arg) and A.type() == arg.type():
				return Typed_COR_Expressions.Typed_EmptyRelation('P', 'P')
				return Typed_COR_Expressions.Typed_EmptyRelation('P', 'Q')
				return Typed_COR_Expressions.Typed_EmptyRelation('P', 'R')
				return Typed_COR_Expressions.Typed_EmptyRelation('P', 'S')
				return Typed_COR_Expressions.Typed_EmptyRelation('Q', 'P')
				return Typed_COR_Expressions.Typed_EmptyRelation('Q', 'Q')
				return Typed_COR_Expressions.Typed_EmptyRelation('Q', 'R')
				return Typed_COR_Expressions.Typed_EmptyRelation('Q', 'S')
				return Typed_COR_Expressions.Typed_EmptyRelation('R', 'P')
				return Typed_COR_Expressions.Typed_EmptyRelation('R', 'Q')
				return Typed_COR_Expressions.Typed_EmptyRelation('R', 'R')
				return Typed_COR_Expressions.Typed_EmptyRelation('R', 'S')
				return Typed_COR_Expressions.Typed_EmptyRelation('S', 'P')
				return Typed_COR_Expressions.Typed_EmptyRelation('S', 'Q')
				return Typed_COR_Expressions.Typed_EmptyRelation('S', 'R')
				return Typed_COR_Expressions.Typed_EmptyRelation('S', 'S')
		if isinstance(lhs1, Typed_COR_Expressions.Typed_Union):
			lhs2, rhs2 = lhs1.argument1, lhs1.argument2
			A = lhs2
			B = rhs2
			if str(B)==str(rhs1) and B.type() == rhs1.type():
				return B
			if str(A)==str(rhs1) and A.type() == rhs1.type():
				return A
		if isinstance(lhs1, Typed_COR_Expressions.Typed_UniversalRelation) and lhs1.set1=='P' and lhs1.set2=='P':
			A = rhs1
			return A
		if isinstance(lhs1, Typed_COR_Expressions.Typed_UniversalRelation) and lhs1.set1=='P' and lhs1.set2=='Q':
			A = rhs1
			return A
		if isinstance(lhs1, Typed_COR_Expressions.Typed_UniversalRelation) and lhs1.set1=='P' and lhs1.set2=='R':
			A = rhs1
			return A
		if isinstance(lhs1, Typed_COR_Expressions.Typed_UniversalRelation) and lhs1.set1=='P' and lhs1.set2=='S':
			A = rhs1
			return A
		if isinstance(lhs1, Typed_COR_Expressions.Typed_UniversalRelation) and lhs1.set1=='Q' and lhs1.set2=='P':
			A = rhs1
			return A
		if isinstance(lhs1, Typed_COR_Expressions.Typed_UniversalRelation) and lhs1.set1=='Q' and lhs1.set2=='Q':
			A = rhs1
			return A
		if isinstance(lhs1, Typed_COR_Expressions.Typed_UniversalRelation) and lhs1.set1=='Q' and lhs1.set2=='R':
			A = rhs1
			return A
		if isinstance(lhs1, Typed_COR_Expressions.Typed_UniversalRelation) and lhs1.set1=='Q' and lhs1.set2=='S':
			A = rhs1
			return A
		if isinstance(lhs1, Typed_COR_Expressions.Typed_UniversalRelation) and lhs1.set1=='R' and lhs1.set2=='P':
			A = rhs1
			return A
		if isinstance(lhs1, Typed_COR_Expressions.Typed_UniversalRelation) and lhs1.set1=='R' and lhs1.set2=='Q':
			A = rhs1
			return A
		if isinstance(lhs1, Typed_COR_Expressions.Typed_UniversalRelation) and lhs1.set1=='R' and lhs1.set2=='R':
			A = rhs1
			return A
		if isinstance(lhs1, Typed_COR_Expressions.Typed_UniversalRelation) and lhs1.set1=='R' and lhs1.set2=='S':
			A = rhs1
			return A
		if isinstance(lhs1, Typed_COR_Expressions.Typed_UniversalRelation) and lhs1.set1=='S' and lhs1.set2=='P':
			A = rhs1
			return A
		if isinstance(lhs1, Typed_COR_Expressions.Typed_UniversalRelation) and lhs1.set1=='S' and lhs1.set2=='Q':
			A = rhs1
			return A
		if isinstance(lhs1, Typed_COR_Expressions.Typed_UniversalRelation) and lhs1.set1=='S' and lhs1.set2=='R':
			A = rhs1
			return A
		if isinstance(lhs1, Typed_COR_Expressions.Typed_UniversalRelation) and lhs1.set1=='S' and lhs1.set2=='S':
			A = rhs1
			return A
		if isinstance(lhs1, Typed_COR_Expressions.Typed_Intersection):
			lhs2, rhs2 = lhs1.argument1, lhs1.argument2
			A = lhs2
			B = rhs2
			if str(A)==str(rhs1) and A.type() == rhs1.type():
				return Typed_COR_Expressions.Typed_Intersection(B, A)
			if str(B)==str(rhs1) and B.type() == rhs1.type():
				return Typed_COR_Expressions.Typed_Intersection(B, A)
		if isinstance(lhs1, Typed_COR_Expressions.Typed_EmptyRelation) and lhs1.set1=='P' and lhs1.set2=='P':
			A = rhs1
			return Typed_COR_Expressions.Typed_EmptyRelation('P', 'P')
		if isinstance(lhs1, Typed_COR_Expressions.Typed_EmptyRelation) and lhs1.set1=='P' and lhs1.set2=='Q':
			A = rhs1
			return Typed_COR_Expressions.Typed_EmptyRelation('P', 'Q')
		if isinstance(lhs1, Typed_COR_Expressions.Typed_EmptyRelation) and lhs1.set1=='P' and lhs1.set2=='R':
			A = rhs1
			return Typed_COR_Expressions.Typed_EmptyRelation('P', 'R')
		if isinstance(lhs1, Typed_COR_Expressions.Typed_EmptyRelation) and lhs1.set1=='P' and lhs1.set2=='S':
			A = rhs1
			return Typed_COR_Expressions.Typed_EmptyRelation('P', 'S')
		if isinstance(lhs1, Typed_COR_Expressions.Typed_EmptyRelation) and lhs1.set1=='Q' and lhs1.set2=='P':
			A = rhs1
			return Typed_COR_Expressions.Typed_EmptyRelation('Q', 'P')
		if isinstance(lhs1, Typed_COR_Expressions.Typed_EmptyRelation) and lhs1.set1=='Q' and lhs1.set2=='Q':
			A = rhs1
			return Typed_COR_Expressions.Typed_EmptyRelation('Q', 'Q')
		if isinstance(lhs1, Typed_COR_Expressions.Typed_EmptyRelation) and lhs1.set1=='Q' and lhs1.set2=='R':
			A = rhs1
			return Typed_COR_Expressions.Typed_EmptyRelation('Q', 'R')
		if isinstance(lhs1, Typed_COR_Expressions.Typed_EmptyRelation) and lhs1.set1=='Q' and lhs1.set2=='S':
			A = rhs1
			return Typed_COR_Expressions.Typed_EmptyRelation('Q', 'S')
		if isinstance(lhs1, Typed_COR_Expressions.Typed_EmptyRelation) and lhs1.set1=='R' and lhs1.set2=='P':
			A = rhs1
			return Typed_COR_Expressions.Typed_EmptyRelation('R', 'P')
		if isinstance(lhs1, Typed_COR_Expressions.Typed_EmptyRelation) and lhs1.set1=='R' and lhs1.set2=='Q':
			A = rhs1
			return Typed_COR_Expressions.Typed_EmptyRelation('R', 'Q')
		if isinstance(lhs1, Typed_COR_Expressions.Typed_EmptyRelation) and lhs1.set1=='R' and lhs1.set2=='R':
			A = rhs1
			return Typed_COR_Expressions.Typed_EmptyRelation('R', 'R')
		if isinstance(lhs1, Typed_COR_Expressions.Typed_EmptyRelation) and lhs1.set1=='R' and lhs1.set2=='S':
			A = rhs1
			return Typed_COR_Expressions.Typed_EmptyRelation('R', 'S')
		if isinstance(lhs1, Typed_COR_Expressions.Typed_EmptyRelation) and lhs1.set1=='S' and lhs1.set2=='P':
			A = rhs1
			return Typed_COR_Expressions.Typed_EmptyRelation('S', 'P')
		if isinstance(lhs1, Typed_COR_Expressions.Typed_EmptyRelation) and lhs1.set1=='S' and lhs1.set2=='Q':
			A = rhs1
			return Typed_COR_Expressions.Typed_EmptyRelation('S', 'Q')
		if isinstance(lhs1, Typed_COR_Expressions.Typed_EmptyRelation) and lhs1.set1=='S' and lhs1.set2=='R':
			A = rhs1
			return Typed_COR_Expressions.Typed_EmptyRelation('S', 'R')
		if isinstance(lhs1, Typed_COR_Expressions.Typed_EmptyRelation) and lhs1.set1=='S' and lhs1.set2=='S':
			A = rhs1
			return Typed_COR_Expressions.Typed_EmptyRelation('S', 'S')
		if isinstance(lhs1, Typed_COR_Expressions.Typed_Complement):
			arg = lhs1.argument
			A = arg
			if str(A)==str(rhs1) and A.type() == rhs1.type():
				return Typed_COR_Expressions.Typed_EmptyRelation('P', 'P')
				return Typed_COR_Expressions.Typed_EmptyRelation('P', 'Q')
				return Typed_COR_Expressions.Typed_EmptyRelation('P', 'R')
				return Typed_COR_Expressions.Typed_EmptyRelation('P', 'S')
				return Typed_COR_Expressions.Typed_EmptyRelation('Q', 'P')
				return Typed_COR_Expressions.Typed_EmptyRelation('Q', 'Q')
				return Typed_COR_Expressions.Typed_EmptyRelation('Q', 'R')
				return Typed_COR_Expressions.Typed_EmptyRelation('Q', 'S')
				return Typed_COR_Expressions.Typed_EmptyRelation('R', 'P')
				return Typed_COR_Expressions.Typed_EmptyRelation('R', 'Q')
				return Typed_COR_Expressions.Typed_EmptyRelation('R', 'R')
				return Typed_COR_Expressions.Typed_EmptyRelation('R', 'S')
				return Typed_COR_Expressions.Typed_EmptyRelation('S', 'P')
				return Typed_COR_Expressions.Typed_EmptyRelation('S', 'Q')
				return Typed_COR_Expressions.Typed_EmptyRelation('S', 'R')
				return Typed_COR_Expressions.Typed_EmptyRelation('S', 'S')
	if isinstance(expression, Typed_COR_Expressions.Typed_Union):
		lhs1, rhs1 = expression.argument1, expression.argument2
		A = lhs1
		if str(A)==str(rhs1) and A.type() == rhs1.type():
			return A
		if isinstance(rhs1, Typed_COR_Expressions.Typed_UniversalRelation) and rhs1.set1=='P' and rhs1.set2=='P':
			return Typed_COR_Expressions.Typed_UniversalRelation('P', 'P')
		if isinstance(rhs1, Typed_COR_Expressions.Typed_UniversalRelation) and rhs1.set1=='P' and rhs1.set2=='Q':
			return Typed_COR_Expressions.Typed_UniversalRelation('P', 'Q')
		if isinstance(rhs1, Typed_COR_Expressions.Typed_UniversalRelation) and rhs1.set1=='P' and rhs1.set2=='R':
			return Typed_COR_Expressions.Typed_UniversalRelation('P', 'R')
		if isinstance(rhs1, Typed_COR_Expressions.Typed_UniversalRelation) and rhs1.set1=='P' and rhs1.set2=='S':
			return Typed_COR_Expressions.Typed_UniversalRelation('P', 'S')
		if isinstance(rhs1, Typed_COR_Expressions.Typed_UniversalRelation) and rhs1.set1=='Q' and rhs1.set2=='P':
			return Typed_COR_Expressions.Typed_UniversalRelation('Q', 'P')
		if isinstance(rhs1, Typed_COR_Expressions.Typed_UniversalRelation) and rhs1.set1=='Q' and rhs1.set2=='Q':
			return Typed_COR_Expressions.Typed_UniversalRelation('Q', 'Q')
		if isinstance(rhs1, Typed_COR_Expressions.Typed_UniversalRelation) and rhs1.set1=='Q' and rhs1.set2=='R':
			return Typed_COR_Expressions.Typed_UniversalRelation('Q', 'R')
		if isinstance(rhs1, Typed_COR_Expressions.Typed_UniversalRelation) and rhs1.set1=='Q' and rhs1.set2=='S':
			return Typed_COR_Expressions.Typed_UniversalRelation('Q', 'S')
		if isinstance(rhs1, Typed_COR_Expressions.Typed_UniversalRelation) and rhs1.set1=='R' and rhs1.set2=='P':
			return Typed_COR_Expressions.Typed_UniversalRelation('R', 'P')
		if isinstance(rhs1, Typed_COR_Expressions.Typed_UniversalRelation) and rhs1.set1=='R' and rhs1.set2=='Q':
			return Typed_COR_Expressions.Typed_UniversalRelation('R', 'Q')
		if isinstance(rhs1, Typed_COR_Expressions.Typed_UniversalRelation) and rhs1.set1=='R' and rhs1.set2=='R':
			return Typed_COR_Expressions.Typed_UniversalRelation('R', 'R')
		if isinstance(rhs1, Typed_COR_Expressions.Typed_UniversalRelation) and rhs1.set1=='R' and rhs1.set2=='S':
			return Typed_COR_Expressions.Typed_UniversalRelation('R', 'S')
		if isinstance(rhs1, Typed_COR_Expressions.Typed_UniversalRelation) and rhs1.set1=='S' and rhs1.set2=='P':
			return Typed_COR_Expressions.Typed_UniversalRelation('S', 'P')
		if isinstance(rhs1, Typed_COR_Expressions.Typed_UniversalRelation) and rhs1.set1=='S' and rhs1.set2=='Q':
			return Typed_COR_Expressions.Typed_UniversalRelation('S', 'Q')
		if isinstance(rhs1, Typed_COR_Expressions.Typed_UniversalRelation) and rhs1.set1=='S' and rhs1.set2=='R':
			return Typed_COR_Expressions.Typed_UniversalRelation('S', 'R')
		if isinstance(rhs1, Typed_COR_Expressions.Typed_UniversalRelation) and rhs1.set1=='S' and rhs1.set2=='S':
			return Typed_COR_Expressions.Typed_UniversalRelation('S', 'S')
		if isinstance(rhs1, Typed_COR_Expressions.Typed_Intersection):
			lhs2, rhs2 = rhs1.argument1, rhs1.argument2
			B = lhs2
			if str(A)==str(rhs2) and A.type() == rhs2.type():
				return A
			if str(A)==str(lhs2) and A.type() == lhs2.type():
				B = rhs2
				return A
		if isinstance(rhs1, Typed_COR_Expressions.Typed_Union):
			lhs2, rhs2 = rhs1.argument1, rhs1.argument2
			if str(A)==str(lhs2) and A.type() == lhs2.type():
				B = rhs2
				return Typed_COR_Expressions.Typed_Union(B, A)
			B = lhs2
			if str(A)==str(rhs2) and A.type() == rhs2.type():
				return Typed_COR_Expressions.Typed_Union(B, A)
		if isinstance(rhs1, Typed_COR_Expressions.Typed_EmptyRelation) and rhs1.set1=='P' and rhs1.set2=='P':
			return A
		if isinstance(rhs1, Typed_COR_Expressions.Typed_EmptyRelation) and rhs1.set1=='P' and rhs1.set2=='Q':
			return A
		if isinstance(rhs1, Typed_COR_Expressions.Typed_EmptyRelation) and rhs1.set1=='P' and rhs1.set2=='R':
			return A
		if isinstance(rhs1, Typed_COR_Expressions.Typed_EmptyRelation) and rhs1.set1=='P' and rhs1.set2=='S':
			return A
		if isinstance(rhs1, Typed_COR_Expressions.Typed_EmptyRelation) and rhs1.set1=='Q' and rhs1.set2=='P':
			return A
		if isinstance(rhs1, Typed_COR_Expressions.Typed_EmptyRelation) and rhs1.set1=='Q' and rhs1.set2=='Q':
			return A
		if isinstance(rhs1, Typed_COR_Expressions.Typed_EmptyRelation) and rhs1.set1=='Q' and rhs1.set2=='R':
			return A
		if isinstance(rhs1, Typed_COR_Expressions.Typed_EmptyRelation) and rhs1.set1=='Q' and rhs1.set2=='S':
			return A
		if isinstance(rhs1, Typed_COR_Expressions.Typed_EmptyRelation) and rhs1.set1=='R' and rhs1.set2=='P':
			return A
		if isinstance(rhs1, Typed_COR_Expressions.Typed_EmptyRelation) and rhs1.set1=='R' and rhs1.set2=='Q':
			return A
		if isinstance(rhs1, Typed_COR_Expressions.Typed_EmptyRelation) and rhs1.set1=='R' and rhs1.set2=='R':
			return A
		if isinstance(rhs1, Typed_COR_Expressions.Typed_EmptyRelation) and rhs1.set1=='R' and rhs1.set2=='S':
			return A
		if isinstance(rhs1, Typed_COR_Expressions.Typed_EmptyRelation) and rhs1.set1=='S' and rhs1.set2=='P':
			return A
		if isinstance(rhs1, Typed_COR_Expressions.Typed_EmptyRelation) and rhs1.set1=='S' and rhs1.set2=='Q':
			return A
		if isinstance(rhs1, Typed_COR_Expressions.Typed_EmptyRelation) and rhs1.set1=='S' and rhs1.set2=='R':
			return A
		if isinstance(rhs1, Typed_COR_Expressions.Typed_EmptyRelation) and rhs1.set1=='S' and rhs1.set2=='S':
			return A
		if isinstance(rhs1, Typed_COR_Expressions.Typed_Complement):
			arg = rhs1.argument
			if str(A)==str(arg) and A.type() == arg.type():
				return Typed_COR_Expressions.Typed_UniversalRelation('P', 'P')
				return Typed_COR_Expressions.Typed_UniversalRelation('P', 'Q')
				return Typed_COR_Expressions.Typed_UniversalRelation('P', 'R')
				return Typed_COR_Expressions.Typed_UniversalRelation('P', 'S')
				return Typed_COR_Expressions.Typed_UniversalRelation('Q', 'P')
				return Typed_COR_Expressions.Typed_UniversalRelation('Q', 'Q')
				return Typed_COR_Expressions.Typed_UniversalRelation('Q', 'R')
				return Typed_COR_Expressions.Typed_UniversalRelation('Q', 'S')
				return Typed_COR_Expressions.Typed_UniversalRelation('R', 'P')
				return Typed_COR_Expressions.Typed_UniversalRelation('R', 'Q')
				return Typed_COR_Expressions.Typed_UniversalRelation('R', 'R')
				return Typed_COR_Expressions.Typed_UniversalRelation('R', 'S')
				return Typed_COR_Expressions.Typed_UniversalRelation('S', 'P')
				return Typed_COR_Expressions.Typed_UniversalRelation('S', 'Q')
				return Typed_COR_Expressions.Typed_UniversalRelation('S', 'R')
				return Typed_COR_Expressions.Typed_UniversalRelation('S', 'S')
		if isinstance(lhs1, Typed_COR_Expressions.Typed_UniversalRelation) and lhs1.set1=='P' and lhs1.set2=='P':
			A = rhs1
			return Typed_COR_Expressions.Typed_UniversalRelation('P', 'P')
		if isinstance(lhs1, Typed_COR_Expressions.Typed_UniversalRelation) and lhs1.set1=='P' and lhs1.set2=='Q':
			A = rhs1
			return Typed_COR_Expressions.Typed_UniversalRelation('P', 'Q')
		if isinstance(lhs1, Typed_COR_Expressions.Typed_UniversalRelation) and lhs1.set1=='P' and lhs1.set2=='R':
			A = rhs1
			return Typed_COR_Expressions.Typed_UniversalRelation('P', 'R')
		if isinstance(lhs1, Typed_COR_Expressions.Typed_UniversalRelation) and lhs1.set1=='P' and lhs1.set2=='S':
			A = rhs1
			return Typed_COR_Expressions.Typed_UniversalRelation('P', 'S')
		if isinstance(lhs1, Typed_COR_Expressions.Typed_UniversalRelation) and lhs1.set1=='Q' and lhs1.set2=='P':
			A = rhs1
			return Typed_COR_Expressions.Typed_UniversalRelation('Q', 'P')
		if isinstance(lhs1, Typed_COR_Expressions.Typed_UniversalRelation) and lhs1.set1=='Q' and lhs1.set2=='Q':
			A = rhs1
			return Typed_COR_Expressions.Typed_UniversalRelation('Q', 'Q')
		if isinstance(lhs1, Typed_COR_Expressions.Typed_UniversalRelation) and lhs1.set1=='Q' and lhs1.set2=='R':
			A = rhs1
			return Typed_COR_Expressions.Typed_UniversalRelation('Q', 'R')
		if isinstance(lhs1, Typed_COR_Expressions.Typed_UniversalRelation) and lhs1.set1=='Q' and lhs1.set2=='S':
			A = rhs1
			return Typed_COR_Expressions.Typed_UniversalRelation('Q', 'S')
		if isinstance(lhs1, Typed_COR_Expressions.Typed_UniversalRelation) and lhs1.set1=='R' and lhs1.set2=='P':
			A = rhs1
			return Typed_COR_Expressions.Typed_UniversalRelation('R', 'P')
		if isinstance(lhs1, Typed_COR_Expressions.Typed_UniversalRelation) and lhs1.set1=='R' and lhs1.set2=='Q':
			A = rhs1
			return Typed_COR_Expressions.Typed_UniversalRelation('R', 'Q')
		if isinstance(lhs1, Typed_COR_Expressions.Typed_UniversalRelation) and lhs1.set1=='R' and lhs1.set2=='R':
			A = rhs1
			return Typed_COR_Expressions.Typed_UniversalRelation('R', 'R')
		if isinstance(lhs1, Typed_COR_Expressions.Typed_UniversalRelation) and lhs1.set1=='R' and lhs1.set2=='S':
			A = rhs1
			return Typed_COR_Expressions.Typed_UniversalRelation('R', 'S')
		if isinstance(lhs1, Typed_COR_Expressions.Typed_UniversalRelation) and lhs1.set1=='S' and lhs1.set2=='P':
			A = rhs1
			return Typed_COR_Expressions.Typed_UniversalRelation('S', 'P')
		if isinstance(lhs1, Typed_COR_Expressions.Typed_UniversalRelation) and lhs1.set1=='S' and lhs1.set2=='Q':
			A = rhs1
			return Typed_COR_Expressions.Typed_UniversalRelation('S', 'Q')
		if isinstance(lhs1, Typed_COR_Expressions.Typed_UniversalRelation) and lhs1.set1=='S' and lhs1.set2=='R':
			A = rhs1
			return Typed_COR_Expressions.Typed_UniversalRelation('S', 'R')
		if isinstance(lhs1, Typed_COR_Expressions.Typed_UniversalRelation) and lhs1.set1=='S' and lhs1.set2=='S':
			A = rhs1
			return Typed_COR_Expressions.Typed_UniversalRelation('S', 'S')
		if isinstance(lhs1, Typed_COR_Expressions.Typed_Intersection):
			lhs2, rhs2 = lhs1.argument1, lhs1.argument2
			A = lhs2
			B = rhs2
			if str(B)==str(rhs1) and B.type() == rhs1.type():
				return B
			if str(A)==str(rhs1) and A.type() == rhs1.type():
				return A
		if isinstance(lhs1, Typed_COR_Expressions.Typed_Union):
			lhs2, rhs2 = lhs1.argument1, lhs1.argument2
			A = lhs2
			B = rhs2
			if str(B)==str(rhs1) and B.type() == rhs1.type():
				return Typed_COR_Expressions.Typed_Union(A, B)
			if str(A)==str(rhs1) and A.type() == rhs1.type():
				return Typed_COR_Expressions.Typed_Union(B, A)
		if isinstance(lhs1, Typed_COR_Expressions.Typed_Complement):
			arg = lhs1.argument
			A = arg
			if str(A)==str(rhs1) and A.type() == rhs1.type():
				return Typed_COR_Expressions.Typed_UniversalRelation('P', 'P')
				return Typed_COR_Expressions.Typed_UniversalRelation('P', 'Q')
				return Typed_COR_Expressions.Typed_UniversalRelation('P', 'R')
				return Typed_COR_Expressions.Typed_UniversalRelation('P', 'S')
				return Typed_COR_Expressions.Typed_UniversalRelation('Q', 'P')
				return Typed_COR_Expressions.Typed_UniversalRelation('Q', 'Q')
				return Typed_COR_Expressions.Typed_UniversalRelation('Q', 'R')
				return Typed_COR_Expressions.Typed_UniversalRelation('Q', 'S')
				return Typed_COR_Expressions.Typed_UniversalRelation('R', 'P')
				return Typed_COR_Expressions.Typed_UniversalRelation('R', 'Q')
				return Typed_COR_Expressions.Typed_UniversalRelation('R', 'R')
				return Typed_COR_Expressions.Typed_UniversalRelation('R', 'S')
				return Typed_COR_Expressions.Typed_UniversalRelation('S', 'P')
				return Typed_COR_Expressions.Typed_UniversalRelation('S', 'Q')
				return Typed_COR_Expressions.Typed_UniversalRelation('S', 'R')
				return Typed_COR_Expressions.Typed_UniversalRelation('S', 'S')
		if isinstance(lhs1, Typed_COR_Expressions.Typed_EmptyRelation) and lhs1.set1=='P' and lhs1.set2=='P':
			A = rhs1
			return A
		if isinstance(lhs1, Typed_COR_Expressions.Typed_EmptyRelation) and lhs1.set1=='P' and lhs1.set2=='Q':
			A = rhs1
			return A
		if isinstance(lhs1, Typed_COR_Expressions.Typed_EmptyRelation) and lhs1.set1=='P' and lhs1.set2=='R':
			A = rhs1
			return A
		if isinstance(lhs1, Typed_COR_Expressions.Typed_EmptyRelation) and lhs1.set1=='P' and lhs1.set2=='S':
			A = rhs1
			return A
		if isinstance(lhs1, Typed_COR_Expressions.Typed_EmptyRelation) and lhs1.set1=='Q' and lhs1.set2=='P':
			A = rhs1
			return A
		if isinstance(lhs1, Typed_COR_Expressions.Typed_EmptyRelation) and lhs1.set1=='Q' and lhs1.set2=='Q':
			A = rhs1
			return A
		if isinstance(lhs1, Typed_COR_Expressions.Typed_EmptyRelation) and lhs1.set1=='Q' and lhs1.set2=='R':
			A = rhs1
			return A
		if isinstance(lhs1, Typed_COR_Expressions.Typed_EmptyRelation) and lhs1.set1=='Q' and lhs1.set2=='S':
			A = rhs1
			return A
		if isinstance(lhs1, Typed_COR_Expressions.Typed_EmptyRelation) and lhs1.set1=='R' and lhs1.set2=='P':
			A = rhs1
			return A
		if isinstance(lhs1, Typed_COR_Expressions.Typed_EmptyRelation) and lhs1.set1=='R' and lhs1.set2=='Q':
			A = rhs1
			return A
		if isinstance(lhs1, Typed_COR_Expressions.Typed_EmptyRelation) and lhs1.set1=='R' and lhs1.set2=='R':
			A = rhs1
			return A
		if isinstance(lhs1, Typed_COR_Expressions.Typed_EmptyRelation) and lhs1.set1=='R' and lhs1.set2=='S':
			A = rhs1
			return A
		if isinstance(lhs1, Typed_COR_Expressions.Typed_EmptyRelation) and lhs1.set1=='S' and lhs1.set2=='P':
			A = rhs1
			return A
		if isinstance(lhs1, Typed_COR_Expressions.Typed_EmptyRelation) and lhs1.set1=='S' and lhs1.set2=='Q':
			A = rhs1
			return A
		if isinstance(lhs1, Typed_COR_Expressions.Typed_EmptyRelation) and lhs1.set1=='S' and lhs1.set2=='R':
			A = rhs1
			return A
		if isinstance(lhs1, Typed_COR_Expressions.Typed_EmptyRelation) and lhs1.set1=='S' and lhs1.set2=='S':
			A = rhs1
			return A
	if isinstance(expression, Typed_COR_Expressions.Typed_Dagger):
		lhs1, rhs1 = expression.argument1, expression.argument2
		if isinstance(lhs1, Typed_COR_Expressions.Typed_UniversalRelation) and lhs1.set1=='P' and lhs1.set2=='P':
			A = rhs1
			return Typed_COR_Expressions.Typed_UniversalRelation('P', 'P')
			return Typed_COR_Expressions.Typed_UniversalRelation('P', 'Q')
			return Typed_COR_Expressions.Typed_UniversalRelation('P', 'R')
			return Typed_COR_Expressions.Typed_UniversalRelation('P', 'S')
		if isinstance(lhs1, Typed_COR_Expressions.Typed_UniversalRelation) and lhs1.set1=='P' and lhs1.set2=='Q':
			A = rhs1
			return Typed_COR_Expressions.Typed_UniversalRelation('P', 'P')
			return Typed_COR_Expressions.Typed_UniversalRelation('P', 'Q')
			return Typed_COR_Expressions.Typed_UniversalRelation('P', 'R')
			return Typed_COR_Expressions.Typed_UniversalRelation('P', 'S')
		if isinstance(lhs1, Typed_COR_Expressions.Typed_UniversalRelation) and lhs1.set1=='P' and lhs1.set2=='R':
			A = rhs1
			return Typed_COR_Expressions.Typed_UniversalRelation('P', 'P')
			return Typed_COR_Expressions.Typed_UniversalRelation('P', 'Q')
			return Typed_COR_Expressions.Typed_UniversalRelation('P', 'R')
			return Typed_COR_Expressions.Typed_UniversalRelation('P', 'S')
		if isinstance(lhs1, Typed_COR_Expressions.Typed_UniversalRelation) and lhs1.set1=='P' and lhs1.set2=='S':
			A = rhs1
			return Typed_COR_Expressions.Typed_UniversalRelation('P', 'P')
			return Typed_COR_Expressions.Typed_UniversalRelation('P', 'Q')
			return Typed_COR_Expressions.Typed_UniversalRelation('P', 'R')
			return Typed_COR_Expressions.Typed_UniversalRelation('P', 'S')
		if isinstance(lhs1, Typed_COR_Expressions.Typed_UniversalRelation) and lhs1.set1=='Q' and lhs1.set2=='P':
			A = rhs1
			return Typed_COR_Expressions.Typed_UniversalRelation('Q', 'P')
			return Typed_COR_Expressions.Typed_UniversalRelation('Q', 'Q')
			return Typed_COR_Expressions.Typed_UniversalRelation('Q', 'R')
			return Typed_COR_Expressions.Typed_UniversalRelation('Q', 'S')
		if isinstance(lhs1, Typed_COR_Expressions.Typed_UniversalRelation) and lhs1.set1=='Q' and lhs1.set2=='Q':
			A = rhs1
			return Typed_COR_Expressions.Typed_UniversalRelation('Q', 'P')
			return Typed_COR_Expressions.Typed_UniversalRelation('Q', 'Q')
			return Typed_COR_Expressions.Typed_UniversalRelation('Q', 'R')
			return Typed_COR_Expressions.Typed_UniversalRelation('Q', 'S')
		if isinstance(lhs1, Typed_COR_Expressions.Typed_UniversalRelation) and lhs1.set1=='Q' and lhs1.set2=='R':
			A = rhs1
			return Typed_COR_Expressions.Typed_UniversalRelation('Q', 'P')
			return Typed_COR_Expressions.Typed_UniversalRelation('Q', 'Q')
			return Typed_COR_Expressions.Typed_UniversalRelation('Q', 'R')
			return Typed_COR_Expressions.Typed_UniversalRelation('Q', 'S')
		if isinstance(lhs1, Typed_COR_Expressions.Typed_UniversalRelation) and lhs1.set1=='Q' and lhs1.set2=='S':
			A = rhs1
			return Typed_COR_Expressions.Typed_UniversalRelation('Q', 'P')
			return Typed_COR_Expressions.Typed_UniversalRelation('Q', 'Q')
			return Typed_COR_Expressions.Typed_UniversalRelation('Q', 'R')
			return Typed_COR_Expressions.Typed_UniversalRelation('Q', 'S')
		if isinstance(lhs1, Typed_COR_Expressions.Typed_UniversalRelation) and lhs1.set1=='R' and lhs1.set2=='P':
			A = rhs1
			return Typed_COR_Expressions.Typed_UniversalRelation('R', 'P')
			return Typed_COR_Expressions.Typed_UniversalRelation('R', 'Q')
			return Typed_COR_Expressions.Typed_UniversalRelation('R', 'R')
			return Typed_COR_Expressions.Typed_UniversalRelation('R', 'S')
		if isinstance(lhs1, Typed_COR_Expressions.Typed_UniversalRelation) and lhs1.set1=='R' and lhs1.set2=='Q':
			A = rhs1
			return Typed_COR_Expressions.Typed_UniversalRelation('R', 'P')
			return Typed_COR_Expressions.Typed_UniversalRelation('R', 'Q')
			return Typed_COR_Expressions.Typed_UniversalRelation('R', 'R')
			return Typed_COR_Expressions.Typed_UniversalRelation('R', 'S')
		if isinstance(lhs1, Typed_COR_Expressions.Typed_UniversalRelation) and lhs1.set1=='R' and lhs1.set2=='R':
			A = rhs1
			return Typed_COR_Expressions.Typed_UniversalRelation('R', 'P')
			return Typed_COR_Expressions.Typed_UniversalRelation('R', 'Q')
			return Typed_COR_Expressions.Typed_UniversalRelation('R', 'R')
			return Typed_COR_Expressions.Typed_UniversalRelation('R', 'S')
		if isinstance(lhs1, Typed_COR_Expressions.Typed_UniversalRelation) and lhs1.set1=='R' and lhs1.set2=='S':
			A = rhs1
			return Typed_COR_Expressions.Typed_UniversalRelation('R', 'P')
			return Typed_COR_Expressions.Typed_UniversalRelation('R', 'Q')
			return Typed_COR_Expressions.Typed_UniversalRelation('R', 'R')
			return Typed_COR_Expressions.Typed_UniversalRelation('R', 'S')
		if isinstance(lhs1, Typed_COR_Expressions.Typed_UniversalRelation) and lhs1.set1=='S' and lhs1.set2=='P':
			A = rhs1
			return Typed_COR_Expressions.Typed_UniversalRelation('S', 'P')
			return Typed_COR_Expressions.Typed_UniversalRelation('S', 'Q')
			return Typed_COR_Expressions.Typed_UniversalRelation('S', 'R')
			return Typed_COR_Expressions.Typed_UniversalRelation('S', 'S')
		if isinstance(lhs1, Typed_COR_Expressions.Typed_UniversalRelation) and lhs1.set1=='S' and lhs1.set2=='Q':
			A = rhs1
			return Typed_COR_Expressions.Typed_UniversalRelation('S', 'P')
			return Typed_COR_Expressions.Typed_UniversalRelation('S', 'Q')
			return Typed_COR_Expressions.Typed_UniversalRelation('S', 'R')
			return Typed_COR_Expressions.Typed_UniversalRelation('S', 'S')
		if isinstance(lhs1, Typed_COR_Expressions.Typed_UniversalRelation) and lhs1.set1=='S' and lhs1.set2=='R':
			A = rhs1
			return Typed_COR_Expressions.Typed_UniversalRelation('S', 'P')
			return Typed_COR_Expressions.Typed_UniversalRelation('S', 'Q')
			return Typed_COR_Expressions.Typed_UniversalRelation('S', 'R')
			return Typed_COR_Expressions.Typed_UniversalRelation('S', 'S')
		if isinstance(lhs1, Typed_COR_Expressions.Typed_UniversalRelation) and lhs1.set1=='S' and lhs1.set2=='S':
			A = rhs1
			return Typed_COR_Expressions.Typed_UniversalRelation('S', 'P')
			return Typed_COR_Expressions.Typed_UniversalRelation('S', 'Q')
			return Typed_COR_Expressions.Typed_UniversalRelation('S', 'R')
			return Typed_COR_Expressions.Typed_UniversalRelation('S', 'S')
		A = lhs1
		if isinstance(rhs1, Typed_COR_Expressions.Typed_UniversalRelation) and rhs1.set1=='P' and rhs1.set2=='P':
			return Typed_COR_Expressions.Typed_UniversalRelation('P', 'P')
			return Typed_COR_Expressions.Typed_UniversalRelation('Q', 'P')
			return Typed_COR_Expressions.Typed_UniversalRelation('R', 'P')
			return Typed_COR_Expressions.Typed_UniversalRelation('S', 'P')
		if isinstance(rhs1, Typed_COR_Expressions.Typed_UniversalRelation) and rhs1.set1=='P' and rhs1.set2=='Q':
			return Typed_COR_Expressions.Typed_UniversalRelation('P', 'Q')
			return Typed_COR_Expressions.Typed_UniversalRelation('Q', 'Q')
			return Typed_COR_Expressions.Typed_UniversalRelation('R', 'Q')
			return Typed_COR_Expressions.Typed_UniversalRelation('S', 'Q')
		if isinstance(rhs1, Typed_COR_Expressions.Typed_UniversalRelation) and rhs1.set1=='P' and rhs1.set2=='R':
			return Typed_COR_Expressions.Typed_UniversalRelation('P', 'R')
			return Typed_COR_Expressions.Typed_UniversalRelation('Q', 'R')
			return Typed_COR_Expressions.Typed_UniversalRelation('R', 'R')
			return Typed_COR_Expressions.Typed_UniversalRelation('S', 'R')
		if isinstance(rhs1, Typed_COR_Expressions.Typed_UniversalRelation) and rhs1.set1=='P' and rhs1.set2=='S':
			return Typed_COR_Expressions.Typed_UniversalRelation('P', 'S')
			return Typed_COR_Expressions.Typed_UniversalRelation('Q', 'S')
			return Typed_COR_Expressions.Typed_UniversalRelation('R', 'S')
			return Typed_COR_Expressions.Typed_UniversalRelation('S', 'S')
		if isinstance(rhs1, Typed_COR_Expressions.Typed_UniversalRelation) and rhs1.set1=='Q' and rhs1.set2=='P':
			return Typed_COR_Expressions.Typed_UniversalRelation('P', 'P')
			return Typed_COR_Expressions.Typed_UniversalRelation('Q', 'P')
			return Typed_COR_Expressions.Typed_UniversalRelation('R', 'P')
			return Typed_COR_Expressions.Typed_UniversalRelation('S', 'P')
		if isinstance(rhs1, Typed_COR_Expressions.Typed_UniversalRelation) and rhs1.set1=='Q' and rhs1.set2=='Q':
			return Typed_COR_Expressions.Typed_UniversalRelation('P', 'Q')
			return Typed_COR_Expressions.Typed_UniversalRelation('Q', 'Q')
			return Typed_COR_Expressions.Typed_UniversalRelation('R', 'Q')
			return Typed_COR_Expressions.Typed_UniversalRelation('S', 'Q')
		if isinstance(rhs1, Typed_COR_Expressions.Typed_UniversalRelation) and rhs1.set1=='Q' and rhs1.set2=='R':
			return Typed_COR_Expressions.Typed_UniversalRelation('P', 'R')
			return Typed_COR_Expressions.Typed_UniversalRelation('Q', 'R')
			return Typed_COR_Expressions.Typed_UniversalRelation('R', 'R')
			return Typed_COR_Expressions.Typed_UniversalRelation('S', 'R')
		if isinstance(rhs1, Typed_COR_Expressions.Typed_UniversalRelation) and rhs1.set1=='Q' and rhs1.set2=='S':
			return Typed_COR_Expressions.Typed_UniversalRelation('P', 'S')
			return Typed_COR_Expressions.Typed_UniversalRelation('Q', 'S')
			return Typed_COR_Expressions.Typed_UniversalRelation('R', 'S')
			return Typed_COR_Expressions.Typed_UniversalRelation('S', 'S')
		if isinstance(rhs1, Typed_COR_Expressions.Typed_UniversalRelation) and rhs1.set1=='R' and rhs1.set2=='P':
			return Typed_COR_Expressions.Typed_UniversalRelation('P', 'P')
			return Typed_COR_Expressions.Typed_UniversalRelation('Q', 'P')
			return Typed_COR_Expressions.Typed_UniversalRelation('R', 'P')
			return Typed_COR_Expressions.Typed_UniversalRelation('S', 'P')
		if isinstance(rhs1, Typed_COR_Expressions.Typed_UniversalRelation) and rhs1.set1=='R' and rhs1.set2=='Q':
			return Typed_COR_Expressions.Typed_UniversalRelation('P', 'Q')
			return Typed_COR_Expressions.Typed_UniversalRelation('Q', 'Q')
			return Typed_COR_Expressions.Typed_UniversalRelation('R', 'Q')
			return Typed_COR_Expressions.Typed_UniversalRelation('S', 'Q')
		if isinstance(rhs1, Typed_COR_Expressions.Typed_UniversalRelation) and rhs1.set1=='R' and rhs1.set2=='R':
			return Typed_COR_Expressions.Typed_UniversalRelation('P', 'R')
			return Typed_COR_Expressions.Typed_UniversalRelation('Q', 'R')
			return Typed_COR_Expressions.Typed_UniversalRelation('R', 'R')
			return Typed_COR_Expressions.Typed_UniversalRelation('S', 'R')
		if isinstance(rhs1, Typed_COR_Expressions.Typed_UniversalRelation) and rhs1.set1=='R' and rhs1.set2=='S':
			return Typed_COR_Expressions.Typed_UniversalRelation('P', 'S')
			return Typed_COR_Expressions.Typed_UniversalRelation('Q', 'S')
			return Typed_COR_Expressions.Typed_UniversalRelation('R', 'S')
			return Typed_COR_Expressions.Typed_UniversalRelation('S', 'S')
		if isinstance(rhs1, Typed_COR_Expressions.Typed_UniversalRelation) and rhs1.set1=='S' and rhs1.set2=='P':
			return Typed_COR_Expressions.Typed_UniversalRelation('P', 'P')
			return Typed_COR_Expressions.Typed_UniversalRelation('Q', 'P')
			return Typed_COR_Expressions.Typed_UniversalRelation('R', 'P')
			return Typed_COR_Expressions.Typed_UniversalRelation('S', 'P')
		if isinstance(rhs1, Typed_COR_Expressions.Typed_UniversalRelation) and rhs1.set1=='S' and rhs1.set2=='Q':
			return Typed_COR_Expressions.Typed_UniversalRelation('P', 'Q')
			return Typed_COR_Expressions.Typed_UniversalRelation('Q', 'Q')
			return Typed_COR_Expressions.Typed_UniversalRelation('R', 'Q')
			return Typed_COR_Expressions.Typed_UniversalRelation('S', 'Q')
		if isinstance(rhs1, Typed_COR_Expressions.Typed_UniversalRelation) and rhs1.set1=='S' and rhs1.set2=='R':
			return Typed_COR_Expressions.Typed_UniversalRelation('P', 'R')
			return Typed_COR_Expressions.Typed_UniversalRelation('Q', 'R')
			return Typed_COR_Expressions.Typed_UniversalRelation('R', 'R')
			return Typed_COR_Expressions.Typed_UniversalRelation('S', 'R')
		if isinstance(rhs1, Typed_COR_Expressions.Typed_UniversalRelation) and rhs1.set1=='S' and rhs1.set2=='S':
			return Typed_COR_Expressions.Typed_UniversalRelation('P', 'S')
			return Typed_COR_Expressions.Typed_UniversalRelation('Q', 'S')
			return Typed_COR_Expressions.Typed_UniversalRelation('R', 'S')
			return Typed_COR_Expressions.Typed_UniversalRelation('S', 'S')
	if isinstance(expression, Typed_COR_Expressions.Typed_Converse):
		arg = expression.argument
		if isinstance(arg, Typed_COR_Expressions.Typed_Converse):
			arg = arg.argument
			A = arg
			return A
		if isinstance(arg, Typed_COR_Expressions.Typed_IdentityRelation) and arg.set1=='P' and arg.set2=='P':
			return Typed_COR_Expressions.Typed_IdentityRelation('P', 'P')
		if isinstance(arg, Typed_COR_Expressions.Typed_IdentityRelation) and arg.set1=='Q' and arg.set2=='Q':
			return Typed_COR_Expressions.Typed_IdentityRelation('Q', 'Q')
		if isinstance(arg, Typed_COR_Expressions.Typed_IdentityRelation) and arg.set1=='R' and arg.set2=='R':
			return Typed_COR_Expressions.Typed_IdentityRelation('R', 'R')
		if isinstance(arg, Typed_COR_Expressions.Typed_IdentityRelation) and arg.set1=='S' and arg.set2=='S':
			return Typed_COR_Expressions.Typed_IdentityRelation('S', 'S')
		if isinstance(arg, Typed_COR_Expressions.Typed_EmptyRelation) and arg.set1=='P' and arg.set2=='P':
			return Typed_COR_Expressions.Typed_EmptyRelation('P', 'P')
		if isinstance(arg, Typed_COR_Expressions.Typed_EmptyRelation) and arg.set1=='P' and arg.set2=='Q':
			return Typed_COR_Expressions.Typed_EmptyRelation('Q', 'P')
		if isinstance(arg, Typed_COR_Expressions.Typed_EmptyRelation) and arg.set1=='P' and arg.set2=='R':
			return Typed_COR_Expressions.Typed_EmptyRelation('R', 'P')
		if isinstance(arg, Typed_COR_Expressions.Typed_EmptyRelation) and arg.set1=='P' and arg.set2=='S':
			return Typed_COR_Expressions.Typed_EmptyRelation('S', 'P')
		if isinstance(arg, Typed_COR_Expressions.Typed_EmptyRelation) and arg.set1=='Q' and arg.set2=='P':
			return Typed_COR_Expressions.Typed_EmptyRelation('P', 'Q')
		if isinstance(arg, Typed_COR_Expressions.Typed_EmptyRelation) and arg.set1=='Q' and arg.set2=='Q':
			return Typed_COR_Expressions.Typed_EmptyRelation('Q', 'Q')
		if isinstance(arg, Typed_COR_Expressions.Typed_EmptyRelation) and arg.set1=='Q' and arg.set2=='R':
			return Typed_COR_Expressions.Typed_EmptyRelation('R', 'Q')
		if isinstance(arg, Typed_COR_Expressions.Typed_EmptyRelation) and arg.set1=='Q' and arg.set2=='S':
			return Typed_COR_Expressions.Typed_EmptyRelation('S', 'Q')
		if isinstance(arg, Typed_COR_Expressions.Typed_EmptyRelation) and arg.set1=='R' and arg.set2=='P':
			return Typed_COR_Expressions.Typed_EmptyRelation('P', 'R')
		if isinstance(arg, Typed_COR_Expressions.Typed_EmptyRelation) and arg.set1=='R' and arg.set2=='Q':
			return Typed_COR_Expressions.Typed_EmptyRelation('Q', 'R')
		if isinstance(arg, Typed_COR_Expressions.Typed_EmptyRelation) and arg.set1=='R' and arg.set2=='R':
			return Typed_COR_Expressions.Typed_EmptyRelation('R', 'R')
		if isinstance(arg, Typed_COR_Expressions.Typed_EmptyRelation) and arg.set1=='R' and arg.set2=='S':
			return Typed_COR_Expressions.Typed_EmptyRelation('S', 'R')
		if isinstance(arg, Typed_COR_Expressions.Typed_EmptyRelation) and arg.set1=='S' and arg.set2=='P':
			return Typed_COR_Expressions.Typed_EmptyRelation('P', 'S')
		if isinstance(arg, Typed_COR_Expressions.Typed_EmptyRelation) and arg.set1=='S' and arg.set2=='Q':
			return Typed_COR_Expressions.Typed_EmptyRelation('Q', 'S')
		if isinstance(arg, Typed_COR_Expressions.Typed_EmptyRelation) and arg.set1=='S' and arg.set2=='R':
			return Typed_COR_Expressions.Typed_EmptyRelation('R', 'S')
		if isinstance(arg, Typed_COR_Expressions.Typed_EmptyRelation) and arg.set1=='S' and arg.set2=='S':
			return Typed_COR_Expressions.Typed_EmptyRelation('S', 'S')
		if isinstance(arg, Typed_COR_Expressions.Typed_UniversalRelation) and arg.set1=='P' and arg.set2=='P':
			return Typed_COR_Expressions.Typed_UniversalRelation('P', 'P')
		if isinstance(arg, Typed_COR_Expressions.Typed_UniversalRelation) and arg.set1=='P' and arg.set2=='Q':
			return Typed_COR_Expressions.Typed_UniversalRelation('Q', 'P')
		if isinstance(arg, Typed_COR_Expressions.Typed_UniversalRelation) and arg.set1=='P' and arg.set2=='R':
			return Typed_COR_Expressions.Typed_UniversalRelation('R', 'P')
		if isinstance(arg, Typed_COR_Expressions.Typed_UniversalRelation) and arg.set1=='P' and arg.set2=='S':
			return Typed_COR_Expressions.Typed_UniversalRelation('S', 'P')
		if isinstance(arg, Typed_COR_Expressions.Typed_UniversalRelation) and arg.set1=='Q' and arg.set2=='P':
			return Typed_COR_Expressions.Typed_UniversalRelation('P', 'Q')
		if isinstance(arg, Typed_COR_Expressions.Typed_UniversalRelation) and arg.set1=='Q' and arg.set2=='Q':
			return Typed_COR_Expressions.Typed_UniversalRelation('Q', 'Q')
		if isinstance(arg, Typed_COR_Expressions.Typed_UniversalRelation) and arg.set1=='Q' and arg.set2=='R':
			return Typed_COR_Expressions.Typed_UniversalRelation('R', 'Q')
		if isinstance(arg, Typed_COR_Expressions.Typed_UniversalRelation) and arg.set1=='Q' and arg.set2=='S':
			return Typed_COR_Expressions.Typed_UniversalRelation('S', 'Q')
		if isinstance(arg, Typed_COR_Expressions.Typed_UniversalRelation) and arg.set1=='R' and arg.set2=='P':
			return Typed_COR_Expressions.Typed_UniversalRelation('P', 'R')
		if isinstance(arg, Typed_COR_Expressions.Typed_UniversalRelation) and arg.set1=='R' and arg.set2=='Q':
			return Typed_COR_Expressions.Typed_UniversalRelation('Q', 'R')
		if isinstance(arg, Typed_COR_Expressions.Typed_UniversalRelation) and arg.set1=='R' and arg.set2=='R':
			return Typed_COR_Expressions.Typed_UniversalRelation('R', 'R')
		if isinstance(arg, Typed_COR_Expressions.Typed_UniversalRelation) and arg.set1=='R' and arg.set2=='S':
			return Typed_COR_Expressions.Typed_UniversalRelation('S', 'R')
		if isinstance(arg, Typed_COR_Expressions.Typed_UniversalRelation) and arg.set1=='S' and arg.set2=='P':
			return Typed_COR_Expressions.Typed_UniversalRelation('P', 'S')
		if isinstance(arg, Typed_COR_Expressions.Typed_UniversalRelation) and arg.set1=='S' and arg.set2=='Q':
			return Typed_COR_Expressions.Typed_UniversalRelation('Q', 'S')
		if isinstance(arg, Typed_COR_Expressions.Typed_UniversalRelation) and arg.set1=='S' and arg.set2=='R':
			return Typed_COR_Expressions.Typed_UniversalRelation('R', 'S')
		if isinstance(arg, Typed_COR_Expressions.Typed_UniversalRelation) and arg.set1=='S' and arg.set2=='S':
			return Typed_COR_Expressions.Typed_UniversalRelation('S', 'S')
	if isinstance(expression, Typed_COR_Expressions.Typed_Composition):
		lhs1, rhs1 = expression.argument1, expression.argument2
		A = lhs1
		if isinstance(rhs1, Typed_COR_Expressions.Typed_IdentityRelation) and rhs1.set1=='P' and rhs1.set2=='P':
			return A
		if isinstance(rhs1, Typed_COR_Expressions.Typed_IdentityRelation) and rhs1.set1=='Q' and rhs1.set2=='Q':
			return A
		if isinstance(rhs1, Typed_COR_Expressions.Typed_IdentityRelation) and rhs1.set1=='R' and rhs1.set2=='R':
			return A
		if isinstance(rhs1, Typed_COR_Expressions.Typed_IdentityRelation) and rhs1.set1=='S' and rhs1.set2=='S':
			return A
		if isinstance(rhs1, Typed_COR_Expressions.Typed_EmptyRelation) and rhs1.set1=='P' and rhs1.set2=='P':
			return Typed_COR_Expressions.Typed_EmptyRelation('P', 'P')
			return Typed_COR_Expressions.Typed_EmptyRelation('Q', 'P')
			return Typed_COR_Expressions.Typed_EmptyRelation('R', 'P')
			return Typed_COR_Expressions.Typed_EmptyRelation('S', 'P')
		if isinstance(rhs1, Typed_COR_Expressions.Typed_EmptyRelation) and rhs1.set1=='P' and rhs1.set2=='Q':
			return Typed_COR_Expressions.Typed_EmptyRelation('P', 'Q')
			return Typed_COR_Expressions.Typed_EmptyRelation('Q', 'Q')
			return Typed_COR_Expressions.Typed_EmptyRelation('R', 'Q')
			return Typed_COR_Expressions.Typed_EmptyRelation('S', 'Q')
		if isinstance(rhs1, Typed_COR_Expressions.Typed_EmptyRelation) and rhs1.set1=='P' and rhs1.set2=='R':
			return Typed_COR_Expressions.Typed_EmptyRelation('P', 'R')
			return Typed_COR_Expressions.Typed_EmptyRelation('Q', 'R')
			return Typed_COR_Expressions.Typed_EmptyRelation('R', 'R')
			return Typed_COR_Expressions.Typed_EmptyRelation('S', 'R')
		if isinstance(rhs1, Typed_COR_Expressions.Typed_EmptyRelation) and rhs1.set1=='P' and rhs1.set2=='S':
			return Typed_COR_Expressions.Typed_EmptyRelation('P', 'S')
			return Typed_COR_Expressions.Typed_EmptyRelation('Q', 'S')
			return Typed_COR_Expressions.Typed_EmptyRelation('R', 'S')
			return Typed_COR_Expressions.Typed_EmptyRelation('S', 'S')
		if isinstance(rhs1, Typed_COR_Expressions.Typed_EmptyRelation) and rhs1.set1=='Q' and rhs1.set2=='P':
			return Typed_COR_Expressions.Typed_EmptyRelation('P', 'P')
			return Typed_COR_Expressions.Typed_EmptyRelation('Q', 'P')
			return Typed_COR_Expressions.Typed_EmptyRelation('R', 'P')
			return Typed_COR_Expressions.Typed_EmptyRelation('S', 'P')
		if isinstance(rhs1, Typed_COR_Expressions.Typed_EmptyRelation) and rhs1.set1=='Q' and rhs1.set2=='Q':
			return Typed_COR_Expressions.Typed_EmptyRelation('P', 'Q')
			return Typed_COR_Expressions.Typed_EmptyRelation('Q', 'Q')
			return Typed_COR_Expressions.Typed_EmptyRelation('R', 'Q')
			return Typed_COR_Expressions.Typed_EmptyRelation('S', 'Q')
		if isinstance(rhs1, Typed_COR_Expressions.Typed_EmptyRelation) and rhs1.set1=='Q' and rhs1.set2=='R':
			return Typed_COR_Expressions.Typed_EmptyRelation('P', 'R')
			return Typed_COR_Expressions.Typed_EmptyRelation('Q', 'R')
			return Typed_COR_Expressions.Typed_EmptyRelation('R', 'R')
			return Typed_COR_Expressions.Typed_EmptyRelation('S', 'R')
		if isinstance(rhs1, Typed_COR_Expressions.Typed_EmptyRelation) and rhs1.set1=='Q' and rhs1.set2=='S':
			return Typed_COR_Expressions.Typed_EmptyRelation('P', 'S')
			return Typed_COR_Expressions.Typed_EmptyRelation('Q', 'S')
			return Typed_COR_Expressions.Typed_EmptyRelation('R', 'S')
			return Typed_COR_Expressions.Typed_EmptyRelation('S', 'S')
		if isinstance(rhs1, Typed_COR_Expressions.Typed_EmptyRelation) and rhs1.set1=='R' and rhs1.set2=='P':
			return Typed_COR_Expressions.Typed_EmptyRelation('P', 'P')
			return Typed_COR_Expressions.Typed_EmptyRelation('Q', 'P')
			return Typed_COR_Expressions.Typed_EmptyRelation('R', 'P')
			return Typed_COR_Expressions.Typed_EmptyRelation('S', 'P')
		if isinstance(rhs1, Typed_COR_Expressions.Typed_EmptyRelation) and rhs1.set1=='R' and rhs1.set2=='Q':
			return Typed_COR_Expressions.Typed_EmptyRelation('P', 'Q')
			return Typed_COR_Expressions.Typed_EmptyRelation('Q', 'Q')
			return Typed_COR_Expressions.Typed_EmptyRelation('R', 'Q')
			return Typed_COR_Expressions.Typed_EmptyRelation('S', 'Q')
		if isinstance(rhs1, Typed_COR_Expressions.Typed_EmptyRelation) and rhs1.set1=='R' and rhs1.set2=='R':
			return Typed_COR_Expressions.Typed_EmptyRelation('P', 'R')
			return Typed_COR_Expressions.Typed_EmptyRelation('Q', 'R')
			return Typed_COR_Expressions.Typed_EmptyRelation('R', 'R')
			return Typed_COR_Expressions.Typed_EmptyRelation('S', 'R')
		if isinstance(rhs1, Typed_COR_Expressions.Typed_EmptyRelation) and rhs1.set1=='R' and rhs1.set2=='S':
			return Typed_COR_Expressions.Typed_EmptyRelation('P', 'S')
			return Typed_COR_Expressions.Typed_EmptyRelation('Q', 'S')
			return Typed_COR_Expressions.Typed_EmptyRelation('R', 'S')
			return Typed_COR_Expressions.Typed_EmptyRelation('S', 'S')
		if isinstance(rhs1, Typed_COR_Expressions.Typed_EmptyRelation) and rhs1.set1=='S' and rhs1.set2=='P':
			return Typed_COR_Expressions.Typed_EmptyRelation('P', 'P')
			return Typed_COR_Expressions.Typed_EmptyRelation('Q', 'P')
			return Typed_COR_Expressions.Typed_EmptyRelation('R', 'P')
			return Typed_COR_Expressions.Typed_EmptyRelation('S', 'P')
		if isinstance(rhs1, Typed_COR_Expressions.Typed_EmptyRelation) and rhs1.set1=='S' and rhs1.set2=='Q':
			return Typed_COR_Expressions.Typed_EmptyRelation('P', 'Q')
			return Typed_COR_Expressions.Typed_EmptyRelation('Q', 'Q')
			return Typed_COR_Expressions.Typed_EmptyRelation('R', 'Q')
			return Typed_COR_Expressions.Typed_EmptyRelation('S', 'Q')
		if isinstance(rhs1, Typed_COR_Expressions.Typed_EmptyRelation) and rhs1.set1=='S' and rhs1.set2=='R':
			return Typed_COR_Expressions.Typed_EmptyRelation('P', 'R')
			return Typed_COR_Expressions.Typed_EmptyRelation('Q', 'R')
			return Typed_COR_Expressions.Typed_EmptyRelation('R', 'R')
			return Typed_COR_Expressions.Typed_EmptyRelation('S', 'R')
		if isinstance(rhs1, Typed_COR_Expressions.Typed_EmptyRelation) and rhs1.set1=='S' and rhs1.set2=='S':
			return Typed_COR_Expressions.Typed_EmptyRelation('P', 'S')
			return Typed_COR_Expressions.Typed_EmptyRelation('Q', 'S')
			return Typed_COR_Expressions.Typed_EmptyRelation('R', 'S')
			return Typed_COR_Expressions.Typed_EmptyRelation('S', 'S')
		if isinstance(lhs1, Typed_COR_Expressions.Typed_EmptyRelation) and lhs1.set1=='P' and lhs1.set2=='P':
			A = rhs1
			return Typed_COR_Expressions.Typed_EmptyRelation('P', 'P')
			return Typed_COR_Expressions.Typed_EmptyRelation('P', 'Q')
			return Typed_COR_Expressions.Typed_EmptyRelation('P', 'R')
			return Typed_COR_Expressions.Typed_EmptyRelation('P', 'S')
		if isinstance(lhs1, Typed_COR_Expressions.Typed_EmptyRelation) and lhs1.set1=='P' and lhs1.set2=='Q':
			A = rhs1
			return Typed_COR_Expressions.Typed_EmptyRelation('P', 'P')
			return Typed_COR_Expressions.Typed_EmptyRelation('P', 'Q')
			return Typed_COR_Expressions.Typed_EmptyRelation('P', 'R')
			return Typed_COR_Expressions.Typed_EmptyRelation('P', 'S')
		if isinstance(lhs1, Typed_COR_Expressions.Typed_EmptyRelation) and lhs1.set1=='P' and lhs1.set2=='R':
			A = rhs1
			return Typed_COR_Expressions.Typed_EmptyRelation('P', 'P')
			return Typed_COR_Expressions.Typed_EmptyRelation('P', 'Q')
			return Typed_COR_Expressions.Typed_EmptyRelation('P', 'R')
			return Typed_COR_Expressions.Typed_EmptyRelation('P', 'S')
		if isinstance(lhs1, Typed_COR_Expressions.Typed_EmptyRelation) and lhs1.set1=='P' and lhs1.set2=='S':
			A = rhs1
			return Typed_COR_Expressions.Typed_EmptyRelation('P', 'P')
			return Typed_COR_Expressions.Typed_EmptyRelation('P', 'Q')
			return Typed_COR_Expressions.Typed_EmptyRelation('P', 'R')
			return Typed_COR_Expressions.Typed_EmptyRelation('P', 'S')
		if isinstance(lhs1, Typed_COR_Expressions.Typed_EmptyRelation) and lhs1.set1=='Q' and lhs1.set2=='P':
			A = rhs1
			return Typed_COR_Expressions.Typed_EmptyRelation('Q', 'P')
			return Typed_COR_Expressions.Typed_EmptyRelation('Q', 'Q')
			return Typed_COR_Expressions.Typed_EmptyRelation('Q', 'R')
			return Typed_COR_Expressions.Typed_EmptyRelation('Q', 'S')
		if isinstance(lhs1, Typed_COR_Expressions.Typed_EmptyRelation) and lhs1.set1=='Q' and lhs1.set2=='Q':
			A = rhs1
			return Typed_COR_Expressions.Typed_EmptyRelation('Q', 'P')
			return Typed_COR_Expressions.Typed_EmptyRelation('Q', 'Q')
			return Typed_COR_Expressions.Typed_EmptyRelation('Q', 'R')
			return Typed_COR_Expressions.Typed_EmptyRelation('Q', 'S')
		if isinstance(lhs1, Typed_COR_Expressions.Typed_EmptyRelation) and lhs1.set1=='Q' and lhs1.set2=='R':
			A = rhs1
			return Typed_COR_Expressions.Typed_EmptyRelation('Q', 'P')
			return Typed_COR_Expressions.Typed_EmptyRelation('Q', 'Q')
			return Typed_COR_Expressions.Typed_EmptyRelation('Q', 'R')
			return Typed_COR_Expressions.Typed_EmptyRelation('Q', 'S')
		if isinstance(lhs1, Typed_COR_Expressions.Typed_EmptyRelation) and lhs1.set1=='Q' and lhs1.set2=='S':
			A = rhs1
			return Typed_COR_Expressions.Typed_EmptyRelation('Q', 'P')
			return Typed_COR_Expressions.Typed_EmptyRelation('Q', 'Q')
			return Typed_COR_Expressions.Typed_EmptyRelation('Q', 'R')
			return Typed_COR_Expressions.Typed_EmptyRelation('Q', 'S')
		if isinstance(lhs1, Typed_COR_Expressions.Typed_EmptyRelation) and lhs1.set1=='R' and lhs1.set2=='P':
			A = rhs1
			return Typed_COR_Expressions.Typed_EmptyRelation('R', 'P')
			return Typed_COR_Expressions.Typed_EmptyRelation('R', 'Q')
			return Typed_COR_Expressions.Typed_EmptyRelation('R', 'R')
			return Typed_COR_Expressions.Typed_EmptyRelation('R', 'S')
		if isinstance(lhs1, Typed_COR_Expressions.Typed_EmptyRelation) and lhs1.set1=='R' and lhs1.set2=='Q':
			A = rhs1
			return Typed_COR_Expressions.Typed_EmptyRelation('R', 'P')
			return Typed_COR_Expressions.Typed_EmptyRelation('R', 'Q')
			return Typed_COR_Expressions.Typed_EmptyRelation('R', 'R')
			return Typed_COR_Expressions.Typed_EmptyRelation('R', 'S')
		if isinstance(lhs1, Typed_COR_Expressions.Typed_EmptyRelation) and lhs1.set1=='R' and lhs1.set2=='R':
			A = rhs1
			return Typed_COR_Expressions.Typed_EmptyRelation('R', 'P')
			return Typed_COR_Expressions.Typed_EmptyRelation('R', 'Q')
			return Typed_COR_Expressions.Typed_EmptyRelation('R', 'R')
			return Typed_COR_Expressions.Typed_EmptyRelation('R', 'S')
		if isinstance(lhs1, Typed_COR_Expressions.Typed_EmptyRelation) and lhs1.set1=='R' and lhs1.set2=='S':
			A = rhs1
			return Typed_COR_Expressions.Typed_EmptyRelation('R', 'P')
			return Typed_COR_Expressions.Typed_EmptyRelation('R', 'Q')
			return Typed_COR_Expressions.Typed_EmptyRelation('R', 'R')
			return Typed_COR_Expressions.Typed_EmptyRelation('R', 'S')
		if isinstance(lhs1, Typed_COR_Expressions.Typed_EmptyRelation) and lhs1.set1=='S' and lhs1.set2=='P':
			A = rhs1
			return Typed_COR_Expressions.Typed_EmptyRelation('S', 'P')
			return Typed_COR_Expressions.Typed_EmptyRelation('S', 'Q')
			return Typed_COR_Expressions.Typed_EmptyRelation('S', 'R')
			return Typed_COR_Expressions.Typed_EmptyRelation('S', 'S')
		if isinstance(lhs1, Typed_COR_Expressions.Typed_EmptyRelation) and lhs1.set1=='S' and lhs1.set2=='Q':
			A = rhs1
			return Typed_COR_Expressions.Typed_EmptyRelation('S', 'P')
			return Typed_COR_Expressions.Typed_EmptyRelation('S', 'Q')
			return Typed_COR_Expressions.Typed_EmptyRelation('S', 'R')
			return Typed_COR_Expressions.Typed_EmptyRelation('S', 'S')
		if isinstance(lhs1, Typed_COR_Expressions.Typed_EmptyRelation) and lhs1.set1=='S' and lhs1.set2=='R':
			A = rhs1
			return Typed_COR_Expressions.Typed_EmptyRelation('S', 'P')
			return Typed_COR_Expressions.Typed_EmptyRelation('S', 'Q')
			return Typed_COR_Expressions.Typed_EmptyRelation('S', 'R')
			return Typed_COR_Expressions.Typed_EmptyRelation('S', 'S')
		if isinstance(lhs1, Typed_COR_Expressions.Typed_EmptyRelation) and lhs1.set1=='S' and lhs1.set2=='S':
			A = rhs1
			return Typed_COR_Expressions.Typed_EmptyRelation('S', 'P')
			return Typed_COR_Expressions.Typed_EmptyRelation('S', 'Q')
			return Typed_COR_Expressions.Typed_EmptyRelation('S', 'R')
			return Typed_COR_Expressions.Typed_EmptyRelation('S', 'S')
		if isinstance(lhs1, Typed_COR_Expressions.Typed_IdentityRelation) and lhs1.set1=='P' and lhs1.set2=='P':
			A = rhs1
			return A
		if isinstance(lhs1, Typed_COR_Expressions.Typed_IdentityRelation) and lhs1.set1=='Q' and lhs1.set2=='Q':
			A = rhs1
			return A
		if isinstance(lhs1, Typed_COR_Expressions.Typed_IdentityRelation) and lhs1.set1=='R' and lhs1.set2=='R':
			A = rhs1
			return A
		if isinstance(lhs1, Typed_COR_Expressions.Typed_IdentityRelation) and lhs1.set1=='S' and lhs1.set2=='S':
			A = rhs1
			return A
	if isinstance(expression, Typed_COR_Expressions.Typed_Complement):
		arg = expression.argument
		if isinstance(arg, Typed_COR_Expressions.Typed_EmptyRelation) and arg.set1=='P' and arg.set2=='P':
			return Typed_COR_Expressions.Typed_UniversalRelation('P', 'P')
		if isinstance(arg, Typed_COR_Expressions.Typed_EmptyRelation) and arg.set1=='P' and arg.set2=='Q':
			return Typed_COR_Expressions.Typed_UniversalRelation('P', 'Q')
		if isinstance(arg, Typed_COR_Expressions.Typed_EmptyRelation) and arg.set1=='P' and arg.set2=='R':
			return Typed_COR_Expressions.Typed_UniversalRelation('P', 'R')
		if isinstance(arg, Typed_COR_Expressions.Typed_EmptyRelation) and arg.set1=='P' and arg.set2=='S':
			return Typed_COR_Expressions.Typed_UniversalRelation('P', 'S')
		if isinstance(arg, Typed_COR_Expressions.Typed_EmptyRelation) and arg.set1=='Q' and arg.set2=='P':
			return Typed_COR_Expressions.Typed_UniversalRelation('Q', 'P')
		if isinstance(arg, Typed_COR_Expressions.Typed_EmptyRelation) and arg.set1=='Q' and arg.set2=='Q':
			return Typed_COR_Expressions.Typed_UniversalRelation('Q', 'Q')
		if isinstance(arg, Typed_COR_Expressions.Typed_EmptyRelation) and arg.set1=='Q' and arg.set2=='R':
			return Typed_COR_Expressions.Typed_UniversalRelation('Q', 'R')
		if isinstance(arg, Typed_COR_Expressions.Typed_EmptyRelation) and arg.set1=='Q' and arg.set2=='S':
			return Typed_COR_Expressions.Typed_UniversalRelation('Q', 'S')
		if isinstance(arg, Typed_COR_Expressions.Typed_EmptyRelation) and arg.set1=='R' and arg.set2=='P':
			return Typed_COR_Expressions.Typed_UniversalRelation('R', 'P')
		if isinstance(arg, Typed_COR_Expressions.Typed_EmptyRelation) and arg.set1=='R' and arg.set2=='Q':
			return Typed_COR_Expressions.Typed_UniversalRelation('R', 'Q')
		if isinstance(arg, Typed_COR_Expressions.Typed_EmptyRelation) and arg.set1=='R' and arg.set2=='R':
			return Typed_COR_Expressions.Typed_UniversalRelation('R', 'R')
		if isinstance(arg, Typed_COR_Expressions.Typed_EmptyRelation) and arg.set1=='R' and arg.set2=='S':
			return Typed_COR_Expressions.Typed_UniversalRelation('R', 'S')
		if isinstance(arg, Typed_COR_Expressions.Typed_EmptyRelation) and arg.set1=='S' and arg.set2=='P':
			return Typed_COR_Expressions.Typed_UniversalRelation('S', 'P')
		if isinstance(arg, Typed_COR_Expressions.Typed_EmptyRelation) and arg.set1=='S' and arg.set2=='Q':
			return Typed_COR_Expressions.Typed_UniversalRelation('S', 'Q')
		if isinstance(arg, Typed_COR_Expressions.Typed_EmptyRelation) and arg.set1=='S' and arg.set2=='R':
			return Typed_COR_Expressions.Typed_UniversalRelation('S', 'R')
		if isinstance(arg, Typed_COR_Expressions.Typed_EmptyRelation) and arg.set1=='S' and arg.set2=='S':
			return Typed_COR_Expressions.Typed_UniversalRelation('S', 'S')
		if isinstance(arg, Typed_COR_Expressions.Typed_UniversalRelation) and arg.set1=='P' and arg.set2=='P':
			return Typed_COR_Expressions.Typed_EmptyRelation('P', 'P')
		if isinstance(arg, Typed_COR_Expressions.Typed_UniversalRelation) and arg.set1=='P' and arg.set2=='Q':
			return Typed_COR_Expressions.Typed_EmptyRelation('P', 'Q')
		if isinstance(arg, Typed_COR_Expressions.Typed_UniversalRelation) and arg.set1=='P' and arg.set2=='R':
			return Typed_COR_Expressions.Typed_EmptyRelation('P', 'R')
		if isinstance(arg, Typed_COR_Expressions.Typed_UniversalRelation) and arg.set1=='P' and arg.set2=='S':
			return Typed_COR_Expressions.Typed_EmptyRelation('P', 'S')
		if isinstance(arg, Typed_COR_Expressions.Typed_UniversalRelation) and arg.set1=='Q' and arg.set2=='P':
			return Typed_COR_Expressions.Typed_EmptyRelation('Q', 'P')
		if isinstance(arg, Typed_COR_Expressions.Typed_UniversalRelation) and arg.set1=='Q' and arg.set2=='Q':
			return Typed_COR_Expressions.Typed_EmptyRelation('Q', 'Q')
		if isinstance(arg, Typed_COR_Expressions.Typed_UniversalRelation) and arg.set1=='Q' and arg.set2=='R':
			return Typed_COR_Expressions.Typed_EmptyRelation('Q', 'R')
		if isinstance(arg, Typed_COR_Expressions.Typed_UniversalRelation) and arg.set1=='Q' and arg.set2=='S':
			return Typed_COR_Expressions.Typed_EmptyRelation('Q', 'S')
		if isinstance(arg, Typed_COR_Expressions.Typed_UniversalRelation) and arg.set1=='R' and arg.set2=='P':
			return Typed_COR_Expressions.Typed_EmptyRelation('R', 'P')
		if isinstance(arg, Typed_COR_Expressions.Typed_UniversalRelation) and arg.set1=='R' and arg.set2=='Q':
			return Typed_COR_Expressions.Typed_EmptyRelation('R', 'Q')
		if isinstance(arg, Typed_COR_Expressions.Typed_UniversalRelation) and arg.set1=='R' and arg.set2=='R':
			return Typed_COR_Expressions.Typed_EmptyRelation('R', 'R')
		if isinstance(arg, Typed_COR_Expressions.Typed_UniversalRelation) and arg.set1=='R' and arg.set2=='S':
			return Typed_COR_Expressions.Typed_EmptyRelation('R', 'S')
		if isinstance(arg, Typed_COR_Expressions.Typed_UniversalRelation) and arg.set1=='S' and arg.set2=='P':
			return Typed_COR_Expressions.Typed_EmptyRelation('S', 'P')
		if isinstance(arg, Typed_COR_Expressions.Typed_UniversalRelation) and arg.set1=='S' and arg.set2=='Q':
			return Typed_COR_Expressions.Typed_EmptyRelation('S', 'Q')
		if isinstance(arg, Typed_COR_Expressions.Typed_UniversalRelation) and arg.set1=='S' and arg.set2=='R':
			return Typed_COR_Expressions.Typed_EmptyRelation('S', 'R')
		if isinstance(arg, Typed_COR_Expressions.Typed_UniversalRelation) and arg.set1=='S' and arg.set2=='S':
			return Typed_COR_Expressions.Typed_EmptyRelation('S', 'S')
		if isinstance(arg, Typed_COR_Expressions.Typed_Complement):
			arg = arg.argument
			A = arg
			return A

	return expression # The given expression was unable to be simplified