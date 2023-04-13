import COR_Expressions

def simplify(expression):
	match expression:
		case COR_Expressions.Converse(argument=arg):
			match arg:
				case COR_Expressions.UniversalRelation():
					return COR_Expressions.UniversalRelation()
				case COR_Expressions.EmptyRelation():
					return COR_Expressions.EmptyRelation()
				case COR_Expressions.IdentityRelation():
					return COR_Expressions.IdentityRelation()
				case COR_Expressions.Converse(argument=arg):
					match arg:
						case _:
							B = arg
							return B
							A = arg
							return A
							C = arg
							return C
				case COR_Expressions.Complement(argument=arg):
					match arg:
						case COR_Expressions.IdentityRelation():
							return COR_Expressions.Complement(COR_Expressions.IdentityRelation())
						case COR_Expressions.Converse(argument=arg):
							match arg:
								case _:
									C = arg
									return COR_Expressions.Complement(C)
									A = arg
									return COR_Expressions.Complement(A)
									B = arg
									return COR_Expressions.Complement(B)
				case COR_Expressions.Dagger(argument1=arg1, argument2=arg2):
					match arg1:
						case COR_Expressions.EmptyRelation():
							match arg2:
								case COR_Expressions.IdentityRelation():
									return COR_Expressions.Dagger(COR_Expressions.EmptyRelation(), COR_Expressions.IdentityRelation())
						case COR_Expressions.IdentityRelation():
							match arg2:
								case COR_Expressions.IdentityRelation():
									return COR_Expressions.Dagger(COR_Expressions.IdentityRelation(), COR_Expressions.IdentityRelation())
								case COR_Expressions.EmptyRelation():
									return COR_Expressions.Dagger(COR_Expressions.IdentityRelation(), COR_Expressions.EmptyRelation())
				case COR_Expressions.Intersection(argument1=arg1, argument2=arg2):
					match arg1:
						case COR_Expressions.IdentityRelation():
							match arg2:
								case _:
									C = arg2
									return COR_Expressions.Intersection(C, COR_Expressions.IdentityRelation())
									A = arg2
									return COR_Expressions.Intersection(COR_Expressions.IdentityRelation(), A)
									B = arg2
									return COR_Expressions.Intersection(COR_Expressions.IdentityRelation(), B)
						case _:
							A = arg1
							match arg2:
								case COR_Expressions.IdentityRelation():
									return COR_Expressions.Intersection(COR_Expressions.IdentityRelation(), A)
							C = arg1
							match arg2:
								case COR_Expressions.IdentityRelation():
									return COR_Expressions.Intersection(C, COR_Expressions.IdentityRelation())
							B = arg1
							match arg2:
								case COR_Expressions.IdentityRelation():
									return COR_Expressions.Intersection(COR_Expressions.IdentityRelation(), B)
		case COR_Expressions.Complement(argument=arg):
			match arg:
				case COR_Expressions.EmptyRelation():
					return COR_Expressions.UniversalRelation()
				case COR_Expressions.UniversalRelation():
					return COR_Expressions.EmptyRelation()
				case COR_Expressions.Complement(argument=arg):
					match arg:
						case COR_Expressions.IdentityRelation():
							return COR_Expressions.IdentityRelation()
						case _:
							B = arg
							return B
							A = arg
							return A
							C = arg
							return C
				case COR_Expressions.Converse(argument=arg):
					match arg:
						case COR_Expressions.Complement(argument=arg):
							match arg:
								case _:
									C = arg
									return COR_Expressions.Converse(C)
									A = arg
									return COR_Expressions.Converse(A)
									B = arg
									return COR_Expressions.Converse(B)
		case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.IdentityRelation():
					match arg2:
						case COR_Expressions.UniversalRelation():
							return COR_Expressions.UniversalRelation()
						case COR_Expressions.IdentityRelation():
							return COR_Expressions.IdentityRelation()
						case COR_Expressions.EmptyRelation():
							return COR_Expressions.EmptyRelation()
						case _:
							B = arg2
							return B
							A = arg2
							return A
							C = arg2
							return C
				case COR_Expressions.EmptyRelation():
					match arg2:
						case COR_Expressions.IdentityRelation():
							return COR_Expressions.EmptyRelation()
						case COR_Expressions.EmptyRelation():
							return COR_Expressions.EmptyRelation()
						case COR_Expressions.UniversalRelation():
							return COR_Expressions.EmptyRelation()
						case _:
							A = arg2
							return COR_Expressions.EmptyRelation()
							B = arg2
							return COR_Expressions.EmptyRelation()
							C = arg2
							return COR_Expressions.EmptyRelation()
				case COR_Expressions.UniversalRelation():
					match arg2:
						case COR_Expressions.EmptyRelation():
							return COR_Expressions.EmptyRelation()
						case COR_Expressions.UniversalRelation():
							return COR_Expressions.UniversalRelation()
						case COR_Expressions.IdentityRelation():
							return COR_Expressions.UniversalRelation()
				case _:
					A = arg1
					match arg2:
						case COR_Expressions.EmptyRelation():
							return COR_Expressions.EmptyRelation()
						case COR_Expressions.IdentityRelation():
							return A
					B = arg1
					match arg2:
						case COR_Expressions.IdentityRelation():
							return B
						case COR_Expressions.EmptyRelation():
							return COR_Expressions.EmptyRelation()
					C = arg1
					match arg2:
						case COR_Expressions.IdentityRelation():
							return C
						case COR_Expressions.EmptyRelation():
							return COR_Expressions.EmptyRelation()
		case COR_Expressions.Union(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.UniversalRelation():
					match arg2:
						case COR_Expressions.IdentityRelation():
							return COR_Expressions.UniversalRelation()
						case COR_Expressions.EmptyRelation():
							return COR_Expressions.UniversalRelation()
						case COR_Expressions.UniversalRelation():
							return COR_Expressions.UniversalRelation()
						case _:
							C = arg2
							return COR_Expressions.UniversalRelation()
							B = arg2
							return COR_Expressions.UniversalRelation()
							A = arg2
							return COR_Expressions.UniversalRelation()
				case COR_Expressions.EmptyRelation():
					match arg2:
						case COR_Expressions.UniversalRelation():
							return COR_Expressions.UniversalRelation()
						case COR_Expressions.EmptyRelation():
							return COR_Expressions.EmptyRelation()
						case COR_Expressions.IdentityRelation():
							return COR_Expressions.IdentityRelation()
						case _:
							A = arg2
							return A
							B = arg2
							return B
							C = arg2
							return C
				case COR_Expressions.IdentityRelation():
					match arg2:
						case COR_Expressions.IdentityRelation():
							return COR_Expressions.IdentityRelation()
						case COR_Expressions.EmptyRelation():
							return COR_Expressions.IdentityRelation()
						case COR_Expressions.UniversalRelation():
							return COR_Expressions.UniversalRelation()
						case COR_Expressions.Complement(argument=arg):
							match arg:
								case COR_Expressions.IdentityRelation():
									return COR_Expressions.UniversalRelation()
				case COR_Expressions.Complement(argument=arg):
					match arg:
						case COR_Expressions.IdentityRelation():
							match arg2:
								case COR_Expressions.IdentityRelation():
									return COR_Expressions.UniversalRelation()
								case COR_Expressions.UniversalRelation():
									return COR_Expressions.UniversalRelation()
								case COR_Expressions.EmptyRelation():
									return COR_Expressions.Complement(COR_Expressions.IdentityRelation())
						case _:
							C = arg
							match arg2:
								case _ if str(C)==str(arg2):
									return COR_Expressions.UniversalRelation()
								case COR_Expressions.UniversalRelation():
									return COR_Expressions.UniversalRelation()
								case COR_Expressions.EmptyRelation():
									return COR_Expressions.Complement(C)
							A = arg
							match arg2:
								case _ if str(A)==str(arg2):
									return COR_Expressions.UniversalRelation()
								case COR_Expressions.EmptyRelation():
									return COR_Expressions.Complement(A)
								case COR_Expressions.UniversalRelation():
									return COR_Expressions.UniversalRelation()
							B = arg
							match arg2:
								case _ if str(B)==str(arg2):
									return COR_Expressions.UniversalRelation()
								case COR_Expressions.EmptyRelation():
									return COR_Expressions.Complement(B)
								case COR_Expressions.UniversalRelation():
									return COR_Expressions.UniversalRelation()
				case _:
					A = arg1
					match arg2:
						case COR_Expressions.UniversalRelation():
							return COR_Expressions.UniversalRelation()
						case _ if str(A)==str(arg2):
							return A
						case COR_Expressions.EmptyRelation():
							return A
						case COR_Expressions.Complement(argument=arg):
							match arg:
								case _ if str(A)==str(arg):
									return COR_Expressions.UniversalRelation()
					C = arg1
					match arg2:
						case _ if str(C)==str(arg2):
							return C
						case COR_Expressions.UniversalRelation():
							return COR_Expressions.UniversalRelation()
						case COR_Expressions.EmptyRelation():
							return C
						case COR_Expressions.Complement(argument=arg):
							match arg:
								case _ if str(C)==str(arg):
									return COR_Expressions.UniversalRelation()
					B = arg1
					match arg2:
						case COR_Expressions.EmptyRelation():
							return B
						case _ if str(B)==str(arg2):
							return B
						case COR_Expressions.UniversalRelation():
							return COR_Expressions.UniversalRelation()
						case COR_Expressions.Complement(argument=arg):
							match arg:
								case _ if str(B)==str(arg):
									return COR_Expressions.UniversalRelation()
		case COR_Expressions.Intersection(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.IdentityRelation():
					match arg2:
						case COR_Expressions.EmptyRelation():
							return COR_Expressions.EmptyRelation()
						case COR_Expressions.IdentityRelation():
							return COR_Expressions.IdentityRelation()
						case COR_Expressions.UniversalRelation():
							return COR_Expressions.IdentityRelation()
						case COR_Expressions.Converse(argument=arg):
							match arg:
								case _:
									B = arg
									return COR_Expressions.Intersection(B, COR_Expressions.IdentityRelation())
									A = arg
									return COR_Expressions.Intersection(COR_Expressions.IdentityRelation(), A)
									C = arg
									return COR_Expressions.Intersection(COR_Expressions.IdentityRelation(), C)
						case COR_Expressions.Complement(argument=arg):
							match arg:
								case COR_Expressions.IdentityRelation():
									return COR_Expressions.EmptyRelation()
				case COR_Expressions.EmptyRelation():
					match arg2:
						case COR_Expressions.EmptyRelation():
							return COR_Expressions.EmptyRelation()
						case COR_Expressions.IdentityRelation():
							return COR_Expressions.EmptyRelation()
						case COR_Expressions.UniversalRelation():
							return COR_Expressions.EmptyRelation()
						case _:
							B = arg2
							return COR_Expressions.EmptyRelation()
							A = arg2
							return COR_Expressions.EmptyRelation()
							C = arg2
							return COR_Expressions.EmptyRelation()
				case COR_Expressions.UniversalRelation():
					match arg2:
						case COR_Expressions.UniversalRelation():
							return COR_Expressions.UniversalRelation()
						case COR_Expressions.EmptyRelation():
							return COR_Expressions.EmptyRelation()
						case COR_Expressions.IdentityRelation():
							return COR_Expressions.IdentityRelation()
						case _:
							A = arg2
							return A
							C = arg2
							return C
							B = arg2
							return B
				case COR_Expressions.Converse(argument=arg):
					match arg:
						case _:
							C = arg
							match arg2:
								case COR_Expressions.IdentityRelation():
									return COR_Expressions.Intersection(COR_Expressions.IdentityRelation(), C)
								case COR_Expressions.UniversalRelation():
									return COR_Expressions.Converse(C)
								case COR_Expressions.EmptyRelation():
									return COR_Expressions.EmptyRelation()
							B = arg
							match arg2:
								case COR_Expressions.IdentityRelation():
									return COR_Expressions.Intersection(B, COR_Expressions.IdentityRelation())
								case COR_Expressions.EmptyRelation():
									return COR_Expressions.EmptyRelation()
								case COR_Expressions.UniversalRelation():
									return COR_Expressions.Converse(B)
							A = arg
							match arg2:
								case COR_Expressions.IdentityRelation():
									return COR_Expressions.Intersection(COR_Expressions.IdentityRelation(), A)
								case COR_Expressions.EmptyRelation():
									return COR_Expressions.EmptyRelation()
								case COR_Expressions.UniversalRelation():
									return COR_Expressions.Converse(A)
				case COR_Expressions.Complement(argument=arg):
					match arg:
						case COR_Expressions.IdentityRelation():
							match arg2:
								case COR_Expressions.IdentityRelation():
									return COR_Expressions.EmptyRelation()
								case COR_Expressions.UniversalRelation():
									return COR_Expressions.Complement(COR_Expressions.IdentityRelation())
								case COR_Expressions.EmptyRelation():
									return COR_Expressions.EmptyRelation()
						case _:
							B = arg
							match arg2:
								case _ if str(B)==str(arg2):
									return COR_Expressions.EmptyRelation()
								case COR_Expressions.UniversalRelation():
									return COR_Expressions.Complement(B)
								case COR_Expressions.EmptyRelation():
									return COR_Expressions.EmptyRelation()
							A = arg
							match arg2:
								case _ if str(A)==str(arg2):
									return COR_Expressions.EmptyRelation()
								case COR_Expressions.EmptyRelation():
									return COR_Expressions.EmptyRelation()
								case COR_Expressions.UniversalRelation():
									return COR_Expressions.Complement(A)
							C = arg
							match arg2:
								case _ if str(C)==str(arg2):
									return COR_Expressions.EmptyRelation()
								case COR_Expressions.UniversalRelation():
									return COR_Expressions.Complement(C)
								case COR_Expressions.EmptyRelation():
									return COR_Expressions.EmptyRelation()
				case _:
					C = arg1
					match arg2:
						case COR_Expressions.UniversalRelation():
							return C
						case _ if str(C)==str(arg2):
							return C
						case COR_Expressions.EmptyRelation():
							return COR_Expressions.EmptyRelation()
						case COR_Expressions.Complement(argument=arg):
							match arg:
								case _ if str(C)==str(arg):
									return COR_Expressions.EmptyRelation()
					B = arg1
					match arg2:
						case _ if str(B)==str(arg2):
							return B
						case COR_Expressions.EmptyRelation():
							return COR_Expressions.EmptyRelation()
						case COR_Expressions.UniversalRelation():
							return B
						case COR_Expressions.Complement(argument=arg):
							match arg:
								case _ if str(B)==str(arg):
									return COR_Expressions.EmptyRelation()
					A = arg1
					match arg2:
						case COR_Expressions.UniversalRelation():
							return A
						case _ if str(A)==str(arg2):
							return A
						case COR_Expressions.EmptyRelation():
							return COR_Expressions.EmptyRelation()
						case COR_Expressions.Complement(argument=arg):
							match arg:
								case _ if str(A)==str(arg):
									return COR_Expressions.EmptyRelation()
		case COR_Expressions.Dagger(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.UniversalRelation():
					match arg2:
						case COR_Expressions.IdentityRelation():
							return COR_Expressions.UniversalRelation()
						case COR_Expressions.UniversalRelation():
							return COR_Expressions.UniversalRelation()
						case COR_Expressions.EmptyRelation():
							return COR_Expressions.UniversalRelation()
						case _:
							A = arg2
							return COR_Expressions.UniversalRelation()
							B = arg2
							return COR_Expressions.UniversalRelation()
							C = arg2
							return COR_Expressions.UniversalRelation()
				case COR_Expressions.EmptyRelation():
					match arg2:
						case COR_Expressions.UniversalRelation():
							return COR_Expressions.UniversalRelation()
						case COR_Expressions.EmptyRelation():
							return COR_Expressions.EmptyRelation()
						case COR_Expressions.Complement(argument=arg):
							match arg:
								case COR_Expressions.IdentityRelation():
									return COR_Expressions.EmptyRelation()
				case COR_Expressions.IdentityRelation():
					match arg2:
						case COR_Expressions.UniversalRelation():
							return COR_Expressions.UniversalRelation()
						case COR_Expressions.Complement(argument=arg):
							match arg:
								case COR_Expressions.IdentityRelation():
									return COR_Expressions.IdentityRelation()
				case COR_Expressions.Complement(argument=arg):
					match arg:
						case COR_Expressions.IdentityRelation():
							match arg2:
								case COR_Expressions.IdentityRelation():
									return COR_Expressions.IdentityRelation()
								case COR_Expressions.EmptyRelation():
									return COR_Expressions.EmptyRelation()
								case _:
									A = arg2
									return A
									B = arg2
									return B
									C = arg2
									return C
						case _:
							B = arg
							match arg2:
								case COR_Expressions.UniversalRelation():
									return COR_Expressions.UniversalRelation()
							C = arg
							match arg2:
								case COR_Expressions.UniversalRelation():
									return COR_Expressions.UniversalRelation()
							A = arg
							match arg2:
								case COR_Expressions.UniversalRelation():
									return COR_Expressions.UniversalRelation()
				case _:
					A = arg1
					match arg2:
						case COR_Expressions.UniversalRelation():
							return COR_Expressions.UniversalRelation()
						case COR_Expressions.Complement(argument=arg):
							match arg:
								case COR_Expressions.IdentityRelation():
									return A
					B = arg1
					match arg2:
						case COR_Expressions.UniversalRelation():
							return COR_Expressions.UniversalRelation()
						case COR_Expressions.Complement(argument=arg):
							match arg:
								case COR_Expressions.IdentityRelation():
									return B
					C = arg1
					match arg2:
						case COR_Expressions.UniversalRelation():
							return COR_Expressions.UniversalRelation()
						case COR_Expressions.Complement(argument=arg):
							match arg:
								case COR_Expressions.IdentityRelation():
									return C

	return expression # The given expression was unable to be simplified