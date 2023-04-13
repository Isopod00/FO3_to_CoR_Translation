import COR_Expressions

def simplify(expression):
	match expression:
		case COR_Expressions.Complement(argument=arg):
			match arg:
				case COR_Expressions.UniversalRelation():
					return COR_Expressions.EmptyRelation()
				case COR_Expressions.EmptyRelation():
					return COR_Expressions.UniversalRelation()
				case COR_Expressions.Complement(argument=arg):
					match arg:
						case COR_Expressions.IdentityRelation:
							return COR_Expressions.IdentityRelation()
						case COR_Expressions.Converse(argument=arg):
							match arg:
								case _:
									B = arg
									return COR_Expressions.Converse(B)
									A = arg
									return COR_Expressions.Converse(A)
									C = arg
									return COR_Expressions.Converse(C)
						case COR_Expressions.Dagger(argument1=arg1, argument2=arg2):
							match arg1:
								case COR_Expressions.EmptyRelation():
									match arg2:
										case COR_Expressions.Converse(argument=arg):
											match arg:
												case _:
													B = arg
													return COR_Expressions.Dagger(COR_Expressions.EmptyRelation(), COR_Expressions.Converse(B))
													C = arg
													return COR_Expressions.Dagger(COR_Expressions.EmptyRelation(), COR_Expressions.Converse(C))
													A = arg
													return COR_Expressions.Dagger(COR_Expressions.EmptyRelation(), COR_Expressions.Converse(A))
										case COR_Expressions.Complement(argument=arg):
											match arg:
												case _:
													C = arg
													return COR_Expressions.Dagger(COR_Expressions.EmptyRelation(), COR_Expressions.Complement(C))
													A = arg
													return COR_Expressions.Dagger(COR_Expressions.EmptyRelation(), COR_Expressions.Complement(A))
													B = arg
													return COR_Expressions.Dagger(COR_Expressions.EmptyRelation(), COR_Expressions.Complement(B))
								case COR_Expressions.IdentityRelation:
									match arg2:
										case COR_Expressions.Complement(argument=arg):
											match arg:
												case _:
													B = arg
													return COR_Expressions.Dagger(COR_Expressions.IdentityRelation(), COR_Expressions.Complement(B))
													C = arg
													return COR_Expressions.Dagger(COR_Expressions.IdentityRelation(), COR_Expressions.Complement(C))
													A = arg
													return COR_Expressions.Dagger(COR_Expressions.IdentityRelation(), COR_Expressions.Complement(A))
										case COR_Expressions.Converse(argument=arg):
											match arg:
												case _:
													B = arg
													return COR_Expressions.Dagger(COR_Expressions.IdentityRelation(), COR_Expressions.Converse(B))
													A = arg
													return COR_Expressions.Dagger(COR_Expressions.IdentityRelation(), COR_Expressions.Converse(A))
													C = arg
													return COR_Expressions.Dagger(COR_Expressions.IdentityRelation(), COR_Expressions.Converse(C))
								case _:
									A = arg1
									match arg2:
										case COR_Expressions.Converse(argument=arg):
											match arg:
												case _ if str(A)==str(arg):
													return COR_Expressions.Dagger(A, COR_Expressions.Converse(A))
												case _:
													B = arg
													return COR_Expressions.Dagger(A, COR_Expressions.Converse(B))
													C = arg
													return COR_Expressions.Dagger(A, COR_Expressions.Converse(C))
										case COR_Expressions.Complement(argument=arg):
											match arg:
												case _ if str(A)==str(arg):
													return COR_Expressions.Dagger(A, COR_Expressions.Complement(A))
												case _:
													C = arg
													return COR_Expressions.Dagger(A, COR_Expressions.Complement(C))
													B = arg
													return COR_Expressions.Dagger(A, COR_Expressions.Complement(B))
									B = arg1
									match arg2:
										case COR_Expressions.Complement(argument=arg):
											match arg:
												case _ if str(B)==str(arg):
													return COR_Expressions.Dagger(B, COR_Expressions.Complement(B))
												case _:
													A = arg
													return COR_Expressions.Dagger(B, COR_Expressions.Complement(A))
													C = arg
													return COR_Expressions.Dagger(B, COR_Expressions.Complement(C))
										case COR_Expressions.Converse(argument=arg):
											match arg:
												case _:
													A = arg
													return COR_Expressions.Dagger(B, COR_Expressions.Converse(A))
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
									A = arg
									return COR_Expressions.Converse(A)
									B = arg
									return COR_Expressions.Converse(B)
									C = arg
									return COR_Expressions.Converse(C)
		case COR_Expressions.Converse(argument=arg):
			match arg:
				case COR_Expressions.UniversalRelation():
					return COR_Expressions.UniversalRelation()
				case COR_Expressions.EmptyRelation():
					return COR_Expressions.EmptyRelation()
				case COR_Expressions.IdentityRelation:
					return COR_Expressions.IdentityRelation()
				case COR_Expressions.Converse(argument=arg):
					match arg:
						case COR_Expressions.Complement(argument=arg):
							match arg:
								case _:
									A = arg
									return COR_Expressions.Complement(A)
									C = arg
									return COR_Expressions.Complement(C)
									B = arg
									return COR_Expressions.Complement(B)
						case _:
							A = arg
							return A
							B = arg
							return B
							C = arg
							return C
				case COR_Expressions.Complement(argument=arg):
					match arg:
						case COR_Expressions.IdentityRelation:
							return COR_Expressions.Complement(COR_Expressions.IdentityRelation())
						case COR_Expressions.Converse(argument=arg):
							match arg:
								case _:
									A = arg
									return COR_Expressions.Complement(A)
									B = arg
									return COR_Expressions.Complement(B)
									C = arg
									return COR_Expressions.Complement(C)
				case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
					match arg1:
						case COR_Expressions.UniversalRelation():
							match arg2:
								case COR_Expressions.Complement(argument=arg):
									match arg:
										case COR_Expressions.IdentityRelation:
											return COR_Expressions.Composition(COR_Expressions.UniversalRelation(), COR_Expressions.Complement(COR_Expressions.IdentityRelation()))
						case _:
							C = arg1
							match arg2:
								case COR_Expressions.Converse(argument=arg):
									match arg:
										case _ if str(C)==str(arg):
											return COR_Expressions.Composition(C, COR_Expressions.Converse(C))
										case _:
											B = arg
											return COR_Expressions.Composition(B, COR_Expressions.Converse(C))
											A = arg
											return COR_Expressions.Composition(A, COR_Expressions.Converse(C))
							B = arg1
							match arg2:
								case COR_Expressions.Converse(argument=arg):
									match arg:
										case _ if str(B)==str(arg):
											return COR_Expressions.Composition(B, COR_Expressions.Converse(B))
										case _:
											C = arg
											return COR_Expressions.Composition(C, COR_Expressions.Converse(B))
											A = arg
											return COR_Expressions.Composition(A, COR_Expressions.Converse(B))
							A = arg1
							match arg2:
								case COR_Expressions.Converse(argument=arg):
									match arg:
										case _ if str(A)==str(arg):
											return COR_Expressions.Composition(A, COR_Expressions.Converse(A))
										case _:
											C = arg
											return COR_Expressions.Composition(C, COR_Expressions.Converse(A))
											B = arg
											return COR_Expressions.Composition(B, COR_Expressions.Converse(A))
				case COR_Expressions.Union(argument1=arg1, argument2=arg2):
					match arg1:
						case _:
							B = arg1
							match arg2:
								case COR_Expressions.Converse(argument=arg):
									match arg:
										case _ if str(B)==str(arg):
											return COR_Expressions.Union(B, COR_Expressions.Converse(B))
										case _:
											A = arg
											return COR_Expressions.Union(A, COR_Expressions.Converse(B))
											C = arg
											return COR_Expressions.Union(C, COR_Expressions.Converse(B))
								case COR_Expressions.Complement(argument=arg):
									match arg:
										case COR_Expressions.IdentityRelation:
											return COR_Expressions.Union(B, COR_Expressions.Complement(COR_Expressions.IdentityRelation()))
							A = arg1
							match arg2:
								case COR_Expressions.Converse(argument=arg):
									match arg:
										case _ if str(A)==str(arg):
											return COR_Expressions.Union(A, COR_Expressions.Converse(A))
										case _:
											C = arg
											return COR_Expressions.Union(C, COR_Expressions.Converse(A))
											B = arg
											return COR_Expressions.Union(B, COR_Expressions.Converse(A))
								case COR_Expressions.Complement(argument=arg):
									match arg:
										case COR_Expressions.IdentityRelation:
											return COR_Expressions.Union(A, COR_Expressions.Complement(COR_Expressions.IdentityRelation()))
							C = arg1
							match arg2:
								case COR_Expressions.Complement(argument=arg):
									match arg:
										case COR_Expressions.IdentityRelation:
											return COR_Expressions.Union(C, COR_Expressions.Complement(COR_Expressions.IdentityRelation()))
								case COR_Expressions.Converse(argument=arg):
									match arg:
										case _ if str(C)==str(arg):
											return COR_Expressions.Union(C, COR_Expressions.Converse(C))
										case _:
											B = arg
											return COR_Expressions.Union(B, COR_Expressions.Converse(C))
											A = arg
											return COR_Expressions.Union(A, COR_Expressions.Converse(C))
				case COR_Expressions.Dagger(argument1=arg1, argument2=arg2):
					match arg1:
						case COR_Expressions.IdentityRelation:
							match arg2:
								case COR_Expressions.EmptyRelation():
									return COR_Expressions.Dagger(COR_Expressions.EmptyRelation(), COR_Expressions.IdentityRelation())
								case COR_Expressions.IdentityRelation:
									return COR_Expressions.Dagger(COR_Expressions.IdentityRelation(), COR_Expressions.IdentityRelation())
						case COR_Expressions.EmptyRelation():
							match arg2:
								case COR_Expressions.IdentityRelation:
									return COR_Expressions.Dagger(COR_Expressions.EmptyRelation(), COR_Expressions.IdentityRelation())
						case _:
							C = arg1
							match arg2:
								case COR_Expressions.Converse(argument=arg):
									match arg:
										case _ if str(C)==str(arg):
											return COR_Expressions.Dagger(C, COR_Expressions.Converse(C))
										case _:
											A = arg
											return COR_Expressions.Dagger(A, COR_Expressions.Converse(C))
											B = arg
											return COR_Expressions.Dagger(B, COR_Expressions.Converse(C))
							A = arg1
							match arg2:
								case COR_Expressions.Converse(argument=arg):
									match arg:
										case _ if str(A)==str(arg):
											return COR_Expressions.Dagger(A, COR_Expressions.Converse(A))
										case _:
											C = arg
											return COR_Expressions.Dagger(C, COR_Expressions.Converse(A))
											B = arg
											return COR_Expressions.Dagger(B, COR_Expressions.Converse(A))
							B = arg1
							match arg2:
								case COR_Expressions.Converse(argument=arg):
									match arg:
										case _ if str(B)==str(arg):
											return COR_Expressions.Dagger(B, COR_Expressions.Converse(B))
										case _:
											C = arg
											return COR_Expressions.Dagger(C, COR_Expressions.Converse(B))
											A = arg
											return COR_Expressions.Dagger(A, COR_Expressions.Converse(B))
				case COR_Expressions.Intersection(argument1=arg1, argument2=arg2):
					match arg1:
						case COR_Expressions.IdentityRelation:
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
								case COR_Expressions.IdentityRelation:
									return COR_Expressions.Intersection(COR_Expressions.IdentityRelation(), A)
							C = arg1
							match arg2:
								case COR_Expressions.IdentityRelation:
									return COR_Expressions.Intersection(COR_Expressions.IdentityRelation(), C)
							B = arg1
							match arg2:
								case COR_Expressions.IdentityRelation:
									return COR_Expressions.Intersection(COR_Expressions.IdentityRelation(), B)
		case COR_Expressions.Union(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.UniversalRelation():
					match arg2:
						case COR_Expressions.Converse(argument=arg):
							match arg:
								case COR_Expressions.Complement(argument=arg):
									match arg:
										case _:
											A = arg
											return COR_Expressions.UniversalRelation()
											C = arg
											return COR_Expressions.UniversalRelation()
											B = arg
											return COR_Expressions.UniversalRelation()
								case _:
									B = arg
									return COR_Expressions.UniversalRelation()
									A = arg
									return COR_Expressions.UniversalRelation()
									C = arg
									return COR_Expressions.UniversalRelation()
						case COR_Expressions.Complement(argument=arg):
							match arg:
								case COR_Expressions.IdentityRelation:
									return COR_Expressions.UniversalRelation()
								case COR_Expressions.Converse(argument=arg):
									match arg:
										case _:
											A = arg
											return COR_Expressions.UniversalRelation()
											B = arg
											return COR_Expressions.UniversalRelation()
											C = arg
											return COR_Expressions.UniversalRelation()
								case _:
									A = arg
									return COR_Expressions.UniversalRelation()
									C = arg
									return COR_Expressions.UniversalRelation()
									B = arg
									return COR_Expressions.UniversalRelation()
						case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
							match arg1:
								case COR_Expressions.UniversalRelation():
									match arg2:
										case COR_Expressions.Converse(argument=arg):
											match arg:
												case _:
													C = arg
													return COR_Expressions.UniversalRelation()
													B = arg
													return COR_Expressions.UniversalRelation()
													A = arg
													return COR_Expressions.UniversalRelation()
										case COR_Expressions.Complement(argument=arg):
											match arg:
												case COR_Expressions.IdentityRelation:
													return COR_Expressions.UniversalRelation()
												case _:
													A = arg
													return COR_Expressions.UniversalRelation()
													B = arg
													return COR_Expressions.UniversalRelation()
													C = arg
													return COR_Expressions.UniversalRelation()
								case _:
									A = arg1
									match arg2:
										case COR_Expressions.Complement(argument=arg):
											match arg:
												case COR_Expressions.IdentityRelation:
													return COR_Expressions.UniversalRelation()
												case _ if str(A)==str(arg):
													return COR_Expressions.UniversalRelation()
												case _:
													C = arg
													return COR_Expressions.UniversalRelation()
													B = arg
													return COR_Expressions.UniversalRelation()
										case COR_Expressions.Converse(argument=arg):
											match arg:
												case _ if str(A)==str(arg):
													return COR_Expressions.UniversalRelation()
												case _:
													C = arg
													return COR_Expressions.UniversalRelation()
													B = arg
													return COR_Expressions.UniversalRelation()
									B = arg1
									match arg2:
										case COR_Expressions.Complement(argument=arg):
											match arg:
												case _ if str(B)==str(arg):
													return COR_Expressions.UniversalRelation()
												case COR_Expressions.IdentityRelation:
													return COR_Expressions.UniversalRelation()
												case _:
													A = arg
													return COR_Expressions.UniversalRelation()
													C = arg
													return COR_Expressions.UniversalRelation()
										case COR_Expressions.Converse(argument=arg):
											match arg:
												case _ if str(B)==str(arg):
													return COR_Expressions.UniversalRelation()
												case _:
													A = arg
													return COR_Expressions.UniversalRelation()
													C = arg
													return COR_Expressions.UniversalRelation()
									C = arg1
									match arg2:
										case COR_Expressions.Complement(argument=arg):
											match arg:
												case COR_Expressions.IdentityRelation:
													return COR_Expressions.UniversalRelation()
												case _ if str(C)==str(arg):
													return COR_Expressions.UniversalRelation()
												case _:
													A = arg
													return COR_Expressions.UniversalRelation()
													B = arg
													return COR_Expressions.UniversalRelation()
										case COR_Expressions.Converse(argument=arg):
											match arg:
												case _ if str(C)==str(arg):
													return COR_Expressions.UniversalRelation()
												case _:
													B = arg
													return COR_Expressions.UniversalRelation()
													A = arg
													return COR_Expressions.UniversalRelation()
						case COR_Expressions.Union(argument1=arg1, argument2=arg2):
							match arg1:
								case COR_Expressions.IdentityRelation:
									match arg2:
										case COR_Expressions.Converse(argument=arg):
											match arg:
												case _:
													B = arg
													return COR_Expressions.UniversalRelation()
													A = arg
													return COR_Expressions.UniversalRelation()
													C = arg
													return COR_Expressions.UniversalRelation()
										case COR_Expressions.Complement(argument=arg):
											match arg:
												case _:
													B = arg
													return COR_Expressions.UniversalRelation()
													A = arg
													return COR_Expressions.UniversalRelation()
													C = arg
													return COR_Expressions.UniversalRelation()
								case _:
									C = arg1
									match arg2:
										case COR_Expressions.Complement(argument=arg):
											match arg:
												case COR_Expressions.IdentityRelation:
													return COR_Expressions.UniversalRelation()
												case _:
													A = arg
													return COR_Expressions.UniversalRelation()
													B = arg
													return COR_Expressions.UniversalRelation()
										case COR_Expressions.Converse(argument=arg):
											match arg:
												case _ if str(C)==str(arg):
													return COR_Expressions.UniversalRelation()
												case _:
													B = arg
													return COR_Expressions.UniversalRelation()
													A = arg
													return COR_Expressions.UniversalRelation()
									A = arg1
									match arg2:
										case COR_Expressions.Complement(argument=arg):
											match arg:
												case COR_Expressions.IdentityRelation:
													return COR_Expressions.UniversalRelation()
												case _:
													C = arg
													return COR_Expressions.UniversalRelation()
													B = arg
													return COR_Expressions.UniversalRelation()
										case COR_Expressions.Converse(argument=arg):
											match arg:
												case _ if str(A)==str(arg):
													return COR_Expressions.UniversalRelation()
												case _:
													B = arg
													return COR_Expressions.UniversalRelation()
													C = arg
													return COR_Expressions.UniversalRelation()
									B = arg1
									match arg2:
										case COR_Expressions.Converse(argument=arg):
											match arg:
												case _ if str(B)==str(arg):
													return COR_Expressions.UniversalRelation()
												case _:
													A = arg
													return COR_Expressions.UniversalRelation()
													C = arg
													return COR_Expressions.UniversalRelation()
										case COR_Expressions.Complement(argument=arg):
											match arg:
												case COR_Expressions.IdentityRelation:
													return COR_Expressions.UniversalRelation()
												case _:
													C = arg
													return COR_Expressions.UniversalRelation()
													A = arg
													return COR_Expressions.UniversalRelation()
						case COR_Expressions.Dagger(argument1=arg1, argument2=arg2):
							match arg1:
								case COR_Expressions.IdentityRelation:
									match arg2:
										case COR_Expressions.Converse(argument=arg):
											match arg:
												case _:
													B = arg
													return COR_Expressions.UniversalRelation()
													C = arg
													return COR_Expressions.UniversalRelation()
													A = arg
													return COR_Expressions.UniversalRelation()
										case COR_Expressions.Complement(argument=arg):
											match arg:
												case _:
													C = arg
													return COR_Expressions.UniversalRelation()
													A = arg
													return COR_Expressions.UniversalRelation()
													B = arg
													return COR_Expressions.UniversalRelation()
								case COR_Expressions.EmptyRelation():
									match arg2:
										case COR_Expressions.Converse(argument=arg):
											match arg:
												case _:
													C = arg
													return COR_Expressions.UniversalRelation()
													A = arg
													return COR_Expressions.UniversalRelation()
													B = arg
													return COR_Expressions.UniversalRelation()
										case COR_Expressions.Complement(argument=arg):
											match arg:
												case _:
													A = arg
													return COR_Expressions.UniversalRelation()
													C = arg
													return COR_Expressions.UniversalRelation()
													B = arg
													return COR_Expressions.UniversalRelation()
								case _:
									C = arg1
									match arg2:
										case COR_Expressions.Converse(argument=arg):
											match arg:
												case _ if str(C)==str(arg):
													return COR_Expressions.UniversalRelation()
												case _:
													B = arg
													return COR_Expressions.UniversalRelation()
													A = arg
													return COR_Expressions.UniversalRelation()
										case COR_Expressions.Complement(argument=arg):
											match arg:
												case _ if str(C)==str(arg):
													return COR_Expressions.UniversalRelation()
												case _:
													A = arg
													return COR_Expressions.UniversalRelation()
													B = arg
													return COR_Expressions.UniversalRelation()
									B = arg1
									match arg2:
										case COR_Expressions.Converse(argument=arg):
											match arg:
												case _ if str(B)==str(arg):
													return COR_Expressions.UniversalRelation()
												case _:
													C = arg
													return COR_Expressions.UniversalRelation()
													A = arg
													return COR_Expressions.UniversalRelation()
										case COR_Expressions.Complement(argument=arg):
											match arg:
												case _ if str(B)==str(arg):
													return COR_Expressions.UniversalRelation()
												case _:
													C = arg
													return COR_Expressions.UniversalRelation()
													A = arg
													return COR_Expressions.UniversalRelation()
									A = arg1
									match arg2:
										case COR_Expressions.Converse(argument=arg):
											match arg:
												case _ if str(A)==str(arg):
													return COR_Expressions.UniversalRelation()
												case _:
													B = arg
													return COR_Expressions.UniversalRelation()
													C = arg
													return COR_Expressions.UniversalRelation()
										case COR_Expressions.Complement(argument=arg):
											match arg:
												case _ if str(A)==str(arg):
													return COR_Expressions.UniversalRelation()
												case _:
													B = arg
													return COR_Expressions.UniversalRelation()
													C = arg
													return COR_Expressions.UniversalRelation()
						case COR_Expressions.IdentityRelation:
							return COR_Expressions.UniversalRelation()
						case COR_Expressions.UniversalRelation():
							return COR_Expressions.UniversalRelation()
						case COR_Expressions.EmptyRelation():
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
						case COR_Expressions.Converse(argument=arg):
							match arg:
								case COR_Expressions.Complement(argument=arg):
									match arg:
										case _:
											A = arg
											return COR_Expressions.Converse(COR_Expressions.Complement(A))
											C = arg
											return COR_Expressions.Converse(COR_Expressions.Complement(C))
											B = arg
											return COR_Expressions.Complement(COR_Expressions.Converse(B))
								case _:
									A = arg
									return COR_Expressions.Converse(A)
									B = arg
									return COR_Expressions.Converse(B)
									C = arg
									return COR_Expressions.Converse(C)
						case COR_Expressions.Complement(argument=arg):
							match arg:
								case COR_Expressions.IdentityRelation:
									return COR_Expressions.Complement(COR_Expressions.IdentityRelation())
								case COR_Expressions.Converse(argument=arg):
									match arg:
										case _:
											C = arg
											return COR_Expressions.Converse(COR_Expressions.Complement(C))
											A = arg
											return COR_Expressions.Converse(COR_Expressions.Complement(A))
											B = arg
											return COR_Expressions.Complement(COR_Expressions.Converse(B))
								case _:
									A = arg
									return COR_Expressions.Complement(A)
									B = arg
									return COR_Expressions.Complement(B)
									C = arg
									return COR_Expressions.Complement(C)
						case COR_Expressions.Dagger(argument1=arg1, argument2=arg2):
							match arg1:
								case COR_Expressions.EmptyRelation():
									match arg2:
										case COR_Expressions.Converse(argument=arg):
											match arg:
												case _:
													B = arg
													return COR_Expressions.Dagger(COR_Expressions.EmptyRelation(), COR_Expressions.Converse(B))
													A = arg
													return COR_Expressions.Dagger(COR_Expressions.EmptyRelation(), COR_Expressions.Converse(A))
													C = arg
													return COR_Expressions.Dagger(COR_Expressions.EmptyRelation(), COR_Expressions.Converse(C))
										case COR_Expressions.Complement(argument=arg):
											match arg:
												case _:
													B = arg
													return COR_Expressions.Dagger(COR_Expressions.EmptyRelation(), COR_Expressions.Complement(B))
													A = arg
													return COR_Expressions.Dagger(COR_Expressions.EmptyRelation(), COR_Expressions.Complement(A))
													C = arg
													return COR_Expressions.Dagger(COR_Expressions.EmptyRelation(), COR_Expressions.Complement(C))
								case COR_Expressions.IdentityRelation:
									match arg2:
										case COR_Expressions.Complement(argument=arg):
											match arg:
												case _:
													C = arg
													return COR_Expressions.Dagger(COR_Expressions.IdentityRelation(), COR_Expressions.Complement(C))
													B = arg
													return COR_Expressions.Dagger(COR_Expressions.IdentityRelation(), COR_Expressions.Complement(B))
													A = arg
													return COR_Expressions.Dagger(COR_Expressions.IdentityRelation(), COR_Expressions.Complement(A))
										case COR_Expressions.Converse(argument=arg):
											match arg:
												case _:
													C = arg
													return COR_Expressions.Dagger(COR_Expressions.IdentityRelation(), COR_Expressions.Converse(C))
													A = arg
													return COR_Expressions.Dagger(COR_Expressions.IdentityRelation(), COR_Expressions.Converse(A))
													B = arg
													return COR_Expressions.Dagger(COR_Expressions.IdentityRelation(), COR_Expressions.Converse(B))
								case _:
									C = arg1
									match arg2:
										case COR_Expressions.Complement(argument=arg):
											match arg:
												case _ if str(C)==str(arg):
													return COR_Expressions.Dagger(C, COR_Expressions.Complement(C))
												case _:
													A = arg
													return COR_Expressions.Dagger(C, COR_Expressions.Complement(A))
													B = arg
													return COR_Expressions.Dagger(C, COR_Expressions.Complement(B))
										case COR_Expressions.Converse(argument=arg):
											match arg:
												case _ if str(C)==str(arg):
													return COR_Expressions.Dagger(C, COR_Expressions.Converse(C))
												case _:
													A = arg
													return COR_Expressions.Dagger(C, COR_Expressions.Converse(A))
													B = arg
													return COR_Expressions.Dagger(C, COR_Expressions.Converse(B))
									A = arg1
									match arg2:
										case COR_Expressions.Complement(argument=arg):
											match arg:
												case _ if str(A)==str(arg):
													return COR_Expressions.Dagger(A, COR_Expressions.Complement(A))
												case _:
													B = arg
													return COR_Expressions.Dagger(A, COR_Expressions.Complement(B))
													C = arg
													return COR_Expressions.Dagger(A, COR_Expressions.Complement(C))
										case COR_Expressions.Converse(argument=arg):
											match arg:
												case _ if str(A)==str(arg):
													return COR_Expressions.Dagger(A, COR_Expressions.Converse(A))
												case _:
													C = arg
													return COR_Expressions.Dagger(A, COR_Expressions.Converse(C))
													B = arg
													return COR_Expressions.Dagger(A, COR_Expressions.Converse(B))
									B = arg1
									match arg2:
										case COR_Expressions.Complement(argument=arg):
											match arg:
												case _ if str(B)==str(arg):
													return COR_Expressions.Dagger(B, COR_Expressions.Complement(B))
												case _:
													C = arg
													return COR_Expressions.Dagger(B, COR_Expressions.Complement(C))
													A = arg
													return COR_Expressions.Dagger(B, COR_Expressions.Complement(A))
										case COR_Expressions.Converse(argument=arg):
											match arg:
												case _ if str(B)==str(arg):
													return COR_Expressions.Dagger(B, COR_Expressions.Converse(B))
												case _:
													A = arg
													return COR_Expressions.Dagger(B, COR_Expressions.Converse(A))
													C = arg
													return COR_Expressions.Dagger(B, COR_Expressions.Converse(C))
						case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
							match arg1:
								case COR_Expressions.UniversalRelation():
									match arg2:
										case COR_Expressions.Converse(argument=arg):
											match arg:
												case _:
													B = arg
													return COR_Expressions.Composition(COR_Expressions.UniversalRelation(), COR_Expressions.Converse(B))
													A = arg
													return COR_Expressions.Composition(COR_Expressions.UniversalRelation(), COR_Expressions.Converse(A))
													C = arg
													return COR_Expressions.Composition(COR_Expressions.UniversalRelation(), COR_Expressions.Converse(C))
										case COR_Expressions.Complement(argument=arg):
											match arg:
												case COR_Expressions.IdentityRelation:
													return COR_Expressions.Composition(COR_Expressions.UniversalRelation(), COR_Expressions.Complement(COR_Expressions.IdentityRelation()))
												case _:
													C = arg
													return COR_Expressions.Composition(COR_Expressions.UniversalRelation(), COR_Expressions.Complement(C))
													A = arg
													return COR_Expressions.Composition(COR_Expressions.UniversalRelation(), COR_Expressions.Complement(A))
													B = arg
													return COR_Expressions.Composition(COR_Expressions.UniversalRelation(), COR_Expressions.Complement(B))
								case _:
									A = arg1
									match arg2:
										case COR_Expressions.Complement(argument=arg):
											match arg:
												case _ if str(A)==str(arg):
													return COR_Expressions.Composition(A, COR_Expressions.Complement(A))
												case COR_Expressions.IdentityRelation:
													return COR_Expressions.Composition(A, COR_Expressions.Complement(COR_Expressions.IdentityRelation()))
												case _:
													C = arg
													return COR_Expressions.Composition(A, COR_Expressions.Complement(C))
													B = arg
													return COR_Expressions.Composition(A, COR_Expressions.Complement(B))
										case COR_Expressions.Converse(argument=arg):
											match arg:
												case _ if str(A)==str(arg):
													return COR_Expressions.Composition(A, COR_Expressions.Converse(A))
												case _:
													C = arg
													return COR_Expressions.Composition(A, COR_Expressions.Converse(C))
													B = arg
													return COR_Expressions.Composition(A, COR_Expressions.Converse(B))
									C = arg1
									match arg2:
										case COR_Expressions.Complement(argument=arg):
											match arg:
												case COR_Expressions.IdentityRelation:
													return COR_Expressions.Composition(C, COR_Expressions.Complement(COR_Expressions.IdentityRelation()))
												case _ if str(C)==str(arg):
													return COR_Expressions.Composition(C, COR_Expressions.Complement(C))
												case _:
													A = arg
													return COR_Expressions.Composition(C, COR_Expressions.Complement(A))
													B = arg
													return COR_Expressions.Composition(C, COR_Expressions.Complement(B))
										case COR_Expressions.Converse(argument=arg):
											match arg:
												case _ if str(C)==str(arg):
													return COR_Expressions.Composition(C, COR_Expressions.Converse(C))
												case _:
													B = arg
													return COR_Expressions.Composition(C, COR_Expressions.Converse(B))
													A = arg
													return COR_Expressions.Composition(C, COR_Expressions.Converse(A))
									B = arg1
									match arg2:
										case COR_Expressions.Complement(argument=arg):
											match arg:
												case _ if str(B)==str(arg):
													return COR_Expressions.Composition(B, COR_Expressions.Complement(B))
												case COR_Expressions.IdentityRelation:
													return COR_Expressions.Composition(B, COR_Expressions.Complement(COR_Expressions.IdentityRelation()))
												case _:
													C = arg
													return COR_Expressions.Composition(B, COR_Expressions.Complement(C))
													A = arg
													return COR_Expressions.Composition(B, COR_Expressions.Complement(A))
										case COR_Expressions.Converse(argument=arg):
											match arg:
												case _ if str(B)==str(arg):
													return COR_Expressions.Composition(B, COR_Expressions.Converse(B))
												case _:
													A = arg
													return COR_Expressions.Composition(B, COR_Expressions.Converse(A))
													C = arg
													return COR_Expressions.Composition(B, COR_Expressions.Converse(C))
						case COR_Expressions.Union(argument1=arg1, argument2=arg2):
							match arg1:
								case COR_Expressions.IdentityRelation:
									match arg2:
										case COR_Expressions.Converse(argument=arg):
											match arg:
												case _:
													B = arg
													return COR_Expressions.Union(COR_Expressions.IdentityRelation(), COR_Expressions.Converse(B))
													A = arg
													return COR_Expressions.Union(COR_Expressions.IdentityRelation(), COR_Expressions.Converse(A))
													C = arg
													return COR_Expressions.Union(COR_Expressions.IdentityRelation(), COR_Expressions.Converse(C))
										case COR_Expressions.Complement(argument=arg):
											match arg:
												case _:
													C = arg
													return COR_Expressions.Union(COR_Expressions.IdentityRelation(), COR_Expressions.Complement(C))
													B = arg
													return COR_Expressions.Union(COR_Expressions.IdentityRelation(), COR_Expressions.Complement(B))
													A = arg
													return COR_Expressions.Union(COR_Expressions.IdentityRelation(), COR_Expressions.Complement(A))
								case _:
									A = arg1
									match arg2:
										case COR_Expressions.Complement(argument=arg):
											match arg:
												case COR_Expressions.IdentityRelation:
													return COR_Expressions.Union(A, COR_Expressions.Complement(COR_Expressions.IdentityRelation()))
												case _:
													B = arg
													return COR_Expressions.Union(A, COR_Expressions.Complement(B))
													C = arg
													return COR_Expressions.Union(A, COR_Expressions.Complement(C))
										case COR_Expressions.Converse(argument=arg):
											match arg:
												case _ if str(A)==str(arg):
													return COR_Expressions.Union(A, COR_Expressions.Converse(A))
												case _:
													C = arg
													return COR_Expressions.Union(A, COR_Expressions.Converse(C))
													B = arg
													return COR_Expressions.Union(A, COR_Expressions.Converse(B))
									C = arg1
									match arg2:
										case COR_Expressions.Converse(argument=arg):
											match arg:
												case _ if str(C)==str(arg):
													return COR_Expressions.Union(C, COR_Expressions.Converse(C))
												case _:
													B = arg
													return COR_Expressions.Union(C, COR_Expressions.Converse(B))
													A = arg
													return COR_Expressions.Union(C, COR_Expressions.Converse(A))
										case COR_Expressions.Complement(argument=arg):
											match arg:
												case COR_Expressions.IdentityRelation:
													return COR_Expressions.Union(C, COR_Expressions.Complement(COR_Expressions.IdentityRelation()))
												case _:
													B = arg
													return COR_Expressions.Union(C, COR_Expressions.Complement(B))
													A = arg
													return COR_Expressions.Union(C, COR_Expressions.Complement(A))
									B = arg1
									match arg2:
										case COR_Expressions.Complement(argument=arg):
											match arg:
												case COR_Expressions.IdentityRelation:
													return COR_Expressions.Union(B, COR_Expressions.Complement(COR_Expressions.IdentityRelation()))
												case _:
													A = arg
													return COR_Expressions.Union(B, COR_Expressions.Complement(A))
													C = arg
													return COR_Expressions.Union(B, COR_Expressions.Complement(C))
										case COR_Expressions.Converse(argument=arg):
											match arg:
												case _ if str(B)==str(arg):
													return COR_Expressions.Union(B, COR_Expressions.Converse(B))
												case _:
													C = arg
													return COR_Expressions.Union(B, COR_Expressions.Converse(C))
													A = arg
													return COR_Expressions.Union(B, COR_Expressions.Converse(A))
						case COR_Expressions.IdentityRelation:
							return COR_Expressions.IdentityRelation()
						case COR_Expressions.EmptyRelation():
							return COR_Expressions.EmptyRelation()
						case COR_Expressions.UniversalRelation():
							return COR_Expressions.UniversalRelation()
						case _:
							C = arg2
							return C
							A = arg2
							return A
							B = arg2
							return B
				case COR_Expressions.IdentityRelation:
					match arg2:
						case COR_Expressions.Complement(argument=arg):
							match arg:
								case COR_Expressions.IdentityRelation:
									return COR_Expressions.UniversalRelation()
						case COR_Expressions.Union(argument1=arg1, argument2=arg2):
							match arg1:
								case COR_Expressions.IdentityRelation:
									match arg2:
										case COR_Expressions.Complement(argument=arg):
											match arg:
												case _:
													B = arg
													return COR_Expressions.Union(COR_Expressions.IdentityRelation(), COR_Expressions.Complement(B))
													A = arg
													return COR_Expressions.Union(COR_Expressions.IdentityRelation(), COR_Expressions.Complement(A))
													C = arg
													return COR_Expressions.Union(COR_Expressions.IdentityRelation(), COR_Expressions.Complement(C))
										case COR_Expressions.Converse(argument=arg):
											match arg:
												case _:
													B = arg
													return COR_Expressions.Union(COR_Expressions.IdentityRelation(), COR_Expressions.Converse(B))
													C = arg
													return COR_Expressions.Union(COR_Expressions.IdentityRelation(), COR_Expressions.Converse(C))
													A = arg
													return COR_Expressions.Union(COR_Expressions.IdentityRelation(), COR_Expressions.Converse(A))
								case _:
									A = arg1
									match arg2:
										case COR_Expressions.Complement(argument=arg):
											match arg:
												case COR_Expressions.IdentityRelation:
													return COR_Expressions.UniversalRelation()
									C = arg1
									match arg2:
										case COR_Expressions.Complement(argument=arg):
											match arg:
												case COR_Expressions.IdentityRelation:
													return COR_Expressions.UniversalRelation()
									B = arg1
									match arg2:
										case COR_Expressions.Complement(argument=arg):
											match arg:
												case COR_Expressions.IdentityRelation:
													return COR_Expressions.UniversalRelation()
						case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
							match arg1:
								case COR_Expressions.UniversalRelation():
									match arg2:
										case COR_Expressions.Complement(argument=arg):
											match arg:
												case COR_Expressions.IdentityRelation:
													return COR_Expressions.UniversalRelation()
						case COR_Expressions.UniversalRelation():
							return COR_Expressions.UniversalRelation()
						case COR_Expressions.EmptyRelation():
							return COR_Expressions.IdentityRelation()
						case COR_Expressions.IdentityRelation:
							return COR_Expressions.IdentityRelation()
				case COR_Expressions.Complement(argument=arg):
					match arg:
						case COR_Expressions.IdentityRelation:
							match arg2:
								case COR_Expressions.Complement(argument=arg):
									match arg:
										case COR_Expressions.IdentityRelation:
											return COR_Expressions.Complement(COR_Expressions.IdentityRelation())
								case COR_Expressions.Converse(argument=arg):
									match arg:
										case _:
											C = arg
											return COR_Expressions.Union(C, COR_Expressions.Complement(COR_Expressions.IdentityRelation()))
											B = arg
											return COR_Expressions.Union(B, COR_Expressions.Complement(COR_Expressions.IdentityRelation()))
											A = arg
											return COR_Expressions.Union(A, COR_Expressions.Complement(COR_Expressions.IdentityRelation()))
								case COR_Expressions.IdentityRelation:
									return COR_Expressions.UniversalRelation()
								case COR_Expressions.UniversalRelation():
									return COR_Expressions.UniversalRelation()
								case COR_Expressions.EmptyRelation():
									return COR_Expressions.Complement(COR_Expressions.IdentityRelation())
						case _:
							B = arg
							match arg2:
								case COR_Expressions.Complement(argument=arg):
									match arg:
										case _ if str(B)==str(arg):
											return COR_Expressions.Complement(B)
								case COR_Expressions.UniversalRelation():
									return COR_Expressions.UniversalRelation()
								case _ if str(B)==str(arg2):
									return COR_Expressions.UniversalRelation()
								case COR_Expressions.EmptyRelation():
									return COR_Expressions.Complement(B)
							C = arg
							match arg2:
								case COR_Expressions.Complement(argument=arg):
									match arg:
										case _ if str(C)==str(arg):
											return COR_Expressions.Complement(C)
								case COR_Expressions.EmptyRelation():
									return COR_Expressions.Complement(C)
								case _ if str(C)==str(arg2):
									return COR_Expressions.UniversalRelation()
								case COR_Expressions.UniversalRelation():
									return COR_Expressions.UniversalRelation()
							A = arg
							match arg2:
								case COR_Expressions.Complement(argument=arg):
									match arg:
										case _ if str(A)==str(arg):
											return COR_Expressions.Complement(A)
								case _ if str(A)==str(arg2):
									return COR_Expressions.UniversalRelation()
								case COR_Expressions.EmptyRelation():
									return COR_Expressions.Complement(A)
								case COR_Expressions.UniversalRelation():
									return COR_Expressions.UniversalRelation()
				case COR_Expressions.Converse(argument=arg):
					match arg:
						case _:
							B = arg
							match arg2:
								case COR_Expressions.Complement(argument=arg):
									match arg:
										case COR_Expressions.IdentityRelation:
											return COR_Expressions.Union(B, COR_Expressions.Complement(COR_Expressions.IdentityRelation()))
								case COR_Expressions.Converse(argument=arg):
									match arg:
										case _ if str(B)==str(arg):
											return COR_Expressions.Converse(B)
								case COR_Expressions.UniversalRelation():
									return COR_Expressions.UniversalRelation()
								case COR_Expressions.EmptyRelation():
									return COR_Expressions.Converse(B)
							C = arg
							match arg2:
								case COR_Expressions.Converse(argument=arg):
									match arg:
										case _ if str(C)==str(arg):
											return COR_Expressions.Converse(C)
								case COR_Expressions.Complement(argument=arg):
									match arg:
										case COR_Expressions.IdentityRelation:
											return COR_Expressions.Union(C, COR_Expressions.Complement(COR_Expressions.IdentityRelation()))
								case COR_Expressions.UniversalRelation():
									return COR_Expressions.UniversalRelation()
								case COR_Expressions.EmptyRelation():
									return COR_Expressions.Converse(C)
							A = arg
							match arg2:
								case COR_Expressions.Converse(argument=arg):
									match arg:
										case _ if str(A)==str(arg):
											return COR_Expressions.Converse(A)
								case COR_Expressions.Complement(argument=arg):
									match arg:
										case COR_Expressions.IdentityRelation:
											return COR_Expressions.Union(A, COR_Expressions.Complement(COR_Expressions.IdentityRelation()))
								case COR_Expressions.UniversalRelation():
									return COR_Expressions.UniversalRelation()
								case COR_Expressions.EmptyRelation():
									return COR_Expressions.Converse(A)
				case _:
					A = arg1
					match arg2:
						case COR_Expressions.Complement(argument=arg):
							match arg:
								case _ if str(A)==str(arg):
									return COR_Expressions.UniversalRelation()
						case COR_Expressions.Union(argument1=arg1, argument2=arg2):
							match arg1:
								case _ if str(A)==str(arg1):
									match arg2:
										case COR_Expressions.Complement(argument=arg):
											match arg:
												case COR_Expressions.IdentityRelation:
													return COR_Expressions.Union(A, COR_Expressions.Complement(COR_Expressions.IdentityRelation()))
												case _:
													C = arg
													return COR_Expressions.Union(A, COR_Expressions.Complement(C))
													B = arg
													return COR_Expressions.Union(A, COR_Expressions.Complement(B))
										case COR_Expressions.Converse(argument=arg):
											match arg:
												case _ if str(A)==str(arg):
													return COR_Expressions.Union(A, COR_Expressions.Converse(A))
												case _:
													B = arg
													return COR_Expressions.Union(A, COR_Expressions.Converse(B))
													C = arg
													return COR_Expressions.Union(A, COR_Expressions.Converse(C))
								case COR_Expressions.IdentityRelation:
									match arg2:
										case COR_Expressions.Complement(argument=arg):
											match arg:
												case _ if str(A)==str(arg):
													return COR_Expressions.UniversalRelation()
								case _:
									B = arg1
									match arg2:
										case COR_Expressions.Complement(argument=arg):
											match arg:
												case _ if str(A)==str(arg):
													return COR_Expressions.UniversalRelation()
									C = arg1
									match arg2:
										case COR_Expressions.Complement(argument=arg):
											match arg:
												case _ if str(A)==str(arg):
													return COR_Expressions.UniversalRelation()
						case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
							match arg1:
								case COR_Expressions.UniversalRelation():
									match arg2:
										case COR_Expressions.Complement(argument=arg):
											match arg:
												case _ if str(A)==str(arg):
													return COR_Expressions.UniversalRelation()
						case COR_Expressions.Dagger(argument1=arg1, argument2=arg2):
							match arg1:
								case COR_Expressions.EmptyRelation():
									match arg2:
										case COR_Expressions.Union(argument1=arg1, argument2=arg2):
											match arg1:
												case _ if str(A)==str(arg1):
													match arg2:
														case COR_Expressions.Complement(argument=arg):
															match arg:
																case COR_Expressions.IdentityRelation:
																	return COR_Expressions.Dagger(A, COR_Expressions.Union(A, COR_Expressions.Complement(COR_Expressions.IdentityRelation())))
												case _:
													B = arg1
													match arg2:
														case COR_Expressions.Complement(argument=arg):
															match arg:
																case COR_Expressions.IdentityRelation:
																	return COR_Expressions.Dagger(A, COR_Expressions.Union(B, COR_Expressions.Complement(COR_Expressions.IdentityRelation())))
						case _ if str(A)==str(arg2):
							return A
						case COR_Expressions.UniversalRelation():
							return COR_Expressions.UniversalRelation()
						case COR_Expressions.EmptyRelation():
							return A
					C = arg1
					match arg2:
						case COR_Expressions.Complement(argument=arg):
							match arg:
								case _ if str(C)==str(arg):
									return COR_Expressions.UniversalRelation()
						case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
							match arg1:
								case COR_Expressions.UniversalRelation():
									match arg2:
										case COR_Expressions.Complement(argument=arg):
											match arg:
												case _ if str(C)==str(arg):
													return COR_Expressions.UniversalRelation()
						case COR_Expressions.Union(argument1=arg1, argument2=arg2):
							match arg1:
								case _ if str(C)==str(arg1):
									match arg2:
										case COR_Expressions.Complement(argument=arg):
											match arg:
												case COR_Expressions.IdentityRelation:
													return COR_Expressions.Union(C, COR_Expressions.Complement(COR_Expressions.IdentityRelation()))
												case _:
													B = arg
													return COR_Expressions.Union(C, COR_Expressions.Complement(B))
													A = arg
													return COR_Expressions.Union(C, COR_Expressions.Complement(A))
										case COR_Expressions.Converse(argument=arg):
											match arg:
												case _ if str(C)==str(arg):
													return COR_Expressions.Union(C, COR_Expressions.Converse(C))
												case _:
													B = arg
													return COR_Expressions.Union(C, COR_Expressions.Converse(B))
													A = arg
													return COR_Expressions.Union(C, COR_Expressions.Converse(A))
								case COR_Expressions.IdentityRelation:
									match arg2:
										case COR_Expressions.Complement(argument=arg):
											match arg:
												case _ if str(C)==str(arg):
													return COR_Expressions.UniversalRelation()
								case _:
									B = arg1
									match arg2:
										case COR_Expressions.Complement(argument=arg):
											match arg:
												case _ if str(C)==str(arg):
													return COR_Expressions.UniversalRelation()
									A = arg1
									match arg2:
										case COR_Expressions.Complement(argument=arg):
											match arg:
												case _ if str(C)==str(arg):
													return COR_Expressions.UniversalRelation()
						case COR_Expressions.UniversalRelation():
							return COR_Expressions.UniversalRelation()
						case _ if str(C)==str(arg2):
							return C
						case COR_Expressions.EmptyRelation():
							return C
					B = arg1
					match arg2:
						case COR_Expressions.Complement(argument=arg):
							match arg:
								case _ if str(B)==str(arg):
									return COR_Expressions.UniversalRelation()
						case COR_Expressions.Union(argument1=arg1, argument2=arg2):
							match arg1:
								case _ if str(B)==str(arg1):
									match arg2:
										case COR_Expressions.Converse(argument=arg):
											match arg:
												case _ if str(B)==str(arg):
													return COR_Expressions.Union(B, COR_Expressions.Converse(B))
												case _:
													A = arg
													return COR_Expressions.Union(B, COR_Expressions.Converse(A))
													C = arg
													return COR_Expressions.Union(B, COR_Expressions.Converse(C))
										case COR_Expressions.Complement(argument=arg):
											match arg:
												case COR_Expressions.IdentityRelation:
													return COR_Expressions.Union(B, COR_Expressions.Complement(COR_Expressions.IdentityRelation()))
												case _:
													A = arg
													return COR_Expressions.Union(B, COR_Expressions.Complement(A))
													C = arg
													return COR_Expressions.Union(B, COR_Expressions.Complement(C))
								case COR_Expressions.IdentityRelation:
									match arg2:
										case COR_Expressions.Complement(argument=arg):
											match arg:
												case _ if str(B)==str(arg):
													return COR_Expressions.UniversalRelation()
								case _:
									C = arg1
									match arg2:
										case COR_Expressions.Complement(argument=arg):
											match arg:
												case _ if str(B)==str(arg):
													return COR_Expressions.UniversalRelation()
									A = arg1
									match arg2:
										case COR_Expressions.Complement(argument=arg):
											match arg:
												case _ if str(B)==str(arg):
													return COR_Expressions.UniversalRelation()
						case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
							match arg1:
								case COR_Expressions.UniversalRelation():
									match arg2:
										case COR_Expressions.Complement(argument=arg):
											match arg:
												case _ if str(B)==str(arg):
													return COR_Expressions.UniversalRelation()
						case COR_Expressions.EmptyRelation():
							return B
						case _ if str(B)==str(arg2):
							return B
						case COR_Expressions.UniversalRelation():
							return COR_Expressions.UniversalRelation()
		case COR_Expressions.Dagger(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.UniversalRelation():
					match arg2:
						case COR_Expressions.Complement(argument=arg):
							match arg:
								case COR_Expressions.IdentityRelation:
									return COR_Expressions.UniversalRelation()
								case COR_Expressions.Converse(argument=arg):
									match arg:
										case _:
											C = arg
											return COR_Expressions.UniversalRelation()
											B = arg
											return COR_Expressions.UniversalRelation()
											A = arg
											return COR_Expressions.UniversalRelation()
								case _:
									B = arg
									return COR_Expressions.UniversalRelation()
									A = arg
									return COR_Expressions.UniversalRelation()
									C = arg
									return COR_Expressions.UniversalRelation()
						case COR_Expressions.Converse(argument=arg):
							match arg:
								case COR_Expressions.Complement(argument=arg):
									match arg:
										case _:
											B = arg
											return COR_Expressions.UniversalRelation()
											A = arg
											return COR_Expressions.UniversalRelation()
											C = arg
											return COR_Expressions.UniversalRelation()
								case _:
									B = arg
									return COR_Expressions.UniversalRelation()
									A = arg
									return COR_Expressions.UniversalRelation()
									C = arg
									return COR_Expressions.UniversalRelation()
						case COR_Expressions.Dagger(argument1=arg1, argument2=arg2):
							match arg1:
								case COR_Expressions.EmptyRelation():
									match arg2:
										case COR_Expressions.Complement(argument=arg):
											match arg:
												case _:
													B = arg
													return COR_Expressions.UniversalRelation()
													A = arg
													return COR_Expressions.UniversalRelation()
													C = arg
													return COR_Expressions.UniversalRelation()
										case COR_Expressions.Converse(argument=arg):
											match arg:
												case _:
													A = arg
													return COR_Expressions.UniversalRelation()
													B = arg
													return COR_Expressions.UniversalRelation()
													C = arg
													return COR_Expressions.UniversalRelation()
								case COR_Expressions.IdentityRelation:
									match arg2:
										case COR_Expressions.Complement(argument=arg):
											match arg:
												case _:
													C = arg
													return COR_Expressions.UniversalRelation()
													A = arg
													return COR_Expressions.UniversalRelation()
													B = arg
													return COR_Expressions.UniversalRelation()
										case COR_Expressions.Converse(argument=arg):
											match arg:
												case _:
													A = arg
													return COR_Expressions.UniversalRelation()
													C = arg
													return COR_Expressions.UniversalRelation()
													B = arg
													return COR_Expressions.UniversalRelation()
								case _:
									A = arg1
									match arg2:
										case COR_Expressions.Converse(argument=arg):
											match arg:
												case _ if str(A)==str(arg):
													return COR_Expressions.UniversalRelation()
												case _:
													C = arg
													return COR_Expressions.UniversalRelation()
													B = arg
													return COR_Expressions.UniversalRelation()
										case COR_Expressions.Complement(argument=arg):
											match arg:
												case _ if str(A)==str(arg):
													return COR_Expressions.UniversalRelation()
												case _:
													C = arg
													return COR_Expressions.UniversalRelation()
													B = arg
													return COR_Expressions.UniversalRelation()
									B = arg1
									match arg2:
										case COR_Expressions.Converse(argument=arg):
											match arg:
												case _ if str(B)==str(arg):
													return COR_Expressions.UniversalRelation()
												case _:
													C = arg
													return COR_Expressions.UniversalRelation()
													A = arg
													return COR_Expressions.UniversalRelation()
										case COR_Expressions.Complement(argument=arg):
											match arg:
												case _ if str(B)==str(arg):
													return COR_Expressions.UniversalRelation()
												case _:
													C = arg
													return COR_Expressions.UniversalRelation()
													A = arg
													return COR_Expressions.UniversalRelation()
									C = arg1
									match arg2:
										case COR_Expressions.Complement(argument=arg):
											match arg:
												case _ if str(C)==str(arg):
													return COR_Expressions.UniversalRelation()
												case _:
													A = arg
													return COR_Expressions.UniversalRelation()
													B = arg
													return COR_Expressions.UniversalRelation()
										case COR_Expressions.Converse(argument=arg):
											match arg:
												case _ if str(C)==str(arg):
													return COR_Expressions.UniversalRelation()
												case _:
													A = arg
													return COR_Expressions.UniversalRelation()
													B = arg
													return COR_Expressions.UniversalRelation()
						case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
							match arg1:
								case COR_Expressions.UniversalRelation():
									match arg2:
										case COR_Expressions.Converse(argument=arg):
											match arg:
												case _:
													A = arg
													return COR_Expressions.UniversalRelation()
													B = arg
													return COR_Expressions.UniversalRelation()
													C = arg
													return COR_Expressions.UniversalRelation()
										case COR_Expressions.Complement(argument=arg):
											match arg:
												case COR_Expressions.IdentityRelation:
													return COR_Expressions.UniversalRelation()
												case _:
													A = arg
													return COR_Expressions.UniversalRelation()
													C = arg
													return COR_Expressions.UniversalRelation()
													B = arg
													return COR_Expressions.UniversalRelation()
								case _:
									B = arg1
									match arg2:
										case COR_Expressions.Converse(argument=arg):
											match arg:
												case _ if str(B)==str(arg):
													return COR_Expressions.UniversalRelation()
												case _:
													A = arg
													return COR_Expressions.UniversalRelation()
													C = arg
													return COR_Expressions.UniversalRelation()
										case COR_Expressions.Complement(argument=arg):
											match arg:
												case _ if str(B)==str(arg):
													return COR_Expressions.UniversalRelation()
												case COR_Expressions.IdentityRelation:
													return COR_Expressions.UniversalRelation()
												case _:
													A = arg
													return COR_Expressions.UniversalRelation()
													C = arg
													return COR_Expressions.UniversalRelation()
									A = arg1
									match arg2:
										case COR_Expressions.Converse(argument=arg):
											match arg:
												case _ if str(A)==str(arg):
													return COR_Expressions.UniversalRelation()
												case _:
													B = arg
													return COR_Expressions.UniversalRelation()
													C = arg
													return COR_Expressions.UniversalRelation()
										case COR_Expressions.Complement(argument=arg):
											match arg:
												case COR_Expressions.IdentityRelation:
													return COR_Expressions.UniversalRelation()
												case _ if str(A)==str(arg):
													return COR_Expressions.UniversalRelation()
												case _:
													B = arg
													return COR_Expressions.UniversalRelation()
													C = arg
													return COR_Expressions.UniversalRelation()
									C = arg1
									match arg2:
										case COR_Expressions.Complement(argument=arg):
											match arg:
												case COR_Expressions.IdentityRelation:
													return COR_Expressions.UniversalRelation()
												case _ if str(C)==str(arg):
													return COR_Expressions.UniversalRelation()
												case _:
													A = arg
													return COR_Expressions.UniversalRelation()
													B = arg
													return COR_Expressions.UniversalRelation()
										case COR_Expressions.Converse(argument=arg):
											match arg:
												case _ if str(C)==str(arg):
													return COR_Expressions.UniversalRelation()
												case _:
													A = arg
													return COR_Expressions.UniversalRelation()
													B = arg
													return COR_Expressions.UniversalRelation()
						case COR_Expressions.Union(argument1=arg1, argument2=arg2):
							match arg1:
								case COR_Expressions.IdentityRelation:
									match arg2:
										case COR_Expressions.Complement(argument=arg):
											match arg:
												case _:
													A = arg
													return COR_Expressions.UniversalRelation()
													B = arg
													return COR_Expressions.UniversalRelation()
													C = arg
													return COR_Expressions.UniversalRelation()
										case COR_Expressions.Converse(argument=arg):
											match arg:
												case _:
													B = arg
													return COR_Expressions.UniversalRelation()
													C = arg
													return COR_Expressions.UniversalRelation()
													A = arg
													return COR_Expressions.UniversalRelation()
								case _:
									A = arg1
									match arg2:
										case COR_Expressions.Converse(argument=arg):
											match arg:
												case _ if str(A)==str(arg):
													return COR_Expressions.UniversalRelation()
												case _:
													B = arg
													return COR_Expressions.UniversalRelation()
													C = arg
													return COR_Expressions.UniversalRelation()
										case COR_Expressions.Complement(argument=arg):
											match arg:
												case COR_Expressions.IdentityRelation:
													return COR_Expressions.UniversalRelation()
												case _:
													B = arg
													return COR_Expressions.UniversalRelation()
													C = arg
													return COR_Expressions.UniversalRelation()
									C = arg1
									match arg2:
										case COR_Expressions.Converse(argument=arg):
											match arg:
												case _ if str(C)==str(arg):
													return COR_Expressions.UniversalRelation()
												case _:
													B = arg
													return COR_Expressions.UniversalRelation()
													A = arg
													return COR_Expressions.UniversalRelation()
										case COR_Expressions.Complement(argument=arg):
											match arg:
												case COR_Expressions.IdentityRelation:
													return COR_Expressions.UniversalRelation()
												case _:
													A = arg
													return COR_Expressions.UniversalRelation()
													B = arg
													return COR_Expressions.UniversalRelation()
									B = arg1
									match arg2:
										case COR_Expressions.Converse(argument=arg):
											match arg:
												case _ if str(B)==str(arg):
													return COR_Expressions.UniversalRelation()
												case _:
													A = arg
													return COR_Expressions.UniversalRelation()
													C = arg
													return COR_Expressions.UniversalRelation()
										case COR_Expressions.Complement(argument=arg):
											match arg:
												case COR_Expressions.IdentityRelation:
													return COR_Expressions.UniversalRelation()
												case _:
													A = arg
													return COR_Expressions.UniversalRelation()
													C = arg
													return COR_Expressions.UniversalRelation()
						case COR_Expressions.EmptyRelation():
							return COR_Expressions.UniversalRelation()
						case COR_Expressions.IdentityRelation:
							return COR_Expressions.UniversalRelation()
						case COR_Expressions.UniversalRelation():
							return COR_Expressions.UniversalRelation()
						case _:
							C = arg2
							return COR_Expressions.UniversalRelation()
							A = arg2
							return COR_Expressions.UniversalRelation()
							B = arg2
							return COR_Expressions.UniversalRelation()
				case COR_Expressions.IdentityRelation:
					match arg2:
						case COR_Expressions.Complement(argument=arg):
							match arg:
								case COR_Expressions.IdentityRelation:
									return COR_Expressions.IdentityRelation()
						case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
							match arg1:
								case COR_Expressions.UniversalRelation():
									match arg2:
										case COR_Expressions.Complement(argument=arg):
											match arg:
												case COR_Expressions.IdentityRelation:
													return COR_Expressions.UniversalRelation()
						case COR_Expressions.UniversalRelation():
							return COR_Expressions.UniversalRelation()
				case COR_Expressions.EmptyRelation():
					match arg2:
						case COR_Expressions.Complement(argument=arg):
							match arg:
								case COR_Expressions.IdentityRelation:
									return COR_Expressions.EmptyRelation()
						case COR_Expressions.Dagger(argument1=arg1, argument2=arg2):
							match arg1:
								case COR_Expressions.EmptyRelation():
									match arg2:
										case COR_Expressions.Complement(argument=arg):
											match arg:
												case _:
													B = arg
													return COR_Expressions.Dagger(COR_Expressions.EmptyRelation(), COR_Expressions.Complement(B))
													C = arg
													return COR_Expressions.Dagger(COR_Expressions.EmptyRelation(), COR_Expressions.Complement(C))
													A = arg
													return COR_Expressions.Dagger(COR_Expressions.EmptyRelation(), COR_Expressions.Complement(A))
										case COR_Expressions.Converse(argument=arg):
											match arg:
												case _:
													B = arg
													return COR_Expressions.Dagger(COR_Expressions.EmptyRelation(), COR_Expressions.Converse(B))
													C = arg
													return COR_Expressions.Dagger(COR_Expressions.EmptyRelation(), COR_Expressions.Converse(C))
													A = arg
													return COR_Expressions.Dagger(COR_Expressions.EmptyRelation(), COR_Expressions.Converse(A))
								case _:
									A = arg1
									match arg2:
										case COR_Expressions.Converse(argument=arg):
											match arg:
												case _ if str(A)==str(arg):
													return COR_Expressions.Dagger(COR_Expressions.EmptyRelation(), COR_Expressions.Converse(A))
									C = arg1
									match arg2:
										case COR_Expressions.Converse(argument=arg):
											match arg:
												case _ if str(C)==str(arg):
													return COR_Expressions.Dagger(COR_Expressions.EmptyRelation(), COR_Expressions.Converse(C))
									B = arg1
									match arg2:
										case COR_Expressions.Converse(argument=arg):
											match arg:
												case _ if str(B)==str(arg):
													return COR_Expressions.Dagger(COR_Expressions.EmptyRelation(), COR_Expressions.Converse(B))
						case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
							match arg1:
								case COR_Expressions.UniversalRelation():
									match arg2:
										case COR_Expressions.Converse(argument=arg):
											match arg:
												case _:
													B = arg
													return COR_Expressions.Composition(COR_Expressions.UniversalRelation(), COR_Expressions.Converse(B))
													C = arg
													return COR_Expressions.Composition(COR_Expressions.UniversalRelation(), COR_Expressions.Converse(C))
													A = arg
													return COR_Expressions.Composition(COR_Expressions.UniversalRelation(), COR_Expressions.Converse(A))
										case COR_Expressions.Complement(argument=arg):
											match arg:
												case COR_Expressions.IdentityRelation:
													return COR_Expressions.Composition(COR_Expressions.UniversalRelation(), COR_Expressions.Complement(COR_Expressions.IdentityRelation()))
												case _:
													A = arg
													return COR_Expressions.Composition(COR_Expressions.UniversalRelation(), COR_Expressions.Complement(A))
													B = arg
													return COR_Expressions.Composition(COR_Expressions.UniversalRelation(), COR_Expressions.Complement(B))
													C = arg
													return COR_Expressions.Composition(COR_Expressions.UniversalRelation(), COR_Expressions.Complement(C))
						case COR_Expressions.UniversalRelation():
							return COR_Expressions.UniversalRelation()
						case COR_Expressions.EmptyRelation():
							return COR_Expressions.EmptyRelation()
				case COR_Expressions.Complement(argument=arg):
					match arg:
						case COR_Expressions.IdentityRelation:
							match arg2:
								case COR_Expressions.Complement(argument=arg):
									match arg:
										case COR_Expressions.IdentityRelation:
											return COR_Expressions.Complement(COR_Expressions.IdentityRelation())
										case _:
											A = arg
											return COR_Expressions.Complement(A)
											C = arg
											return COR_Expressions.Complement(C)
											B = arg
											return COR_Expressions.Complement(B)
								case COR_Expressions.Converse(argument=arg):
									match arg:
										case _:
											C = arg
											return COR_Expressions.Converse(C)
											A = arg
											return COR_Expressions.Converse(A)
											B = arg
											return COR_Expressions.Converse(B)
								case COR_Expressions.UniversalRelation():
									return COR_Expressions.UniversalRelation()
								case COR_Expressions.IdentityRelation:
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
						case _:
							B = arg
							match arg2:
								case COR_Expressions.Complement(argument=arg):
									match arg:
										case COR_Expressions.IdentityRelation:
											return COR_Expressions.Complement(B)
								case COR_Expressions.UniversalRelation():
									return COR_Expressions.UniversalRelation()
							A = arg
							match arg2:
								case COR_Expressions.Complement(argument=arg):
									match arg:
										case COR_Expressions.IdentityRelation:
											return COR_Expressions.Complement(A)
								case COR_Expressions.UniversalRelation():
									return COR_Expressions.UniversalRelation()
							C = arg
							match arg2:
								case COR_Expressions.Complement(argument=arg):
									match arg:
										case COR_Expressions.IdentityRelation:
											return COR_Expressions.Complement(C)
								case COR_Expressions.UniversalRelation():
									return COR_Expressions.UniversalRelation()
				case COR_Expressions.Converse(argument=arg):
					match arg:
						case _:
							B = arg
							match arg2:
								case COR_Expressions.Complement(argument=arg):
									match arg:
										case COR_Expressions.IdentityRelation:
											return COR_Expressions.Converse(B)
								case COR_Expressions.UniversalRelation():
									return COR_Expressions.UniversalRelation()
							A = arg
							match arg2:
								case COR_Expressions.Complement(argument=arg):
									match arg:
										case COR_Expressions.IdentityRelation:
											return COR_Expressions.Converse(A)
								case COR_Expressions.UniversalRelation():
									return COR_Expressions.UniversalRelation()
							C = arg
							match arg2:
								case COR_Expressions.Complement(argument=arg):
									match arg:
										case COR_Expressions.IdentityRelation:
											return COR_Expressions.Converse(C)
								case COR_Expressions.UniversalRelation():
									return COR_Expressions.UniversalRelation()
				case _:
					B = arg1
					match arg2:
						case COR_Expressions.Complement(argument=arg):
							match arg:
								case COR_Expressions.IdentityRelation:
									return B
						case COR_Expressions.UniversalRelation():
							return COR_Expressions.UniversalRelation()
					A = arg1
					match arg2:
						case COR_Expressions.Complement(argument=arg):
							match arg:
								case COR_Expressions.IdentityRelation:
									return A
						case COR_Expressions.UniversalRelation():
							return COR_Expressions.UniversalRelation()
					C = arg1
					match arg2:
						case COR_Expressions.Complement(argument=arg):
							match arg:
								case COR_Expressions.IdentityRelation:
									return C
						case COR_Expressions.UniversalRelation():
							return COR_Expressions.UniversalRelation()
		case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.IdentityRelation:
					match arg2:
						case COR_Expressions.Complement(argument=arg):
							match arg:
								case COR_Expressions.IdentityRelation:
									return COR_Expressions.Complement(COR_Expressions.IdentityRelation())
								case COR_Expressions.Converse(argument=arg):
									match arg:
										case _:
											B = arg
											return COR_Expressions.Converse(COR_Expressions.Complement(B))
											A = arg
											return COR_Expressions.Converse(COR_Expressions.Complement(A))
											C = arg
											return COR_Expressions.Converse(COR_Expressions.Complement(C))
								case _:
									C = arg
									return COR_Expressions.Complement(C)
									A = arg
									return COR_Expressions.Complement(A)
									B = arg
									return COR_Expressions.Complement(B)
						case COR_Expressions.Converse(argument=arg):
							match arg:
								case COR_Expressions.Complement(argument=arg):
									match arg:
										case _:
											C = arg
											return COR_Expressions.Complement(COR_Expressions.Converse(C))
											A = arg
											return COR_Expressions.Complement(COR_Expressions.Converse(A))
											B = arg
											return COR_Expressions.Complement(COR_Expressions.Converse(B))
								case _:
									B = arg
									return COR_Expressions.Converse(B)
									A = arg
									return COR_Expressions.Converse(A)
									C = arg
									return COR_Expressions.Converse(C)
						case COR_Expressions.Union(argument1=arg1, argument2=arg2):
							match arg1:
								case COR_Expressions.IdentityRelation:
									match arg2:
										case COR_Expressions.Complement(argument=arg):
											match arg:
												case _:
													C = arg
													return COR_Expressions.Union(COR_Expressions.IdentityRelation(), COR_Expressions.Complement(C))
													A = arg
													return COR_Expressions.Union(COR_Expressions.IdentityRelation(), COR_Expressions.Complement(A))
													B = arg
													return COR_Expressions.Union(COR_Expressions.IdentityRelation(), COR_Expressions.Complement(B))
										case COR_Expressions.Converse(argument=arg):
											match arg:
												case _:
													C = arg
													return COR_Expressions.Union(COR_Expressions.IdentityRelation(), COR_Expressions.Converse(C))
													A = arg
													return COR_Expressions.Union(COR_Expressions.IdentityRelation(), COR_Expressions.Converse(A))
													B = arg
													return COR_Expressions.Union(COR_Expressions.IdentityRelation(), COR_Expressions.Converse(B))
								case _:
									B = arg1
									match arg2:
										case COR_Expressions.Converse(argument=arg):
											match arg:
												case _ if str(B)==str(arg):
													return COR_Expressions.Union(B, COR_Expressions.Converse(B))
												case _:
													A = arg
													return COR_Expressions.Union(B, COR_Expressions.Converse(A))
													C = arg
													return COR_Expressions.Union(B, COR_Expressions.Converse(C))
										case COR_Expressions.Complement(argument=arg):
											match arg:
												case COR_Expressions.IdentityRelation:
													return COR_Expressions.Union(B, COR_Expressions.Complement(COR_Expressions.IdentityRelation()))
												case _:
													C = arg
													return COR_Expressions.Union(B, COR_Expressions.Complement(C))
													A = arg
													return COR_Expressions.Union(B, COR_Expressions.Complement(A))
									A = arg1
									match arg2:
										case COR_Expressions.Complement(argument=arg):
											match arg:
												case COR_Expressions.IdentityRelation:
													return COR_Expressions.Union(A, COR_Expressions.Complement(COR_Expressions.IdentityRelation()))
												case _:
													C = arg
													return COR_Expressions.Union(A, COR_Expressions.Complement(C))
													B = arg
													return COR_Expressions.Union(A, COR_Expressions.Complement(B))
										case COR_Expressions.Converse(argument=arg):
											match arg:
												case _ if str(A)==str(arg):
													return COR_Expressions.Union(A, COR_Expressions.Converse(A))
												case _:
													B = arg
													return COR_Expressions.Union(A, COR_Expressions.Converse(B))
													C = arg
													return COR_Expressions.Union(A, COR_Expressions.Converse(C))
									C = arg1
									match arg2:
										case COR_Expressions.Converse(argument=arg):
											match arg:
												case _ if str(C)==str(arg):
													return COR_Expressions.Union(C, COR_Expressions.Converse(C))
												case _:
													A = arg
													return COR_Expressions.Union(C, COR_Expressions.Converse(A))
													B = arg
													return COR_Expressions.Union(C, COR_Expressions.Converse(B))
										case COR_Expressions.Complement(argument=arg):
											match arg:
												case COR_Expressions.IdentityRelation:
													return COR_Expressions.Union(C, COR_Expressions.Complement(COR_Expressions.IdentityRelation()))
												case _:
													B = arg
													return COR_Expressions.Union(C, COR_Expressions.Complement(B))
													A = arg
													return COR_Expressions.Union(C, COR_Expressions.Complement(A))
						case COR_Expressions.Dagger(argument1=arg1, argument2=arg2):
							match arg1:
								case COR_Expressions.IdentityRelation:
									match arg2:
										case COR_Expressions.Complement(argument=arg):
											match arg:
												case _:
													B = arg
													return COR_Expressions.Dagger(COR_Expressions.IdentityRelation(), COR_Expressions.Complement(B))
													A = arg
													return COR_Expressions.Dagger(COR_Expressions.IdentityRelation(), COR_Expressions.Complement(A))
													C = arg
													return COR_Expressions.Dagger(COR_Expressions.IdentityRelation(), COR_Expressions.Complement(C))
										case COR_Expressions.Converse(argument=arg):
											match arg:
												case _:
													A = arg
													return COR_Expressions.Dagger(COR_Expressions.IdentityRelation(), COR_Expressions.Converse(A))
													B = arg
													return COR_Expressions.Dagger(COR_Expressions.IdentityRelation(), COR_Expressions.Converse(B))
													C = arg
													return COR_Expressions.Dagger(COR_Expressions.IdentityRelation(), COR_Expressions.Converse(C))
								case COR_Expressions.EmptyRelation():
									match arg2:
										case COR_Expressions.Converse(argument=arg):
											match arg:
												case _:
													C = arg
													return COR_Expressions.Dagger(COR_Expressions.EmptyRelation(), COR_Expressions.Converse(C))
													A = arg
													return COR_Expressions.Dagger(COR_Expressions.EmptyRelation(), COR_Expressions.Converse(A))
													B = arg
													return COR_Expressions.Dagger(COR_Expressions.EmptyRelation(), COR_Expressions.Converse(B))
										case COR_Expressions.Complement(argument=arg):
											match arg:
												case _:
													A = arg
													return COR_Expressions.Dagger(COR_Expressions.EmptyRelation(), COR_Expressions.Complement(A))
													B = arg
													return COR_Expressions.Dagger(COR_Expressions.EmptyRelation(), COR_Expressions.Complement(B))
													C = arg
													return COR_Expressions.Dagger(COR_Expressions.EmptyRelation(), COR_Expressions.Complement(C))
								case _:
									C = arg1
									match arg2:
										case COR_Expressions.Complement(argument=arg):
											match arg:
												case _ if str(C)==str(arg):
													return COR_Expressions.Dagger(C, COR_Expressions.Complement(C))
												case _:
													B = arg
													return COR_Expressions.Dagger(C, COR_Expressions.Complement(B))
													A = arg
													return COR_Expressions.Dagger(C, COR_Expressions.Complement(A))
										case COR_Expressions.Converse(argument=arg):
											match arg:
												case _ if str(C)==str(arg):
													return COR_Expressions.Dagger(C, COR_Expressions.Converse(C))
												case _:
													B = arg
													return COR_Expressions.Dagger(C, COR_Expressions.Converse(B))
													A = arg
													return COR_Expressions.Dagger(C, COR_Expressions.Converse(A))
									A = arg1
									match arg2:
										case COR_Expressions.Complement(argument=arg):
											match arg:
												case _ if str(A)==str(arg):
													return COR_Expressions.Dagger(A, COR_Expressions.Complement(A))
												case _:
													C = arg
													return COR_Expressions.Dagger(A, COR_Expressions.Complement(C))
													B = arg
													return COR_Expressions.Dagger(A, COR_Expressions.Complement(B))
										case COR_Expressions.Converse(argument=arg):
											match arg:
												case _ if str(A)==str(arg):
													return COR_Expressions.Dagger(A, COR_Expressions.Converse(A))
												case _:
													C = arg
													return COR_Expressions.Dagger(A, COR_Expressions.Converse(C))
													B = arg
													return COR_Expressions.Dagger(A, COR_Expressions.Converse(B))
									B = arg1
									match arg2:
										case COR_Expressions.Complement(argument=arg):
											match arg:
												case _ if str(B)==str(arg):
													return COR_Expressions.Dagger(B, COR_Expressions.Complement(B))
												case _:
													C = arg
													return COR_Expressions.Dagger(B, COR_Expressions.Complement(C))
													A = arg
													return COR_Expressions.Dagger(B, COR_Expressions.Complement(A))
										case COR_Expressions.Converse(argument=arg):
											match arg:
												case _ if str(B)==str(arg):
													return COR_Expressions.Dagger(B, COR_Expressions.Converse(B))
												case _:
													C = arg
													return COR_Expressions.Dagger(B, COR_Expressions.Converse(C))
													A = arg
													return COR_Expressions.Dagger(B, COR_Expressions.Converse(A))
						case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
							match arg1:
								case COR_Expressions.UniversalRelation():
									match arg2:
										case COR_Expressions.Converse(argument=arg):
											match arg:
												case _:
													A = arg
													return COR_Expressions.Composition(COR_Expressions.UniversalRelation(), COR_Expressions.Converse(A))
													B = arg
													return COR_Expressions.Composition(COR_Expressions.UniversalRelation(), COR_Expressions.Converse(B))
													C = arg
													return COR_Expressions.Composition(COR_Expressions.UniversalRelation(), COR_Expressions.Converse(C))
										case COR_Expressions.Complement(argument=arg):
											match arg:
												case COR_Expressions.IdentityRelation:
													return COR_Expressions.Composition(COR_Expressions.UniversalRelation(), COR_Expressions.Complement(COR_Expressions.IdentityRelation()))
												case _:
													C = arg
													return COR_Expressions.Composition(COR_Expressions.UniversalRelation(), COR_Expressions.Complement(C))
													B = arg
													return COR_Expressions.Composition(COR_Expressions.UniversalRelation(), COR_Expressions.Complement(B))
													A = arg
													return COR_Expressions.Composition(COR_Expressions.UniversalRelation(), COR_Expressions.Complement(A))
										case COR_Expressions.Dagger(argument1=arg1, argument2=arg2):
											match arg1:
												case _:
													C = arg1
													match arg2:
														case COR_Expressions.Converse(argument=arg):
															match arg:
																case _ if str(C)==str(arg):
																	return COR_Expressions.Composition(COR_Expressions.UniversalRelation(), COR_Expressions.Dagger(C, COR_Expressions.Converse(C)))
																case _:
																	B = arg
																	return COR_Expressions.Composition(COR_Expressions.UniversalRelation(), COR_Expressions.Dagger(C, COR_Expressions.Converse(B)))
																	A = arg
																	return COR_Expressions.Composition(COR_Expressions.UniversalRelation(), COR_Expressions.Dagger(C, COR_Expressions.Converse(A)))
														case COR_Expressions.Complement(argument=arg):
															match arg:
																case _ if str(C)==str(arg):
																	return COR_Expressions.Composition(COR_Expressions.UniversalRelation(), COR_Expressions.Dagger(C, COR_Expressions.Complement(C)))
																case _:
																	B = arg
																	return COR_Expressions.Composition(COR_Expressions.UniversalRelation(), COR_Expressions.Dagger(C, COR_Expressions.Complement(B)))
										case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
											match arg1:
												case _:
													B = arg1
													match arg2:
														case COR_Expressions.Converse(argument=arg):
															match arg:
																case _:
																	A = arg
																	return COR_Expressions.Composition(COR_Expressions.UniversalRelation(), COR_Expressions.Composition(B, COR_Expressions.Converse(A)))
																	C = arg
																	return COR_Expressions.Composition(COR_Expressions.UniversalRelation(), COR_Expressions.Composition(B, COR_Expressions.Converse(C)))
														case COR_Expressions.Complement(argument=arg):
															match arg:
																case _ if str(B)==str(arg):
																	return COR_Expressions.Composition(COR_Expressions.UniversalRelation(), COR_Expressions.Composition(B, COR_Expressions.Complement(B)))
																case COR_Expressions.IdentityRelation:
																	return COR_Expressions.Composition(COR_Expressions.UniversalRelation(), COR_Expressions.Composition(B, COR_Expressions.Complement(COR_Expressions.IdentityRelation())))
																case _:
																	A = arg
																	return COR_Expressions.Composition(COR_Expressions.UniversalRelation(), COR_Expressions.Composition(B, COR_Expressions.Complement(A)))
																	C = arg
																	return COR_Expressions.Composition(COR_Expressions.UniversalRelation(), COR_Expressions.Composition(B, COR_Expressions.Complement(C)))
													A = arg1
													match arg2:
														case COR_Expressions.Complement(argument=arg):
															match arg:
																case _ if str(A)==str(arg):
																	return COR_Expressions.Composition(COR_Expressions.UniversalRelation(), COR_Expressions.Composition(A, COR_Expressions.Complement(A)))
																case COR_Expressions.IdentityRelation:
																	return COR_Expressions.Composition(COR_Expressions.UniversalRelation(), COR_Expressions.Composition(A, COR_Expressions.Complement(COR_Expressions.IdentityRelation())))
																case _:
																	B = arg
																	return COR_Expressions.Composition(COR_Expressions.UniversalRelation(), COR_Expressions.Composition(A, COR_Expressions.Complement(B)))
																	C = arg
																	return COR_Expressions.Composition(COR_Expressions.UniversalRelation(), COR_Expressions.Composition(A, COR_Expressions.Complement(C)))
														case COR_Expressions.Converse(argument=arg):
															match arg:
																case _:
																	C = arg
																	return COR_Expressions.Composition(COR_Expressions.UniversalRelation(), COR_Expressions.Composition(A, COR_Expressions.Converse(C)))
																	B = arg
																	return COR_Expressions.Composition(COR_Expressions.UniversalRelation(), COR_Expressions.Composition(A, COR_Expressions.Converse(B)))
													C = arg1
													match arg2:
														case COR_Expressions.Complement(argument=arg):
															match arg:
																case COR_Expressions.IdentityRelation:
																	return COR_Expressions.Composition(COR_Expressions.UniversalRelation(), COR_Expressions.Composition(C, COR_Expressions.Complement(COR_Expressions.IdentityRelation())))
																case _:
																	A = arg
																	return COR_Expressions.Composition(COR_Expressions.UniversalRelation(), COR_Expressions.Composition(C, COR_Expressions.Complement(A)))
																	B = arg
																	return COR_Expressions.Composition(COR_Expressions.UniversalRelation(), COR_Expressions.Composition(C, COR_Expressions.Complement(B)))
								case _:
									B = arg1
									match arg2:
										case COR_Expressions.Converse(argument=arg):
											match arg:
												case _ if str(B)==str(arg):
													return COR_Expressions.Composition(B, COR_Expressions.Converse(B))
												case _:
													C = arg
													return COR_Expressions.Composition(B, COR_Expressions.Converse(C))
													A = arg
													return COR_Expressions.Composition(B, COR_Expressions.Converse(A))
										case COR_Expressions.Complement(argument=arg):
											match arg:
												case _ if str(B)==str(arg):
													return COR_Expressions.Composition(B, COR_Expressions.Complement(B))
												case COR_Expressions.IdentityRelation:
													return COR_Expressions.Composition(B, COR_Expressions.Complement(COR_Expressions.IdentityRelation()))
												case _:
													A = arg
													return COR_Expressions.Composition(B, COR_Expressions.Complement(A))
													C = arg
													return COR_Expressions.Composition(B, COR_Expressions.Complement(C))
									A = arg1
									match arg2:
										case COR_Expressions.Complement(argument=arg):
											match arg:
												case _ if str(A)==str(arg):
													return COR_Expressions.Composition(A, COR_Expressions.Complement(A))
												case COR_Expressions.IdentityRelation:
													return COR_Expressions.Composition(A, COR_Expressions.Complement(COR_Expressions.IdentityRelation()))
												case _:
													B = arg
													return COR_Expressions.Composition(A, COR_Expressions.Complement(B))
													C = arg
													return COR_Expressions.Composition(A, COR_Expressions.Complement(C))
										case COR_Expressions.Converse(argument=arg):
											match arg:
												case _ if str(A)==str(arg):
													return COR_Expressions.Composition(A, COR_Expressions.Converse(A))
												case _:
													B = arg
													return COR_Expressions.Composition(A, COR_Expressions.Converse(B))
													C = arg
													return COR_Expressions.Composition(A, COR_Expressions.Converse(C))
									C = arg1
									match arg2:
										case COR_Expressions.Complement(argument=arg):
											match arg:
												case COR_Expressions.IdentityRelation:
													return COR_Expressions.Composition(C, COR_Expressions.Complement(COR_Expressions.IdentityRelation()))
												case _ if str(C)==str(arg):
													return COR_Expressions.Composition(C, COR_Expressions.Complement(C))
												case _:
													B = arg
													return COR_Expressions.Composition(C, COR_Expressions.Complement(B))
													A = arg
													return COR_Expressions.Composition(C, COR_Expressions.Complement(A))
										case COR_Expressions.Converse(argument=arg):
											match arg:
												case _ if str(C)==str(arg):
													return COR_Expressions.Composition(C, COR_Expressions.Converse(C))
												case _:
													A = arg
													return COR_Expressions.Composition(C, COR_Expressions.Converse(A))
													B = arg
													return COR_Expressions.Composition(C, COR_Expressions.Converse(B))
						case COR_Expressions.UniversalRelation():
							return COR_Expressions.UniversalRelation()
						case COR_Expressions.EmptyRelation():
							return COR_Expressions.EmptyRelation()
						case COR_Expressions.IdentityRelation:
							return COR_Expressions.IdentityRelation()
						case _:
							B = arg2
							return B
							C = arg2
							return C
							A = arg2
							return A
				case COR_Expressions.EmptyRelation():
					match arg2:
						case COR_Expressions.Converse(argument=arg):
							match arg:
								case COR_Expressions.Complement(argument=arg):
									match arg:
										case _:
											A = arg
											return COR_Expressions.EmptyRelation()
											B = arg
											return COR_Expressions.EmptyRelation()
											C = arg
											return COR_Expressions.EmptyRelation()
								case _:
									B = arg
									return COR_Expressions.EmptyRelation()
									C = arg
									return COR_Expressions.EmptyRelation()
									A = arg
									return COR_Expressions.EmptyRelation()
						case COR_Expressions.Complement(argument=arg):
							match arg:
								case COR_Expressions.IdentityRelation:
									return COR_Expressions.EmptyRelation()
								case COR_Expressions.Converse(argument=arg):
									match arg:
										case _:
											A = arg
											return COR_Expressions.EmptyRelation()
											B = arg
											return COR_Expressions.EmptyRelation()
											C = arg
											return COR_Expressions.EmptyRelation()
								case _:
									B = arg
									return COR_Expressions.EmptyRelation()
									C = arg
									return COR_Expressions.EmptyRelation()
									A = arg
									return COR_Expressions.EmptyRelation()
						case COR_Expressions.Union(argument1=arg1, argument2=arg2):
							match arg1:
								case COR_Expressions.IdentityRelation:
									match arg2:
										case COR_Expressions.Complement(argument=arg):
											match arg:
												case _:
													C = arg
													return COR_Expressions.EmptyRelation()
													B = arg
													return COR_Expressions.EmptyRelation()
													A = arg
													return COR_Expressions.EmptyRelation()
										case COR_Expressions.Converse(argument=arg):
											match arg:
												case _:
													C = arg
													return COR_Expressions.EmptyRelation()
													A = arg
													return COR_Expressions.EmptyRelation()
													B = arg
													return COR_Expressions.EmptyRelation()
								case _:
									B = arg1
									match arg2:
										case COR_Expressions.Complement(argument=arg):
											match arg:
												case COR_Expressions.IdentityRelation:
													return COR_Expressions.EmptyRelation()
												case _:
													A = arg
													return COR_Expressions.EmptyRelation()
													C = arg
													return COR_Expressions.EmptyRelation()
										case COR_Expressions.Converse(argument=arg):
											match arg:
												case _ if str(B)==str(arg):
													return COR_Expressions.EmptyRelation()
												case _:
													A = arg
													return COR_Expressions.EmptyRelation()
													C = arg
													return COR_Expressions.EmptyRelation()
									C = arg1
									match arg2:
										case COR_Expressions.Converse(argument=arg):
											match arg:
												case _ if str(C)==str(arg):
													return COR_Expressions.EmptyRelation()
												case _:
													B = arg
													return COR_Expressions.EmptyRelation()
													A = arg
													return COR_Expressions.EmptyRelation()
										case COR_Expressions.Complement(argument=arg):
											match arg:
												case COR_Expressions.IdentityRelation:
													return COR_Expressions.EmptyRelation()
												case _:
													A = arg
													return COR_Expressions.EmptyRelation()
													B = arg
													return COR_Expressions.EmptyRelation()
									A = arg1
									match arg2:
										case COR_Expressions.Converse(argument=arg):
											match arg:
												case _ if str(A)==str(arg):
													return COR_Expressions.EmptyRelation()
												case _:
													B = arg
													return COR_Expressions.EmptyRelation()
													C = arg
													return COR_Expressions.EmptyRelation()
										case COR_Expressions.Complement(argument=arg):
											match arg:
												case COR_Expressions.IdentityRelation:
													return COR_Expressions.EmptyRelation()
												case _:
													C = arg
													return COR_Expressions.EmptyRelation()
													B = arg
													return COR_Expressions.EmptyRelation()
						case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
							match arg1:
								case COR_Expressions.UniversalRelation():
									match arg2:
										case COR_Expressions.Converse(argument=arg):
											match arg:
												case _:
													A = arg
													return COR_Expressions.EmptyRelation()
													B = arg
													return COR_Expressions.EmptyRelation()
													C = arg
													return COR_Expressions.EmptyRelation()
										case COR_Expressions.Complement(argument=arg):
											match arg:
												case COR_Expressions.IdentityRelation:
													return COR_Expressions.EmptyRelation()
												case _:
													B = arg
													return COR_Expressions.EmptyRelation()
													C = arg
													return COR_Expressions.EmptyRelation()
													A = arg
													return COR_Expressions.EmptyRelation()
								case _:
									C = arg1
									match arg2:
										case COR_Expressions.Complement(argument=arg):
											match arg:
												case _ if str(C)==str(arg):
													return COR_Expressions.EmptyRelation()
												case COR_Expressions.IdentityRelation:
													return COR_Expressions.EmptyRelation()
												case _:
													A = arg
													return COR_Expressions.EmptyRelation()
													B = arg
													return COR_Expressions.EmptyRelation()
										case COR_Expressions.Converse(argument=arg):
											match arg:
												case _ if str(C)==str(arg):
													return COR_Expressions.EmptyRelation()
												case _:
													A = arg
													return COR_Expressions.EmptyRelation()
													B = arg
													return COR_Expressions.EmptyRelation()
									B = arg1
									match arg2:
										case COR_Expressions.Complement(argument=arg):
											match arg:
												case COR_Expressions.IdentityRelation:
													return COR_Expressions.EmptyRelation()
												case _ if str(B)==str(arg):
													return COR_Expressions.EmptyRelation()
												case _:
													A = arg
													return COR_Expressions.EmptyRelation()
													C = arg
													return COR_Expressions.EmptyRelation()
										case COR_Expressions.Converse(argument=arg):
											match arg:
												case _ if str(B)==str(arg):
													return COR_Expressions.EmptyRelation()
												case _:
													C = arg
													return COR_Expressions.EmptyRelation()
													A = arg
													return COR_Expressions.EmptyRelation()
									A = arg1
									match arg2:
										case COR_Expressions.Converse(argument=arg):
											match arg:
												case _ if str(A)==str(arg):
													return COR_Expressions.EmptyRelation()
												case _:
													B = arg
													return COR_Expressions.EmptyRelation()
													C = arg
													return COR_Expressions.EmptyRelation()
										case COR_Expressions.Complement(argument=arg):
											match arg:
												case COR_Expressions.IdentityRelation:
													return COR_Expressions.EmptyRelation()
												case _ if str(A)==str(arg):
													return COR_Expressions.EmptyRelation()
												case _:
													B = arg
													return COR_Expressions.EmptyRelation()
													C = arg
													return COR_Expressions.EmptyRelation()
						case COR_Expressions.Dagger(argument1=arg1, argument2=arg2):
							match arg1:
								case COR_Expressions.IdentityRelation:
									match arg2:
										case COR_Expressions.Converse(argument=arg):
											match arg:
												case _:
													A = arg
													return COR_Expressions.EmptyRelation()
													B = arg
													return COR_Expressions.EmptyRelation()
													C = arg
													return COR_Expressions.EmptyRelation()
										case COR_Expressions.Complement(argument=arg):
											match arg:
												case _:
													B = arg
													return COR_Expressions.EmptyRelation()
													A = arg
													return COR_Expressions.EmptyRelation()
													C = arg
													return COR_Expressions.EmptyRelation()
								case COR_Expressions.EmptyRelation():
									match arg2:
										case COR_Expressions.Complement(argument=arg):
											match arg:
												case _:
													C = arg
													return COR_Expressions.EmptyRelation()
													A = arg
													return COR_Expressions.EmptyRelation()
													B = arg
													return COR_Expressions.EmptyRelation()
										case COR_Expressions.Converse(argument=arg):
											match arg:
												case _:
													A = arg
													return COR_Expressions.EmptyRelation()
													B = arg
													return COR_Expressions.EmptyRelation()
													C = arg
													return COR_Expressions.EmptyRelation()
								case _:
									C = arg1
									match arg2:
										case COR_Expressions.Converse(argument=arg):
											match arg:
												case _ if str(C)==str(arg):
													return COR_Expressions.EmptyRelation()
												case _:
													A = arg
													return COR_Expressions.EmptyRelation()
													B = arg
													return COR_Expressions.EmptyRelation()
										case COR_Expressions.Complement(argument=arg):
											match arg:
												case _ if str(C)==str(arg):
													return COR_Expressions.EmptyRelation()
												case _:
													A = arg
													return COR_Expressions.EmptyRelation()
													B = arg
													return COR_Expressions.EmptyRelation()
									A = arg1
									match arg2:
										case COR_Expressions.Converse(argument=arg):
											match arg:
												case _ if str(A)==str(arg):
													return COR_Expressions.EmptyRelation()
												case _:
													B = arg
													return COR_Expressions.EmptyRelation()
													C = arg
													return COR_Expressions.EmptyRelation()
										case COR_Expressions.Complement(argument=arg):
											match arg:
												case _ if str(A)==str(arg):
													return COR_Expressions.EmptyRelation()
												case _:
													C = arg
													return COR_Expressions.EmptyRelation()
													B = arg
													return COR_Expressions.EmptyRelation()
									B = arg1
									match arg2:
										case COR_Expressions.Converse(argument=arg):
											match arg:
												case _ if str(B)==str(arg):
													return COR_Expressions.EmptyRelation()
												case _:
													A = arg
													return COR_Expressions.EmptyRelation()
													C = arg
													return COR_Expressions.EmptyRelation()
										case COR_Expressions.Complement(argument=arg):
											match arg:
												case _ if str(B)==str(arg):
													return COR_Expressions.EmptyRelation()
												case _:
													C = arg
													return COR_Expressions.EmptyRelation()
													A = arg
													return COR_Expressions.EmptyRelation()
						case COR_Expressions.EmptyRelation():
							return COR_Expressions.EmptyRelation()
						case COR_Expressions.UniversalRelation():
							return COR_Expressions.EmptyRelation()
						case COR_Expressions.IdentityRelation:
							return COR_Expressions.EmptyRelation()
						case _:
							B = arg2
							return COR_Expressions.EmptyRelation()
							C = arg2
							return COR_Expressions.EmptyRelation()
							A = arg2
							return COR_Expressions.EmptyRelation()
				case COR_Expressions.UniversalRelation():
					match arg2:
						case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
							match arg1:
								case COR_Expressions.UniversalRelation():
									match arg2:
										case COR_Expressions.Converse(argument=arg):
											match arg:
												case _:
													A = arg
													return COR_Expressions.Composition(COR_Expressions.UniversalRelation(), COR_Expressions.Converse(A))
													C = arg
													return COR_Expressions.Composition(COR_Expressions.UniversalRelation(), COR_Expressions.Converse(C))
													B = arg
													return COR_Expressions.Composition(COR_Expressions.UniversalRelation(), COR_Expressions.Converse(B))
										case COR_Expressions.Complement(argument=arg):
											match arg:
												case COR_Expressions.IdentityRelation:
													return COR_Expressions.Composition(COR_Expressions.UniversalRelation(), COR_Expressions.Complement(COR_Expressions.IdentityRelation()))
												case _:
													C = arg
													return COR_Expressions.Composition(COR_Expressions.UniversalRelation(), COR_Expressions.Complement(C))
													A = arg
													return COR_Expressions.Composition(COR_Expressions.UniversalRelation(), COR_Expressions.Complement(A))
													B = arg
													return COR_Expressions.Composition(COR_Expressions.UniversalRelation(), COR_Expressions.Complement(B))
								case _:
									B = arg1
									match arg2:
										case COR_Expressions.Converse(argument=arg):
											match arg:
												case _ if str(B)==str(arg):
													return COR_Expressions.Composition(COR_Expressions.UniversalRelation(), COR_Expressions.Converse(B))
									C = arg1
									match arg2:
										case COR_Expressions.Converse(argument=arg):
											match arg:
												case _ if str(C)==str(arg):
													return COR_Expressions.Composition(COR_Expressions.UniversalRelation(), COR_Expressions.Converse(C))
									A = arg1
									match arg2:
										case COR_Expressions.Converse(argument=arg):
											match arg:
												case _ if str(A)==str(arg):
													return COR_Expressions.Composition(COR_Expressions.UniversalRelation(), COR_Expressions.Converse(A))
						case COR_Expressions.Union(argument1=arg1, argument2=arg2):
							match arg1:
								case COR_Expressions.IdentityRelation:
									match arg2:
										case COR_Expressions.Complement(argument=arg):
											match arg:
												case _:
													C = arg
													return COR_Expressions.UniversalRelation()
													A = arg
													return COR_Expressions.UniversalRelation()
													B = arg
													return COR_Expressions.UniversalRelation()
										case COR_Expressions.Converse(argument=arg):
											match arg:
												case _:
													C = arg
													return COR_Expressions.UniversalRelation()
													A = arg
													return COR_Expressions.UniversalRelation()
													B = arg
													return COR_Expressions.UniversalRelation()
						case COR_Expressions.Dagger(argument1=arg1, argument2=arg2):
							match arg1:
								case COR_Expressions.EmptyRelation():
									match arg2:
										case COR_Expressions.Complement(argument=arg):
											match arg:
												case _:
													A = arg
													return COR_Expressions.Dagger(COR_Expressions.EmptyRelation(), COR_Expressions.Complement(A))
													B = arg
													return COR_Expressions.Dagger(COR_Expressions.EmptyRelation(), COR_Expressions.Complement(B))
													C = arg
													return COR_Expressions.Dagger(COR_Expressions.EmptyRelation(), COR_Expressions.Complement(C))
										case COR_Expressions.Converse(argument=arg):
											match arg:
												case _:
													C = arg
													return COR_Expressions.Dagger(COR_Expressions.EmptyRelation(), COR_Expressions.Converse(C))
													B = arg
													return COR_Expressions.Dagger(COR_Expressions.EmptyRelation(), COR_Expressions.Converse(B))
													A = arg
													return COR_Expressions.Dagger(COR_Expressions.EmptyRelation(), COR_Expressions.Converse(A))
						case COR_Expressions.IdentityRelation:
							return COR_Expressions.UniversalRelation()
						case COR_Expressions.UniversalRelation():
							return COR_Expressions.UniversalRelation()
						case COR_Expressions.EmptyRelation():
							return COR_Expressions.EmptyRelation()
				case COR_Expressions.Converse(argument=arg):
					match arg:
						case _:
							A = arg
							match arg2:
								case COR_Expressions.Dagger(argument1=arg1, argument2=arg2):
									match arg1:
										case COR_Expressions.EmptyRelation():
											match arg2:
												case COR_Expressions.Converse(argument=arg):
													match arg:
														case _ if str(A)==str(arg):
															return COR_Expressions.Dagger(COR_Expressions.EmptyRelation(), COR_Expressions.Converse(A))
								case COR_Expressions.IdentityRelation:
									return COR_Expressions.Converse(A)
								case COR_Expressions.EmptyRelation():
									return COR_Expressions.EmptyRelation()
							B = arg
							match arg2:
								case COR_Expressions.EmptyRelation():
									return COR_Expressions.EmptyRelation()
								case COR_Expressions.IdentityRelation:
									return COR_Expressions.Converse(B)
							C = arg
							match arg2:
								case COR_Expressions.IdentityRelation:
									return COR_Expressions.Converse(C)
								case COR_Expressions.EmptyRelation():
									return COR_Expressions.EmptyRelation()
				case COR_Expressions.Complement(argument=arg):
					match arg:
						case COR_Expressions.IdentityRelation:
							match arg2:
								case COR_Expressions.IdentityRelation:
									return COR_Expressions.Complement(COR_Expressions.IdentityRelation())
								case COR_Expressions.EmptyRelation():
									return COR_Expressions.EmptyRelation()
						case _:
							C = arg
							match arg2:
								case COR_Expressions.IdentityRelation:
									return COR_Expressions.Complement(C)
								case COR_Expressions.EmptyRelation():
									return COR_Expressions.EmptyRelation()
							B = arg
							match arg2:
								case COR_Expressions.IdentityRelation:
									return COR_Expressions.Complement(B)
								case COR_Expressions.EmptyRelation():
									return COR_Expressions.EmptyRelation()
							A = arg
							match arg2:
								case COR_Expressions.IdentityRelation:
									return COR_Expressions.Complement(A)
								case COR_Expressions.EmptyRelation():
									return COR_Expressions.EmptyRelation()
				case _:
					B = arg1
					match arg2:
						case COR_Expressions.IdentityRelation:
							return B
						case COR_Expressions.EmptyRelation():
							return COR_Expressions.EmptyRelation()
					A = arg1
					match arg2:
						case COR_Expressions.EmptyRelation():
							return COR_Expressions.EmptyRelation()
						case COR_Expressions.IdentityRelation:
							return A
					C = arg1
					match arg2:
						case COR_Expressions.IdentityRelation:
							return C
						case COR_Expressions.EmptyRelation():
							return COR_Expressions.EmptyRelation()
		case COR_Expressions.Intersection(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.UniversalRelation():
					match arg2:
						case COR_Expressions.EmptyRelation():
							return COR_Expressions.EmptyRelation()
						case COR_Expressions.IdentityRelation:
							return COR_Expressions.IdentityRelation()
						case COR_Expressions.UniversalRelation():
							return COR_Expressions.UniversalRelation()
						case COR_Expressions.Converse(argument=arg):
							match arg:
								case _:
									B = arg
									return COR_Expressions.Converse(B)
									A = arg
									return COR_Expressions.Converse(A)
									C = arg
									return COR_Expressions.Converse(C)
						case COR_Expressions.Complement(argument=arg):
							match arg:
								case COR_Expressions.IdentityRelation:
									return COR_Expressions.Complement(COR_Expressions.IdentityRelation())
								case _:
									A = arg
									return COR_Expressions.Complement(A)
									B = arg
									return COR_Expressions.Complement(B)
									C = arg
									return COR_Expressions.Complement(C)
						case _:
							A = arg2
							return A
							B = arg2
							return B
							C = arg2
							return C
				case COR_Expressions.IdentityRelation:
					match arg2:
						case COR_Expressions.IdentityRelation:
							return COR_Expressions.IdentityRelation()
						case COR_Expressions.EmptyRelation():
							return COR_Expressions.EmptyRelation()
						case COR_Expressions.UniversalRelation():
							return COR_Expressions.IdentityRelation()
						case COR_Expressions.Converse(argument=arg):
							match arg:
								case _:
									A = arg
									return COR_Expressions.Intersection(COR_Expressions.IdentityRelation(), A)
									B = arg
									return COR_Expressions.Intersection(B, COR_Expressions.IdentityRelation())
									C = arg
									return COR_Expressions.Intersection(COR_Expressions.IdentityRelation(), C)
						case COR_Expressions.Complement(argument=arg):
							match arg:
								case COR_Expressions.IdentityRelation:
									return COR_Expressions.EmptyRelation()
				case COR_Expressions.EmptyRelation():
					match arg2:
						case COR_Expressions.UniversalRelation():
							return COR_Expressions.EmptyRelation()
						case COR_Expressions.EmptyRelation():
							return COR_Expressions.EmptyRelation()
						case COR_Expressions.IdentityRelation:
							return COR_Expressions.EmptyRelation()
						case COR_Expressions.Complement(argument=arg):
							match arg:
								case COR_Expressions.IdentityRelation:
									return COR_Expressions.EmptyRelation()
								case _:
									C = arg
									return COR_Expressions.EmptyRelation()
									A = arg
									return COR_Expressions.EmptyRelation()
									B = arg
									return COR_Expressions.EmptyRelation()
						case COR_Expressions.Converse(argument=arg):
							match arg:
								case _:
									A = arg
									return COR_Expressions.EmptyRelation()
									B = arg
									return COR_Expressions.EmptyRelation()
									C = arg
									return COR_Expressions.EmptyRelation()
						case _:
							B = arg2
							return COR_Expressions.EmptyRelation()
							A = arg2
							return COR_Expressions.EmptyRelation()
							C = arg2
							return COR_Expressions.EmptyRelation()
				case COR_Expressions.Complement(argument=arg):
					match arg:
						case COR_Expressions.IdentityRelation:
							match arg2:
								case COR_Expressions.UniversalRelation():
									return COR_Expressions.Complement(COR_Expressions.IdentityRelation())
								case COR_Expressions.IdentityRelation:
									return COR_Expressions.EmptyRelation()
								case COR_Expressions.EmptyRelation():
									return COR_Expressions.EmptyRelation()
						case _:
							C = arg
							match arg2:
								case _ if str(C)==str(arg2):
									return COR_Expressions.EmptyRelation()
								case COR_Expressions.UniversalRelation():
									return COR_Expressions.Complement(C)
								case COR_Expressions.EmptyRelation():
									return COR_Expressions.EmptyRelation()
							B = arg
							match arg2:
								case COR_Expressions.EmptyRelation():
									return COR_Expressions.EmptyRelation()
								case COR_Expressions.UniversalRelation():
									return COR_Expressions.Complement(B)
								case _ if str(B)==str(arg2):
									return COR_Expressions.EmptyRelation()
							A = arg
							match arg2:
								case COR_Expressions.EmptyRelation():
									return COR_Expressions.EmptyRelation()
								case COR_Expressions.UniversalRelation():
									return COR_Expressions.Complement(A)
								case _ if str(A)==str(arg2):
									return COR_Expressions.EmptyRelation()
				case COR_Expressions.Converse(argument=arg):
					match arg:
						case _:
							B = arg
							match arg2:
								case COR_Expressions.UniversalRelation():
									return COR_Expressions.Converse(B)
								case COR_Expressions.IdentityRelation:
									return COR_Expressions.Intersection(B, COR_Expressions.IdentityRelation())
								case COR_Expressions.EmptyRelation():
									return COR_Expressions.EmptyRelation()
							A = arg
							match arg2:
								case COR_Expressions.EmptyRelation():
									return COR_Expressions.EmptyRelation()
								case COR_Expressions.UniversalRelation():
									return COR_Expressions.Converse(A)
								case COR_Expressions.IdentityRelation:
									return COR_Expressions.Intersection(A, COR_Expressions.IdentityRelation())
							C = arg
							match arg2:
								case COR_Expressions.EmptyRelation():
									return COR_Expressions.EmptyRelation()
								case COR_Expressions.IdentityRelation:
									return COR_Expressions.Intersection(C, COR_Expressions.IdentityRelation())
								case COR_Expressions.UniversalRelation():
									return COR_Expressions.Converse(C)
				case _:
					C = arg1
					match arg2:
						case COR_Expressions.EmptyRelation():
							return COR_Expressions.EmptyRelation()
						case _ if str(C)==str(arg2):
							return C
						case COR_Expressions.UniversalRelation():
							return C
						case COR_Expressions.Complement(argument=arg):
							match arg:
								case _ if str(C)==str(arg):
									return COR_Expressions.EmptyRelation()
					A = arg1
					match arg2:
						case _ if str(A)==str(arg2):
							return A
						case COR_Expressions.EmptyRelation():
							return COR_Expressions.EmptyRelation()
						case COR_Expressions.UniversalRelation():
							return A
						case COR_Expressions.Complement(argument=arg):
							match arg:
								case _ if str(A)==str(arg):
									return COR_Expressions.EmptyRelation()
					B = arg1
					match arg2:
						case COR_Expressions.EmptyRelation():
							return COR_Expressions.EmptyRelation()
						case COR_Expressions.UniversalRelation():
							return B
						case _ if str(B)==str(arg2):
							return B
						case COR_Expressions.Complement(argument=arg):
							match arg:
								case _ if str(B)==str(arg):
									return COR_Expressions.EmptyRelation()

	return None # The given expression was unable to be simplified