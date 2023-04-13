import COR_Expressions

def simplify(expression):
	# (T)⁻ = 𝟎
	match expression:
		case COR_Expressions.Complement(argument=arg):
			match arg:
				case COR_Expressions.UniversalRelation():
					return COR_Expressions.EmptyRelation()
	# (T)⁻¹ = T
	match expression:
		case COR_Expressions.Converse(argument=arg):
			match arg:
				case COR_Expressions.UniversalRelation():
					return COR_Expressions.UniversalRelation()
	# (𝟎)⁻¹ = 𝟎
	match expression:
		case COR_Expressions.Converse(argument=arg):
			match arg:
				case COR_Expressions.EmptyRelation():
					return COR_Expressions.EmptyRelation()
	# (𝟎)⁻ = T
	match expression:
		case COR_Expressions.Complement(argument=arg):
			match arg:
				case COR_Expressions.EmptyRelation():
					return COR_Expressions.UniversalRelation()
	# (𝟏)⁻¹ = 𝟏
	match expression:
		case COR_Expressions.Converse(argument=arg):
			match arg:
				case COR_Expressions.IdentityRelation:
					return COR_Expressions.IdentityRelation()
	# (T) ∪ ((B)⁻¹) = T
	match expression:
		case COR_Expressions.Union(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.UniversalRelation():
					match arg2:
						case COR_Expressions.Converse(argument=arg):
							match arg:
								case _:
									B = arg
									return COR_Expressions.UniversalRelation()
	# ((B)⁻)⁻ = B
	match expression:
		case COR_Expressions.Complement(argument=arg):
			match arg:
				case COR_Expressions.Complement(argument=arg):
					match arg:
						case _:
							B = arg
							return B
	# (T) ∪ ((A)⁻¹) = T
	match expression:
		case COR_Expressions.Union(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.UniversalRelation():
					match arg2:
						case COR_Expressions.Converse(argument=arg):
							match arg:
								case _:
									A = arg
									return COR_Expressions.UniversalRelation()
	# (T) † ((B)⁻) = T
	match expression:
		case COR_Expressions.Dagger(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.UniversalRelation():
					match arg2:
						case COR_Expressions.Complement(argument=arg):
							match arg:
								case _:
									B = arg
									return COR_Expressions.UniversalRelation()
	# (A) ∪ ((A)⁻) = T
	match expression:
		case COR_Expressions.Union(argument1=arg1, argument2=arg2):
			match arg1:
				case _:
					A = arg1
					match arg2:
						case COR_Expressions.Complement(argument=arg):
							match arg:
								case _:
									A = arg
									return COR_Expressions.UniversalRelation()
	# ((𝟏)⁻)⁻ = 𝟏
	match expression:
		case COR_Expressions.Complement(argument=arg):
			match arg:
				case COR_Expressions.Complement(argument=arg):
					match arg:
						case COR_Expressions.IdentityRelation:
							return COR_Expressions.IdentityRelation()
	# (𝟎) ∪ ((A)⁻¹) = (A)⁻¹
	match expression:
		case COR_Expressions.Union(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.EmptyRelation():
					match arg2:
						case COR_Expressions.Converse(argument=arg):
							match arg:
								case _:
									A = arg
									return COR_Expressions.Converse(A)
	# (𝟏) † ((𝟏)⁻) = 𝟏
	match expression:
		case COR_Expressions.Dagger(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.IdentityRelation:
					match arg2:
						case COR_Expressions.Complement(argument=arg):
							match arg:
								case COR_Expressions.IdentityRelation:
									return COR_Expressions.IdentityRelation()
	# (𝟎) ∪ ((B)⁻¹) = (B)⁻¹
	match expression:
		case COR_Expressions.Union(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.EmptyRelation():
					match arg2:
						case COR_Expressions.Converse(argument=arg):
							match arg:
								case _:
									B = arg
									return COR_Expressions.Converse(B)
	# (T) † ((B)⁻¹) = T
	match expression:
		case COR_Expressions.Dagger(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.UniversalRelation():
					match arg2:
						case COR_Expressions.Converse(argument=arg):
							match arg:
								case _:
									B = arg
									return COR_Expressions.UniversalRelation()
	# (C) ∪ ((C)⁻) = T
	match expression:
		case COR_Expressions.Union(argument1=arg1, argument2=arg2):
			match arg1:
				case _:
					C = arg1
					match arg2:
						case COR_Expressions.Complement(argument=arg):
							match arg:
								case _:
									C = arg
									return COR_Expressions.UniversalRelation()
	# (𝟏) ∘ ((C)⁻) = (C)⁻
	match expression:
		case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.IdentityRelation:
					match arg2:
						case COR_Expressions.Complement(argument=arg):
							match arg:
								case _:
									C = arg
									return COR_Expressions.Complement(C)
	# ((A)⁻¹)⁻¹ = A
	match expression:
		case COR_Expressions.Converse(argument=arg):
			match arg:
				case COR_Expressions.Converse(argument=arg):
					match arg:
						case _:
							A = arg
							return A
	# (𝟎) ∪ ((A)⁻) = (A)⁻
	match expression:
		case COR_Expressions.Union(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.EmptyRelation():
					match arg2:
						case COR_Expressions.Complement(argument=arg):
							match arg:
								case _:
									A = arg
									return COR_Expressions.Complement(A)
	# (T) † ((𝟏)⁻) = T
	match expression:
		case COR_Expressions.Dagger(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.UniversalRelation():
					match arg2:
						case COR_Expressions.Complement(argument=arg):
							match arg:
								case COR_Expressions.IdentityRelation:
									return COR_Expressions.UniversalRelation()
	# (𝟎) ∘ ((B)⁻¹) = 𝟎
	match expression:
		case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.EmptyRelation():
					match arg2:
						case COR_Expressions.Converse(argument=arg):
							match arg:
								case _:
									B = arg
									return COR_Expressions.EmptyRelation()
	# (B) † ((𝟏)⁻) = B
	match expression:
		case COR_Expressions.Dagger(argument1=arg1, argument2=arg2):
			match arg1:
				case _:
					B = arg1
					match arg2:
						case COR_Expressions.Complement(argument=arg):
							match arg:
								case COR_Expressions.IdentityRelation:
									return B
	# (T) † ((A)⁻¹) = T
	match expression:
		case COR_Expressions.Dagger(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.UniversalRelation():
					match arg2:
						case COR_Expressions.Converse(argument=arg):
							match arg:
								case _:
									A = arg
									return COR_Expressions.UniversalRelation()
	# (𝟏) ∘ ((A)⁻) = (A)⁻
	match expression:
		case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.IdentityRelation:
					match arg2:
						case COR_Expressions.Complement(argument=arg):
							match arg:
								case _:
									A = arg
									return COR_Expressions.Complement(A)
	# (T) ∪ ((A)⁻) = T
	match expression:
		case COR_Expressions.Union(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.UniversalRelation():
					match arg2:
						case COR_Expressions.Complement(argument=arg):
							match arg:
								case _:
									A = arg
									return COR_Expressions.UniversalRelation()
	# (𝟏) ∘ ((𝟏)⁻) = (𝟏)⁻
	match expression:
		case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.IdentityRelation:
					match arg2:
						case COR_Expressions.Complement(argument=arg):
							match arg:
								case COR_Expressions.IdentityRelation:
									return COR_Expressions.Complement(COR_Expressions.IdentityRelation())
	# ((A)⁻)⁻ = A
	match expression:
		case COR_Expressions.Complement(argument=arg):
			match arg:
				case COR_Expressions.Complement(argument=arg):
					match arg:
						case _:
							A = arg
							return A
	# (𝟎) ∘ ((B)⁻) = 𝟎
	match expression:
		case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.EmptyRelation():
					match arg2:
						case COR_Expressions.Complement(argument=arg):
							match arg:
								case _:
									B = arg
									return COR_Expressions.EmptyRelation()
	# (T) ∪ ((C)⁻¹) = T
	match expression:
		case COR_Expressions.Union(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.UniversalRelation():
					match arg2:
						case COR_Expressions.Converse(argument=arg):
							match arg:
								case _:
									C = arg
									return COR_Expressions.UniversalRelation()
	# (𝟎) ∪ ((B)⁻) = (B)⁻
	match expression:
		case COR_Expressions.Union(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.EmptyRelation():
					match arg2:
						case COR_Expressions.Complement(argument=arg):
							match arg:
								case _:
									B = arg
									return COR_Expressions.Complement(B)
	# ((𝟏)⁻)⁻¹ = (𝟏)⁻
	match expression:
		case COR_Expressions.Converse(argument=arg):
			match arg:
				case COR_Expressions.Complement(argument=arg):
					match arg:
						case COR_Expressions.IdentityRelation:
							return COR_Expressions.Complement(COR_Expressions.IdentityRelation())
	# (T) † ((A)⁻) = T
	match expression:
		case COR_Expressions.Dagger(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.UniversalRelation():
					match arg2:
						case COR_Expressions.Complement(argument=arg):
							match arg:
								case _:
									A = arg
									return COR_Expressions.UniversalRelation()
	# (𝟎) ∘ ((C)⁻¹) = 𝟎
	match expression:
		case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.EmptyRelation():
					match arg2:
						case COR_Expressions.Converse(argument=arg):
							match arg:
								case _:
									C = arg
									return COR_Expressions.EmptyRelation()
	# (T) ∪ ((C)⁻) = T
	match expression:
		case COR_Expressions.Union(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.UniversalRelation():
					match arg2:
						case COR_Expressions.Complement(argument=arg):
							match arg:
								case _:
									C = arg
									return COR_Expressions.UniversalRelation()
	# (𝟏) ∘ ((B)⁻¹) = (B)⁻¹
	match expression:
		case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.IdentityRelation:
					match arg2:
						case COR_Expressions.Converse(argument=arg):
							match arg:
								case _:
									B = arg
									return COR_Expressions.Converse(B)
	# (T) † ((C)⁻¹) = T
	match expression:
		case COR_Expressions.Dagger(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.UniversalRelation():
					match arg2:
						case COR_Expressions.Converse(argument=arg):
							match arg:
								case _:
									C = arg
									return COR_Expressions.UniversalRelation()
	# (T) † ((C)⁻) = T
	match expression:
		case COR_Expressions.Dagger(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.UniversalRelation():
					match arg2:
						case COR_Expressions.Complement(argument=arg):
							match arg:
								case _:
									C = arg
									return COR_Expressions.UniversalRelation()
	# (𝟎) ∘ ((C)⁻) = 𝟎
	match expression:
		case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.EmptyRelation():
					match arg2:
						case COR_Expressions.Complement(argument=arg):
							match arg:
								case _:
									C = arg
									return COR_Expressions.EmptyRelation()
	# (𝟎) ∪ ((C)⁻¹) = (C)⁻¹
	match expression:
		case COR_Expressions.Union(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.EmptyRelation():
					match arg2:
						case COR_Expressions.Converse(argument=arg):
							match arg:
								case _:
									C = arg
									return COR_Expressions.Converse(C)
	# (T) ∪ ((B)⁻) = T
	match expression:
		case COR_Expressions.Union(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.UniversalRelation():
					match arg2:
						case COR_Expressions.Complement(argument=arg):
							match arg:
								case _:
									B = arg
									return COR_Expressions.UniversalRelation()
	# (𝟎) ∪ ((C)⁻) = (C)⁻
	match expression:
		case COR_Expressions.Union(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.EmptyRelation():
					match arg2:
						case COR_Expressions.Complement(argument=arg):
							match arg:
								case _:
									C = arg
									return COR_Expressions.Complement(C)
	# (𝟏) ∘ ((B)⁻) = (B)⁻
	match expression:
		case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.IdentityRelation:
					match arg2:
						case COR_Expressions.Complement(argument=arg):
							match arg:
								case _:
									B = arg
									return COR_Expressions.Complement(B)
	# (𝟏) ∪ ((𝟏)⁻) = T
	match expression:
		case COR_Expressions.Union(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.IdentityRelation:
					match arg2:
						case COR_Expressions.Complement(argument=arg):
							match arg:
								case COR_Expressions.IdentityRelation:
									return COR_Expressions.UniversalRelation()
	# ((C)⁻)⁻ = C
	match expression:
		case COR_Expressions.Complement(argument=arg):
			match arg:
				case COR_Expressions.Complement(argument=arg):
					match arg:
						case _:
							C = arg
							return C
	# (𝟏) ∘ ((A)⁻¹) = (A)⁻¹
	match expression:
		case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.IdentityRelation:
					match arg2:
						case COR_Expressions.Converse(argument=arg):
							match arg:
								case _:
									A = arg
									return COR_Expressions.Converse(A)
	# (𝟎) ∪ ((𝟏)⁻) = (𝟏)⁻
	match expression:
		case COR_Expressions.Union(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.EmptyRelation():
					match arg2:
						case COR_Expressions.Complement(argument=arg):
							match arg:
								case COR_Expressions.IdentityRelation:
									return COR_Expressions.Complement(COR_Expressions.IdentityRelation())
	# (𝟎) † ((𝟏)⁻) = 𝟎
	match expression:
		case COR_Expressions.Dagger(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.EmptyRelation():
					match arg2:
						case COR_Expressions.Complement(argument=arg):
							match arg:
								case COR_Expressions.IdentityRelation:
									return COR_Expressions.EmptyRelation()
	# (𝟎) ∘ ((𝟏)⁻) = 𝟎
	match expression:
		case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.EmptyRelation():
					match arg2:
						case COR_Expressions.Complement(argument=arg):
							match arg:
								case COR_Expressions.IdentityRelation:
									return COR_Expressions.EmptyRelation()
	# ((B)⁻¹)⁻¹ = B
	match expression:
		case COR_Expressions.Converse(argument=arg):
			match arg:
				case COR_Expressions.Converse(argument=arg):
					match arg:
						case _:
							B = arg
							return B
	# ((C)⁻¹)⁻¹ = C
	match expression:
		case COR_Expressions.Converse(argument=arg):
			match arg:
				case COR_Expressions.Converse(argument=arg):
					match arg:
						case _:
							C = arg
							return C
	# (𝟎) ∘ ((A)⁻) = 𝟎
	match expression:
		case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.EmptyRelation():
					match arg2:
						case COR_Expressions.Complement(argument=arg):
							match arg:
								case _:
									A = arg
									return COR_Expressions.EmptyRelation()
	# (B) ∪ ((B)⁻) = T
	match expression:
		case COR_Expressions.Union(argument1=arg1, argument2=arg2):
			match arg1:
				case _:
					B = arg1
					match arg2:
						case COR_Expressions.Complement(argument=arg):
							match arg:
								case _:
									B = arg
									return COR_Expressions.UniversalRelation()
	# (A) † ((𝟏)⁻) = A
	match expression:
		case COR_Expressions.Dagger(argument1=arg1, argument2=arg2):
			match arg1:
				case _:
					A = arg1
					match arg2:
						case COR_Expressions.Complement(argument=arg):
							match arg:
								case COR_Expressions.IdentityRelation:
									return A
	# (𝟎) ∘ ((A)⁻¹) = 𝟎
	match expression:
		case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.EmptyRelation():
					match arg2:
						case COR_Expressions.Converse(argument=arg):
							match arg:
								case _:
									A = arg
									return COR_Expressions.EmptyRelation()
	# (C) † ((𝟏)⁻) = C
	match expression:
		case COR_Expressions.Dagger(argument1=arg1, argument2=arg2):
			match arg1:
				case _:
					C = arg1
					match arg2:
						case COR_Expressions.Complement(argument=arg):
							match arg:
								case COR_Expressions.IdentityRelation:
									return C
	# (𝟏) ∘ ((C)⁻¹) = (C)⁻¹
	match expression:
		case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.IdentityRelation:
					match arg2:
						case COR_Expressions.Converse(argument=arg):
							match arg:
								case _:
									C = arg
									return COR_Expressions.Converse(C)
	# (T) ∪ ((𝟏)⁻) = T
	match expression:
		case COR_Expressions.Union(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.UniversalRelation():
					match arg2:
						case COR_Expressions.Complement(argument=arg):
							match arg:
								case COR_Expressions.IdentityRelation:
									return COR_Expressions.UniversalRelation()
	# ((C) ∘ ((C)⁻¹))⁻¹ = (C) ∘ ((C)⁻¹)
	match expression:
		case COR_Expressions.Converse(argument=arg):
			match arg:
				case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
					match arg1:
						case _:
							C = arg1
							match arg2:
								case COR_Expressions.Converse(argument=arg):
									match arg:
										case _:
											C = arg
											return COR_Expressions.Composition(C, COR_Expressions.Converse(C))
	# (T) ∘ ((T) ∘ ((A)⁻¹)) = (T) ∘ ((A)⁻¹)
	match expression:
		case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
			match arg1:
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
	# ((B)⁻) ∪ ((B)⁻) = (B)⁻
	match expression:
		case COR_Expressions.Union(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.Complement(argument=arg):
					match arg:
						case _:
							B = arg
							match arg2:
								case COR_Expressions.Complement(argument=arg):
									match arg:
										case _:
											B = arg
											return COR_Expressions.Complement(B)
	# (𝟎) ∘ ((𝟏) ∪ ((C)⁻)) = 𝟎
	match expression:
		case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.EmptyRelation():
					match arg2:
						case COR_Expressions.Union(argument1=arg1, argument2=arg2):
							match arg1:
								case COR_Expressions.IdentityRelation:
									match arg2:
										case COR_Expressions.Complement(argument=arg):
											match arg:
												case _:
													C = arg
													return COR_Expressions.EmptyRelation()
	# (T) ∪ ((T) ∘ ((C)⁻¹)) = T
	match expression:
		case COR_Expressions.Union(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.UniversalRelation():
					match arg2:
						case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
							match arg1:
								case COR_Expressions.UniversalRelation():
									match arg2:
										case COR_Expressions.Converse(argument=arg):
											match arg:
												case _:
													C = arg
													return COR_Expressions.UniversalRelation()
	# (𝟎) ∪ ((𝟎) † ((B)⁻¹)) = (𝟎) † ((B)⁻¹)
	match expression:
		case COR_Expressions.Union(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.EmptyRelation():
					match arg2:
						case COR_Expressions.Dagger(argument1=arg1, argument2=arg2):
							match arg1:
								case COR_Expressions.EmptyRelation():
									match arg2:
										case COR_Expressions.Converse(argument=arg):
											match arg:
												case _:
													B = arg
													return COR_Expressions.Dagger(COR_Expressions.EmptyRelation(), COR_Expressions.Converse(B))
	# (𝟏) ∘ ((B) ∪ ((A)⁻¹)) = (B) ∪ ((A)⁻¹)
	match expression:
		case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.IdentityRelation:
					match arg2:
						case COR_Expressions.Union(argument1=arg1, argument2=arg2):
							match arg1:
								case _:
									B = arg1
									match arg2:
										case COR_Expressions.Converse(argument=arg):
											match arg:
												case _:
													A = arg
													return COR_Expressions.Union(B, COR_Expressions.Converse(A))
	# (𝟎) ∪ ((A) ∘ ((C)⁻)) = (A) ∘ ((C)⁻)
	match expression:
		case COR_Expressions.Union(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.EmptyRelation():
					match arg2:
						case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
							match arg1:
								case _:
									A = arg1
									match arg2:
										case COR_Expressions.Complement(argument=arg):
											match arg:
												case _:
													C = arg
													return COR_Expressions.Composition(A, COR_Expressions.Complement(C))
	# (T) † (((C)⁻¹)⁻) = T
	match expression:
		case COR_Expressions.Dagger(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.UniversalRelation():
					match arg2:
						case COR_Expressions.Complement(argument=arg):
							match arg:
								case COR_Expressions.Converse(argument=arg):
									match arg:
										case _:
											C = arg
											return COR_Expressions.UniversalRelation()
	# (𝟎) ∘ ((C) ∘ ((A)⁻)) = 𝟎
	match expression:
		case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.EmptyRelation():
					match arg2:
						case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
							match arg1:
								case _:
									C = arg1
									match arg2:
										case COR_Expressions.Complement(argument=arg):
											match arg:
												case _:
													A = arg
													return COR_Expressions.EmptyRelation()
	# (T) ∪ (((A)⁻)⁻¹) = T
	match expression:
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
	# (𝟎) ∘ ((𝟏) † ((A)⁻¹)) = 𝟎
	match expression:
		case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.EmptyRelation():
					match arg2:
						case COR_Expressions.Dagger(argument1=arg1, argument2=arg2):
							match arg1:
								case COR_Expressions.IdentityRelation:
									match arg2:
										case COR_Expressions.Converse(argument=arg):
											match arg:
												case _:
													A = arg
													return COR_Expressions.EmptyRelation()
	# (T) ∪ ((C) ∪ ((A)⁻)) = T
	match expression:
		case COR_Expressions.Union(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.UniversalRelation():
					match arg2:
						case COR_Expressions.Union(argument1=arg1, argument2=arg2):
							match arg1:
								case _:
									C = arg1
									match arg2:
										case COR_Expressions.Complement(argument=arg):
											match arg:
												case _:
													A = arg
													return COR_Expressions.UniversalRelation()
	# (T) † ((𝟎) † ((B)⁻)) = T
	match expression:
		case COR_Expressions.Dagger(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.UniversalRelation():
					match arg2:
						case COR_Expressions.Dagger(argument1=arg1, argument2=arg2):
							match arg1:
								case COR_Expressions.EmptyRelation():
									match arg2:
										case COR_Expressions.Complement(argument=arg):
											match arg:
												case _:
													B = arg
													return COR_Expressions.UniversalRelation()
	# (T) ∪ ((A) ∪ ((C)⁻)) = T
	match expression:
		case COR_Expressions.Union(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.UniversalRelation():
					match arg2:
						case COR_Expressions.Union(argument1=arg1, argument2=arg2):
							match arg1:
								case _:
									A = arg1
									match arg2:
										case COR_Expressions.Complement(argument=arg):
											match arg:
												case _:
													C = arg
													return COR_Expressions.UniversalRelation()
	# (𝟏) ∘ ((𝟏) ∪ ((C)⁻)) = (𝟏) ∪ ((C)⁻)
	match expression:
		case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.IdentityRelation:
					match arg2:
						case COR_Expressions.Union(argument1=arg1, argument2=arg2):
							match arg1:
								case COR_Expressions.IdentityRelation:
									match arg2:
										case COR_Expressions.Complement(argument=arg):
											match arg:
												case _:
													C = arg
													return COR_Expressions.Union(COR_Expressions.IdentityRelation(), COR_Expressions.Complement(C))
	# (T) † ((B) ∘ ((A)⁻¹)) = T
	match expression:
		case COR_Expressions.Dagger(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.UniversalRelation():
					match arg2:
						case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
							match arg1:
								case _:
									B = arg1
									match arg2:
										case COR_Expressions.Converse(argument=arg):
											match arg:
												case _:
													A = arg
													return COR_Expressions.UniversalRelation()
	# (T) ∘ ((𝟏) ∪ ((C)⁻)) = T
	match expression:
		case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.UniversalRelation():
					match arg2:
						case COR_Expressions.Union(argument1=arg1, argument2=arg2):
							match arg1:
								case COR_Expressions.IdentityRelation:
									match arg2:
										case COR_Expressions.Complement(argument=arg):
											match arg:
												case _:
													C = arg
													return COR_Expressions.UniversalRelation()
	# (B) ∪ ((B) ∪ ((A)⁻¹)) = (B) ∪ ((A)⁻¹)
	match expression:
		case COR_Expressions.Union(argument1=arg1, argument2=arg2):
			match arg1:
				case _:
					B = arg1
					match arg2:
						case COR_Expressions.Union(argument1=arg1, argument2=arg2):
							match arg1:
								case _:
									B = arg1
									match arg2:
										case COR_Expressions.Converse(argument=arg):
											match arg:
												case _:
													A = arg
													return COR_Expressions.Union(B, COR_Expressions.Converse(A))
	# (T) † ((A) † ((C)⁻¹)) = T
	match expression:
		case COR_Expressions.Dagger(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.UniversalRelation():
					match arg2:
						case COR_Expressions.Dagger(argument1=arg1, argument2=arg2):
							match arg1:
								case _:
									A = arg1
									match arg2:
										case COR_Expressions.Converse(argument=arg):
											match arg:
												case _:
													C = arg
													return COR_Expressions.UniversalRelation()
	# (C) ∪ ((T) ∘ ((C)⁻)) = T
	match expression:
		case COR_Expressions.Union(argument1=arg1, argument2=arg2):
			match arg1:
				case _:
					C = arg1
					match arg2:
						case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
							match arg1:
								case COR_Expressions.UniversalRelation():
									match arg2:
										case COR_Expressions.Complement(argument=arg):
											match arg:
												case _:
													C = arg
													return COR_Expressions.UniversalRelation()
	# (T) ∪ ((C) † ((B)⁻¹)) = T
	match expression:
		case COR_Expressions.Union(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.UniversalRelation():
					match arg2:
						case COR_Expressions.Dagger(argument1=arg1, argument2=arg2):
							match arg1:
								case _:
									C = arg1
									match arg2:
										case COR_Expressions.Converse(argument=arg):
											match arg:
												case _:
													B = arg
													return COR_Expressions.UniversalRelation()
	# (𝟎) ∘ ((C) † ((A)⁻¹)) = 𝟎
	match expression:
		case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.EmptyRelation():
					match arg2:
						case COR_Expressions.Dagger(argument1=arg1, argument2=arg2):
							match arg1:
								case _:
									C = arg1
									match arg2:
										case COR_Expressions.Converse(argument=arg):
											match arg:
												case _:
													A = arg
													return COR_Expressions.EmptyRelation()
	# (𝟎) ∘ ((C) † ((C)⁻)) = 𝟎
	match expression:
		case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.EmptyRelation():
					match arg2:
						case COR_Expressions.Dagger(argument1=arg1, argument2=arg2):
							match arg1:
								case _:
									C = arg1
									match arg2:
										case COR_Expressions.Complement(argument=arg):
											match arg:
												case _:
													C = arg
													return COR_Expressions.EmptyRelation()
	# (𝟎) ∘ ((B) ∘ ((𝟏)⁻)) = 𝟎
	match expression:
		case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.EmptyRelation():
					match arg2:
						case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
							match arg1:
								case _:
									B = arg1
									match arg2:
										case COR_Expressions.Complement(argument=arg):
											match arg:
												case COR_Expressions.IdentityRelation:
													return COR_Expressions.EmptyRelation()
	# (T) † ((B) ∘ ((C)⁻¹)) = T
	match expression:
		case COR_Expressions.Dagger(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.UniversalRelation():
					match arg2:
						case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
							match arg1:
								case _:
									B = arg1
									match arg2:
										case COR_Expressions.Converse(argument=arg):
											match arg:
												case _:
													C = arg
													return COR_Expressions.UniversalRelation()
	# (𝟎) ∘ ((A) † ((B)⁻¹)) = 𝟎
	match expression:
		case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.EmptyRelation():
					match arg2:
						case COR_Expressions.Dagger(argument1=arg1, argument2=arg2):
							match arg1:
								case _:
									A = arg1
									match arg2:
										case COR_Expressions.Converse(argument=arg):
											match arg:
												case _:
													B = arg
													return COR_Expressions.EmptyRelation()
	# (A) ∪ ((B) ∪ ((A)⁻)) = T
	match expression:
		case COR_Expressions.Union(argument1=arg1, argument2=arg2):
			match arg1:
				case _:
					A = arg1
					match arg2:
						case COR_Expressions.Union(argument1=arg1, argument2=arg2):
							match arg1:
								case _:
									B = arg1
									match arg2:
										case COR_Expressions.Complement(argument=arg):
											match arg:
												case _:
													A = arg
													return COR_Expressions.UniversalRelation()
	# (𝟎) ∘ ((T) ∘ ((A)⁻¹)) = 𝟎
	match expression:
		case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.EmptyRelation():
					match arg2:
						case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
							match arg1:
								case COR_Expressions.UniversalRelation():
									match arg2:
										case COR_Expressions.Converse(argument=arg):
											match arg:
												case _:
													A = arg
													return COR_Expressions.EmptyRelation()
	# (𝟎) ∪ (((C)⁻¹)⁻) = ((C)⁻)⁻¹
	match expression:
		case COR_Expressions.Union(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.EmptyRelation():
					match arg2:
						case COR_Expressions.Complement(argument=arg):
							match arg:
								case COR_Expressions.Converse(argument=arg):
									match arg:
										case _:
											C = arg
											return COR_Expressions.Converse(COR_Expressions.Complement(C))
	# (𝟎) ∪ (((A)⁻)⁻¹) = ((A)⁻)⁻¹
	match expression:
		case COR_Expressions.Union(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.EmptyRelation():
					match arg2:
						case COR_Expressions.Converse(argument=arg):
							match arg:
								case COR_Expressions.Complement(argument=arg):
									match arg:
										case _:
											A = arg
											return COR_Expressions.Converse(COR_Expressions.Complement(A))
	# (T) † ((B) † ((B)⁻¹)) = T
	match expression:
		case COR_Expressions.Dagger(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.UniversalRelation():
					match arg2:
						case COR_Expressions.Dagger(argument1=arg1, argument2=arg2):
							match arg1:
								case _:
									B = arg1
									match arg2:
										case COR_Expressions.Converse(argument=arg):
											match arg:
												case _:
													B = arg
													return COR_Expressions.UniversalRelation()
	# (T) ∘ ((B) ∘ ((B)⁻¹)) = (T) ∘ ((B)⁻¹)
	match expression:
		case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.UniversalRelation():
					match arg2:
						case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
							match arg1:
								case _:
									B = arg1
									match arg2:
										case COR_Expressions.Converse(argument=arg):
											match arg:
												case _:
													B = arg
													return COR_Expressions.Composition(COR_Expressions.UniversalRelation(), COR_Expressions.Converse(B))
	# ((𝟏)⁻) † ((A)⁻) = (A)⁻
	match expression:
		case COR_Expressions.Dagger(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.Complement(argument=arg):
					match arg:
						case COR_Expressions.IdentityRelation:
							match arg2:
								case COR_Expressions.Complement(argument=arg):
									match arg:
										case _:
											A = arg
											return COR_Expressions.Complement(A)
	# (T) ∘ ((T) ∘ ((C)⁻)) = (T) ∘ ((C)⁻)
	match expression:
		case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.UniversalRelation():
					match arg2:
						case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
							match arg1:
								case COR_Expressions.UniversalRelation():
									match arg2:
										case COR_Expressions.Complement(argument=arg):
											match arg:
												case _:
													C = arg
													return COR_Expressions.Composition(COR_Expressions.UniversalRelation(), COR_Expressions.Complement(C))
	# (T) † ((C) † ((C)⁻)) = T
	match expression:
		case COR_Expressions.Dagger(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.UniversalRelation():
					match arg2:
						case COR_Expressions.Dagger(argument1=arg1, argument2=arg2):
							match arg1:
								case _:
									C = arg1
									match arg2:
										case COR_Expressions.Complement(argument=arg):
											match arg:
												case _:
													C = arg
													return COR_Expressions.UniversalRelation()
	# (T) † (((B)⁻)⁻¹) = T
	match expression:
		case COR_Expressions.Dagger(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.UniversalRelation():
					match arg2:
						case COR_Expressions.Converse(argument=arg):
							match arg:
								case COR_Expressions.Complement(argument=arg):
									match arg:
										case _:
											B = arg
											return COR_Expressions.UniversalRelation()
	# (𝟏) ∘ ((𝟏) † ((B)⁻)) = (𝟏) † ((B)⁻)
	match expression:
		case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.IdentityRelation:
					match arg2:
						case COR_Expressions.Dagger(argument1=arg1, argument2=arg2):
							match arg1:
								case COR_Expressions.IdentityRelation:
									match arg2:
										case COR_Expressions.Complement(argument=arg):
											match arg:
												case _:
													B = arg
													return COR_Expressions.Dagger(COR_Expressions.IdentityRelation(), COR_Expressions.Complement(B))
	# (A) ∪ ((A) ∪ ((𝟏)⁻)) = (A) ∪ ((𝟏)⁻)
	match expression:
		case COR_Expressions.Union(argument1=arg1, argument2=arg2):
			match arg1:
				case _:
					A = arg1
					match arg2:
						case COR_Expressions.Union(argument1=arg1, argument2=arg2):
							match arg1:
								case _:
									A = arg1
									match arg2:
										case COR_Expressions.Complement(argument=arg):
											match arg:
												case COR_Expressions.IdentityRelation:
													return COR_Expressions.Union(A, COR_Expressions.Complement(COR_Expressions.IdentityRelation()))
	# (T) † ((A) ∪ ((B)⁻¹)) = T
	match expression:
		case COR_Expressions.Dagger(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.UniversalRelation():
					match arg2:
						case COR_Expressions.Union(argument1=arg1, argument2=arg2):
							match arg1:
								case _:
									A = arg1
									match arg2:
										case COR_Expressions.Converse(argument=arg):
											match arg:
												case _:
													B = arg
													return COR_Expressions.UniversalRelation()
	# (T) † ((A) † ((C)⁻)) = T
	match expression:
		case COR_Expressions.Dagger(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.UniversalRelation():
					match arg2:
						case COR_Expressions.Dagger(argument1=arg1, argument2=arg2):
							match arg1:
								case _:
									A = arg1
									match arg2:
										case COR_Expressions.Complement(argument=arg):
											match arg:
												case _:
													C = arg
													return COR_Expressions.UniversalRelation()
	# (𝟎) ∪ ((A) ∪ ((B)⁻)) = (A) ∪ ((B)⁻)
	match expression:
		case COR_Expressions.Union(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.EmptyRelation():
					match arg2:
						case COR_Expressions.Union(argument1=arg1, argument2=arg2):
							match arg1:
								case _:
									A = arg1
									match arg2:
										case COR_Expressions.Complement(argument=arg):
											match arg:
												case _:
													B = arg
													return COR_Expressions.Union(A, COR_Expressions.Complement(B))
	# (T) † ((B) † ((B)⁻)) = T
	match expression:
		case COR_Expressions.Dagger(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.UniversalRelation():
					match arg2:
						case COR_Expressions.Dagger(argument1=arg1, argument2=arg2):
							match arg1:
								case _:
									B = arg1
									match arg2:
										case COR_Expressions.Complement(argument=arg):
											match arg:
												case _:
													B = arg
													return COR_Expressions.UniversalRelation()
	# (B) ∪ ((C) ∪ ((B)⁻)) = T
	match expression:
		case COR_Expressions.Union(argument1=arg1, argument2=arg2):
			match arg1:
				case _:
					B = arg1
					match arg2:
						case COR_Expressions.Union(argument1=arg1, argument2=arg2):
							match arg1:
								case _:
									C = arg1
									match arg2:
										case COR_Expressions.Complement(argument=arg):
											match arg:
												case _:
													B = arg
													return COR_Expressions.UniversalRelation()
	# (T) ∘ ((𝟎) † ((A)⁻)) = (𝟎) † ((A)⁻)
	match expression:
		case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.UniversalRelation():
					match arg2:
						case COR_Expressions.Dagger(argument1=arg1, argument2=arg2):
							match arg1:
								case COR_Expressions.EmptyRelation():
									match arg2:
										case COR_Expressions.Complement(argument=arg):
											match arg:
												case _:
													A = arg
													return COR_Expressions.Dagger(COR_Expressions.EmptyRelation(), COR_Expressions.Complement(A))
	# (T) ∪ ((B) ∪ ((A)⁻¹)) = T
	match expression:
		case COR_Expressions.Union(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.UniversalRelation():
					match arg2:
						case COR_Expressions.Union(argument1=arg1, argument2=arg2):
							match arg1:
								case _:
									B = arg1
									match arg2:
										case COR_Expressions.Converse(argument=arg):
											match arg:
												case _:
													A = arg
													return COR_Expressions.UniversalRelation()
	# (𝟎) ∘ ((B) ∘ ((B)⁻)) = 𝟎
	match expression:
		case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.EmptyRelation():
					match arg2:
						case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
							match arg1:
								case _:
									B = arg1
									match arg2:
										case COR_Expressions.Complement(argument=arg):
											match arg:
												case _:
													B = arg
													return COR_Expressions.EmptyRelation()
	# (𝟎) ∘ ((C) † ((A)⁻)) = 𝟎
	match expression:
		case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.EmptyRelation():
					match arg2:
						case COR_Expressions.Dagger(argument1=arg1, argument2=arg2):
							match arg1:
								case _:
									C = arg1
									match arg2:
										case COR_Expressions.Complement(argument=arg):
											match arg:
												case _:
													A = arg
													return COR_Expressions.EmptyRelation()
	# ((B) ∪ ((A)⁻¹))⁻¹ = (A) ∪ ((B)⁻¹)
	match expression:
		case COR_Expressions.Converse(argument=arg):
			match arg:
				case COR_Expressions.Union(argument1=arg1, argument2=arg2):
					match arg1:
						case _:
							B = arg1
							match arg2:
								case COR_Expressions.Converse(argument=arg):
									match arg:
										case _:
											A = arg
											return COR_Expressions.Union(A, COR_Expressions.Converse(B))
	# (𝟎) ∪ ((C) † ((A)⁻)) = (C) † ((A)⁻)
	match expression:
		case COR_Expressions.Union(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.EmptyRelation():
					match arg2:
						case COR_Expressions.Dagger(argument1=arg1, argument2=arg2):
							match arg1:
								case _:
									C = arg1
									match arg2:
										case COR_Expressions.Complement(argument=arg):
											match arg:
												case _:
													A = arg
													return COR_Expressions.Dagger(C, COR_Expressions.Complement(A))
	# (T) † ((C) ∪ ((B)⁻¹)) = T
	match expression:
		case COR_Expressions.Dagger(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.UniversalRelation():
					match arg2:
						case COR_Expressions.Union(argument1=arg1, argument2=arg2):
							match arg1:
								case _:
									C = arg1
									match arg2:
										case COR_Expressions.Converse(argument=arg):
											match arg:
												case _:
													B = arg
													return COR_Expressions.UniversalRelation()
	# (𝟎) ∘ ((B) ∪ ((A)⁻)) = 𝟎
	match expression:
		case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.EmptyRelation():
					match arg2:
						case COR_Expressions.Union(argument1=arg1, argument2=arg2):
							match arg1:
								case _:
									B = arg1
									match arg2:
										case COR_Expressions.Complement(argument=arg):
											match arg:
												case _:
													A = arg
													return COR_Expressions.EmptyRelation()
	# (𝟎) ∘ ((B) † ((A)⁻¹)) = 𝟎
	match expression:
		case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.EmptyRelation():
					match arg2:
						case COR_Expressions.Dagger(argument1=arg1, argument2=arg2):
							match arg1:
								case _:
									B = arg1
									match arg2:
										case COR_Expressions.Converse(argument=arg):
											match arg:
												case _:
													A = arg
													return COR_Expressions.EmptyRelation()
	# (𝟎) ∪ ((A) ∘ ((A)⁻¹)) = (A) ∘ ((A)⁻¹)
	match expression:
		case COR_Expressions.Union(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.EmptyRelation():
					match arg2:
						case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
							match arg1:
								case _:
									A = arg1
									match arg2:
										case COR_Expressions.Converse(argument=arg):
											match arg:
												case _:
													A = arg
													return COR_Expressions.Composition(A, COR_Expressions.Converse(A))
	# (𝟎) † ((𝟎) † ((B)⁻)) = (𝟎) † ((B)⁻)
	match expression:
		case COR_Expressions.Dagger(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.EmptyRelation():
					match arg2:
						case COR_Expressions.Dagger(argument1=arg1, argument2=arg2):
							match arg1:
								case COR_Expressions.EmptyRelation():
									match arg2:
										case COR_Expressions.Complement(argument=arg):
											match arg:
												case _:
													B = arg
													return COR_Expressions.Dagger(COR_Expressions.EmptyRelation(), COR_Expressions.Complement(B))
	# (𝟎) ∘ ((A) † ((A)⁻¹)) = 𝟎
	match expression:
		case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.EmptyRelation():
					match arg2:
						case COR_Expressions.Dagger(argument1=arg1, argument2=arg2):
							match arg1:
								case _:
									A = arg1
									match arg2:
										case COR_Expressions.Converse(argument=arg):
											match arg:
												case _:
													A = arg
													return COR_Expressions.EmptyRelation()
	# (𝟏) ∘ ((B) ∘ ((C)⁻¹)) = (B) ∘ ((C)⁻¹)
	match expression:
		case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.IdentityRelation:
					match arg2:
						case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
							match arg1:
								case _:
									B = arg1
									match arg2:
										case COR_Expressions.Converse(argument=arg):
											match arg:
												case _:
													C = arg
													return COR_Expressions.Composition(B, COR_Expressions.Converse(C))
	# (𝟏) ∘ ((A) ∘ ((A)⁻)) = (A) ∘ ((A)⁻)
	match expression:
		case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.IdentityRelation:
					match arg2:
						case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
							match arg1:
								case _:
									A = arg1
									match arg2:
										case COR_Expressions.Complement(argument=arg):
											match arg:
												case _:
													A = arg
													return COR_Expressions.Composition(A, COR_Expressions.Complement(A))
	# ((B) ∘ ((C)⁻¹))⁻¹ = (C) ∘ ((B)⁻¹)
	match expression:
		case COR_Expressions.Converse(argument=arg):
			match arg:
				case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
					match arg1:
						case _:
							B = arg1
							match arg2:
								case COR_Expressions.Converse(argument=arg):
									match arg:
										case _:
											C = arg
											return COR_Expressions.Composition(C, COR_Expressions.Converse(B))
	# ((A) ∪ ((C)⁻¹))⁻¹ = (C) ∪ ((A)⁻¹)
	match expression:
		case COR_Expressions.Converse(argument=arg):
			match arg:
				case COR_Expressions.Union(argument1=arg1, argument2=arg2):
					match arg1:
						case _:
							A = arg1
							match arg2:
								case COR_Expressions.Converse(argument=arg):
									match arg:
										case _:
											C = arg
											return COR_Expressions.Union(C, COR_Expressions.Converse(A))
	# (𝟎) ∪ ((A) † ((B)⁻)) = (A) † ((B)⁻)
	match expression:
		case COR_Expressions.Union(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.EmptyRelation():
					match arg2:
						case COR_Expressions.Dagger(argument1=arg1, argument2=arg2):
							match arg1:
								case _:
									A = arg1
									match arg2:
										case COR_Expressions.Complement(argument=arg):
											match arg:
												case _:
													B = arg
													return COR_Expressions.Dagger(A, COR_Expressions.Complement(B))
	# (T) ∘ ((T) ∘ ((C)⁻¹)) = (T) ∘ ((C)⁻¹)
	match expression:
		case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.UniversalRelation():
					match arg2:
						case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
							match arg1:
								case COR_Expressions.UniversalRelation():
									match arg2:
										case COR_Expressions.Converse(argument=arg):
											match arg:
												case _:
													C = arg
													return COR_Expressions.Composition(COR_Expressions.UniversalRelation(), COR_Expressions.Converse(C))
	# ((A) ∘ ((A)⁻¹))⁻¹ = (A) ∘ ((A)⁻¹)
	match expression:
		case COR_Expressions.Converse(argument=arg):
			match arg:
				case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
					match arg1:
						case _:
							A = arg1
							match arg2:
								case COR_Expressions.Converse(argument=arg):
									match arg:
										case _:
											A = arg
											return COR_Expressions.Composition(A, COR_Expressions.Converse(A))
	# (A) ∪ ((A) ∪ ((C)⁻)) = (A) ∪ ((C)⁻)
	match expression:
		case COR_Expressions.Union(argument1=arg1, argument2=arg2):
			match arg1:
				case _:
					A = arg1
					match arg2:
						case COR_Expressions.Union(argument1=arg1, argument2=arg2):
							match arg1:
								case _:
									A = arg1
									match arg2:
										case COR_Expressions.Complement(argument=arg):
											match arg:
												case _:
													C = arg
													return COR_Expressions.Union(A, COR_Expressions.Complement(C))
	# (B) ∪ ((T) ∘ ((B)⁻)) = T
	match expression:
		case COR_Expressions.Union(argument1=arg1, argument2=arg2):
			match arg1:
				case _:
					B = arg1
					match arg2:
						case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
							match arg1:
								case COR_Expressions.UniversalRelation():
									match arg2:
										case COR_Expressions.Complement(argument=arg):
											match arg:
												case _:
													B = arg
													return COR_Expressions.UniversalRelation()
	# (𝟎) ∪ ((A) † ((A)⁻)) = (A) † ((A)⁻)
	match expression:
		case COR_Expressions.Union(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.EmptyRelation():
					match arg2:
						case COR_Expressions.Dagger(argument1=arg1, argument2=arg2):
							match arg1:
								case _:
									A = arg1
									match arg2:
										case COR_Expressions.Complement(argument=arg):
											match arg:
												case _:
													A = arg
													return COR_Expressions.Dagger(A, COR_Expressions.Complement(A))
	# (𝟎) ∪ ((A) ∘ ((A)⁻)) = (A) ∘ ((A)⁻)
	match expression:
		case COR_Expressions.Union(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.EmptyRelation():
					match arg2:
						case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
							match arg1:
								case _:
									A = arg1
									match arg2:
										case COR_Expressions.Complement(argument=arg):
											match arg:
												case _:
													A = arg
													return COR_Expressions.Composition(A, COR_Expressions.Complement(A))
	# (𝟎) ∪ ((A) ∪ ((𝟏)⁻)) = (A) ∪ ((𝟏)⁻)
	match expression:
		case COR_Expressions.Union(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.EmptyRelation():
					match arg2:
						case COR_Expressions.Union(argument1=arg1, argument2=arg2):
							match arg1:
								case _:
									A = arg1
									match arg2:
										case COR_Expressions.Complement(argument=arg):
											match arg:
												case COR_Expressions.IdentityRelation:
													return COR_Expressions.Union(A, COR_Expressions.Complement(COR_Expressions.IdentityRelation()))
	# (T) ∪ ((T) ∘ ((B)⁻¹)) = T
	match expression:
		case COR_Expressions.Union(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.UniversalRelation():
					match arg2:
						case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
							match arg1:
								case COR_Expressions.UniversalRelation():
									match arg2:
										case COR_Expressions.Converse(argument=arg):
											match arg:
												case _:
													B = arg
													return COR_Expressions.UniversalRelation()
	# ((C) † ((C)⁻¹))⁻¹ = (C) † ((C)⁻¹)
	match expression:
		case COR_Expressions.Converse(argument=arg):
			match arg:
				case COR_Expressions.Dagger(argument1=arg1, argument2=arg2):
					match arg1:
						case _:
							C = arg1
							match arg2:
								case COR_Expressions.Converse(argument=arg):
									match arg:
										case _:
											C = arg
											return COR_Expressions.Dagger(C, COR_Expressions.Converse(C))
	# (T) † ((𝟎) † ((A)⁻¹)) = T
	match expression:
		case COR_Expressions.Dagger(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.UniversalRelation():
					match arg2:
						case COR_Expressions.Dagger(argument1=arg1, argument2=arg2):
							match arg1:
								case COR_Expressions.EmptyRelation():
									match arg2:
										case COR_Expressions.Converse(argument=arg):
											match arg:
												case _:
													A = arg
													return COR_Expressions.UniversalRelation()
	# (𝟏) ∘ ((C) ∘ ((B)⁻)) = (C) ∘ ((B)⁻)
	match expression:
		case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.IdentityRelation:
					match arg2:
						case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
							match arg1:
								case _:
									C = arg1
									match arg2:
										case COR_Expressions.Complement(argument=arg):
											match arg:
												case _:
													B = arg
													return COR_Expressions.Composition(C, COR_Expressions.Complement(B))
	# (𝟎) ∪ ((C) ∘ ((A)⁻)) = (C) ∘ ((A)⁻)
	match expression:
		case COR_Expressions.Union(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.EmptyRelation():
					match arg2:
						case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
							match arg1:
								case _:
									C = arg1
									match arg2:
										case COR_Expressions.Complement(argument=arg):
											match arg:
												case _:
													A = arg
													return COR_Expressions.Composition(C, COR_Expressions.Complement(A))
	# (T) ∪ ((𝟏) † ((B)⁻¹)) = T
	match expression:
		case COR_Expressions.Union(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.UniversalRelation():
					match arg2:
						case COR_Expressions.Dagger(argument1=arg1, argument2=arg2):
							match arg1:
								case COR_Expressions.IdentityRelation:
									match arg2:
										case COR_Expressions.Converse(argument=arg):
											match arg:
												case _:
													B = arg
													return COR_Expressions.UniversalRelation()
	# (𝟏) ∘ ((C) † ((C)⁻)) = (C) † ((C)⁻)
	match expression:
		case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.IdentityRelation:
					match arg2:
						case COR_Expressions.Dagger(argument1=arg1, argument2=arg2):
							match arg1:
								case _:
									C = arg1
									match arg2:
										case COR_Expressions.Complement(argument=arg):
											match arg:
												case _:
													C = arg
													return COR_Expressions.Dagger(C, COR_Expressions.Complement(C))
	# (T) ∘ ((𝟎) † ((C)⁻¹)) = (𝟎) † ((C)⁻¹)
	match expression:
		case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.UniversalRelation():
					match arg2:
						case COR_Expressions.Dagger(argument1=arg1, argument2=arg2):
							match arg1:
								case COR_Expressions.EmptyRelation():
									match arg2:
										case COR_Expressions.Converse(argument=arg):
											match arg:
												case _:
													C = arg
													return COR_Expressions.Dagger(COR_Expressions.EmptyRelation(), COR_Expressions.Converse(C))
	# (𝟎) ∪ ((C) ∪ ((C)⁻¹)) = (C) ∪ ((C)⁻¹)
	match expression:
		case COR_Expressions.Union(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.EmptyRelation():
					match arg2:
						case COR_Expressions.Union(argument1=arg1, argument2=arg2):
							match arg1:
								case _:
									C = arg1
									match arg2:
										case COR_Expressions.Converse(argument=arg):
											match arg:
												case _:
													C = arg
													return COR_Expressions.Union(C, COR_Expressions.Converse(C))
	# (𝟎) † ((𝟎) † ((C)⁻)) = (𝟎) † ((C)⁻)
	match expression:
		case COR_Expressions.Dagger(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.EmptyRelation():
					match arg2:
						case COR_Expressions.Dagger(argument1=arg1, argument2=arg2):
							match arg1:
								case COR_Expressions.EmptyRelation():
									match arg2:
										case COR_Expressions.Complement(argument=arg):
											match arg:
												case _:
													C = arg
													return COR_Expressions.Dagger(COR_Expressions.EmptyRelation(), COR_Expressions.Complement(C))
	# (T) ∪ ((A) ∪ ((A)⁻¹)) = T
	match expression:
		case COR_Expressions.Union(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.UniversalRelation():
					match arg2:
						case COR_Expressions.Union(argument1=arg1, argument2=arg2):
							match arg1:
								case _:
									A = arg1
									match arg2:
										case COR_Expressions.Converse(argument=arg):
											match arg:
												case _:
													A = arg
													return COR_Expressions.UniversalRelation()
	# (𝟎) ∪ ((A) ∪ ((A)⁻¹)) = (A) ∪ ((A)⁻¹)
	match expression:
		case COR_Expressions.Union(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.EmptyRelation():
					match arg2:
						case COR_Expressions.Union(argument1=arg1, argument2=arg2):
							match arg1:
								case _:
									A = arg1
									match arg2:
										case COR_Expressions.Converse(argument=arg):
											match arg:
												case _:
													A = arg
													return COR_Expressions.Union(A, COR_Expressions.Converse(A))
	# (𝟎) † ((T) ∘ ((B)⁻¹)) = (T) ∘ ((B)⁻¹)
	match expression:
		case COR_Expressions.Dagger(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.EmptyRelation():
					match arg2:
						case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
							match arg1:
								case COR_Expressions.UniversalRelation():
									match arg2:
										case COR_Expressions.Converse(argument=arg):
											match arg:
												case _:
													B = arg
													return COR_Expressions.Composition(COR_Expressions.UniversalRelation(), COR_Expressions.Converse(B))
	# (T) † ((𝟏) ∪ ((A)⁻)) = T
	match expression:
		case COR_Expressions.Dagger(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.UniversalRelation():
					match arg2:
						case COR_Expressions.Union(argument1=arg1, argument2=arg2):
							match arg1:
								case COR_Expressions.IdentityRelation:
									match arg2:
										case COR_Expressions.Complement(argument=arg):
											match arg:
												case _:
													A = arg
													return COR_Expressions.UniversalRelation()
	# (T) † ((C) † ((A)⁻¹)) = T
	match expression:
		case COR_Expressions.Dagger(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.UniversalRelation():
					match arg2:
						case COR_Expressions.Dagger(argument1=arg1, argument2=arg2):
							match arg1:
								case _:
									C = arg1
									match arg2:
										case COR_Expressions.Converse(argument=arg):
											match arg:
												case _:
													A = arg
													return COR_Expressions.UniversalRelation()
	# (𝟎) ∪ ((C) † ((C)⁻¹)) = (C) † ((C)⁻¹)
	match expression:
		case COR_Expressions.Union(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.EmptyRelation():
					match arg2:
						case COR_Expressions.Dagger(argument1=arg1, argument2=arg2):
							match arg1:
								case _:
									C = arg1
									match arg2:
										case COR_Expressions.Converse(argument=arg):
											match arg:
												case _:
													C = arg
													return COR_Expressions.Dagger(C, COR_Expressions.Converse(C))
	# ((B) ∘ ((A)⁻¹))⁻¹ = (A) ∘ ((B)⁻¹)
	match expression:
		case COR_Expressions.Converse(argument=arg):
			match arg:
				case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
					match arg1:
						case _:
							B = arg1
							match arg2:
								case COR_Expressions.Converse(argument=arg):
									match arg:
										case _:
											A = arg
											return COR_Expressions.Composition(A, COR_Expressions.Converse(B))
	# (T) ∪ ((C) ∪ ((C)⁻¹)) = T
	match expression:
		case COR_Expressions.Union(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.UniversalRelation():
					match arg2:
						case COR_Expressions.Union(argument1=arg1, argument2=arg2):
							match arg1:
								case _:
									C = arg1
									match arg2:
										case COR_Expressions.Converse(argument=arg):
											match arg:
												case _:
													C = arg
													return COR_Expressions.UniversalRelation()
	# (𝟎) ∪ ((B) ∪ ((𝟏)⁻)) = (B) ∪ ((𝟏)⁻)
	match expression:
		case COR_Expressions.Union(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.EmptyRelation():
					match arg2:
						case COR_Expressions.Union(argument1=arg1, argument2=arg2):
							match arg1:
								case _:
									B = arg1
									match arg2:
										case COR_Expressions.Complement(argument=arg):
											match arg:
												case COR_Expressions.IdentityRelation:
													return COR_Expressions.Union(B, COR_Expressions.Complement(COR_Expressions.IdentityRelation()))
	# (𝟏) ∘ ((C) † ((C)⁻¹)) = (C) † ((C)⁻¹)
	match expression:
		case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.IdentityRelation:
					match arg2:
						case COR_Expressions.Dagger(argument1=arg1, argument2=arg2):
							match arg1:
								case _:
									C = arg1
									match arg2:
										case COR_Expressions.Converse(argument=arg):
											match arg:
												case _:
													C = arg
													return COR_Expressions.Dagger(C, COR_Expressions.Converse(C))
	# (𝟎) ∘ ((𝟏) ∪ ((B)⁻)) = 𝟎
	match expression:
		case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.EmptyRelation():
					match arg2:
						case COR_Expressions.Union(argument1=arg1, argument2=arg2):
							match arg1:
								case COR_Expressions.IdentityRelation:
									match arg2:
										case COR_Expressions.Complement(argument=arg):
											match arg:
												case _:
													B = arg
													return COR_Expressions.EmptyRelation()
	# (𝟎) ∪ (((C)⁻)⁻¹) = ((C)⁻)⁻¹
	match expression:
		case COR_Expressions.Union(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.EmptyRelation():
					match arg2:
						case COR_Expressions.Converse(argument=arg):
							match arg:
								case COR_Expressions.Complement(argument=arg):
									match arg:
										case _:
											C = arg
											return COR_Expressions.Converse(COR_Expressions.Complement(C))
	# (T) † ((T) ∘ ((A)⁻¹)) = T
	match expression:
		case COR_Expressions.Dagger(argument1=arg1, argument2=arg2):
			match arg1:
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
													return COR_Expressions.UniversalRelation()
	# (T) ∪ ((𝟏) † ((C)⁻)) = T
	match expression:
		case COR_Expressions.Union(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.UniversalRelation():
					match arg2:
						case COR_Expressions.Dagger(argument1=arg1, argument2=arg2):
							match arg1:
								case COR_Expressions.IdentityRelation:
									match arg2:
										case COR_Expressions.Complement(argument=arg):
											match arg:
												case _:
													C = arg
													return COR_Expressions.UniversalRelation()
	# (A) ∪ ((A) ∪ ((B)⁻)) = (A) ∪ ((B)⁻)
	match expression:
		case COR_Expressions.Union(argument1=arg1, argument2=arg2):
			match arg1:
				case _:
					A = arg1
					match arg2:
						case COR_Expressions.Union(argument1=arg1, argument2=arg2):
							match arg1:
								case _:
									A = arg1
									match arg2:
										case COR_Expressions.Complement(argument=arg):
											match arg:
												case _:
													B = arg
													return COR_Expressions.Union(A, COR_Expressions.Complement(B))
	# (𝟎) ∪ ((C) ∪ ((B)⁻)) = (C) ∪ ((B)⁻)
	match expression:
		case COR_Expressions.Union(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.EmptyRelation():
					match arg2:
						case COR_Expressions.Union(argument1=arg1, argument2=arg2):
							match arg1:
								case _:
									C = arg1
									match arg2:
										case COR_Expressions.Complement(argument=arg):
											match arg:
												case _:
													B = arg
													return COR_Expressions.Union(C, COR_Expressions.Complement(B))
	# (T) ∘ ((𝟎) † ((B)⁻¹)) = (𝟎) † ((B)⁻¹)
	match expression:
		case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.UniversalRelation():
					match arg2:
						case COR_Expressions.Dagger(argument1=arg1, argument2=arg2):
							match arg1:
								case COR_Expressions.EmptyRelation():
									match arg2:
										case COR_Expressions.Converse(argument=arg):
											match arg:
												case _:
													B = arg
													return COR_Expressions.Dagger(COR_Expressions.EmptyRelation(), COR_Expressions.Converse(B))
	# (𝟏) ∘ ((𝟎) † ((C)⁻¹)) = (𝟎) † ((C)⁻¹)
	match expression:
		case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.IdentityRelation:
					match arg2:
						case COR_Expressions.Dagger(argument1=arg1, argument2=arg2):
							match arg1:
								case COR_Expressions.EmptyRelation():
									match arg2:
										case COR_Expressions.Converse(argument=arg):
											match arg:
												case _:
													C = arg
													return COR_Expressions.Dagger(COR_Expressions.EmptyRelation(), COR_Expressions.Converse(C))
	# ((C) ∪ ((𝟏)⁻))⁻¹ = (C) ∪ ((𝟏)⁻)
	match expression:
		case COR_Expressions.Converse(argument=arg):
			match arg:
				case COR_Expressions.Union(argument1=arg1, argument2=arg2):
					match arg1:
						case _:
							C = arg1
							match arg2:
								case COR_Expressions.Complement(argument=arg):
									match arg:
										case COR_Expressions.IdentityRelation:
											return COR_Expressions.Union(C, COR_Expressions.Complement(COR_Expressions.IdentityRelation()))
	# (T) ∪ ((A) ∘ ((𝟏)⁻)) = T
	match expression:
		case COR_Expressions.Union(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.UniversalRelation():
					match arg2:
						case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
							match arg1:
								case _:
									A = arg1
									match arg2:
										case COR_Expressions.Complement(argument=arg):
											match arg:
												case COR_Expressions.IdentityRelation:
													return COR_Expressions.UniversalRelation()
	# (B) ∪ ((𝟏) ∪ ((B)⁻)) = T
	match expression:
		case COR_Expressions.Union(argument1=arg1, argument2=arg2):
			match arg1:
				case _:
					B = arg1
					match arg2:
						case COR_Expressions.Union(argument1=arg1, argument2=arg2):
							match arg1:
								case COR_Expressions.IdentityRelation:
									match arg2:
										case COR_Expressions.Complement(argument=arg):
											match arg:
												case _:
													B = arg
													return COR_Expressions.UniversalRelation()
	# (A) ∪ ((T) ∘ ((A)⁻)) = T
	match expression:
		case COR_Expressions.Union(argument1=arg1, argument2=arg2):
			match arg1:
				case _:
					A = arg1
					match arg2:
						case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
							match arg1:
								case COR_Expressions.UniversalRelation():
									match arg2:
										case COR_Expressions.Complement(argument=arg):
											match arg:
												case _:
													A = arg
													return COR_Expressions.UniversalRelation()
	# (𝟎) ∪ ((B) ∘ ((C)⁻)) = (B) ∘ ((C)⁻)
	match expression:
		case COR_Expressions.Union(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.EmptyRelation():
					match arg2:
						case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
							match arg1:
								case _:
									B = arg1
									match arg2:
										case COR_Expressions.Complement(argument=arg):
											match arg:
												case _:
													C = arg
													return COR_Expressions.Composition(B, COR_Expressions.Complement(C))
	# (𝟎) ∪ ((B) ∘ ((B)⁻)) = (B) ∘ ((B)⁻)
	match expression:
		case COR_Expressions.Union(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.EmptyRelation():
					match arg2:
						case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
							match arg1:
								case _:
									B = arg1
									match arg2:
										case COR_Expressions.Complement(argument=arg):
											match arg:
												case _:
													B = arg
													return COR_Expressions.Composition(B, COR_Expressions.Complement(B))
	# (𝟏) ∘ ((A) ∪ ((𝟏)⁻)) = (A) ∪ ((𝟏)⁻)
	match expression:
		case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.IdentityRelation:
					match arg2:
						case COR_Expressions.Union(argument1=arg1, argument2=arg2):
							match arg1:
								case _:
									A = arg1
									match arg2:
										case COR_Expressions.Complement(argument=arg):
											match arg:
												case COR_Expressions.IdentityRelation:
													return COR_Expressions.Union(A, COR_Expressions.Complement(COR_Expressions.IdentityRelation()))
	# (T) † ((A) ∘ ((B)⁻¹)) = T
	match expression:
		case COR_Expressions.Dagger(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.UniversalRelation():
					match arg2:
						case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
							match arg1:
								case _:
									A = arg1
									match arg2:
										case COR_Expressions.Converse(argument=arg):
											match arg:
												case _:
													B = arg
													return COR_Expressions.UniversalRelation()
	# (((A)⁻)⁻¹)⁻¹ = (A)⁻
	match expression:
		case COR_Expressions.Converse(argument=arg):
			match arg:
				case COR_Expressions.Converse(argument=arg):
					match arg:
						case COR_Expressions.Complement(argument=arg):
							match arg:
								case _:
									A = arg
									return COR_Expressions.Complement(A)
	# (T) † ((B) † ((C)⁻)) = T
	match expression:
		case COR_Expressions.Dagger(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.UniversalRelation():
					match arg2:
						case COR_Expressions.Dagger(argument1=arg1, argument2=arg2):
							match arg1:
								case _:
									B = arg1
									match arg2:
										case COR_Expressions.Complement(argument=arg):
											match arg:
												case _:
													C = arg
													return COR_Expressions.UniversalRelation()
	# (T) † (((B)⁻¹)⁻) = T
	match expression:
		case COR_Expressions.Dagger(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.UniversalRelation():
					match arg2:
						case COR_Expressions.Complement(argument=arg):
							match arg:
								case COR_Expressions.Converse(argument=arg):
									match arg:
										case _:
											B = arg
											return COR_Expressions.UniversalRelation()
	# (𝟏) ∘ ((A) ∘ ((B)⁻¹)) = (A) ∘ ((B)⁻¹)
	match expression:
		case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.IdentityRelation:
					match arg2:
						case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
							match arg1:
								case _:
									A = arg1
									match arg2:
										case COR_Expressions.Converse(argument=arg):
											match arg:
												case _:
													B = arg
													return COR_Expressions.Composition(A, COR_Expressions.Converse(B))
	# (𝟏) ∘ (((B)⁻¹)⁻) = ((B)⁻)⁻¹
	match expression:
		case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.IdentityRelation:
					match arg2:
						case COR_Expressions.Complement(argument=arg):
							match arg:
								case COR_Expressions.Converse(argument=arg):
									match arg:
										case _:
											B = arg
											return COR_Expressions.Converse(COR_Expressions.Complement(B))
	# (𝟎) ∘ ((T) ∘ ((B)⁻¹)) = 𝟎
	match expression:
		case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.EmptyRelation():
					match arg2:
						case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
							match arg1:
								case COR_Expressions.UniversalRelation():
									match arg2:
										case COR_Expressions.Converse(argument=arg):
											match arg:
												case _:
													B = arg
													return COR_Expressions.EmptyRelation()
	# (T) ∪ ((B) † ((C)⁻¹)) = T
	match expression:
		case COR_Expressions.Union(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.UniversalRelation():
					match arg2:
						case COR_Expressions.Dagger(argument1=arg1, argument2=arg2):
							match arg1:
								case _:
									B = arg1
									match arg2:
										case COR_Expressions.Converse(argument=arg):
											match arg:
												case _:
													C = arg
													return COR_Expressions.UniversalRelation()
	# (T) † ((B) ∪ ((B)⁻¹)) = T
	match expression:
		case COR_Expressions.Dagger(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.UniversalRelation():
					match arg2:
						case COR_Expressions.Union(argument1=arg1, argument2=arg2):
							match arg1:
								case _:
									B = arg1
									match arg2:
										case COR_Expressions.Converse(argument=arg):
											match arg:
												case _:
													B = arg
													return COR_Expressions.UniversalRelation()
	# (T) ∪ (((A)⁻¹)⁻) = T
	match expression:
		case COR_Expressions.Union(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.UniversalRelation():
					match arg2:
						case COR_Expressions.Complement(argument=arg):
							match arg:
								case COR_Expressions.Converse(argument=arg):
									match arg:
										case _:
											A = arg
											return COR_Expressions.UniversalRelation()
	# (𝟏) ∘ ((A) † ((C)⁻)) = (A) † ((C)⁻)
	match expression:
		case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.IdentityRelation:
					match arg2:
						case COR_Expressions.Dagger(argument1=arg1, argument2=arg2):
							match arg1:
								case _:
									A = arg1
									match arg2:
										case COR_Expressions.Complement(argument=arg):
											match arg:
												case _:
													C = arg
													return COR_Expressions.Dagger(A, COR_Expressions.Complement(C))
	# (T) † ((C) ∘ ((A)⁻)) = T
	match expression:
		case COR_Expressions.Dagger(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.UniversalRelation():
					match arg2:
						case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
							match arg1:
								case _:
									C = arg1
									match arg2:
										case COR_Expressions.Complement(argument=arg):
											match arg:
												case _:
													A = arg
													return COR_Expressions.UniversalRelation()
	# (𝟏) ∘ (((C)⁻)⁻¹) = ((C)⁻¹)⁻
	match expression:
		case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.IdentityRelation:
					match arg2:
						case COR_Expressions.Converse(argument=arg):
							match arg:
								case COR_Expressions.Complement(argument=arg):
									match arg:
										case _:
											C = arg
											return COR_Expressions.Complement(COR_Expressions.Converse(C))
	# (𝟏) ∘ (((A)⁻¹)⁻) = ((A)⁻)⁻¹
	match expression:
		case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.IdentityRelation:
					match arg2:
						case COR_Expressions.Complement(argument=arg):
							match arg:
								case COR_Expressions.Converse(argument=arg):
									match arg:
										case _:
											A = arg
											return COR_Expressions.Converse(COR_Expressions.Complement(A))
	# (𝟏) ∘ (((C)⁻¹)⁻) = ((C)⁻)⁻¹
	match expression:
		case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.IdentityRelation:
					match arg2:
						case COR_Expressions.Complement(argument=arg):
							match arg:
								case COR_Expressions.Converse(argument=arg):
									match arg:
										case _:
											C = arg
											return COR_Expressions.Converse(COR_Expressions.Complement(C))
	# (T) † ((C) ∘ ((A)⁻¹)) = T
	match expression:
		case COR_Expressions.Dagger(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.UniversalRelation():
					match arg2:
						case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
							match arg1:
								case _:
									C = arg1
									match arg2:
										case COR_Expressions.Converse(argument=arg):
											match arg:
												case _:
													A = arg
													return COR_Expressions.UniversalRelation()
	# (𝟎) ∪ ((B) ∘ ((𝟏)⁻)) = (B) ∘ ((𝟏)⁻)
	match expression:
		case COR_Expressions.Union(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.EmptyRelation():
					match arg2:
						case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
							match arg1:
								case _:
									B = arg1
									match arg2:
										case COR_Expressions.Complement(argument=arg):
											match arg:
												case COR_Expressions.IdentityRelation:
													return COR_Expressions.Composition(B, COR_Expressions.Complement(COR_Expressions.IdentityRelation()))
	# (𝟏) ∘ ((B) ∪ ((𝟏)⁻)) = (B) ∪ ((𝟏)⁻)
	match expression:
		case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.IdentityRelation:
					match arg2:
						case COR_Expressions.Union(argument1=arg1, argument2=arg2):
							match arg1:
								case _:
									B = arg1
									match arg2:
										case COR_Expressions.Complement(argument=arg):
											match arg:
												case COR_Expressions.IdentityRelation:
													return COR_Expressions.Union(B, COR_Expressions.Complement(COR_Expressions.IdentityRelation()))
	# ((𝟏)⁻) † ((C)⁻) = (C)⁻
	match expression:
		case COR_Expressions.Dagger(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.Complement(argument=arg):
					match arg:
						case COR_Expressions.IdentityRelation:
							match arg2:
								case COR_Expressions.Complement(argument=arg):
									match arg:
										case _:
											C = arg
											return COR_Expressions.Complement(C)
	# (𝟎) ∘ (((A)⁻)⁻¹) = 𝟎
	match expression:
		case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.EmptyRelation():
					match arg2:
						case COR_Expressions.Converse(argument=arg):
							match arg:
								case COR_Expressions.Complement(argument=arg):
									match arg:
										case _:
											A = arg
											return COR_Expressions.EmptyRelation()
	# (T) † ((B) ∘ ((B)⁻)) = T
	match expression:
		case COR_Expressions.Dagger(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.UniversalRelation():
					match arg2:
						case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
							match arg1:
								case _:
									B = arg1
									match arg2:
										case COR_Expressions.Complement(argument=arg):
											match arg:
												case _:
													B = arg
													return COR_Expressions.UniversalRelation()
	# (𝟎) ∪ (((A)⁻¹)⁻) = ((A)⁻)⁻¹
	match expression:
		case COR_Expressions.Union(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.EmptyRelation():
					match arg2:
						case COR_Expressions.Complement(argument=arg):
							match arg:
								case COR_Expressions.Converse(argument=arg):
									match arg:
										case _:
											A = arg
											return COR_Expressions.Converse(COR_Expressions.Complement(A))
	# (T) † ((A) ∘ ((B)⁻)) = T
	match expression:
		case COR_Expressions.Dagger(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.UniversalRelation():
					match arg2:
						case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
							match arg1:
								case _:
									A = arg1
									match arg2:
										case COR_Expressions.Complement(argument=arg):
											match arg:
												case _:
													B = arg
													return COR_Expressions.UniversalRelation()
	# (𝟎) ∘ ((A) † ((A)⁻)) = 𝟎
	match expression:
		case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.EmptyRelation():
					match arg2:
						case COR_Expressions.Dagger(argument1=arg1, argument2=arg2):
							match arg1:
								case _:
									A = arg1
									match arg2:
										case COR_Expressions.Complement(argument=arg):
											match arg:
												case _:
													A = arg
													return COR_Expressions.EmptyRelation()
	# (𝟎) ∪ ((A) ∘ ((𝟏)⁻)) = (A) ∘ ((𝟏)⁻)
	match expression:
		case COR_Expressions.Union(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.EmptyRelation():
					match arg2:
						case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
							match arg1:
								case _:
									A = arg1
									match arg2:
										case COR_Expressions.Complement(argument=arg):
											match arg:
												case COR_Expressions.IdentityRelation:
													return COR_Expressions.Composition(A, COR_Expressions.Complement(COR_Expressions.IdentityRelation()))
	# ((A) ∪ ((B)⁻¹))⁻¹ = (B) ∪ ((A)⁻¹)
	match expression:
		case COR_Expressions.Converse(argument=arg):
			match arg:
				case COR_Expressions.Union(argument1=arg1, argument2=arg2):
					match arg1:
						case _:
							A = arg1
							match arg2:
								case COR_Expressions.Converse(argument=arg):
									match arg:
										case _:
											B = arg
											return COR_Expressions.Union(B, COR_Expressions.Converse(A))
	# (T) † ((B) ∪ ((A)⁻¹)) = T
	match expression:
		case COR_Expressions.Dagger(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.UniversalRelation():
					match arg2:
						case COR_Expressions.Union(argument1=arg1, argument2=arg2):
							match arg1:
								case _:
									B = arg1
									match arg2:
										case COR_Expressions.Converse(argument=arg):
											match arg:
												case _:
													A = arg
													return COR_Expressions.UniversalRelation()
	# (T) ∪ ((B) ∪ ((C)⁻)) = T
	match expression:
		case COR_Expressions.Union(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.UniversalRelation():
					match arg2:
						case COR_Expressions.Union(argument1=arg1, argument2=arg2):
							match arg1:
								case _:
									B = arg1
									match arg2:
										case COR_Expressions.Complement(argument=arg):
											match arg:
												case _:
													C = arg
													return COR_Expressions.UniversalRelation()
	# (𝟎) ∘ (((A)⁻¹)⁻) = 𝟎
	match expression:
		case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.EmptyRelation():
					match arg2:
						case COR_Expressions.Complement(argument=arg):
							match arg:
								case COR_Expressions.Converse(argument=arg):
									match arg:
										case _:
											A = arg
											return COR_Expressions.EmptyRelation()
	# (T) ∘ ((T) ∘ ((A)⁻)) = (T) ∘ ((A)⁻)
	match expression:
		case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.UniversalRelation():
					match arg2:
						case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
							match arg1:
								case COR_Expressions.UniversalRelation():
									match arg2:
										case COR_Expressions.Complement(argument=arg):
											match arg:
												case _:
													A = arg
													return COR_Expressions.Composition(COR_Expressions.UniversalRelation(), COR_Expressions.Complement(A))
	# (𝟎) ∘ ((C) † ((C)⁻¹)) = 𝟎
	match expression:
		case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.EmptyRelation():
					match arg2:
						case COR_Expressions.Dagger(argument1=arg1, argument2=arg2):
							match arg1:
								case _:
									C = arg1
									match arg2:
										case COR_Expressions.Converse(argument=arg):
											match arg:
												case _:
													C = arg
													return COR_Expressions.EmptyRelation()
	# (T) † ((B) ∘ ((A)⁻)) = T
	match expression:
		case COR_Expressions.Dagger(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.UniversalRelation():
					match arg2:
						case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
							match arg1:
								case _:
									B = arg1
									match arg2:
										case COR_Expressions.Complement(argument=arg):
											match arg:
												case _:
													A = arg
													return COR_Expressions.UniversalRelation()
	# ((C) † ((A)⁻¹))⁻¹ = (A) † ((C)⁻¹)
	match expression:
		case COR_Expressions.Converse(argument=arg):
			match arg:
				case COR_Expressions.Dagger(argument1=arg1, argument2=arg2):
					match arg1:
						case _:
							C = arg1
							match arg2:
								case COR_Expressions.Converse(argument=arg):
									match arg:
										case _:
											A = arg
											return COR_Expressions.Dagger(A, COR_Expressions.Converse(C))
	# (𝟎) ∪ ((C) † ((A)⁻¹)) = (C) † ((A)⁻¹)
	match expression:
		case COR_Expressions.Union(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.EmptyRelation():
					match arg2:
						case COR_Expressions.Dagger(argument1=arg1, argument2=arg2):
							match arg1:
								case _:
									C = arg1
									match arg2:
										case COR_Expressions.Converse(argument=arg):
											match arg:
												case _:
													A = arg
													return COR_Expressions.Dagger(C, COR_Expressions.Converse(A))
	# (𝟎) † ((T) ∘ ((A)⁻)) = (T) ∘ ((A)⁻)
	match expression:
		case COR_Expressions.Dagger(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.EmptyRelation():
					match arg2:
						case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
							match arg1:
								case COR_Expressions.UniversalRelation():
									match arg2:
										case COR_Expressions.Complement(argument=arg):
											match arg:
												case _:
													A = arg
													return COR_Expressions.Composition(COR_Expressions.UniversalRelation(), COR_Expressions.Complement(A))
	# (𝟏) ∪ ((A) ∪ ((𝟏)⁻)) = T
	match expression:
		case COR_Expressions.Union(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.IdentityRelation:
					match arg2:
						case COR_Expressions.Union(argument1=arg1, argument2=arg2):
							match arg1:
								case _:
									A = arg1
									match arg2:
										case COR_Expressions.Complement(argument=arg):
											match arg:
												case COR_Expressions.IdentityRelation:
													return COR_Expressions.UniversalRelation()
	# (𝟎) ∘ ((C) ∪ ((B)⁻¹)) = 𝟎
	match expression:
		case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.EmptyRelation():
					match arg2:
						case COR_Expressions.Union(argument1=arg1, argument2=arg2):
							match arg1:
								case _:
									C = arg1
									match arg2:
										case COR_Expressions.Converse(argument=arg):
											match arg:
												case _:
													B = arg
													return COR_Expressions.EmptyRelation()
	# (C) ∪ ((C) ∪ ((B)⁻)) = (C) ∪ ((B)⁻)
	match expression:
		case COR_Expressions.Union(argument1=arg1, argument2=arg2):
			match arg1:
				case _:
					C = arg1
					match arg2:
						case COR_Expressions.Union(argument1=arg1, argument2=arg2):
							match arg1:
								case _:
									C = arg1
									match arg2:
										case COR_Expressions.Complement(argument=arg):
											match arg:
												case _:
													B = arg
													return COR_Expressions.Union(C, COR_Expressions.Complement(B))
	# (T) † ((C) ∪ ((C)⁻¹)) = T
	match expression:
		case COR_Expressions.Dagger(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.UniversalRelation():
					match arg2:
						case COR_Expressions.Union(argument1=arg1, argument2=arg2):
							match arg1:
								case _:
									C = arg1
									match arg2:
										case COR_Expressions.Converse(argument=arg):
											match arg:
												case _:
													C = arg
													return COR_Expressions.UniversalRelation()
	# (𝟎) ∘ ((𝟏) ∪ ((A)⁻)) = 𝟎
	match expression:
		case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.EmptyRelation():
					match arg2:
						case COR_Expressions.Union(argument1=arg1, argument2=arg2):
							match arg1:
								case COR_Expressions.IdentityRelation:
									match arg2:
										case COR_Expressions.Complement(argument=arg):
											match arg:
												case _:
													A = arg
													return COR_Expressions.EmptyRelation()
	# (𝟎) ∘ ((C) ∘ ((C)⁻)) = 𝟎
	match expression:
		case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.EmptyRelation():
					match arg2:
						case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
							match arg1:
								case _:
									C = arg1
									match arg2:
										case COR_Expressions.Complement(argument=arg):
											match arg:
												case _:
													C = arg
													return COR_Expressions.EmptyRelation()
	# (𝟏) ∘ ((A) ∪ ((C)⁻)) = (A) ∪ ((C)⁻)
	match expression:
		case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.IdentityRelation:
					match arg2:
						case COR_Expressions.Union(argument1=arg1, argument2=arg2):
							match arg1:
								case _:
									A = arg1
									match arg2:
										case COR_Expressions.Complement(argument=arg):
											match arg:
												case _:
													C = arg
													return COR_Expressions.Union(A, COR_Expressions.Complement(C))
	# (𝟎) ∪ ((𝟏) ∪ ((B)⁻¹)) = (𝟏) ∪ ((B)⁻¹)
	match expression:
		case COR_Expressions.Union(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.EmptyRelation():
					match arg2:
						case COR_Expressions.Union(argument1=arg1, argument2=arg2):
							match arg1:
								case COR_Expressions.IdentityRelation:
									match arg2:
										case COR_Expressions.Converse(argument=arg):
											match arg:
												case _:
													B = arg
													return COR_Expressions.Union(COR_Expressions.IdentityRelation(), COR_Expressions.Converse(B))
	# (𝟎) ∘ ((A) ∘ ((B)⁻¹)) = 𝟎
	match expression:
		case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.EmptyRelation():
					match arg2:
						case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
							match arg1:
								case _:
									A = arg1
									match arg2:
										case COR_Expressions.Converse(argument=arg):
											match arg:
												case _:
													B = arg
													return COR_Expressions.EmptyRelation()
	# (T) ∪ ((B) ∘ ((A)⁻)) = T
	match expression:
		case COR_Expressions.Union(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.UniversalRelation():
					match arg2:
						case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
							match arg1:
								case _:
									B = arg1
									match arg2:
										case COR_Expressions.Complement(argument=arg):
											match arg:
												case _:
													A = arg
													return COR_Expressions.UniversalRelation()
	# (𝟎) ∘ ((A) † ((C)⁻¹)) = 𝟎
	match expression:
		case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.EmptyRelation():
					match arg2:
						case COR_Expressions.Dagger(argument1=arg1, argument2=arg2):
							match arg1:
								case _:
									A = arg1
									match arg2:
										case COR_Expressions.Converse(argument=arg):
											match arg:
												case _:
													C = arg
													return COR_Expressions.EmptyRelation()
	# (𝟎) ∘ ((B) ∪ ((𝟏)⁻)) = 𝟎
	match expression:
		case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.EmptyRelation():
					match arg2:
						case COR_Expressions.Union(argument1=arg1, argument2=arg2):
							match arg1:
								case _:
									B = arg1
									match arg2:
										case COR_Expressions.Complement(argument=arg):
											match arg:
												case COR_Expressions.IdentityRelation:
													return COR_Expressions.EmptyRelation()
	# (𝟏) ∘ ((T) ∘ ((A)⁻¹)) = (T) ∘ ((A)⁻¹)
	match expression:
		case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.IdentityRelation:
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
	# (B) ∪ ((A) ∪ ((B)⁻)) = T
	match expression:
		case COR_Expressions.Union(argument1=arg1, argument2=arg2):
			match arg1:
				case _:
					B = arg1
					match arg2:
						case COR_Expressions.Union(argument1=arg1, argument2=arg2):
							match arg1:
								case _:
									A = arg1
									match arg2:
										case COR_Expressions.Complement(argument=arg):
											match arg:
												case _:
													B = arg
													return COR_Expressions.UniversalRelation()
	# ((B)⁻¹) ∪ ((𝟏)⁻) = (B) ∪ ((𝟏)⁻)
	match expression:
		case COR_Expressions.Union(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.Converse(argument=arg):
					match arg:
						case _:
							B = arg
							match arg2:
								case COR_Expressions.Complement(argument=arg):
									match arg:
										case COR_Expressions.IdentityRelation:
											return COR_Expressions.Union(B, COR_Expressions.Complement(COR_Expressions.IdentityRelation()))
	# (𝟎) ∘ ((B) † ((C)⁻)) = 𝟎
	match expression:
		case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.EmptyRelation():
					match arg2:
						case COR_Expressions.Dagger(argument1=arg1, argument2=arg2):
							match arg1:
								case _:
									B = arg1
									match arg2:
										case COR_Expressions.Complement(argument=arg):
											match arg:
												case _:
													C = arg
													return COR_Expressions.EmptyRelation()
	# (((A)⁻¹)⁻)⁻¹ = (A)⁻
	match expression:
		case COR_Expressions.Converse(argument=arg):
			match arg:
				case COR_Expressions.Complement(argument=arg):
					match arg:
						case COR_Expressions.Converse(argument=arg):
							match arg:
								case _:
									A = arg
									return COR_Expressions.Complement(A)
	# (C) ∪ ((𝟏) ∪ ((C)⁻)) = T
	match expression:
		case COR_Expressions.Union(argument1=arg1, argument2=arg2):
			match arg1:
				case _:
					C = arg1
					match arg2:
						case COR_Expressions.Union(argument1=arg1, argument2=arg2):
							match arg1:
								case COR_Expressions.IdentityRelation:
									match arg2:
										case COR_Expressions.Complement(argument=arg):
											match arg:
												case _:
													C = arg
													return COR_Expressions.UniversalRelation()
	# (T) ∪ ((𝟏) ∪ ((B)⁻¹)) = T
	match expression:
		case COR_Expressions.Union(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.UniversalRelation():
					match arg2:
						case COR_Expressions.Union(argument1=arg1, argument2=arg2):
							match arg1:
								case COR_Expressions.IdentityRelation:
									match arg2:
										case COR_Expressions.Converse(argument=arg):
											match arg:
												case _:
													B = arg
													return COR_Expressions.UniversalRelation()
	# (𝟎) ∘ ((𝟎) † ((C)⁻)) = 𝟎
	match expression:
		case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.EmptyRelation():
					match arg2:
						case COR_Expressions.Dagger(argument1=arg1, argument2=arg2):
							match arg1:
								case COR_Expressions.EmptyRelation():
									match arg2:
										case COR_Expressions.Complement(argument=arg):
											match arg:
												case _:
													C = arg
													return COR_Expressions.EmptyRelation()
	# ((B) ∘ ((B)⁻¹))⁻¹ = (B) ∘ ((B)⁻¹)
	match expression:
		case COR_Expressions.Converse(argument=arg):
			match arg:
				case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
					match arg1:
						case _:
							B = arg1
							match arg2:
								case COR_Expressions.Converse(argument=arg):
									match arg:
										case _:
											B = arg
											return COR_Expressions.Composition(B, COR_Expressions.Converse(B))
	# (𝟎) ∘ ((B) ∪ ((B)⁻¹)) = 𝟎
	match expression:
		case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.EmptyRelation():
					match arg2:
						case COR_Expressions.Union(argument1=arg1, argument2=arg2):
							match arg1:
								case _:
									B = arg1
									match arg2:
										case COR_Expressions.Converse(argument=arg):
											match arg:
												case _:
													B = arg
													return COR_Expressions.EmptyRelation()
	# (C) ∪ ((B) ∪ ((C)⁻)) = T
	match expression:
		case COR_Expressions.Union(argument1=arg1, argument2=arg2):
			match arg1:
				case _:
					C = arg1
					match arg2:
						case COR_Expressions.Union(argument1=arg1, argument2=arg2):
							match arg1:
								case _:
									B = arg1
									match arg2:
										case COR_Expressions.Complement(argument=arg):
											match arg:
												case _:
													C = arg
													return COR_Expressions.UniversalRelation()
	# (𝟏) ∪ ((𝟏) ∪ ((B)⁻)) = (𝟏) ∪ ((B)⁻)
	match expression:
		case COR_Expressions.Union(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.IdentityRelation:
					match arg2:
						case COR_Expressions.Union(argument1=arg1, argument2=arg2):
							match arg1:
								case COR_Expressions.IdentityRelation:
									match arg2:
										case COR_Expressions.Complement(argument=arg):
											match arg:
												case _:
													B = arg
													return COR_Expressions.Union(COR_Expressions.IdentityRelation(), COR_Expressions.Complement(B))
	# (𝟎) ∪ ((B) ∪ ((B)⁻¹)) = (B) ∪ ((B)⁻¹)
	match expression:
		case COR_Expressions.Union(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.EmptyRelation():
					match arg2:
						case COR_Expressions.Union(argument1=arg1, argument2=arg2):
							match arg1:
								case _:
									B = arg1
									match arg2:
										case COR_Expressions.Converse(argument=arg):
											match arg:
												case _:
													B = arg
													return COR_Expressions.Union(B, COR_Expressions.Converse(B))
	# ((C) ∘ ((B)⁻¹))⁻¹ = (B) ∘ ((C)⁻¹)
	match expression:
		case COR_Expressions.Converse(argument=arg):
			match arg:
				case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
					match arg1:
						case _:
							C = arg1
							match arg2:
								case COR_Expressions.Converse(argument=arg):
									match arg:
										case _:
											B = arg
											return COR_Expressions.Composition(B, COR_Expressions.Converse(C))
	# (T) † ((𝟏) ∪ ((B)⁻¹)) = T
	match expression:
		case COR_Expressions.Dagger(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.UniversalRelation():
					match arg2:
						case COR_Expressions.Union(argument1=arg1, argument2=arg2):
							match arg1:
								case COR_Expressions.IdentityRelation:
									match arg2:
										case COR_Expressions.Converse(argument=arg):
											match arg:
												case _:
													B = arg
													return COR_Expressions.UniversalRelation()
	# ((𝟏)⁻) † ((B)⁻) = (B)⁻
	match expression:
		case COR_Expressions.Dagger(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.Complement(argument=arg):
					match arg:
						case COR_Expressions.IdentityRelation:
							match arg2:
								case COR_Expressions.Complement(argument=arg):
									match arg:
										case _:
											B = arg
											return COR_Expressions.Complement(B)
	# (𝟎) ∪ (((B)⁻)⁻¹) = ((B)⁻¹)⁻
	match expression:
		case COR_Expressions.Union(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.EmptyRelation():
					match arg2:
						case COR_Expressions.Converse(argument=arg):
							match arg:
								case COR_Expressions.Complement(argument=arg):
									match arg:
										case _:
											B = arg
											return COR_Expressions.Complement(COR_Expressions.Converse(B))
	# (T) ∪ ((A) † ((A)⁻¹)) = T
	match expression:
		case COR_Expressions.Union(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.UniversalRelation():
					match arg2:
						case COR_Expressions.Dagger(argument1=arg1, argument2=arg2):
							match arg1:
								case _:
									A = arg1
									match arg2:
										case COR_Expressions.Converse(argument=arg):
											match arg:
												case _:
													A = arg
													return COR_Expressions.UniversalRelation()
	# (𝟎) † ((T) ∘ ((B)⁻)) = (T) ∘ ((B)⁻)
	match expression:
		case COR_Expressions.Dagger(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.EmptyRelation():
					match arg2:
						case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
							match arg1:
								case COR_Expressions.UniversalRelation():
									match arg2:
										case COR_Expressions.Complement(argument=arg):
											match arg:
												case _:
													B = arg
													return COR_Expressions.Composition(COR_Expressions.UniversalRelation(), COR_Expressions.Complement(B))
	# (T) † ((𝟏) ∪ ((B)⁻)) = T
	match expression:
		case COR_Expressions.Dagger(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.UniversalRelation():
					match arg2:
						case COR_Expressions.Union(argument1=arg1, argument2=arg2):
							match arg1:
								case COR_Expressions.IdentityRelation:
									match arg2:
										case COR_Expressions.Complement(argument=arg):
											match arg:
												case _:
													B = arg
													return COR_Expressions.UniversalRelation()
	# (𝟏) ∘ ((𝟎) † ((A)⁻)) = (𝟎) † ((A)⁻)
	match expression:
		case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.IdentityRelation:
					match arg2:
						case COR_Expressions.Dagger(argument1=arg1, argument2=arg2):
							match arg1:
								case COR_Expressions.EmptyRelation():
									match arg2:
										case COR_Expressions.Complement(argument=arg):
											match arg:
												case _:
													A = arg
													return COR_Expressions.Dagger(COR_Expressions.EmptyRelation(), COR_Expressions.Complement(A))
	# (𝟎) ∘ ((C) † ((B)⁻¹)) = 𝟎
	match expression:
		case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.EmptyRelation():
					match arg2:
						case COR_Expressions.Dagger(argument1=arg1, argument2=arg2):
							match arg1:
								case _:
									C = arg1
									match arg2:
										case COR_Expressions.Converse(argument=arg):
											match arg:
												case _:
													B = arg
													return COR_Expressions.EmptyRelation()
	# (𝟎) ∘ ((B) ∘ ((B)⁻¹)) = 𝟎
	match expression:
		case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.EmptyRelation():
					match arg2:
						case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
							match arg1:
								case _:
									B = arg1
									match arg2:
										case COR_Expressions.Converse(argument=arg):
											match arg:
												case _:
													B = arg
													return COR_Expressions.EmptyRelation()
	# (𝟏) ∘ ((T) ∘ ((B)⁻¹)) = (T) ∘ ((B)⁻¹)
	match expression:
		case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.IdentityRelation:
					match arg2:
						case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
							match arg1:
								case COR_Expressions.UniversalRelation():
									match arg2:
										case COR_Expressions.Converse(argument=arg):
											match arg:
												case _:
													B = arg
													return COR_Expressions.Composition(COR_Expressions.UniversalRelation(), COR_Expressions.Converse(B))
	# (T) † ((A) ∘ ((C)⁻)) = T
	match expression:
		case COR_Expressions.Dagger(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.UniversalRelation():
					match arg2:
						case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
							match arg1:
								case _:
									A = arg1
									match arg2:
										case COR_Expressions.Complement(argument=arg):
											match arg:
												case _:
													C = arg
													return COR_Expressions.UniversalRelation()
	# (𝟎) ∪ ((A) † ((C)⁻¹)) = (A) † ((C)⁻¹)
	match expression:
		case COR_Expressions.Union(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.EmptyRelation():
					match arg2:
						case COR_Expressions.Dagger(argument1=arg1, argument2=arg2):
							match arg1:
								case _:
									A = arg1
									match arg2:
										case COR_Expressions.Converse(argument=arg):
											match arg:
												case _:
													C = arg
													return COR_Expressions.Dagger(A, COR_Expressions.Converse(C))
	# ((A) † ((C)⁻¹))⁻¹ = (C) † ((A)⁻¹)
	match expression:
		case COR_Expressions.Converse(argument=arg):
			match arg:
				case COR_Expressions.Dagger(argument1=arg1, argument2=arg2):
					match arg1:
						case _:
							A = arg1
							match arg2:
								case COR_Expressions.Converse(argument=arg):
									match arg:
										case _:
											C = arg
											return COR_Expressions.Dagger(C, COR_Expressions.Converse(A))
	# (T) † (((A)⁻)⁻¹) = T
	match expression:
		case COR_Expressions.Dagger(argument1=arg1, argument2=arg2):
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
	# (𝟎) ∪ ((𝟏) ∪ ((A)⁻¹)) = (𝟏) ∪ ((A)⁻¹)
	match expression:
		case COR_Expressions.Union(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.EmptyRelation():
					match arg2:
						case COR_Expressions.Union(argument1=arg1, argument2=arg2):
							match arg1:
								case COR_Expressions.IdentityRelation:
									match arg2:
										case COR_Expressions.Converse(argument=arg):
											match arg:
												case _:
													A = arg
													return COR_Expressions.Union(COR_Expressions.IdentityRelation(), COR_Expressions.Converse(A))
	# (𝟏) ∘ ((𝟎) † ((B)⁻)) = (𝟎) † ((B)⁻)
	match expression:
		case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.IdentityRelation:
					match arg2:
						case COR_Expressions.Dagger(argument1=arg1, argument2=arg2):
							match arg1:
								case COR_Expressions.EmptyRelation():
									match arg2:
										case COR_Expressions.Complement(argument=arg):
											match arg:
												case _:
													B = arg
													return COR_Expressions.Dagger(COR_Expressions.EmptyRelation(), COR_Expressions.Complement(B))
	# (T) ∪ ((A) ∪ ((B)⁻¹)) = T
	match expression:
		case COR_Expressions.Union(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.UniversalRelation():
					match arg2:
						case COR_Expressions.Union(argument1=arg1, argument2=arg2):
							match arg1:
								case _:
									A = arg1
									match arg2:
										case COR_Expressions.Converse(argument=arg):
											match arg:
												case _:
													B = arg
													return COR_Expressions.UniversalRelation()
	# (𝟏) ∪ ((𝟏) ∪ ((A)⁻)) = (𝟏) ∪ ((A)⁻)
	match expression:
		case COR_Expressions.Union(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.IdentityRelation:
					match arg2:
						case COR_Expressions.Union(argument1=arg1, argument2=arg2):
							match arg1:
								case COR_Expressions.IdentityRelation:
									match arg2:
										case COR_Expressions.Complement(argument=arg):
											match arg:
												case _:
													A = arg
													return COR_Expressions.Union(COR_Expressions.IdentityRelation(), COR_Expressions.Complement(A))
	# (𝟏) ∘ ((C) ∘ ((A)⁻¹)) = (C) ∘ ((A)⁻¹)
	match expression:
		case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.IdentityRelation:
					match arg2:
						case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
							match arg1:
								case _:
									C = arg1
									match arg2:
										case COR_Expressions.Converse(argument=arg):
											match arg:
												case _:
													A = arg
													return COR_Expressions.Composition(C, COR_Expressions.Converse(A))
	# (T) † ((T) ∘ ((B)⁻¹)) = T
	match expression:
		case COR_Expressions.Dagger(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.UniversalRelation():
					match arg2:
						case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
							match arg1:
								case COR_Expressions.UniversalRelation():
									match arg2:
										case COR_Expressions.Converse(argument=arg):
											match arg:
												case _:
													B = arg
													return COR_Expressions.UniversalRelation()
	# (𝟏) ∘ ((𝟏) ∪ ((C)⁻¹)) = (𝟏) ∪ ((C)⁻¹)
	match expression:
		case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.IdentityRelation:
					match arg2:
						case COR_Expressions.Union(argument1=arg1, argument2=arg2):
							match arg1:
								case COR_Expressions.IdentityRelation:
									match arg2:
										case COR_Expressions.Converse(argument=arg):
											match arg:
												case _:
													C = arg
													return COR_Expressions.Union(COR_Expressions.IdentityRelation(), COR_Expressions.Converse(C))
	# (T) † ((B) ∘ ((B)⁻¹)) = T
	match expression:
		case COR_Expressions.Dagger(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.UniversalRelation():
					match arg2:
						case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
							match arg1:
								case _:
									B = arg1
									match arg2:
										case COR_Expressions.Converse(argument=arg):
											match arg:
												case _:
													B = arg
													return COR_Expressions.UniversalRelation()
	# (𝟎) ∘ ((A) ∘ ((B)⁻)) = 𝟎
	match expression:
		case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.EmptyRelation():
					match arg2:
						case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
							match arg1:
								case _:
									A = arg1
									match arg2:
										case COR_Expressions.Complement(argument=arg):
											match arg:
												case _:
													B = arg
													return COR_Expressions.EmptyRelation()
	# (T) ∪ ((A) ∘ ((C)⁻¹)) = T
	match expression:
		case COR_Expressions.Union(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.UniversalRelation():
					match arg2:
						case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
							match arg1:
								case _:
									A = arg1
									match arg2:
										case COR_Expressions.Converse(argument=arg):
											match arg:
												case _:
													C = arg
													return COR_Expressions.UniversalRelation()
	# (𝟎) ∘ ((B) ∪ ((A)⁻¹)) = 𝟎
	match expression:
		case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.EmptyRelation():
					match arg2:
						case COR_Expressions.Union(argument1=arg1, argument2=arg2):
							match arg1:
								case _:
									B = arg1
									match arg2:
										case COR_Expressions.Converse(argument=arg):
											match arg:
												case _:
													A = arg
													return COR_Expressions.EmptyRelation()
	# (𝟏) ∘ ((B) † ((C)⁻)) = (B) † ((C)⁻)
	match expression:
		case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.IdentityRelation:
					match arg2:
						case COR_Expressions.Dagger(argument1=arg1, argument2=arg2):
							match arg1:
								case _:
									B = arg1
									match arg2:
										case COR_Expressions.Complement(argument=arg):
											match arg:
												case _:
													C = arg
													return COR_Expressions.Dagger(B, COR_Expressions.Complement(C))
	# (𝟎) ∪ ((B) † ((C)⁻)) = (B) † ((C)⁻)
	match expression:
		case COR_Expressions.Union(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.EmptyRelation():
					match arg2:
						case COR_Expressions.Dagger(argument1=arg1, argument2=arg2):
							match arg1:
								case _:
									B = arg1
									match arg2:
										case COR_Expressions.Complement(argument=arg):
											match arg:
												case _:
													C = arg
													return COR_Expressions.Dagger(B, COR_Expressions.Complement(C))
	# (T) † ((C) ∪ ((A)⁻¹)) = T
	match expression:
		case COR_Expressions.Dagger(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.UniversalRelation():
					match arg2:
						case COR_Expressions.Union(argument1=arg1, argument2=arg2):
							match arg1:
								case _:
									C = arg1
									match arg2:
										case COR_Expressions.Converse(argument=arg):
											match arg:
												case _:
													A = arg
													return COR_Expressions.UniversalRelation()
	# (𝟎) ∪ ((A) † ((A)⁻¹)) = (A) † ((A)⁻¹)
	match expression:
		case COR_Expressions.Union(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.EmptyRelation():
					match arg2:
						case COR_Expressions.Dagger(argument1=arg1, argument2=arg2):
							match arg1:
								case _:
									A = arg1
									match arg2:
										case COR_Expressions.Converse(argument=arg):
											match arg:
												case _:
													A = arg
													return COR_Expressions.Dagger(A, COR_Expressions.Converse(A))
	# (T) ∪ ((B) ∪ ((𝟏)⁻)) = T
	match expression:
		case COR_Expressions.Union(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.UniversalRelation():
					match arg2:
						case COR_Expressions.Union(argument1=arg1, argument2=arg2):
							match arg1:
								case _:
									B = arg1
									match arg2:
										case COR_Expressions.Complement(argument=arg):
											match arg:
												case COR_Expressions.IdentityRelation:
													return COR_Expressions.UniversalRelation()
	# (𝟏) ∘ ((B) ∘ ((A)⁻¹)) = (B) ∘ ((A)⁻¹)
	match expression:
		case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.IdentityRelation:
					match arg2:
						case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
							match arg1:
								case _:
									B = arg1
									match arg2:
										case COR_Expressions.Converse(argument=arg):
											match arg:
												case _:
													A = arg
													return COR_Expressions.Composition(B, COR_Expressions.Converse(A))
	# (C) ∪ ((C) ∪ ((C)⁻¹)) = (C) ∪ ((C)⁻¹)
	match expression:
		case COR_Expressions.Union(argument1=arg1, argument2=arg2):
			match arg1:
				case _:
					C = arg1
					match arg2:
						case COR_Expressions.Union(argument1=arg1, argument2=arg2):
							match arg1:
								case _:
									C = arg1
									match arg2:
										case COR_Expressions.Converse(argument=arg):
											match arg:
												case _:
													C = arg
													return COR_Expressions.Union(C, COR_Expressions.Converse(C))
	# (T) † ((C) ∪ ((𝟏)⁻)) = T
	match expression:
		case COR_Expressions.Dagger(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.UniversalRelation():
					match arg2:
						case COR_Expressions.Union(argument1=arg1, argument2=arg2):
							match arg1:
								case _:
									C = arg1
									match arg2:
										case COR_Expressions.Complement(argument=arg):
											match arg:
												case COR_Expressions.IdentityRelation:
													return COR_Expressions.UniversalRelation()
	# (𝟎) ∘ ((T) ∘ ((𝟏)⁻)) = 𝟎
	match expression:
		case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.EmptyRelation():
					match arg2:
						case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
							match arg1:
								case COR_Expressions.UniversalRelation():
									match arg2:
										case COR_Expressions.Complement(argument=arg):
											match arg:
												case COR_Expressions.IdentityRelation:
													return COR_Expressions.EmptyRelation()
	# ((C)⁻) ∪ ((C)⁻) = (C)⁻
	match expression:
		case COR_Expressions.Union(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.Complement(argument=arg):
					match arg:
						case _:
							C = arg
							match arg2:
								case COR_Expressions.Complement(argument=arg):
									match arg:
										case _:
											C = arg
											return COR_Expressions.Complement(C)
	# (𝟎) ∪ ((𝟏) ∪ ((C)⁻)) = (𝟏) ∪ ((C)⁻)
	match expression:
		case COR_Expressions.Union(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.EmptyRelation():
					match arg2:
						case COR_Expressions.Union(argument1=arg1, argument2=arg2):
							match arg1:
								case COR_Expressions.IdentityRelation:
									match arg2:
										case COR_Expressions.Complement(argument=arg):
											match arg:
												case _:
													C = arg
													return COR_Expressions.Union(COR_Expressions.IdentityRelation(), COR_Expressions.Complement(C))
	# (T) ∪ ((T) ∘ ((A)⁻)) = T
	match expression:
		case COR_Expressions.Union(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.UniversalRelation():
					match arg2:
						case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
							match arg1:
								case COR_Expressions.UniversalRelation():
									match arg2:
										case COR_Expressions.Complement(argument=arg):
											match arg:
												case _:
													A = arg
													return COR_Expressions.UniversalRelation()
	# (𝟏) ∘ ((A) † ((C)⁻¹)) = (A) † ((C)⁻¹)
	match expression:
		case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.IdentityRelation:
					match arg2:
						case COR_Expressions.Dagger(argument1=arg1, argument2=arg2):
							match arg1:
								case _:
									A = arg1
									match arg2:
										case COR_Expressions.Converse(argument=arg):
											match arg:
												case _:
													C = arg
													return COR_Expressions.Dagger(A, COR_Expressions.Converse(C))
	# (𝟎) ∪ (((B)⁻¹)⁻) = ((B)⁻¹)⁻
	match expression:
		case COR_Expressions.Union(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.EmptyRelation():
					match arg2:
						case COR_Expressions.Complement(argument=arg):
							match arg:
								case COR_Expressions.Converse(argument=arg):
									match arg:
										case _:
											B = arg
											return COR_Expressions.Complement(COR_Expressions.Converse(B))
	# (T) ∪ ((B) † ((A)⁻¹)) = T
	match expression:
		case COR_Expressions.Union(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.UniversalRelation():
					match arg2:
						case COR_Expressions.Dagger(argument1=arg1, argument2=arg2):
							match arg1:
								case _:
									B = arg1
									match arg2:
										case COR_Expressions.Converse(argument=arg):
											match arg:
												case _:
													A = arg
													return COR_Expressions.UniversalRelation()
	# (T) ∪ ((C) ∪ ((B)⁻¹)) = T
	match expression:
		case COR_Expressions.Union(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.UniversalRelation():
					match arg2:
						case COR_Expressions.Union(argument1=arg1, argument2=arg2):
							match arg1:
								case _:
									C = arg1
									match arg2:
										case COR_Expressions.Converse(argument=arg):
											match arg:
												case _:
													B = arg
													return COR_Expressions.UniversalRelation()
	# (𝟏) ∘ ((C) ∘ ((C)⁻¹)) = (C) ∘ ((C)⁻¹)
	match expression:
		case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.IdentityRelation:
					match arg2:
						case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
							match arg1:
								case _:
									C = arg1
									match arg2:
										case COR_Expressions.Converse(argument=arg):
											match arg:
												case _:
													C = arg
													return COR_Expressions.Composition(C, COR_Expressions.Converse(C))
	# (𝟎) ∪ ((T) ∘ ((B)⁻¹)) = (T) ∘ ((B)⁻¹)
	match expression:
		case COR_Expressions.Union(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.EmptyRelation():
					match arg2:
						case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
							match arg1:
								case COR_Expressions.UniversalRelation():
									match arg2:
										case COR_Expressions.Converse(argument=arg):
											match arg:
												case _:
													B = arg
													return COR_Expressions.Composition(COR_Expressions.UniversalRelation(), COR_Expressions.Converse(B))
	# ((C) ∪ ((B)⁻¹))⁻¹ = (B) ∪ ((C)⁻¹)
	match expression:
		case COR_Expressions.Converse(argument=arg):
			match arg:
				case COR_Expressions.Union(argument1=arg1, argument2=arg2):
					match arg1:
						case _:
							C = arg1
							match arg2:
								case COR_Expressions.Converse(argument=arg):
									match arg:
										case _:
											B = arg
											return COR_Expressions.Union(B, COR_Expressions.Converse(C))
	# (𝟏) ∘ ((C) ∘ ((𝟏)⁻)) = (C) ∘ ((𝟏)⁻)
	match expression:
		case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.IdentityRelation:
					match arg2:
						case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
							match arg1:
								case _:
									C = arg1
									match arg2:
										case COR_Expressions.Complement(argument=arg):
											match arg:
												case COR_Expressions.IdentityRelation:
													return COR_Expressions.Composition(C, COR_Expressions.Complement(COR_Expressions.IdentityRelation()))
	# (T) ∪ ((C) † ((C)⁻¹)) = T
	match expression:
		case COR_Expressions.Union(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.UniversalRelation():
					match arg2:
						case COR_Expressions.Dagger(argument1=arg1, argument2=arg2):
							match arg1:
								case _:
									C = arg1
									match arg2:
										case COR_Expressions.Converse(argument=arg):
											match arg:
												case _:
													C = arg
													return COR_Expressions.UniversalRelation()
	# (𝟎) ∪ ((B) † ((A)⁻¹)) = (B) † ((A)⁻¹)
	match expression:
		case COR_Expressions.Union(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.EmptyRelation():
					match arg2:
						case COR_Expressions.Dagger(argument1=arg1, argument2=arg2):
							match arg1:
								case _:
									B = arg1
									match arg2:
										case COR_Expressions.Converse(argument=arg):
											match arg:
												case _:
													A = arg
													return COR_Expressions.Dagger(B, COR_Expressions.Converse(A))
	# (T) † ((𝟏) ∪ ((C)⁻¹)) = T
	match expression:
		case COR_Expressions.Dagger(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.UniversalRelation():
					match arg2:
						case COR_Expressions.Union(argument1=arg1, argument2=arg2):
							match arg1:
								case COR_Expressions.IdentityRelation:
									match arg2:
										case COR_Expressions.Converse(argument=arg):
											match arg:
												case _:
													C = arg
													return COR_Expressions.UniversalRelation()
	# (((B)⁻¹)⁻)⁻ = (B)⁻¹
	match expression:
		case COR_Expressions.Complement(argument=arg):
			match arg:
				case COR_Expressions.Complement(argument=arg):
					match arg:
						case COR_Expressions.Converse(argument=arg):
							match arg:
								case _:
									B = arg
									return COR_Expressions.Converse(B)
	# (𝟏) ∪ ((𝟏) ∪ ((B)⁻¹)) = (𝟏) ∪ ((B)⁻¹)
	match expression:
		case COR_Expressions.Union(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.IdentityRelation:
					match arg2:
						case COR_Expressions.Union(argument1=arg1, argument2=arg2):
							match arg1:
								case COR_Expressions.IdentityRelation:
									match arg2:
										case COR_Expressions.Converse(argument=arg):
											match arg:
												case _:
													B = arg
													return COR_Expressions.Union(COR_Expressions.IdentityRelation(), COR_Expressions.Converse(B))
	# (T) † ((𝟎) † ((A)⁻)) = T
	match expression:
		case COR_Expressions.Dagger(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.UniversalRelation():
					match arg2:
						case COR_Expressions.Dagger(argument1=arg1, argument2=arg2):
							match arg1:
								case COR_Expressions.EmptyRelation():
									match arg2:
										case COR_Expressions.Complement(argument=arg):
											match arg:
												case _:
													A = arg
													return COR_Expressions.UniversalRelation()
	# ((𝟏)⁻) ∪ ((𝟏)⁻) = (𝟏)⁻
	match expression:
		case COR_Expressions.Union(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.Complement(argument=arg):
					match arg:
						case COR_Expressions.IdentityRelation:
							match arg2:
								case COR_Expressions.Complement(argument=arg):
									match arg:
										case COR_Expressions.IdentityRelation:
											return COR_Expressions.Complement(COR_Expressions.IdentityRelation())
	# (𝟏) ∘ ((𝟏) ∪ ((A)⁻¹)) = (𝟏) ∪ ((A)⁻¹)
	match expression:
		case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.IdentityRelation:
					match arg2:
						case COR_Expressions.Union(argument1=arg1, argument2=arg2):
							match arg1:
								case COR_Expressions.IdentityRelation:
									match arg2:
										case COR_Expressions.Converse(argument=arg):
											match arg:
												case _:
													A = arg
													return COR_Expressions.Union(COR_Expressions.IdentityRelation(), COR_Expressions.Converse(A))
	# (T) ∪ ((C) † ((A)⁻)) = T
	match expression:
		case COR_Expressions.Union(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.UniversalRelation():
					match arg2:
						case COR_Expressions.Dagger(argument1=arg1, argument2=arg2):
							match arg1:
								case _:
									C = arg1
									match arg2:
										case COR_Expressions.Complement(argument=arg):
											match arg:
												case _:
													A = arg
													return COR_Expressions.UniversalRelation()
	# (𝟎) ∪ ((𝟎) † ((A)⁻¹)) = (𝟎) † ((A)⁻¹)
	match expression:
		case COR_Expressions.Union(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.EmptyRelation():
					match arg2:
						case COR_Expressions.Dagger(argument1=arg1, argument2=arg2):
							match arg1:
								case COR_Expressions.EmptyRelation():
									match arg2:
										case COR_Expressions.Converse(argument=arg):
											match arg:
												case _:
													A = arg
													return COR_Expressions.Dagger(COR_Expressions.EmptyRelation(), COR_Expressions.Converse(A))
	# (𝟎) ∘ ((𝟎) † ((A)⁻)) = 𝟎
	match expression:
		case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.EmptyRelation():
					match arg2:
						case COR_Expressions.Dagger(argument1=arg1, argument2=arg2):
							match arg1:
								case COR_Expressions.EmptyRelation():
									match arg2:
										case COR_Expressions.Complement(argument=arg):
											match arg:
												case _:
													A = arg
													return COR_Expressions.EmptyRelation()
	# ((C)⁻¹) ∪ ((C)⁻¹) = (C)⁻¹
	match expression:
		case COR_Expressions.Union(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.Converse(argument=arg):
					match arg:
						case _:
							C = arg
							match arg2:
								case COR_Expressions.Converse(argument=arg):
									match arg:
										case _:
											C = arg
											return COR_Expressions.Converse(C)
	# (T) † ((𝟏) † ((C)⁻)) = T
	match expression:
		case COR_Expressions.Dagger(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.UniversalRelation():
					match arg2:
						case COR_Expressions.Dagger(argument1=arg1, argument2=arg2):
							match arg1:
								case COR_Expressions.IdentityRelation:
									match arg2:
										case COR_Expressions.Complement(argument=arg):
											match arg:
												case _:
													C = arg
													return COR_Expressions.UniversalRelation()
	# (𝟏) ∪ ((𝟏) ∪ ((C)⁻¹)) = (𝟏) ∪ ((C)⁻¹)
	match expression:
		case COR_Expressions.Union(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.IdentityRelation:
					match arg2:
						case COR_Expressions.Union(argument1=arg1, argument2=arg2):
							match arg1:
								case COR_Expressions.IdentityRelation:
									match arg2:
										case COR_Expressions.Converse(argument=arg):
											match arg:
												case _:
													C = arg
													return COR_Expressions.Union(COR_Expressions.IdentityRelation(), COR_Expressions.Converse(C))
	# (𝟏) ∘ ((B) ∘ ((A)⁻)) = (B) ∘ ((A)⁻)
	match expression:
		case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.IdentityRelation:
					match arg2:
						case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
							match arg1:
								case _:
									B = arg1
									match arg2:
										case COR_Expressions.Complement(argument=arg):
											match arg:
												case _:
													A = arg
													return COR_Expressions.Composition(B, COR_Expressions.Complement(A))
	# (T) ∪ (((C)⁻)⁻¹) = T
	match expression:
		case COR_Expressions.Union(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.UniversalRelation():
					match arg2:
						case COR_Expressions.Converse(argument=arg):
							match arg:
								case COR_Expressions.Complement(argument=arg):
									match arg:
										case _:
											C = arg
											return COR_Expressions.UniversalRelation()
	# (𝟎) † ((A) † ((A)⁻¹)) = (𝟎) † ((A)⁻¹)
	match expression:
		case COR_Expressions.Dagger(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.EmptyRelation():
					match arg2:
						case COR_Expressions.Dagger(argument1=arg1, argument2=arg2):
							match arg1:
								case _:
									A = arg1
									match arg2:
										case COR_Expressions.Converse(argument=arg):
											match arg:
												case _:
													A = arg
													return COR_Expressions.Dagger(COR_Expressions.EmptyRelation(), COR_Expressions.Converse(A))
	# (𝟎) ∘ ((𝟎) † ((B)⁻)) = 𝟎
	match expression:
		case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.EmptyRelation():
					match arg2:
						case COR_Expressions.Dagger(argument1=arg1, argument2=arg2):
							match arg1:
								case COR_Expressions.EmptyRelation():
									match arg2:
										case COR_Expressions.Complement(argument=arg):
											match arg:
												case _:
													B = arg
													return COR_Expressions.EmptyRelation()
	# (T) † ((C) † ((B)⁻¹)) = T
	match expression:
		case COR_Expressions.Dagger(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.UniversalRelation():
					match arg2:
						case COR_Expressions.Dagger(argument1=arg1, argument2=arg2):
							match arg1:
								case _:
									C = arg1
									match arg2:
										case COR_Expressions.Converse(argument=arg):
											match arg:
												case _:
													B = arg
													return COR_Expressions.UniversalRelation()
	# (T) ∪ ((𝟏) † ((C)⁻¹)) = T
	match expression:
		case COR_Expressions.Union(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.UniversalRelation():
					match arg2:
						case COR_Expressions.Dagger(argument1=arg1, argument2=arg2):
							match arg1:
								case COR_Expressions.IdentityRelation:
									match arg2:
										case COR_Expressions.Converse(argument=arg):
											match arg:
												case _:
													C = arg
													return COR_Expressions.UniversalRelation()
	# (𝟎) ∪ ((B) ∪ ((A)⁻)) = (B) ∪ ((A)⁻)
	match expression:
		case COR_Expressions.Union(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.EmptyRelation():
					match arg2:
						case COR_Expressions.Union(argument1=arg1, argument2=arg2):
							match arg1:
								case _:
									B = arg1
									match arg2:
										case COR_Expressions.Complement(argument=arg):
											match arg:
												case _:
													A = arg
													return COR_Expressions.Union(B, COR_Expressions.Complement(A))
	# (T) ∪ ((B) ∪ ((A)⁻)) = T
	match expression:
		case COR_Expressions.Union(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.UniversalRelation():
					match arg2:
						case COR_Expressions.Union(argument1=arg1, argument2=arg2):
							match arg1:
								case _:
									B = arg1
									match arg2:
										case COR_Expressions.Complement(argument=arg):
											match arg:
												case _:
													A = arg
													return COR_Expressions.UniversalRelation()
	# (𝟏) ∘ ((A) ∘ ((C)⁻¹)) = (A) ∘ ((C)⁻¹)
	match expression:
		case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.IdentityRelation:
					match arg2:
						case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
							match arg1:
								case _:
									A = arg1
									match arg2:
										case COR_Expressions.Converse(argument=arg):
											match arg:
												case _:
													C = arg
													return COR_Expressions.Composition(A, COR_Expressions.Converse(C))
	# (T) † ((𝟎) † ((B)⁻¹)) = T
	match expression:
		case COR_Expressions.Dagger(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.UniversalRelation():
					match arg2:
						case COR_Expressions.Dagger(argument1=arg1, argument2=arg2):
							match arg1:
								case COR_Expressions.EmptyRelation():
									match arg2:
										case COR_Expressions.Converse(argument=arg):
											match arg:
												case _:
													B = arg
													return COR_Expressions.UniversalRelation()
	# (T) ∪ ((B) ∪ ((C)⁻¹)) = T
	match expression:
		case COR_Expressions.Union(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.UniversalRelation():
					match arg2:
						case COR_Expressions.Union(argument1=arg1, argument2=arg2):
							match arg1:
								case _:
									B = arg1
									match arg2:
										case COR_Expressions.Converse(argument=arg):
											match arg:
												case _:
													C = arg
													return COR_Expressions.UniversalRelation()
	# (T) † ((𝟏) † ((A)⁻¹)) = T
	match expression:
		case COR_Expressions.Dagger(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.UniversalRelation():
					match arg2:
						case COR_Expressions.Dagger(argument1=arg1, argument2=arg2):
							match arg1:
								case COR_Expressions.IdentityRelation:
									match arg2:
										case COR_Expressions.Converse(argument=arg):
											match arg:
												case _:
													A = arg
													return COR_Expressions.UniversalRelation()
	# (𝟎) ∘ ((𝟏) † ((B)⁻¹)) = 𝟎
	match expression:
		case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.EmptyRelation():
					match arg2:
						case COR_Expressions.Dagger(argument1=arg1, argument2=arg2):
							match arg1:
								case COR_Expressions.IdentityRelation:
									match arg2:
										case COR_Expressions.Converse(argument=arg):
											match arg:
												case _:
													B = arg
													return COR_Expressions.EmptyRelation()
	# (𝟎) ∪ ((B) † ((A)⁻)) = (B) † ((A)⁻)
	match expression:
		case COR_Expressions.Union(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.EmptyRelation():
					match arg2:
						case COR_Expressions.Dagger(argument1=arg1, argument2=arg2):
							match arg1:
								case _:
									B = arg1
									match arg2:
										case COR_Expressions.Complement(argument=arg):
											match arg:
												case _:
													A = arg
													return COR_Expressions.Dagger(B, COR_Expressions.Complement(A))
	# (𝟏) ∘ ((𝟏) † ((A)⁻¹)) = (𝟏) † ((A)⁻¹)
	match expression:
		case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.IdentityRelation:
					match arg2:
						case COR_Expressions.Dagger(argument1=arg1, argument2=arg2):
							match arg1:
								case COR_Expressions.IdentityRelation:
									match arg2:
										case COR_Expressions.Converse(argument=arg):
											match arg:
												case _:
													A = arg
													return COR_Expressions.Dagger(COR_Expressions.IdentityRelation(), COR_Expressions.Converse(A))
	# (T) † ((B) ∪ ((C)⁻¹)) = T
	match expression:
		case COR_Expressions.Dagger(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.UniversalRelation():
					match arg2:
						case COR_Expressions.Union(argument1=arg1, argument2=arg2):
							match arg1:
								case _:
									B = arg1
									match arg2:
										case COR_Expressions.Converse(argument=arg):
											match arg:
												case _:
													C = arg
													return COR_Expressions.UniversalRelation()
	# (T) † ((𝟏) † ((A)⁻)) = T
	match expression:
		case COR_Expressions.Dagger(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.UniversalRelation():
					match arg2:
						case COR_Expressions.Dagger(argument1=arg1, argument2=arg2):
							match arg1:
								case COR_Expressions.IdentityRelation:
									match arg2:
										case COR_Expressions.Complement(argument=arg):
											match arg:
												case _:
													A = arg
													return COR_Expressions.UniversalRelation()
	# (𝟎) ∘ ((𝟏) † ((B)⁻)) = 𝟎
	match expression:
		case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.EmptyRelation():
					match arg2:
						case COR_Expressions.Dagger(argument1=arg1, argument2=arg2):
							match arg1:
								case COR_Expressions.IdentityRelation:
									match arg2:
										case COR_Expressions.Complement(argument=arg):
											match arg:
												case _:
													B = arg
													return COR_Expressions.EmptyRelation()
	# (𝟎) ∘ ((T) ∘ ((B)⁻)) = 𝟎
	match expression:
		case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.EmptyRelation():
					match arg2:
						case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
							match arg1:
								case COR_Expressions.UniversalRelation():
									match arg2:
										case COR_Expressions.Complement(argument=arg):
											match arg:
												case _:
													B = arg
													return COR_Expressions.EmptyRelation()
	# (𝟎) ∘ ((B) † ((A)⁻)) = 𝟎
	match expression:
		case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.EmptyRelation():
					match arg2:
						case COR_Expressions.Dagger(argument1=arg1, argument2=arg2):
							match arg1:
								case _:
									B = arg1
									match arg2:
										case COR_Expressions.Complement(argument=arg):
											match arg:
												case _:
													A = arg
													return COR_Expressions.EmptyRelation()
	# (T) † ((B) ∘ ((𝟏)⁻)) = T
	match expression:
		case COR_Expressions.Dagger(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.UniversalRelation():
					match arg2:
						case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
							match arg1:
								case _:
									B = arg1
									match arg2:
										case COR_Expressions.Complement(argument=arg):
											match arg:
												case COR_Expressions.IdentityRelation:
													return COR_Expressions.UniversalRelation()
	# ((C) ∘ ((A)⁻¹))⁻¹ = (A) ∘ ((C)⁻¹)
	match expression:
		case COR_Expressions.Converse(argument=arg):
			match arg:
				case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
					match arg1:
						case _:
							C = arg1
							match arg2:
								case COR_Expressions.Converse(argument=arg):
									match arg:
										case _:
											A = arg
											return COR_Expressions.Composition(A, COR_Expressions.Converse(C))
	# (T) ∪ (((B)⁻¹)⁻) = T
	match expression:
		case COR_Expressions.Union(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.UniversalRelation():
					match arg2:
						case COR_Expressions.Complement(argument=arg):
							match arg:
								case COR_Expressions.Converse(argument=arg):
									match arg:
										case _:
											B = arg
											return COR_Expressions.UniversalRelation()
	# (T) ∪ ((T) ∘ ((B)⁻)) = T
	match expression:
		case COR_Expressions.Union(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.UniversalRelation():
					match arg2:
						case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
							match arg1:
								case COR_Expressions.UniversalRelation():
									match arg2:
										case COR_Expressions.Complement(argument=arg):
											match arg:
												case _:
													B = arg
													return COR_Expressions.UniversalRelation()
	# (𝟎) ∘ ((A) ∪ ((A)⁻¹)) = 𝟎
	match expression:
		case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.EmptyRelation():
					match arg2:
						case COR_Expressions.Union(argument1=arg1, argument2=arg2):
							match arg1:
								case _:
									A = arg1
									match arg2:
										case COR_Expressions.Converse(argument=arg):
											match arg:
												case _:
													A = arg
													return COR_Expressions.EmptyRelation()
	# (𝟏) ∘ ((𝟎) † ((C)⁻)) = (𝟎) † ((C)⁻)
	match expression:
		case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.IdentityRelation:
					match arg2:
						case COR_Expressions.Dagger(argument1=arg1, argument2=arg2):
							match arg1:
								case COR_Expressions.EmptyRelation():
									match arg2:
										case COR_Expressions.Complement(argument=arg):
											match arg:
												case _:
													C = arg
													return COR_Expressions.Dagger(COR_Expressions.EmptyRelation(), COR_Expressions.Complement(C))
	# (𝟎) ∘ ((𝟏) † ((C)⁻¹)) = 𝟎
	match expression:
		case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.EmptyRelation():
					match arg2:
						case COR_Expressions.Dagger(argument1=arg1, argument2=arg2):
							match arg1:
								case COR_Expressions.IdentityRelation:
									match arg2:
										case COR_Expressions.Converse(argument=arg):
											match arg:
												case _:
													C = arg
													return COR_Expressions.EmptyRelation()
	# (T) † ((A) ∪ ((𝟏)⁻)) = T
	match expression:
		case COR_Expressions.Dagger(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.UniversalRelation():
					match arg2:
						case COR_Expressions.Union(argument1=arg1, argument2=arg2):
							match arg1:
								case _:
									A = arg1
									match arg2:
										case COR_Expressions.Complement(argument=arg):
											match arg:
												case COR_Expressions.IdentityRelation:
													return COR_Expressions.UniversalRelation()
	# ((T) ∘ ((𝟏)⁻))⁻¹ = (T) ∘ ((𝟏)⁻)
	match expression:
		case COR_Expressions.Converse(argument=arg):
			match arg:
				case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
					match arg1:
						case COR_Expressions.UniversalRelation():
							match arg2:
								case COR_Expressions.Complement(argument=arg):
									match arg:
										case COR_Expressions.IdentityRelation:
											return COR_Expressions.Composition(COR_Expressions.UniversalRelation(), COR_Expressions.Complement(COR_Expressions.IdentityRelation()))
	# (𝟎) ∪ ((C) ∪ ((B)⁻¹)) = (C) ∪ ((B)⁻¹)
	match expression:
		case COR_Expressions.Union(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.EmptyRelation():
					match arg2:
						case COR_Expressions.Union(argument1=arg1, argument2=arg2):
							match arg1:
								case _:
									C = arg1
									match arg2:
										case COR_Expressions.Converse(argument=arg):
											match arg:
												case _:
													B = arg
													return COR_Expressions.Union(C, COR_Expressions.Converse(B))
	# (T) ∘ ((𝟎) † ((B)⁻)) = (𝟎) † ((B)⁻)
	match expression:
		case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.UniversalRelation():
					match arg2:
						case COR_Expressions.Dagger(argument1=arg1, argument2=arg2):
							match arg1:
								case COR_Expressions.EmptyRelation():
									match arg2:
										case COR_Expressions.Complement(argument=arg):
											match arg:
												case _:
													B = arg
													return COR_Expressions.Dagger(COR_Expressions.EmptyRelation(), COR_Expressions.Complement(B))
	# (𝟏) ∘ ((B) † ((B)⁻¹)) = (B) † ((B)⁻¹)
	match expression:
		case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.IdentityRelation:
					match arg2:
						case COR_Expressions.Dagger(argument1=arg1, argument2=arg2):
							match arg1:
								case _:
									B = arg1
									match arg2:
										case COR_Expressions.Converse(argument=arg):
											match arg:
												case _:
													B = arg
													return COR_Expressions.Dagger(B, COR_Expressions.Converse(B))
	# (T) ∘ ((𝟏) ∪ ((C)⁻¹)) = T
	match expression:
		case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.UniversalRelation():
					match arg2:
						case COR_Expressions.Union(argument1=arg1, argument2=arg2):
							match arg1:
								case COR_Expressions.IdentityRelation:
									match arg2:
										case COR_Expressions.Converse(argument=arg):
											match arg:
												case _:
													C = arg
													return COR_Expressions.UniversalRelation()
	# (𝟎) ∘ ((C) ∘ ((A)⁻¹)) = 𝟎
	match expression:
		case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.EmptyRelation():
					match arg2:
						case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
							match arg1:
								case _:
									C = arg1
									match arg2:
										case COR_Expressions.Converse(argument=arg):
											match arg:
												case _:
													A = arg
													return COR_Expressions.EmptyRelation()
	# (T) † ((T) ∘ ((A)⁻)) = T
	match expression:
		case COR_Expressions.Dagger(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.UniversalRelation():
					match arg2:
						case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
							match arg1:
								case COR_Expressions.UniversalRelation():
									match arg2:
										case COR_Expressions.Complement(argument=arg):
											match arg:
												case _:
													A = arg
													return COR_Expressions.UniversalRelation()
	# (𝟎) ∘ ((A) ∘ ((C)⁻)) = 𝟎
	match expression:
		case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.EmptyRelation():
					match arg2:
						case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
							match arg1:
								case _:
									A = arg1
									match arg2:
										case COR_Expressions.Complement(argument=arg):
											match arg:
												case _:
													C = arg
													return COR_Expressions.EmptyRelation()
	# (𝟎) ∪ ((C) ∘ ((B)⁻¹)) = (C) ∘ ((B)⁻¹)
	match expression:
		case COR_Expressions.Union(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.EmptyRelation():
					match arg2:
						case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
							match arg1:
								case _:
									C = arg1
									match arg2:
										case COR_Expressions.Converse(argument=arg):
											match arg:
												case _:
													B = arg
													return COR_Expressions.Composition(C, COR_Expressions.Converse(B))
	# (T) ∪ ((B) ∘ ((B)⁻)) = T
	match expression:
		case COR_Expressions.Union(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.UniversalRelation():
					match arg2:
						case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
							match arg1:
								case _:
									B = arg1
									match arg2:
										case COR_Expressions.Complement(argument=arg):
											match arg:
												case _:
													B = arg
													return COR_Expressions.UniversalRelation()
	# (T) ∪ ((A) † ((A)⁻)) = T
	match expression:
		case COR_Expressions.Union(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.UniversalRelation():
					match arg2:
						case COR_Expressions.Dagger(argument1=arg1, argument2=arg2):
							match arg1:
								case _:
									A = arg1
									match arg2:
										case COR_Expressions.Complement(argument=arg):
											match arg:
												case _:
													A = arg
													return COR_Expressions.UniversalRelation()
	# (𝟎) ∪ ((A) † ((B)⁻¹)) = (A) † ((B)⁻¹)
	match expression:
		case COR_Expressions.Union(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.EmptyRelation():
					match arg2:
						case COR_Expressions.Dagger(argument1=arg1, argument2=arg2):
							match arg1:
								case _:
									A = arg1
									match arg2:
										case COR_Expressions.Converse(argument=arg):
											match arg:
												case _:
													B = arg
													return COR_Expressions.Dagger(A, COR_Expressions.Converse(B))
	# (T) † ((B) ∪ ((A)⁻)) = T
	match expression:
		case COR_Expressions.Dagger(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.UniversalRelation():
					match arg2:
						case COR_Expressions.Union(argument1=arg1, argument2=arg2):
							match arg1:
								case _:
									B = arg1
									match arg2:
										case COR_Expressions.Complement(argument=arg):
											match arg:
												case _:
													A = arg
													return COR_Expressions.UniversalRelation()
	# (𝟎) ∘ ((B) ∘ ((A)⁻)) = 𝟎
	match expression:
		case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.EmptyRelation():
					match arg2:
						case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
							match arg1:
								case _:
									B = arg1
									match arg2:
										case COR_Expressions.Complement(argument=arg):
											match arg:
												case _:
													A = arg
													return COR_Expressions.EmptyRelation()
	# (𝟏) ∘ ((C) ∪ ((C)⁻¹)) = (C) ∪ ((C)⁻¹)
	match expression:
		case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.IdentityRelation:
					match arg2:
						case COR_Expressions.Union(argument1=arg1, argument2=arg2):
							match arg1:
								case _:
									C = arg1
									match arg2:
										case COR_Expressions.Converse(argument=arg):
											match arg:
												case _:
													C = arg
													return COR_Expressions.Union(C, COR_Expressions.Converse(C))
	# (B) ∪ ((B) ∪ ((𝟏)⁻)) = (B) ∪ ((𝟏)⁻)
	match expression:
		case COR_Expressions.Union(argument1=arg1, argument2=arg2):
			match arg1:
				case _:
					B = arg1
					match arg2:
						case COR_Expressions.Union(argument1=arg1, argument2=arg2):
							match arg1:
								case _:
									B = arg1
									match arg2:
										case COR_Expressions.Complement(argument=arg):
											match arg:
												case COR_Expressions.IdentityRelation:
													return COR_Expressions.Union(B, COR_Expressions.Complement(COR_Expressions.IdentityRelation()))
	# (T) ∪ ((C) ∘ ((𝟏)⁻)) = T
	match expression:
		case COR_Expressions.Union(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.UniversalRelation():
					match arg2:
						case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
							match arg1:
								case _:
									C = arg1
									match arg2:
										case COR_Expressions.Complement(argument=arg):
											match arg:
												case COR_Expressions.IdentityRelation:
													return COR_Expressions.UniversalRelation()
	# (𝟎) ∘ ((A) † ((C)⁻)) = 𝟎
	match expression:
		case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.EmptyRelation():
					match arg2:
						case COR_Expressions.Dagger(argument1=arg1, argument2=arg2):
							match arg1:
								case _:
									A = arg1
									match arg2:
										case COR_Expressions.Complement(argument=arg):
											match arg:
												case _:
													C = arg
													return COR_Expressions.EmptyRelation()
	# ((𝟏)⁻) ∪ ((C)⁻¹) = (C) ∪ ((𝟏)⁻)
	match expression:
		case COR_Expressions.Union(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.Complement(argument=arg):
					match arg:
						case COR_Expressions.IdentityRelation:
							match arg2:
								case COR_Expressions.Converse(argument=arg):
									match arg:
										case _:
											C = arg
											return COR_Expressions.Union(C, COR_Expressions.Complement(COR_Expressions.IdentityRelation()))
	# (C) ∪ ((C) ∪ ((A)⁻)) = (C) ∪ ((A)⁻)
	match expression:
		case COR_Expressions.Union(argument1=arg1, argument2=arg2):
			match arg1:
				case _:
					C = arg1
					match arg2:
						case COR_Expressions.Union(argument1=arg1, argument2=arg2):
							match arg1:
								case _:
									C = arg1
									match arg2:
										case COR_Expressions.Complement(argument=arg):
											match arg:
												case _:
													A = arg
													return COR_Expressions.Union(C, COR_Expressions.Complement(A))
	# (C) ∪ ((C) ∪ ((B)⁻¹)) = (C) ∪ ((B)⁻¹)
	match expression:
		case COR_Expressions.Union(argument1=arg1, argument2=arg2):
			match arg1:
				case _:
					C = arg1
					match arg2:
						case COR_Expressions.Union(argument1=arg1, argument2=arg2):
							match arg1:
								case _:
									C = arg1
									match arg2:
										case COR_Expressions.Converse(argument=arg):
											match arg:
												case _:
													B = arg
													return COR_Expressions.Union(C, COR_Expressions.Converse(B))
	# (𝟏) ∘ ((𝟎) † ((A)⁻¹)) = (𝟎) † ((A)⁻¹)
	match expression:
		case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.IdentityRelation:
					match arg2:
						case COR_Expressions.Dagger(argument1=arg1, argument2=arg2):
							match arg1:
								case COR_Expressions.EmptyRelation():
									match arg2:
										case COR_Expressions.Converse(argument=arg):
											match arg:
												case _:
													A = arg
													return COR_Expressions.Dagger(COR_Expressions.EmptyRelation(), COR_Expressions.Converse(A))
	# (𝟏) ∘ ((A) ∪ ((A)⁻¹)) = (A) ∪ ((A)⁻¹)
	match expression:
		case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.IdentityRelation:
					match arg2:
						case COR_Expressions.Union(argument1=arg1, argument2=arg2):
							match arg1:
								case _:
									A = arg1
									match arg2:
										case COR_Expressions.Converse(argument=arg):
											match arg:
												case _:
													A = arg
													return COR_Expressions.Union(A, COR_Expressions.Converse(A))
	# (T) † ((A) ∪ ((B)⁻)) = T
	match expression:
		case COR_Expressions.Dagger(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.UniversalRelation():
					match arg2:
						case COR_Expressions.Union(argument1=arg1, argument2=arg2):
							match arg1:
								case _:
									A = arg1
									match arg2:
										case COR_Expressions.Complement(argument=arg):
											match arg:
												case _:
													B = arg
													return COR_Expressions.UniversalRelation()
	# (𝟏) ∘ ((B) ∪ ((C)⁻)) = (B) ∪ ((C)⁻)
	match expression:
		case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.IdentityRelation:
					match arg2:
						case COR_Expressions.Union(argument1=arg1, argument2=arg2):
							match arg1:
								case _:
									B = arg1
									match arg2:
										case COR_Expressions.Complement(argument=arg):
											match arg:
												case _:
													C = arg
													return COR_Expressions.Union(B, COR_Expressions.Complement(C))
	# (𝟎) ∘ ((A) ∘ ((C)⁻¹)) = 𝟎
	match expression:
		case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.EmptyRelation():
					match arg2:
						case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
							match arg1:
								case _:
									A = arg1
									match arg2:
										case COR_Expressions.Converse(argument=arg):
											match arg:
												case _:
													C = arg
													return COR_Expressions.EmptyRelation()
	# (T) ∘ ((𝟎) † ((C)⁻)) = (𝟎) † ((C)⁻)
	match expression:
		case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.UniversalRelation():
					match arg2:
						case COR_Expressions.Dagger(argument1=arg1, argument2=arg2):
							match arg1:
								case COR_Expressions.EmptyRelation():
									match arg2:
										case COR_Expressions.Complement(argument=arg):
											match arg:
												case _:
													C = arg
													return COR_Expressions.Dagger(COR_Expressions.EmptyRelation(), COR_Expressions.Complement(C))
	# (C) ∪ ((C) ∪ ((𝟏)⁻)) = (C) ∪ ((𝟏)⁻)
	match expression:
		case COR_Expressions.Union(argument1=arg1, argument2=arg2):
			match arg1:
				case _:
					C = arg1
					match arg2:
						case COR_Expressions.Union(argument1=arg1, argument2=arg2):
							match arg1:
								case _:
									C = arg1
									match arg2:
										case COR_Expressions.Complement(argument=arg):
											match arg:
												case COR_Expressions.IdentityRelation:
													return COR_Expressions.Union(C, COR_Expressions.Complement(COR_Expressions.IdentityRelation()))
	# (B) ∪ ((B) ∪ ((B)⁻¹)) = (B) ∪ ((B)⁻¹)
	match expression:
		case COR_Expressions.Union(argument1=arg1, argument2=arg2):
			match arg1:
				case _:
					B = arg1
					match arg2:
						case COR_Expressions.Union(argument1=arg1, argument2=arg2):
							match arg1:
								case _:
									B = arg1
									match arg2:
										case COR_Expressions.Converse(argument=arg):
											match arg:
												case _:
													B = arg
													return COR_Expressions.Union(B, COR_Expressions.Converse(B))
	# (T) † ((A) † ((B)⁻)) = T
	match expression:
		case COR_Expressions.Dagger(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.UniversalRelation():
					match arg2:
						case COR_Expressions.Dagger(argument1=arg1, argument2=arg2):
							match arg1:
								case _:
									A = arg1
									match arg2:
										case COR_Expressions.Complement(argument=arg):
											match arg:
												case _:
													B = arg
													return COR_Expressions.UniversalRelation()
	# (T) ∪ ((C) ∘ ((C)⁻)) = T
	match expression:
		case COR_Expressions.Union(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.UniversalRelation():
					match arg2:
						case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
							match arg1:
								case _:
									C = arg1
									match arg2:
										case COR_Expressions.Complement(argument=arg):
											match arg:
												case _:
													C = arg
													return COR_Expressions.UniversalRelation()
	# ((A) ∪ ((𝟏)⁻))⁻¹ = (A) ∪ ((𝟏)⁻)
	match expression:
		case COR_Expressions.Converse(argument=arg):
			match arg:
				case COR_Expressions.Union(argument1=arg1, argument2=arg2):
					match arg1:
						case _:
							A = arg1
							match arg2:
								case COR_Expressions.Complement(argument=arg):
									match arg:
										case COR_Expressions.IdentityRelation:
											return COR_Expressions.Union(A, COR_Expressions.Complement(COR_Expressions.IdentityRelation()))
	# (T) † ((𝟎) † ((C)⁻¹)) = T
	match expression:
		case COR_Expressions.Dagger(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.UniversalRelation():
					match arg2:
						case COR_Expressions.Dagger(argument1=arg1, argument2=arg2):
							match arg1:
								case COR_Expressions.EmptyRelation():
									match arg2:
										case COR_Expressions.Converse(argument=arg):
											match arg:
												case _:
													C = arg
													return COR_Expressions.UniversalRelation()
	# ((A)⁻¹) ∪ ((A)⁻¹) = (A)⁻¹
	match expression:
		case COR_Expressions.Union(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.Converse(argument=arg):
					match arg:
						case _:
							A = arg
							match arg2:
								case COR_Expressions.Converse(argument=arg):
									match arg:
										case _:
											A = arg
											return COR_Expressions.Converse(A)
	# (T) † ((A) ∪ ((C)⁻)) = T
	match expression:
		case COR_Expressions.Dagger(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.UniversalRelation():
					match arg2:
						case COR_Expressions.Union(argument1=arg1, argument2=arg2):
							match arg1:
								case _:
									A = arg1
									match arg2:
										case COR_Expressions.Complement(argument=arg):
											match arg:
												case _:
													C = arg
													return COR_Expressions.UniversalRelation()
	# (T) † ((A) ∪ ((A)⁻¹)) = T
	match expression:
		case COR_Expressions.Dagger(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.UniversalRelation():
					match arg2:
						case COR_Expressions.Union(argument1=arg1, argument2=arg2):
							match arg1:
								case _:
									A = arg1
									match arg2:
										case COR_Expressions.Converse(argument=arg):
											match arg:
												case _:
													A = arg
													return COR_Expressions.UniversalRelation()
	# (T) ∪ ((T) ∘ ((A)⁻¹)) = T
	match expression:
		case COR_Expressions.Union(argument1=arg1, argument2=arg2):
			match arg1:
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
													return COR_Expressions.UniversalRelation()
	# (𝟎) † ((T) ∘ ((C)⁻¹)) = (T) ∘ ((C)⁻¹)
	match expression:
		case COR_Expressions.Dagger(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.EmptyRelation():
					match arg2:
						case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
							match arg1:
								case COR_Expressions.UniversalRelation():
									match arg2:
										case COR_Expressions.Converse(argument=arg):
											match arg:
												case _:
													C = arg
													return COR_Expressions.Composition(COR_Expressions.UniversalRelation(), COR_Expressions.Converse(C))
	# (A) ∪ ((A) ∪ ((B)⁻¹)) = (A) ∪ ((B)⁻¹)
	match expression:
		case COR_Expressions.Union(argument1=arg1, argument2=arg2):
			match arg1:
				case _:
					A = arg1
					match arg2:
						case COR_Expressions.Union(argument1=arg1, argument2=arg2):
							match arg1:
								case _:
									A = arg1
									match arg2:
										case COR_Expressions.Converse(argument=arg):
											match arg:
												case _:
													B = arg
													return COR_Expressions.Union(A, COR_Expressions.Converse(B))
	# (T) ∪ ((𝟎) † ((C)⁻¹)) = T
	match expression:
		case COR_Expressions.Union(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.UniversalRelation():
					match arg2:
						case COR_Expressions.Dagger(argument1=arg1, argument2=arg2):
							match arg1:
								case COR_Expressions.EmptyRelation():
									match arg2:
										case COR_Expressions.Converse(argument=arg):
											match arg:
												case _:
													C = arg
													return COR_Expressions.UniversalRelation()
	# (𝟏) ∘ ((C) † ((B)⁻¹)) = (C) † ((B)⁻¹)
	match expression:
		case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.IdentityRelation:
					match arg2:
						case COR_Expressions.Dagger(argument1=arg1, argument2=arg2):
							match arg1:
								case _:
									C = arg1
									match arg2:
										case COR_Expressions.Converse(argument=arg):
											match arg:
												case _:
													B = arg
													return COR_Expressions.Dagger(C, COR_Expressions.Converse(B))
	# (𝟎) ∪ ((A) ∘ ((C)⁻¹)) = (A) ∘ ((C)⁻¹)
	match expression:
		case COR_Expressions.Union(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.EmptyRelation():
					match arg2:
						case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
							match arg1:
								case _:
									A = arg1
									match arg2:
										case COR_Expressions.Converse(argument=arg):
											match arg:
												case _:
													C = arg
													return COR_Expressions.Composition(A, COR_Expressions.Converse(C))
	# (𝟎) ∪ ((𝟎) † ((B)⁻)) = (𝟎) † ((B)⁻)
	match expression:
		case COR_Expressions.Union(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.EmptyRelation():
					match arg2:
						case COR_Expressions.Dagger(argument1=arg1, argument2=arg2):
							match arg1:
								case COR_Expressions.EmptyRelation():
									match arg2:
										case COR_Expressions.Complement(argument=arg):
											match arg:
												case _:
													B = arg
													return COR_Expressions.Dagger(COR_Expressions.EmptyRelation(), COR_Expressions.Complement(B))
	# (𝟎) ∘ ((T) ∘ ((C)⁻)) = 𝟎
	match expression:
		case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.EmptyRelation():
					match arg2:
						case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
							match arg1:
								case COR_Expressions.UniversalRelation():
									match arg2:
										case COR_Expressions.Complement(argument=arg):
											match arg:
												case _:
													C = arg
													return COR_Expressions.EmptyRelation()
	# (𝟏) ∪ ((𝟏) ∪ ((C)⁻)) = (𝟏) ∪ ((C)⁻)
	match expression:
		case COR_Expressions.Union(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.IdentityRelation:
					match arg2:
						case COR_Expressions.Union(argument1=arg1, argument2=arg2):
							match arg1:
								case COR_Expressions.IdentityRelation:
									match arg2:
										case COR_Expressions.Complement(argument=arg):
											match arg:
												case _:
													C = arg
													return COR_Expressions.Union(COR_Expressions.IdentityRelation(), COR_Expressions.Complement(C))
	# (𝟎) ∘ ((B) † ((C)⁻¹)) = 𝟎
	match expression:
		case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.EmptyRelation():
					match arg2:
						case COR_Expressions.Dagger(argument1=arg1, argument2=arg2):
							match arg1:
								case _:
									B = arg1
									match arg2:
										case COR_Expressions.Converse(argument=arg):
											match arg:
												case _:
													C = arg
													return COR_Expressions.EmptyRelation()
	# (𝟎) † ((T) ∘ ((𝟏)⁻)) = (T) ∘ ((𝟏)⁻)
	match expression:
		case COR_Expressions.Dagger(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.EmptyRelation():
					match arg2:
						case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
							match arg1:
								case COR_Expressions.UniversalRelation():
									match arg2:
										case COR_Expressions.Complement(argument=arg):
											match arg:
												case COR_Expressions.IdentityRelation:
													return COR_Expressions.Composition(COR_Expressions.UniversalRelation(), COR_Expressions.Complement(COR_Expressions.IdentityRelation()))
	# (T) † ((T) ∘ ((C)⁻)) = T
	match expression:
		case COR_Expressions.Dagger(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.UniversalRelation():
					match arg2:
						case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
							match arg1:
								case COR_Expressions.UniversalRelation():
									match arg2:
										case COR_Expressions.Complement(argument=arg):
											match arg:
												case _:
													C = arg
													return COR_Expressions.UniversalRelation()
	# ((B) ∪ ((𝟏)⁻))⁻¹ = (B) ∪ ((𝟏)⁻)
	match expression:
		case COR_Expressions.Converse(argument=arg):
			match arg:
				case COR_Expressions.Union(argument1=arg1, argument2=arg2):
					match arg1:
						case _:
							B = arg1
							match arg2:
								case COR_Expressions.Complement(argument=arg):
									match arg:
										case COR_Expressions.IdentityRelation:
											return COR_Expressions.Union(B, COR_Expressions.Complement(COR_Expressions.IdentityRelation()))
	# (𝟎) ∪ ((𝟏) † ((C)⁻)) = (𝟏) † ((C)⁻)
	match expression:
		case COR_Expressions.Union(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.EmptyRelation():
					match arg2:
						case COR_Expressions.Dagger(argument1=arg1, argument2=arg2):
							match arg1:
								case COR_Expressions.IdentityRelation:
									match arg2:
										case COR_Expressions.Complement(argument=arg):
											match arg:
												case _:
													C = arg
													return COR_Expressions.Dagger(COR_Expressions.IdentityRelation(), COR_Expressions.Complement(C))
	# (𝟏) ∘ ((B) ∘ ((B)⁻)) = (B) ∘ ((B)⁻)
	match expression:
		case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.IdentityRelation:
					match arg2:
						case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
							match arg1:
								case _:
									B = arg1
									match arg2:
										case COR_Expressions.Complement(argument=arg):
											match arg:
												case _:
													B = arg
													return COR_Expressions.Composition(B, COR_Expressions.Complement(B))
	# (T) ∘ ((C) ∘ ((C)⁻¹)) = (T) ∘ ((C)⁻¹)
	match expression:
		case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.UniversalRelation():
					match arg2:
						case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
							match arg1:
								case _:
									C = arg1
									match arg2:
										case COR_Expressions.Converse(argument=arg):
											match arg:
												case _:
													C = arg
													return COR_Expressions.Composition(COR_Expressions.UniversalRelation(), COR_Expressions.Converse(C))
	# (𝟏) ∘ (((A)⁻)⁻¹) = ((A)⁻¹)⁻
	match expression:
		case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.IdentityRelation:
					match arg2:
						case COR_Expressions.Converse(argument=arg):
							match arg:
								case COR_Expressions.Complement(argument=arg):
									match arg:
										case _:
											A = arg
											return COR_Expressions.Complement(COR_Expressions.Converse(A))
	# (T) ∪ ((𝟏) ∪ ((A)⁻¹)) = T
	match expression:
		case COR_Expressions.Union(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.UniversalRelation():
					match arg2:
						case COR_Expressions.Union(argument1=arg1, argument2=arg2):
							match arg1:
								case COR_Expressions.IdentityRelation:
									match arg2:
										case COR_Expressions.Converse(argument=arg):
											match arg:
												case _:
													A = arg
													return COR_Expressions.UniversalRelation()
	# ((B)⁻¹) † ((𝟏)⁻) = (B)⁻¹
	match expression:
		case COR_Expressions.Dagger(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.Converse(argument=arg):
					match arg:
						case _:
							B = arg
							match arg2:
								case COR_Expressions.Complement(argument=arg):
									match arg:
										case COR_Expressions.IdentityRelation:
											return COR_Expressions.Converse(B)
	# (T) ∪ ((B) † ((C)⁻)) = T
	match expression:
		case COR_Expressions.Union(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.UniversalRelation():
					match arg2:
						case COR_Expressions.Dagger(argument1=arg1, argument2=arg2):
							match arg1:
								case _:
									B = arg1
									match arg2:
										case COR_Expressions.Complement(argument=arg):
											match arg:
												case _:
													C = arg
													return COR_Expressions.UniversalRelation()
	# ((B) ∪ ((C)⁻¹))⁻¹ = (C) ∪ ((B)⁻¹)
	match expression:
		case COR_Expressions.Converse(argument=arg):
			match arg:
				case COR_Expressions.Union(argument1=arg1, argument2=arg2):
					match arg1:
						case _:
							B = arg1
							match arg2:
								case COR_Expressions.Converse(argument=arg):
									match arg:
										case _:
											C = arg
											return COR_Expressions.Union(C, COR_Expressions.Converse(B))
	# (((A)⁻¹)⁻)⁻ = (A)⁻¹
	match expression:
		case COR_Expressions.Complement(argument=arg):
			match arg:
				case COR_Expressions.Complement(argument=arg):
					match arg:
						case COR_Expressions.Converse(argument=arg):
							match arg:
								case _:
									A = arg
									return COR_Expressions.Converse(A)
	# (T) ∪ ((B) † ((B)⁻)) = T
	match expression:
		case COR_Expressions.Union(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.UniversalRelation():
					match arg2:
						case COR_Expressions.Dagger(argument1=arg1, argument2=arg2):
							match arg1:
								case _:
									B = arg1
									match arg2:
										case COR_Expressions.Complement(argument=arg):
											match arg:
												case _:
													B = arg
													return COR_Expressions.UniversalRelation()
	# (𝟎) ∪ ((B) ∘ ((A)⁻¹)) = (B) ∘ ((A)⁻¹)
	match expression:
		case COR_Expressions.Union(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.EmptyRelation():
					match arg2:
						case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
							match arg1:
								case _:
									B = arg1
									match arg2:
										case COR_Expressions.Converse(argument=arg):
											match arg:
												case _:
													A = arg
													return COR_Expressions.Composition(B, COR_Expressions.Converse(A))
	# (𝟏) ∘ ((T) ∘ ((C)⁻)) = (T) ∘ ((C)⁻)
	match expression:
		case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.IdentityRelation:
					match arg2:
						case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
							match arg1:
								case COR_Expressions.UniversalRelation():
									match arg2:
										case COR_Expressions.Complement(argument=arg):
											match arg:
												case _:
													C = arg
													return COR_Expressions.Composition(COR_Expressions.UniversalRelation(), COR_Expressions.Complement(C))
	# (𝟏) ∘ ((C) ∪ ((A)⁻¹)) = (C) ∪ ((A)⁻¹)
	match expression:
		case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.IdentityRelation:
					match arg2:
						case COR_Expressions.Union(argument1=arg1, argument2=arg2):
							match arg1:
								case _:
									C = arg1
									match arg2:
										case COR_Expressions.Converse(argument=arg):
											match arg:
												case _:
													A = arg
													return COR_Expressions.Union(C, COR_Expressions.Converse(A))
	# (T) ∪ (((C)⁻¹)⁻) = T
	match expression:
		case COR_Expressions.Union(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.UniversalRelation():
					match arg2:
						case COR_Expressions.Complement(argument=arg):
							match arg:
								case COR_Expressions.Converse(argument=arg):
									match arg:
										case _:
											C = arg
											return COR_Expressions.UniversalRelation()
	# (𝟎) ∪ ((T) ∘ ((C)⁻)) = (T) ∘ ((C)⁻)
	match expression:
		case COR_Expressions.Union(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.EmptyRelation():
					match arg2:
						case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
							match arg1:
								case COR_Expressions.UniversalRelation():
									match arg2:
										case COR_Expressions.Complement(argument=arg):
											match arg:
												case _:
													C = arg
													return COR_Expressions.Composition(COR_Expressions.UniversalRelation(), COR_Expressions.Complement(C))
	# (T) ∪ ((𝟏) ∪ ((B)⁻)) = T
	match expression:
		case COR_Expressions.Union(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.UniversalRelation():
					match arg2:
						case COR_Expressions.Union(argument1=arg1, argument2=arg2):
							match arg1:
								case COR_Expressions.IdentityRelation:
									match arg2:
										case COR_Expressions.Complement(argument=arg):
											match arg:
												case _:
													B = arg
													return COR_Expressions.UniversalRelation()
	# (T) ∪ ((C) † ((C)⁻)) = T
	match expression:
		case COR_Expressions.Union(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.UniversalRelation():
					match arg2:
						case COR_Expressions.Dagger(argument1=arg1, argument2=arg2):
							match arg1:
								case _:
									C = arg1
									match arg2:
										case COR_Expressions.Complement(argument=arg):
											match arg:
												case _:
													C = arg
													return COR_Expressions.UniversalRelation()
	# (𝟎) ∘ ((B) † ((B)⁻)) = 𝟎
	match expression:
		case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.EmptyRelation():
					match arg2:
						case COR_Expressions.Dagger(argument1=arg1, argument2=arg2):
							match arg1:
								case _:
									B = arg1
									match arg2:
										case COR_Expressions.Complement(argument=arg):
											match arg:
												case _:
													B = arg
													return COR_Expressions.EmptyRelation()
	# (𝟎) ∪ ((B) ∪ ((C)⁻¹)) = (B) ∪ ((C)⁻¹)
	match expression:
		case COR_Expressions.Union(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.EmptyRelation():
					match arg2:
						case COR_Expressions.Union(argument1=arg1, argument2=arg2):
							match arg1:
								case _:
									B = arg1
									match arg2:
										case COR_Expressions.Converse(argument=arg):
											match arg:
												case _:
													C = arg
													return COR_Expressions.Union(B, COR_Expressions.Converse(C))
	# (T) ∪ ((A) † ((B)⁻)) = T
	match expression:
		case COR_Expressions.Union(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.UniversalRelation():
					match arg2:
						case COR_Expressions.Dagger(argument1=arg1, argument2=arg2):
							match arg1:
								case _:
									A = arg1
									match arg2:
										case COR_Expressions.Complement(argument=arg):
											match arg:
												case _:
													B = arg
													return COR_Expressions.UniversalRelation()
	# (𝟏) ∘ ((T) ∘ ((𝟏)⁻)) = (T) ∘ ((𝟏)⁻)
	match expression:
		case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.IdentityRelation:
					match arg2:
						case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
							match arg1:
								case COR_Expressions.UniversalRelation():
									match arg2:
										case COR_Expressions.Complement(argument=arg):
											match arg:
												case COR_Expressions.IdentityRelation:
													return COR_Expressions.Composition(COR_Expressions.UniversalRelation(), COR_Expressions.Complement(COR_Expressions.IdentityRelation()))
	# (T) ∪ ((𝟎) † ((A)⁻¹)) = T
	match expression:
		case COR_Expressions.Union(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.UniversalRelation():
					match arg2:
						case COR_Expressions.Dagger(argument1=arg1, argument2=arg2):
							match arg1:
								case COR_Expressions.EmptyRelation():
									match arg2:
										case COR_Expressions.Converse(argument=arg):
											match arg:
												case _:
													A = arg
													return COR_Expressions.UniversalRelation()
	# (𝟎) † ((𝟎) † ((B)⁻¹)) = (𝟎) † ((B)⁻¹)
	match expression:
		case COR_Expressions.Dagger(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.EmptyRelation():
					match arg2:
						case COR_Expressions.Dagger(argument1=arg1, argument2=arg2):
							match arg1:
								case COR_Expressions.EmptyRelation():
									match arg2:
										case COR_Expressions.Converse(argument=arg):
											match arg:
												case _:
													B = arg
													return COR_Expressions.Dagger(COR_Expressions.EmptyRelation(), COR_Expressions.Converse(B))
	# (T) ∪ (((B)⁻)⁻¹) = T
	match expression:
		case COR_Expressions.Union(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.UniversalRelation():
					match arg2:
						case COR_Expressions.Converse(argument=arg):
							match arg:
								case COR_Expressions.Complement(argument=arg):
									match arg:
										case _:
											B = arg
											return COR_Expressions.UniversalRelation()
	# (((A)⁻)⁻¹)⁻ = (A)⁻¹
	match expression:
		case COR_Expressions.Complement(argument=arg):
			match arg:
				case COR_Expressions.Converse(argument=arg):
					match arg:
						case COR_Expressions.Complement(argument=arg):
							match arg:
								case _:
									A = arg
									return COR_Expressions.Converse(A)
	# (𝟎) ∪ ((C) † ((B)⁻)) = (C) † ((B)⁻)
	match expression:
		case COR_Expressions.Union(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.EmptyRelation():
					match arg2:
						case COR_Expressions.Dagger(argument1=arg1, argument2=arg2):
							match arg1:
								case _:
									C = arg1
									match arg2:
										case COR_Expressions.Complement(argument=arg):
											match arg:
												case _:
													B = arg
													return COR_Expressions.Dagger(C, COR_Expressions.Complement(B))
	# (𝟏) ∘ ((𝟏) † ((A)⁻)) = (𝟏) † ((A)⁻)
	match expression:
		case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.IdentityRelation:
					match arg2:
						case COR_Expressions.Dagger(argument1=arg1, argument2=arg2):
							match arg1:
								case COR_Expressions.IdentityRelation:
									match arg2:
										case COR_Expressions.Complement(argument=arg):
											match arg:
												case _:
													A = arg
													return COR_Expressions.Dagger(COR_Expressions.IdentityRelation(), COR_Expressions.Complement(A))
	# (𝟎) ∪ ((B) † ((C)⁻¹)) = (B) † ((C)⁻¹)
	match expression:
		case COR_Expressions.Union(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.EmptyRelation():
					match arg2:
						case COR_Expressions.Dagger(argument1=arg1, argument2=arg2):
							match arg1:
								case _:
									B = arg1
									match arg2:
										case COR_Expressions.Converse(argument=arg):
											match arg:
												case _:
													C = arg
													return COR_Expressions.Dagger(B, COR_Expressions.Converse(C))
	# (𝟎) ∘ ((B) ∘ ((C)⁻¹)) = 𝟎
	match expression:
		case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.EmptyRelation():
					match arg2:
						case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
							match arg1:
								case _:
									B = arg1
									match arg2:
										case COR_Expressions.Converse(argument=arg):
											match arg:
												case _:
													C = arg
													return COR_Expressions.EmptyRelation()
	# (𝟎) ∘ ((𝟏) ∪ ((C)⁻¹)) = 𝟎
	match expression:
		case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.EmptyRelation():
					match arg2:
						case COR_Expressions.Union(argument1=arg1, argument2=arg2):
							match arg1:
								case COR_Expressions.IdentityRelation:
									match arg2:
										case COR_Expressions.Converse(argument=arg):
											match arg:
												case _:
													C = arg
													return COR_Expressions.EmptyRelation()
	# (T) † ((C) ∘ ((C)⁻¹)) = T
	match expression:
		case COR_Expressions.Dagger(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.UniversalRelation():
					match arg2:
						case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
							match arg1:
								case _:
									C = arg1
									match arg2:
										case COR_Expressions.Converse(argument=arg):
											match arg:
												case _:
													C = arg
													return COR_Expressions.UniversalRelation()
	# (𝟎) ∘ ((A) ∘ ((𝟏)⁻)) = 𝟎
	match expression:
		case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.EmptyRelation():
					match arg2:
						case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
							match arg1:
								case _:
									A = arg1
									match arg2:
										case COR_Expressions.Complement(argument=arg):
											match arg:
												case COR_Expressions.IdentityRelation:
													return COR_Expressions.EmptyRelation()
	# (𝟎) ∘ (((B)⁻)⁻¹) = 𝟎
	match expression:
		case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.EmptyRelation():
					match arg2:
						case COR_Expressions.Converse(argument=arg):
							match arg:
								case COR_Expressions.Complement(argument=arg):
									match arg:
										case _:
											B = arg
											return COR_Expressions.EmptyRelation()
	# (T) † ((C) ∘ ((𝟏)⁻)) = T
	match expression:
		case COR_Expressions.Dagger(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.UniversalRelation():
					match arg2:
						case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
							match arg1:
								case _:
									C = arg1
									match arg2:
										case COR_Expressions.Complement(argument=arg):
											match arg:
												case COR_Expressions.IdentityRelation:
													return COR_Expressions.UniversalRelation()
	# (𝟎) ∘ (((B)⁻¹)⁻) = 𝟎
	match expression:
		case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.EmptyRelation():
					match arg2:
						case COR_Expressions.Complement(argument=arg):
							match arg:
								case COR_Expressions.Converse(argument=arg):
									match arg:
										case _:
											B = arg
											return COR_Expressions.EmptyRelation()
	# ((𝟏)⁻) † ((C)⁻¹) = (C)⁻¹
	match expression:
		case COR_Expressions.Dagger(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.Complement(argument=arg):
					match arg:
						case COR_Expressions.IdentityRelation:
							match arg2:
								case COR_Expressions.Converse(argument=arg):
									match arg:
										case _:
											C = arg
											return COR_Expressions.Converse(C)
	# ((A) ∘ ((C)⁻¹))⁻¹ = (C) ∘ ((A)⁻¹)
	match expression:
		case COR_Expressions.Converse(argument=arg):
			match arg:
				case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
					match arg1:
						case _:
							A = arg1
							match arg2:
								case COR_Expressions.Converse(argument=arg):
									match arg:
										case _:
											C = arg
											return COR_Expressions.Composition(C, COR_Expressions.Converse(A))
	# ((B) † ((C)⁻¹))⁻¹ = (C) † ((B)⁻¹)
	match expression:
		case COR_Expressions.Converse(argument=arg):
			match arg:
				case COR_Expressions.Dagger(argument1=arg1, argument2=arg2):
					match arg1:
						case _:
							B = arg1
							match arg2:
								case COR_Expressions.Converse(argument=arg):
									match arg:
										case _:
											C = arg
											return COR_Expressions.Dagger(C, COR_Expressions.Converse(B))
	# (T) ∪ ((C) ∘ ((C)⁻¹)) = T
	match expression:
		case COR_Expressions.Union(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.UniversalRelation():
					match arg2:
						case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
							match arg1:
								case _:
									C = arg1
									match arg2:
										case COR_Expressions.Converse(argument=arg):
											match arg:
												case _:
													C = arg
													return COR_Expressions.UniversalRelation()
	# (A) ∪ ((A) ∪ ((C)⁻¹)) = (A) ∪ ((C)⁻¹)
	match expression:
		case COR_Expressions.Union(argument1=arg1, argument2=arg2):
			match arg1:
				case _:
					A = arg1
					match arg2:
						case COR_Expressions.Union(argument1=arg1, argument2=arg2):
							match arg1:
								case _:
									A = arg1
									match arg2:
										case COR_Expressions.Converse(argument=arg):
											match arg:
												case _:
													C = arg
													return COR_Expressions.Union(A, COR_Expressions.Converse(C))
	# (𝟎) ∪ ((B) ∪ ((C)⁻)) = (B) ∪ ((C)⁻)
	match expression:
		case COR_Expressions.Union(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.EmptyRelation():
					match arg2:
						case COR_Expressions.Union(argument1=arg1, argument2=arg2):
							match arg1:
								case _:
									B = arg1
									match arg2:
										case COR_Expressions.Complement(argument=arg):
											match arg:
												case _:
													C = arg
													return COR_Expressions.Union(B, COR_Expressions.Complement(C))
	# (T) † ((T) ∘ ((B)⁻)) = T
	match expression:
		case COR_Expressions.Dagger(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.UniversalRelation():
					match arg2:
						case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
							match arg1:
								case COR_Expressions.UniversalRelation():
									match arg2:
										case COR_Expressions.Complement(argument=arg):
											match arg:
												case _:
													B = arg
													return COR_Expressions.UniversalRelation()
	# (T) † (((C)⁻)⁻¹) = T
	match expression:
		case COR_Expressions.Dagger(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.UniversalRelation():
					match arg2:
						case COR_Expressions.Converse(argument=arg):
							match arg:
								case COR_Expressions.Complement(argument=arg):
									match arg:
										case _:
											C = arg
											return COR_Expressions.UniversalRelation()
	# (T) † ((C) ∪ ((A)⁻)) = T
	match expression:
		case COR_Expressions.Dagger(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.UniversalRelation():
					match arg2:
						case COR_Expressions.Union(argument1=arg1, argument2=arg2):
							match arg1:
								case _:
									C = arg1
									match arg2:
										case COR_Expressions.Complement(argument=arg):
											match arg:
												case _:
													A = arg
													return COR_Expressions.UniversalRelation()
	# (𝟎) ∪ ((T) ∘ ((A)⁻¹)) = (T) ∘ ((A)⁻¹)
	match expression:
		case COR_Expressions.Union(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.EmptyRelation():
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
	# (𝟎) ∪ ((𝟏) † ((C)⁻¹)) = (𝟏) † ((C)⁻¹)
	match expression:
		case COR_Expressions.Union(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.EmptyRelation():
					match arg2:
						case COR_Expressions.Dagger(argument1=arg1, argument2=arg2):
							match arg1:
								case COR_Expressions.IdentityRelation:
									match arg2:
										case COR_Expressions.Converse(argument=arg):
											match arg:
												case _:
													C = arg
													return COR_Expressions.Dagger(COR_Expressions.IdentityRelation(), COR_Expressions.Converse(C))
	# (((B)⁻¹)⁻)⁻¹ = (B)⁻
	match expression:
		case COR_Expressions.Converse(argument=arg):
			match arg:
				case COR_Expressions.Complement(argument=arg):
					match arg:
						case COR_Expressions.Converse(argument=arg):
							match arg:
								case _:
									B = arg
									return COR_Expressions.Complement(B)
	# ((C) † ((B)⁻¹))⁻¹ = (B) † ((C)⁻¹)
	match expression:
		case COR_Expressions.Converse(argument=arg):
			match arg:
				case COR_Expressions.Dagger(argument1=arg1, argument2=arg2):
					match arg1:
						case _:
							C = arg1
							match arg2:
								case COR_Expressions.Converse(argument=arg):
									match arg:
										case _:
											B = arg
											return COR_Expressions.Dagger(B, COR_Expressions.Converse(C))
	# (𝟎) ∪ ((T) ∘ ((C)⁻¹)) = (T) ∘ ((C)⁻¹)
	match expression:
		case COR_Expressions.Union(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.EmptyRelation():
					match arg2:
						case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
							match arg1:
								case COR_Expressions.UniversalRelation():
									match arg2:
										case COR_Expressions.Converse(argument=arg):
											match arg:
												case _:
													C = arg
													return COR_Expressions.Composition(COR_Expressions.UniversalRelation(), COR_Expressions.Converse(C))
	# (𝟏) ∘ ((A) ∪ ((B)⁻¹)) = (A) ∪ ((B)⁻¹)
	match expression:
		case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.IdentityRelation:
					match arg2:
						case COR_Expressions.Union(argument1=arg1, argument2=arg2):
							match arg1:
								case _:
									A = arg1
									match arg2:
										case COR_Expressions.Converse(argument=arg):
											match arg:
												case _:
													B = arg
													return COR_Expressions.Union(A, COR_Expressions.Converse(B))
	# (𝟎) ∘ ((B) ∪ ((C)⁻¹)) = 𝟎
	match expression:
		case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.EmptyRelation():
					match arg2:
						case COR_Expressions.Union(argument1=arg1, argument2=arg2):
							match arg1:
								case _:
									B = arg1
									match arg2:
										case COR_Expressions.Converse(argument=arg):
											match arg:
												case _:
													C = arg
													return COR_Expressions.EmptyRelation()
	# (𝟏) ∘ ((𝟏) † ((B)⁻¹)) = (𝟏) † ((B)⁻¹)
	match expression:
		case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.IdentityRelation:
					match arg2:
						case COR_Expressions.Dagger(argument1=arg1, argument2=arg2):
							match arg1:
								case COR_Expressions.IdentityRelation:
									match arg2:
										case COR_Expressions.Converse(argument=arg):
											match arg:
												case _:
													B = arg
													return COR_Expressions.Dagger(COR_Expressions.IdentityRelation(), COR_Expressions.Converse(B))
	# (C) ∪ ((C) ∪ ((A)⁻¹)) = (C) ∪ ((A)⁻¹)
	match expression:
		case COR_Expressions.Union(argument1=arg1, argument2=arg2):
			match arg1:
				case _:
					C = arg1
					match arg2:
						case COR_Expressions.Union(argument1=arg1, argument2=arg2):
							match arg1:
								case _:
									C = arg1
									match arg2:
										case COR_Expressions.Converse(argument=arg):
											match arg:
												case _:
													A = arg
													return COR_Expressions.Union(C, COR_Expressions.Converse(A))
	# (𝟏) ∘ ((A) † ((B)⁻)) = (A) † ((B)⁻)
	match expression:
		case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.IdentityRelation:
					match arg2:
						case COR_Expressions.Dagger(argument1=arg1, argument2=arg2):
							match arg1:
								case _:
									A = arg1
									match arg2:
										case COR_Expressions.Complement(argument=arg):
											match arg:
												case _:
													B = arg
													return COR_Expressions.Dagger(A, COR_Expressions.Complement(B))
	# (T) ∪ ((C) ∘ ((A)⁻)) = T
	match expression:
		case COR_Expressions.Union(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.UniversalRelation():
					match arg2:
						case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
							match arg1:
								case _:
									C = arg1
									match arg2:
										case COR_Expressions.Complement(argument=arg):
											match arg:
												case _:
													A = arg
													return COR_Expressions.UniversalRelation()
	# (𝟎) ∪ ((𝟏) ∪ ((C)⁻¹)) = (𝟏) ∪ ((C)⁻¹)
	match expression:
		case COR_Expressions.Union(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.EmptyRelation():
					match arg2:
						case COR_Expressions.Union(argument1=arg1, argument2=arg2):
							match arg1:
								case COR_Expressions.IdentityRelation:
									match arg2:
										case COR_Expressions.Converse(argument=arg):
											match arg:
												case _:
													C = arg
													return COR_Expressions.Union(COR_Expressions.IdentityRelation(), COR_Expressions.Converse(C))
	# (𝟎) ∘ ((C) ∪ ((C)⁻¹)) = 𝟎
	match expression:
		case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.EmptyRelation():
					match arg2:
						case COR_Expressions.Union(argument1=arg1, argument2=arg2):
							match arg1:
								case _:
									C = arg1
									match arg2:
										case COR_Expressions.Converse(argument=arg):
											match arg:
												case _:
													C = arg
													return COR_Expressions.EmptyRelation()
	# (𝟎) ∪ ((B) ∘ ((A)⁻)) = (B) ∘ ((A)⁻)
	match expression:
		case COR_Expressions.Union(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.EmptyRelation():
					match arg2:
						case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
							match arg1:
								case _:
									B = arg1
									match arg2:
										case COR_Expressions.Complement(argument=arg):
											match arg:
												case _:
													A = arg
													return COR_Expressions.Composition(B, COR_Expressions.Complement(A))
	# (𝟏) ∘ ((A) † ((B)⁻¹)) = (A) † ((B)⁻¹)
	match expression:
		case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.IdentityRelation:
					match arg2:
						case COR_Expressions.Dagger(argument1=arg1, argument2=arg2):
							match arg1:
								case _:
									A = arg1
									match arg2:
										case COR_Expressions.Converse(argument=arg):
											match arg:
												case _:
													B = arg
													return COR_Expressions.Dagger(A, COR_Expressions.Converse(B))
	# (T) ∪ ((B) ∘ ((C)⁻)) = T
	match expression:
		case COR_Expressions.Union(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.UniversalRelation():
					match arg2:
						case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
							match arg1:
								case _:
									B = arg1
									match arg2:
										case COR_Expressions.Complement(argument=arg):
											match arg:
												case _:
													C = arg
													return COR_Expressions.UniversalRelation()
	# (𝟎) ∘ ((A) ∪ ((C)⁻)) = 𝟎
	match expression:
		case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.EmptyRelation():
					match arg2:
						case COR_Expressions.Union(argument1=arg1, argument2=arg2):
							match arg1:
								case _:
									A = arg1
									match arg2:
										case COR_Expressions.Complement(argument=arg):
											match arg:
												case _:
													C = arg
													return COR_Expressions.EmptyRelation()
	# (T) † ((B) ∪ ((C)⁻)) = T
	match expression:
		case COR_Expressions.Dagger(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.UniversalRelation():
					match arg2:
						case COR_Expressions.Union(argument1=arg1, argument2=arg2):
							match arg1:
								case _:
									B = arg1
									match arg2:
										case COR_Expressions.Complement(argument=arg):
											match arg:
												case _:
													C = arg
													return COR_Expressions.UniversalRelation()
	# (𝟎) ∪ ((T) ∘ ((𝟏)⁻)) = (T) ∘ ((𝟏)⁻)
	match expression:
		case COR_Expressions.Union(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.EmptyRelation():
					match arg2:
						case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
							match arg1:
								case COR_Expressions.UniversalRelation():
									match arg2:
										case COR_Expressions.Complement(argument=arg):
											match arg:
												case COR_Expressions.IdentityRelation:
													return COR_Expressions.Composition(COR_Expressions.UniversalRelation(), COR_Expressions.Complement(COR_Expressions.IdentityRelation()))
	# (𝟏) ∘ ((B) ∘ ((B)⁻¹)) = (B) ∘ ((B)⁻¹)
	match expression:
		case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.IdentityRelation:
					match arg2:
						case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
							match arg1:
								case _:
									B = arg1
									match arg2:
										case COR_Expressions.Converse(argument=arg):
											match arg:
												case _:
													B = arg
													return COR_Expressions.Composition(B, COR_Expressions.Converse(B))
	# (T) ∪ ((C) ∪ ((𝟏)⁻)) = T
	match expression:
		case COR_Expressions.Union(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.UniversalRelation():
					match arg2:
						case COR_Expressions.Union(argument1=arg1, argument2=arg2):
							match arg1:
								case _:
									C = arg1
									match arg2:
										case COR_Expressions.Complement(argument=arg):
											match arg:
												case COR_Expressions.IdentityRelation:
													return COR_Expressions.UniversalRelation()
	# (T) ∪ ((𝟏) ∪ ((A)⁻)) = T
	match expression:
		case COR_Expressions.Union(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.UniversalRelation():
					match arg2:
						case COR_Expressions.Union(argument1=arg1, argument2=arg2):
							match arg1:
								case COR_Expressions.IdentityRelation:
									match arg2:
										case COR_Expressions.Complement(argument=arg):
											match arg:
												case _:
													A = arg
													return COR_Expressions.UniversalRelation()
	# (𝟎) ∪ ((𝟏) † ((A)⁻¹)) = (𝟏) † ((A)⁻¹)
	match expression:
		case COR_Expressions.Union(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.EmptyRelation():
					match arg2:
						case COR_Expressions.Dagger(argument1=arg1, argument2=arg2):
							match arg1:
								case COR_Expressions.IdentityRelation:
									match arg2:
										case COR_Expressions.Converse(argument=arg):
											match arg:
												case _:
													A = arg
													return COR_Expressions.Dagger(COR_Expressions.IdentityRelation(), COR_Expressions.Converse(A))
	# (T) † ((A) † ((B)⁻¹)) = T
	match expression:
		case COR_Expressions.Dagger(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.UniversalRelation():
					match arg2:
						case COR_Expressions.Dagger(argument1=arg1, argument2=arg2):
							match arg1:
								case _:
									A = arg1
									match arg2:
										case COR_Expressions.Converse(argument=arg):
											match arg:
												case _:
													B = arg
													return COR_Expressions.UniversalRelation()
	# (𝟏) ∘ ((T) ∘ ((B)⁻)) = (T) ∘ ((B)⁻)
	match expression:
		case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.IdentityRelation:
					match arg2:
						case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
							match arg1:
								case COR_Expressions.UniversalRelation():
									match arg2:
										case COR_Expressions.Complement(argument=arg):
											match arg:
												case _:
													B = arg
													return COR_Expressions.Composition(COR_Expressions.UniversalRelation(), COR_Expressions.Complement(B))
	# (T) † ((𝟎) † ((C)⁻)) = T
	match expression:
		case COR_Expressions.Dagger(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.UniversalRelation():
					match arg2:
						case COR_Expressions.Dagger(argument1=arg1, argument2=arg2):
							match arg1:
								case COR_Expressions.EmptyRelation():
									match arg2:
										case COR_Expressions.Complement(argument=arg):
											match arg:
												case _:
													C = arg
													return COR_Expressions.UniversalRelation()
	# (A) ∪ ((A) ∪ ((A)⁻¹)) = (A) ∪ ((A)⁻¹)
	match expression:
		case COR_Expressions.Union(argument1=arg1, argument2=arg2):
			match arg1:
				case _:
					A = arg1
					match arg2:
						case COR_Expressions.Union(argument1=arg1, argument2=arg2):
							match arg1:
								case _:
									A = arg1
									match arg2:
										case COR_Expressions.Converse(argument=arg):
											match arg:
												case _:
													A = arg
													return COR_Expressions.Union(A, COR_Expressions.Converse(A))
	# (T) † ((B) † ((C)⁻¹)) = T
	match expression:
		case COR_Expressions.Dagger(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.UniversalRelation():
					match arg2:
						case COR_Expressions.Dagger(argument1=arg1, argument2=arg2):
							match arg1:
								case _:
									B = arg1
									match arg2:
										case COR_Expressions.Converse(argument=arg):
											match arg:
												case _:
													C = arg
													return COR_Expressions.UniversalRelation()
	# (𝟎) ∪ ((𝟏) † ((B)⁻¹)) = (𝟏) † ((B)⁻¹)
	match expression:
		case COR_Expressions.Union(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.EmptyRelation():
					match arg2:
						case COR_Expressions.Dagger(argument1=arg1, argument2=arg2):
							match arg1:
								case COR_Expressions.IdentityRelation:
									match arg2:
										case COR_Expressions.Converse(argument=arg):
											match arg:
												case _:
													B = arg
													return COR_Expressions.Dagger(COR_Expressions.IdentityRelation(), COR_Expressions.Converse(B))
	# (T) ∪ ((B) ∪ ((B)⁻¹)) = T
	match expression:
		case COR_Expressions.Union(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.UniversalRelation():
					match arg2:
						case COR_Expressions.Union(argument1=arg1, argument2=arg2):
							match arg1:
								case _:
									B = arg1
									match arg2:
										case COR_Expressions.Converse(argument=arg):
											match arg:
												case _:
													B = arg
													return COR_Expressions.UniversalRelation()
	# (𝟎) ∪ ((C) ∪ ((A)⁻¹)) = (C) ∪ ((A)⁻¹)
	match expression:
		case COR_Expressions.Union(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.EmptyRelation():
					match arg2:
						case COR_Expressions.Union(argument1=arg1, argument2=arg2):
							match arg1:
								case _:
									C = arg1
									match arg2:
										case COR_Expressions.Converse(argument=arg):
											match arg:
												case _:
													A = arg
													return COR_Expressions.Union(C, COR_Expressions.Converse(A))
	# (𝟎) ∪ ((𝟎) † ((A)⁻)) = (𝟎) † ((A)⁻)
	match expression:
		case COR_Expressions.Union(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.EmptyRelation():
					match arg2:
						case COR_Expressions.Dagger(argument1=arg1, argument2=arg2):
							match arg1:
								case COR_Expressions.EmptyRelation():
									match arg2:
										case COR_Expressions.Complement(argument=arg):
											match arg:
												case _:
													A = arg
													return COR_Expressions.Dagger(COR_Expressions.EmptyRelation(), COR_Expressions.Complement(A))
	# (T) ∪ ((C) ∪ ((A)⁻¹)) = T
	match expression:
		case COR_Expressions.Union(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.UniversalRelation():
					match arg2:
						case COR_Expressions.Union(argument1=arg1, argument2=arg2):
							match arg1:
								case _:
									C = arg1
									match arg2:
										case COR_Expressions.Converse(argument=arg):
											match arg:
												case _:
													A = arg
													return COR_Expressions.UniversalRelation()
	# (T) ∪ ((A) † ((C)⁻)) = T
	match expression:
		case COR_Expressions.Union(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.UniversalRelation():
					match arg2:
						case COR_Expressions.Dagger(argument1=arg1, argument2=arg2):
							match arg1:
								case _:
									A = arg1
									match arg2:
										case COR_Expressions.Complement(argument=arg):
											match arg:
												case _:
													C = arg
													return COR_Expressions.UniversalRelation()
	# (𝟎) ∘ ((T) ∘ ((C)⁻¹)) = 𝟎
	match expression:
		case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.EmptyRelation():
					match arg2:
						case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
							match arg1:
								case COR_Expressions.UniversalRelation():
									match arg2:
										case COR_Expressions.Converse(argument=arg):
											match arg:
												case _:
													C = arg
													return COR_Expressions.EmptyRelation()
	# (T) † ((A) ∘ ((𝟏)⁻)) = T
	match expression:
		case COR_Expressions.Dagger(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.UniversalRelation():
					match arg2:
						case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
							match arg1:
								case _:
									A = arg1
									match arg2:
										case COR_Expressions.Complement(argument=arg):
											match arg:
												case COR_Expressions.IdentityRelation:
													return COR_Expressions.UniversalRelation()
	# (T) ∪ ((A) ∪ ((C)⁻¹)) = T
	match expression:
		case COR_Expressions.Union(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.UniversalRelation():
					match arg2:
						case COR_Expressions.Union(argument1=arg1, argument2=arg2):
							match arg1:
								case _:
									A = arg1
									match arg2:
										case COR_Expressions.Converse(argument=arg):
											match arg:
												case _:
													C = arg
													return COR_Expressions.UniversalRelation()
	# (𝟎) ∪ ((𝟏) † ((B)⁻)) = (𝟏) † ((B)⁻)
	match expression:
		case COR_Expressions.Union(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.EmptyRelation():
					match arg2:
						case COR_Expressions.Dagger(argument1=arg1, argument2=arg2):
							match arg1:
								case COR_Expressions.IdentityRelation:
									match arg2:
										case COR_Expressions.Complement(argument=arg):
											match arg:
												case _:
													B = arg
													return COR_Expressions.Dagger(COR_Expressions.IdentityRelation(), COR_Expressions.Complement(B))
	# (𝟎) ∪ ((C) ∘ ((C)⁻¹)) = (C) ∘ ((C)⁻¹)
	match expression:
		case COR_Expressions.Union(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.EmptyRelation():
					match arg2:
						case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
							match arg1:
								case _:
									C = arg1
									match arg2:
										case COR_Expressions.Converse(argument=arg):
											match arg:
												case _:
													C = arg
													return COR_Expressions.Composition(C, COR_Expressions.Converse(C))
	# (𝟎) ∘ (((C)⁻)⁻¹) = 𝟎
	match expression:
		case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.EmptyRelation():
					match arg2:
						case COR_Expressions.Converse(argument=arg):
							match arg:
								case COR_Expressions.Complement(argument=arg):
									match arg:
										case _:
											C = arg
											return COR_Expressions.EmptyRelation()
	# (𝟏) ∪ ((𝟏) ∪ ((A)⁻¹)) = (𝟏) ∪ ((A)⁻¹)
	match expression:
		case COR_Expressions.Union(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.IdentityRelation:
					match arg2:
						case COR_Expressions.Union(argument1=arg1, argument2=arg2):
							match arg1:
								case COR_Expressions.IdentityRelation:
									match arg2:
										case COR_Expressions.Converse(argument=arg):
											match arg:
												case _:
													A = arg
													return COR_Expressions.Union(COR_Expressions.IdentityRelation(), COR_Expressions.Converse(A))
	# (T) † ((A) ∪ ((C)⁻¹)) = T
	match expression:
		case COR_Expressions.Dagger(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.UniversalRelation():
					match arg2:
						case COR_Expressions.Union(argument1=arg1, argument2=arg2):
							match arg1:
								case _:
									A = arg1
									match arg2:
										case COR_Expressions.Converse(argument=arg):
											match arg:
												case _:
													C = arg
													return COR_Expressions.UniversalRelation()
	# (𝟏) ∘ ((C) ∪ ((B)⁻)) = (C) ∪ ((B)⁻)
	match expression:
		case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.IdentityRelation:
					match arg2:
						case COR_Expressions.Union(argument1=arg1, argument2=arg2):
							match arg1:
								case _:
									C = arg1
									match arg2:
										case COR_Expressions.Complement(argument=arg):
											match arg:
												case _:
													B = arg
													return COR_Expressions.Union(C, COR_Expressions.Complement(B))
	# (𝟎) ∘ ((𝟎) † ((A)⁻¹)) = 𝟎
	match expression:
		case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.EmptyRelation():
					match arg2:
						case COR_Expressions.Dagger(argument1=arg1, argument2=arg2):
							match arg1:
								case COR_Expressions.EmptyRelation():
									match arg2:
										case COR_Expressions.Converse(argument=arg):
											match arg:
												case _:
													A = arg
													return COR_Expressions.EmptyRelation()
	# (T) ∪ ((A) ∘ ((A)⁻¹)) = T
	match expression:
		case COR_Expressions.Union(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.UniversalRelation():
					match arg2:
						case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
							match arg1:
								case _:
									A = arg1
									match arg2:
										case COR_Expressions.Converse(argument=arg):
											match arg:
												case _:
													A = arg
													return COR_Expressions.UniversalRelation()
	# (𝟎) ∘ ((A) † ((B)⁻)) = 𝟎
	match expression:
		case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.EmptyRelation():
					match arg2:
						case COR_Expressions.Dagger(argument1=arg1, argument2=arg2):
							match arg1:
								case _:
									A = arg1
									match arg2:
										case COR_Expressions.Complement(argument=arg):
											match arg:
												case _:
													B = arg
													return COR_Expressions.EmptyRelation()
	# (B) ∪ ((B) ∪ ((C)⁻¹)) = (B) ∪ ((C)⁻¹)
	match expression:
		case COR_Expressions.Union(argument1=arg1, argument2=arg2):
			match arg1:
				case _:
					B = arg1
					match arg2:
						case COR_Expressions.Union(argument1=arg1, argument2=arg2):
							match arg1:
								case _:
									B = arg1
									match arg2:
										case COR_Expressions.Converse(argument=arg):
											match arg:
												case _:
													C = arg
													return COR_Expressions.Union(B, COR_Expressions.Converse(C))
	# (𝟏) ∘ (((B)⁻)⁻¹) = ((B)⁻¹)⁻
	match expression:
		case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.IdentityRelation:
					match arg2:
						case COR_Expressions.Converse(argument=arg):
							match arg:
								case COR_Expressions.Complement(argument=arg):
									match arg:
										case _:
											B = arg
											return COR_Expressions.Complement(COR_Expressions.Converse(B))
	# (T) ∘ ((𝟏) ∪ ((A)⁻)) = T
	match expression:
		case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.UniversalRelation():
					match arg2:
						case COR_Expressions.Union(argument1=arg1, argument2=arg2):
							match arg1:
								case COR_Expressions.IdentityRelation:
									match arg2:
										case COR_Expressions.Complement(argument=arg):
											match arg:
												case _:
													A = arg
													return COR_Expressions.UniversalRelation()
	# (T) † ((C) † ((C)⁻¹)) = T
	match expression:
		case COR_Expressions.Dagger(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.UniversalRelation():
					match arg2:
						case COR_Expressions.Dagger(argument1=arg1, argument2=arg2):
							match arg1:
								case _:
									C = arg1
									match arg2:
										case COR_Expressions.Converse(argument=arg):
											match arg:
												case _:
													C = arg
													return COR_Expressions.UniversalRelation()
	# (𝟏) ∪ ((C) ∪ ((𝟏)⁻)) = T
	match expression:
		case COR_Expressions.Union(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.IdentityRelation:
					match arg2:
						case COR_Expressions.Union(argument1=arg1, argument2=arg2):
							match arg1:
								case _:
									C = arg1
									match arg2:
										case COR_Expressions.Complement(argument=arg):
											match arg:
												case COR_Expressions.IdentityRelation:
													return COR_Expressions.UniversalRelation()
	# (T) ∪ ((𝟏) ∪ ((C)⁻¹)) = T
	match expression:
		case COR_Expressions.Union(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.UniversalRelation():
					match arg2:
						case COR_Expressions.Union(argument1=arg1, argument2=arg2):
							match arg1:
								case COR_Expressions.IdentityRelation:
									match arg2:
										case COR_Expressions.Converse(argument=arg):
											match arg:
												case _:
													C = arg
													return COR_Expressions.UniversalRelation()
	# (𝟎) ∘ (((C)⁻¹)⁻) = 𝟎
	match expression:
		case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.EmptyRelation():
					match arg2:
						case COR_Expressions.Complement(argument=arg):
							match arg:
								case COR_Expressions.Converse(argument=arg):
									match arg:
										case _:
											C = arg
											return COR_Expressions.EmptyRelation()
	# (𝟎) ∪ ((C) ∪ ((𝟏)⁻)) = (C) ∪ ((𝟏)⁻)
	match expression:
		case COR_Expressions.Union(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.EmptyRelation():
					match arg2:
						case COR_Expressions.Union(argument1=arg1, argument2=arg2):
							match arg1:
								case _:
									C = arg1
									match arg2:
										case COR_Expressions.Complement(argument=arg):
											match arg:
												case COR_Expressions.IdentityRelation:
													return COR_Expressions.Union(C, COR_Expressions.Complement(COR_Expressions.IdentityRelation()))
	# (𝟏) ∘ ((T) ∘ ((A)⁻)) = (T) ∘ ((A)⁻)
	match expression:
		case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.IdentityRelation:
					match arg2:
						case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
							match arg1:
								case COR_Expressions.UniversalRelation():
									match arg2:
										case COR_Expressions.Complement(argument=arg):
											match arg:
												case _:
													A = arg
													return COR_Expressions.Composition(COR_Expressions.UniversalRelation(), COR_Expressions.Complement(A))
	# (T) ∪ ((T) ∘ ((𝟏)⁻)) = T
	match expression:
		case COR_Expressions.Union(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.UniversalRelation():
					match arg2:
						case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
							match arg1:
								case COR_Expressions.UniversalRelation():
									match arg2:
										case COR_Expressions.Complement(argument=arg):
											match arg:
												case COR_Expressions.IdentityRelation:
													return COR_Expressions.UniversalRelation()
	# (𝟎) † ((𝟎) † ((C)⁻¹)) = (𝟎) † ((C)⁻¹)
	match expression:
		case COR_Expressions.Dagger(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.EmptyRelation():
					match arg2:
						case COR_Expressions.Dagger(argument1=arg1, argument2=arg2):
							match arg1:
								case COR_Expressions.EmptyRelation():
									match arg2:
										case COR_Expressions.Converse(argument=arg):
											match arg:
												case _:
													C = arg
													return COR_Expressions.Dagger(COR_Expressions.EmptyRelation(), COR_Expressions.Converse(C))
	# (𝟏) ∘ ((B) † ((C)⁻¹)) = (B) † ((C)⁻¹)
	match expression:
		case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.IdentityRelation:
					match arg2:
						case COR_Expressions.Dagger(argument1=arg1, argument2=arg2):
							match arg1:
								case _:
									B = arg1
									match arg2:
										case COR_Expressions.Converse(argument=arg):
											match arg:
												case _:
													C = arg
													return COR_Expressions.Dagger(B, COR_Expressions.Converse(C))
	# (𝟏) ∘ ((𝟏) † ((C)⁻)) = (𝟏) † ((C)⁻)
	match expression:
		case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.IdentityRelation:
					match arg2:
						case COR_Expressions.Dagger(argument1=arg1, argument2=arg2):
							match arg1:
								case COR_Expressions.IdentityRelation:
									match arg2:
										case COR_Expressions.Complement(argument=arg):
											match arg:
												case _:
													C = arg
													return COR_Expressions.Dagger(COR_Expressions.IdentityRelation(), COR_Expressions.Complement(C))
	# (𝟏) ∘ ((C) † ((B)⁻)) = (C) † ((B)⁻)
	match expression:
		case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.IdentityRelation:
					match arg2:
						case COR_Expressions.Dagger(argument1=arg1, argument2=arg2):
							match arg1:
								case _:
									C = arg1
									match arg2:
										case COR_Expressions.Complement(argument=arg):
											match arg:
												case _:
													B = arg
													return COR_Expressions.Dagger(C, COR_Expressions.Complement(B))
	# (T) † ((C) † ((A)⁻)) = T
	match expression:
		case COR_Expressions.Dagger(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.UniversalRelation():
					match arg2:
						case COR_Expressions.Dagger(argument1=arg1, argument2=arg2):
							match arg1:
								case _:
									C = arg1
									match arg2:
										case COR_Expressions.Complement(argument=arg):
											match arg:
												case _:
													A = arg
													return COR_Expressions.UniversalRelation()
	# (T) ∪ ((A) ∘ ((A)⁻)) = T
	match expression:
		case COR_Expressions.Union(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.UniversalRelation():
					match arg2:
						case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
							match arg1:
								case _:
									A = arg1
									match arg2:
										case COR_Expressions.Complement(argument=arg):
											match arg:
												case _:
													A = arg
													return COR_Expressions.UniversalRelation()
	# (B) ∪ ((B) ∪ ((A)⁻)) = (B) ∪ ((A)⁻)
	match expression:
		case COR_Expressions.Union(argument1=arg1, argument2=arg2):
			match arg1:
				case _:
					B = arg1
					match arg2:
						case COR_Expressions.Union(argument1=arg1, argument2=arg2):
							match arg1:
								case _:
									B = arg1
									match arg2:
										case COR_Expressions.Complement(argument=arg):
											match arg:
												case _:
													A = arg
													return COR_Expressions.Union(B, COR_Expressions.Complement(A))
	# (𝟎) ∘ ((C) ∘ ((𝟏)⁻)) = 𝟎
	match expression:
		case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.EmptyRelation():
					match arg2:
						case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
							match arg1:
								case _:
									C = arg1
									match arg2:
										case COR_Expressions.Complement(argument=arg):
											match arg:
												case COR_Expressions.IdentityRelation:
													return COR_Expressions.EmptyRelation()
	# ((B) ∪ ((B)⁻¹))⁻¹ = (B) ∪ ((B)⁻¹)
	match expression:
		case COR_Expressions.Converse(argument=arg):
			match arg:
				case COR_Expressions.Union(argument1=arg1, argument2=arg2):
					match arg1:
						case _:
							B = arg1
							match arg2:
								case COR_Expressions.Converse(argument=arg):
									match arg:
										case _:
											B = arg
											return COR_Expressions.Union(B, COR_Expressions.Converse(B))
	# ((C)⁻¹) ∪ ((𝟏)⁻) = (C) ∪ ((𝟏)⁻)
	match expression:
		case COR_Expressions.Union(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.Converse(argument=arg):
					match arg:
						case _:
							C = arg
							match arg2:
								case COR_Expressions.Complement(argument=arg):
									match arg:
										case COR_Expressions.IdentityRelation:
											return COR_Expressions.Union(C, COR_Expressions.Complement(COR_Expressions.IdentityRelation()))
	# (T) † ((C) ∪ ((B)⁻)) = T
	match expression:
		case COR_Expressions.Dagger(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.UniversalRelation():
					match arg2:
						case COR_Expressions.Union(argument1=arg1, argument2=arg2):
							match arg1:
								case _:
									C = arg1
									match arg2:
										case COR_Expressions.Complement(argument=arg):
											match arg:
												case _:
													B = arg
													return COR_Expressions.UniversalRelation()
	# (𝟎) ∪ ((B) ∘ ((B)⁻¹)) = (B) ∘ ((B)⁻¹)
	match expression:
		case COR_Expressions.Union(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.EmptyRelation():
					match arg2:
						case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
							match arg1:
								case _:
									B = arg1
									match arg2:
										case COR_Expressions.Converse(argument=arg):
											match arg:
												case _:
													B = arg
													return COR_Expressions.Composition(B, COR_Expressions.Converse(B))
	# (T) † ((A) ∘ ((C)⁻¹)) = T
	match expression:
		case COR_Expressions.Dagger(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.UniversalRelation():
					match arg2:
						case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
							match arg1:
								case _:
									A = arg1
									match arg2:
										case COR_Expressions.Converse(argument=arg):
											match arg:
												case _:
													C = arg
													return COR_Expressions.UniversalRelation()
	# (T) ∪ ((𝟎) † ((B)⁻¹)) = T
	match expression:
		case COR_Expressions.Union(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.UniversalRelation():
					match arg2:
						case COR_Expressions.Dagger(argument1=arg1, argument2=arg2):
							match arg1:
								case COR_Expressions.EmptyRelation():
									match arg2:
										case COR_Expressions.Converse(argument=arg):
											match arg:
												case _:
													B = arg
													return COR_Expressions.UniversalRelation()
	# (T) ∘ ((𝟎) † ((A)⁻¹)) = (𝟎) † ((A)⁻¹)
	match expression:
		case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.UniversalRelation():
					match arg2:
						case COR_Expressions.Dagger(argument1=arg1, argument2=arg2):
							match arg1:
								case COR_Expressions.EmptyRelation():
									match arg2:
										case COR_Expressions.Converse(argument=arg):
											match arg:
												case _:
													A = arg
													return COR_Expressions.Dagger(COR_Expressions.EmptyRelation(), COR_Expressions.Converse(A))
	# (𝟎) ∪ ((C) † ((C)⁻)) = (C) † ((C)⁻)
	match expression:
		case COR_Expressions.Union(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.EmptyRelation():
					match arg2:
						case COR_Expressions.Dagger(argument1=arg1, argument2=arg2):
							match arg1:
								case _:
									C = arg1
									match arg2:
										case COR_Expressions.Complement(argument=arg):
											match arg:
												case _:
													C = arg
													return COR_Expressions.Dagger(C, COR_Expressions.Complement(C))
	# (𝟎) ∘ ((B) † ((B)⁻¹)) = 𝟎
	match expression:
		case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.EmptyRelation():
					match arg2:
						case COR_Expressions.Dagger(argument1=arg1, argument2=arg2):
							match arg1:
								case _:
									B = arg1
									match arg2:
										case COR_Expressions.Converse(argument=arg):
											match arg:
												case _:
													B = arg
													return COR_Expressions.EmptyRelation()
	# (𝟎) ∘ ((𝟏) † ((A)⁻)) = 𝟎
	match expression:
		case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.EmptyRelation():
					match arg2:
						case COR_Expressions.Dagger(argument1=arg1, argument2=arg2):
							match arg1:
								case COR_Expressions.IdentityRelation:
									match arg2:
										case COR_Expressions.Complement(argument=arg):
											match arg:
												case _:
													A = arg
													return COR_Expressions.EmptyRelation()
	# (𝟏) ∘ ((C) † ((A)⁻)) = (C) † ((A)⁻)
	match expression:
		case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.IdentityRelation:
					match arg2:
						case COR_Expressions.Dagger(argument1=arg1, argument2=arg2):
							match arg1:
								case _:
									C = arg1
									match arg2:
										case COR_Expressions.Complement(argument=arg):
											match arg:
												case _:
													A = arg
													return COR_Expressions.Dagger(C, COR_Expressions.Complement(A))
	# ((B)⁻¹) ∪ ((B)⁻¹) = (B)⁻¹
	match expression:
		case COR_Expressions.Union(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.Converse(argument=arg):
					match arg:
						case _:
							B = arg
							match arg2:
								case COR_Expressions.Converse(argument=arg):
									match arg:
										case _:
											B = arg
											return COR_Expressions.Converse(B)
	# ((𝟏)⁻) † ((𝟏)⁻) = (𝟏)⁻
	match expression:
		case COR_Expressions.Dagger(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.Complement(argument=arg):
					match arg:
						case COR_Expressions.IdentityRelation:
							match arg2:
								case COR_Expressions.Complement(argument=arg):
									match arg:
										case COR_Expressions.IdentityRelation:
											return COR_Expressions.Complement(COR_Expressions.IdentityRelation())
	# ((B)⁻) † ((𝟏)⁻) = (B)⁻
	match expression:
		case COR_Expressions.Dagger(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.Complement(argument=arg):
					match arg:
						case _:
							B = arg
							match arg2:
								case COR_Expressions.Complement(argument=arg):
									match arg:
										case COR_Expressions.IdentityRelation:
											return COR_Expressions.Complement(B)
	# (𝟏) ∘ ((C) ∪ ((A)⁻)) = (C) ∪ ((A)⁻)
	match expression:
		case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.IdentityRelation:
					match arg2:
						case COR_Expressions.Union(argument1=arg1, argument2=arg2):
							match arg1:
								case _:
									C = arg1
									match arg2:
										case COR_Expressions.Complement(argument=arg):
											match arg:
												case _:
													A = arg
													return COR_Expressions.Union(C, COR_Expressions.Complement(A))
	# (𝟎) ∪ ((B) † ((B)⁻)) = (B) † ((B)⁻)
	match expression:
		case COR_Expressions.Union(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.EmptyRelation():
					match arg2:
						case COR_Expressions.Dagger(argument1=arg1, argument2=arg2):
							match arg1:
								case _:
									B = arg1
									match arg2:
										case COR_Expressions.Complement(argument=arg):
											match arg:
												case _:
													B = arg
													return COR_Expressions.Dagger(B, COR_Expressions.Complement(B))
	# (𝟎) ∘ ((C) ∪ ((A)⁻¹)) = 𝟎
	match expression:
		case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.EmptyRelation():
					match arg2:
						case COR_Expressions.Union(argument1=arg1, argument2=arg2):
							match arg1:
								case _:
									C = arg1
									match arg2:
										case COR_Expressions.Converse(argument=arg):
											match arg:
												case _:
													A = arg
													return COR_Expressions.EmptyRelation()
	# (T) ∘ ((A) ∘ ((A)⁻¹)) = (T) ∘ ((A)⁻¹)
	match expression:
		case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.UniversalRelation():
					match arg2:
						case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
							match arg1:
								case _:
									A = arg1
									match arg2:
										case COR_Expressions.Converse(argument=arg):
											match arg:
												case _:
													A = arg
													return COR_Expressions.Composition(COR_Expressions.UniversalRelation(), COR_Expressions.Converse(A))
	# (𝟎) ∪ ((B) ∘ ((C)⁻¹)) = (B) ∘ ((C)⁻¹)
	match expression:
		case COR_Expressions.Union(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.EmptyRelation():
					match arg2:
						case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
							match arg1:
								case _:
									B = arg1
									match arg2:
										case COR_Expressions.Converse(argument=arg):
											match arg:
												case _:
													C = arg
													return COR_Expressions.Composition(B, COR_Expressions.Converse(C))
	# (T) ∘ ((𝟏) ∪ ((A)⁻¹)) = T
	match expression:
		case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.UniversalRelation():
					match arg2:
						case COR_Expressions.Union(argument1=arg1, argument2=arg2):
							match arg1:
								case COR_Expressions.IdentityRelation:
									match arg2:
										case COR_Expressions.Converse(argument=arg):
											match arg:
												case _:
													A = arg
													return COR_Expressions.UniversalRelation()
	# (𝟎) ∪ ((T) ∘ ((A)⁻)) = (T) ∘ ((A)⁻)
	match expression:
		case COR_Expressions.Union(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.EmptyRelation():
					match arg2:
						case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
							match arg1:
								case COR_Expressions.UniversalRelation():
									match arg2:
										case COR_Expressions.Complement(argument=arg):
											match arg:
												case _:
													A = arg
													return COR_Expressions.Composition(COR_Expressions.UniversalRelation(), COR_Expressions.Complement(A))
	# (𝟎) ∘ ((𝟎) † ((B)⁻¹)) = 𝟎
	match expression:
		case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.EmptyRelation():
					match arg2:
						case COR_Expressions.Dagger(argument1=arg1, argument2=arg2):
							match arg1:
								case COR_Expressions.EmptyRelation():
									match arg2:
										case COR_Expressions.Converse(argument=arg):
											match arg:
												case _:
													B = arg
													return COR_Expressions.EmptyRelation()
	# (𝟎) ∪ ((A) ∘ ((B)⁻¹)) = (A) ∘ ((B)⁻¹)
	match expression:
		case COR_Expressions.Union(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.EmptyRelation():
					match arg2:
						case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
							match arg1:
								case _:
									A = arg1
									match arg2:
										case COR_Expressions.Converse(argument=arg):
											match arg:
												case _:
													B = arg
													return COR_Expressions.Composition(A, COR_Expressions.Converse(B))
	# (𝟎) ∘ ((𝟏) ∪ ((A)⁻¹)) = 𝟎
	match expression:
		case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.EmptyRelation():
					match arg2:
						case COR_Expressions.Union(argument1=arg1, argument2=arg2):
							match arg1:
								case COR_Expressions.IdentityRelation:
									match arg2:
										case COR_Expressions.Converse(argument=arg):
											match arg:
												case _:
													A = arg
													return COR_Expressions.EmptyRelation()
	# (𝟏) ∘ ((C) ∪ ((B)⁻¹)) = (C) ∪ ((B)⁻¹)
	match expression:
		case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.IdentityRelation:
					match arg2:
						case COR_Expressions.Union(argument1=arg1, argument2=arg2):
							match arg1:
								case _:
									C = arg1
									match arg2:
										case COR_Expressions.Converse(argument=arg):
											match arg:
												case _:
													B = arg
													return COR_Expressions.Union(C, COR_Expressions.Converse(B))
	# (T) ∪ ((A) ∘ ((C)⁻)) = T
	match expression:
		case COR_Expressions.Union(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.UniversalRelation():
					match arg2:
						case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
							match arg1:
								case _:
									A = arg1
									match arg2:
										case COR_Expressions.Complement(argument=arg):
											match arg:
												case _:
													C = arg
													return COR_Expressions.UniversalRelation()
	# ((C) ∪ ((A)⁻¹))⁻¹ = (A) ∪ ((C)⁻¹)
	match expression:
		case COR_Expressions.Converse(argument=arg):
			match arg:
				case COR_Expressions.Union(argument1=arg1, argument2=arg2):
					match arg1:
						case _:
							C = arg1
							match arg2:
								case COR_Expressions.Converse(argument=arg):
									match arg:
										case _:
											A = arg
											return COR_Expressions.Union(A, COR_Expressions.Converse(C))
	# (T) ∪ ((B) † ((B)⁻¹)) = T
	match expression:
		case COR_Expressions.Union(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.UniversalRelation():
					match arg2:
						case COR_Expressions.Dagger(argument1=arg1, argument2=arg2):
							match arg1:
								case _:
									B = arg1
									match arg2:
										case COR_Expressions.Converse(argument=arg):
											match arg:
												case _:
													B = arg
													return COR_Expressions.UniversalRelation()
	# (𝟏) ∘ ((B) † ((A)⁻¹)) = (B) † ((A)⁻¹)
	match expression:
		case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.IdentityRelation:
					match arg2:
						case COR_Expressions.Dagger(argument1=arg1, argument2=arg2):
							match arg1:
								case _:
									B = arg1
									match arg2:
										case COR_Expressions.Converse(argument=arg):
											match arg:
												case _:
													A = arg
													return COR_Expressions.Dagger(B, COR_Expressions.Converse(A))
	# (𝟎) ∘ ((𝟎) † ((C)⁻¹)) = 𝟎
	match expression:
		case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.EmptyRelation():
					match arg2:
						case COR_Expressions.Dagger(argument1=arg1, argument2=arg2):
							match arg1:
								case COR_Expressions.EmptyRelation():
									match arg2:
										case COR_Expressions.Converse(argument=arg):
											match arg:
												case _:
													C = arg
													return COR_Expressions.EmptyRelation()
	# ((A)⁻¹) ∪ ((𝟏)⁻) = (A) ∪ ((𝟏)⁻)
	match expression:
		case COR_Expressions.Union(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.Converse(argument=arg):
					match arg:
						case _:
							A = arg
							match arg2:
								case COR_Expressions.Complement(argument=arg):
									match arg:
										case COR_Expressions.IdentityRelation:
											return COR_Expressions.Union(A, COR_Expressions.Complement(COR_Expressions.IdentityRelation()))
	# ((A)⁻¹) † ((𝟏)⁻) = (A)⁻¹
	match expression:
		case COR_Expressions.Dagger(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.Converse(argument=arg):
					match arg:
						case _:
							A = arg
							match arg2:
								case COR_Expressions.Complement(argument=arg):
									match arg:
										case COR_Expressions.IdentityRelation:
											return COR_Expressions.Converse(A)
	# (𝟎) ∘ ((B) ∘ ((A)⁻¹)) = 𝟎
	match expression:
		case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.EmptyRelation():
					match arg2:
						case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
							match arg1:
								case _:
									B = arg1
									match arg2:
										case COR_Expressions.Converse(argument=arg):
											match arg:
												case _:
													A = arg
													return COR_Expressions.EmptyRelation()
	# (𝟎) ∪ ((A) ∪ ((C)⁻¹)) = (A) ∪ ((C)⁻¹)
	match expression:
		case COR_Expressions.Union(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.EmptyRelation():
					match arg2:
						case COR_Expressions.Union(argument1=arg1, argument2=arg2):
							match arg1:
								case _:
									A = arg1
									match arg2:
										case COR_Expressions.Converse(argument=arg):
											match arg:
												case _:
													C = arg
													return COR_Expressions.Union(A, COR_Expressions.Converse(C))
	# (T) ∪ ((C) ∘ ((B)⁻¹)) = T
	match expression:
		case COR_Expressions.Union(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.UniversalRelation():
					match arg2:
						case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
							match arg1:
								case _:
									C = arg1
									match arg2:
										case COR_Expressions.Converse(argument=arg):
											match arg:
												case _:
													B = arg
													return COR_Expressions.UniversalRelation()
	# (𝟎) ∘ ((𝟏) † ((C)⁻)) = 𝟎
	match expression:
		case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.EmptyRelation():
					match arg2:
						case COR_Expressions.Dagger(argument1=arg1, argument2=arg2):
							match arg1:
								case COR_Expressions.IdentityRelation:
									match arg2:
										case COR_Expressions.Complement(argument=arg):
											match arg:
												case _:
													C = arg
													return COR_Expressions.EmptyRelation()
	# (𝟎) ∪ ((B) † ((B)⁻¹)) = (B) † ((B)⁻¹)
	match expression:
		case COR_Expressions.Union(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.EmptyRelation():
					match arg2:
						case COR_Expressions.Dagger(argument1=arg1, argument2=arg2):
							match arg1:
								case _:
									B = arg1
									match arg2:
										case COR_Expressions.Converse(argument=arg):
											match arg:
												case _:
													B = arg
													return COR_Expressions.Dagger(B, COR_Expressions.Converse(B))
	# (𝟏) ∘ ((C) † ((A)⁻¹)) = (C) † ((A)⁻¹)
	match expression:
		case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.IdentityRelation:
					match arg2:
						case COR_Expressions.Dagger(argument1=arg1, argument2=arg2):
							match arg1:
								case _:
									C = arg1
									match arg2:
										case COR_Expressions.Converse(argument=arg):
											match arg:
												case _:
													A = arg
													return COR_Expressions.Dagger(C, COR_Expressions.Converse(A))
	# (𝟎) ∪ ((T) ∘ ((B)⁻)) = (T) ∘ ((B)⁻)
	match expression:
		case COR_Expressions.Union(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.EmptyRelation():
					match arg2:
						case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
							match arg1:
								case COR_Expressions.UniversalRelation():
									match arg2:
										case COR_Expressions.Complement(argument=arg):
											match arg:
												case _:
													B = arg
													return COR_Expressions.Composition(COR_Expressions.UniversalRelation(), COR_Expressions.Complement(B))
	# (𝟎) ∪ ((𝟎) † ((C)⁻¹)) = (𝟎) † ((C)⁻¹)
	match expression:
		case COR_Expressions.Union(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.EmptyRelation():
					match arg2:
						case COR_Expressions.Dagger(argument1=arg1, argument2=arg2):
							match arg1:
								case COR_Expressions.EmptyRelation():
									match arg2:
										case COR_Expressions.Converse(argument=arg):
											match arg:
												case _:
													C = arg
													return COR_Expressions.Dagger(COR_Expressions.EmptyRelation(), COR_Expressions.Converse(C))
	# (T) ∪ ((C) ∘ ((A)⁻¹)) = T
	match expression:
		case COR_Expressions.Union(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.UniversalRelation():
					match arg2:
						case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
							match arg1:
								case _:
									C = arg1
									match arg2:
										case COR_Expressions.Converse(argument=arg):
											match arg:
												case _:
													A = arg
													return COR_Expressions.UniversalRelation()
	# (T) † ((𝟏) † ((C)⁻¹)) = T
	match expression:
		case COR_Expressions.Dagger(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.UniversalRelation():
					match arg2:
						case COR_Expressions.Dagger(argument1=arg1, argument2=arg2):
							match arg1:
								case COR_Expressions.IdentityRelation:
									match arg2:
										case COR_Expressions.Converse(argument=arg):
											match arg:
												case _:
													C = arg
													return COR_Expressions.UniversalRelation()
	# (𝟏) ∘ ((A) † ((A)⁻¹)) = (A) † ((A)⁻¹)
	match expression:
		case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.IdentityRelation:
					match arg2:
						case COR_Expressions.Dagger(argument1=arg1, argument2=arg2):
							match arg1:
								case _:
									A = arg1
									match arg2:
										case COR_Expressions.Converse(argument=arg):
											match arg:
												case _:
													A = arg
													return COR_Expressions.Dagger(A, COR_Expressions.Converse(A))
	# ((𝟏)⁻) † ((A)⁻¹) = (A)⁻¹
	match expression:
		case COR_Expressions.Dagger(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.Complement(argument=arg):
					match arg:
						case COR_Expressions.IdentityRelation:
							match arg2:
								case COR_Expressions.Converse(argument=arg):
									match arg:
										case _:
											A = arg
											return COR_Expressions.Converse(A)
	# (T) ∪ ((B) † ((A)⁻)) = T
	match expression:
		case COR_Expressions.Union(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.UniversalRelation():
					match arg2:
						case COR_Expressions.Dagger(argument1=arg1, argument2=arg2):
							match arg1:
								case _:
									B = arg1
									match arg2:
										case COR_Expressions.Complement(argument=arg):
											match arg:
												case _:
													A = arg
													return COR_Expressions.UniversalRelation()
	# ((A) † ((B)⁻¹))⁻¹ = (B) † ((A)⁻¹)
	match expression:
		case COR_Expressions.Converse(argument=arg):
			match arg:
				case COR_Expressions.Dagger(argument1=arg1, argument2=arg2):
					match arg1:
						case _:
							A = arg1
							match arg2:
								case COR_Expressions.Converse(argument=arg):
									match arg:
										case _:
											B = arg
											return COR_Expressions.Dagger(B, COR_Expressions.Converse(A))
	# (𝟎) ∘ ((C) ∘ ((B)⁻)) = 𝟎
	match expression:
		case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.EmptyRelation():
					match arg2:
						case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
							match arg1:
								case _:
									C = arg1
									match arg2:
										case COR_Expressions.Complement(argument=arg):
											match arg:
												case _:
													B = arg
													return COR_Expressions.EmptyRelation()
	# (𝟎) † ((T) ∘ ((A)⁻¹)) = (T) ∘ ((A)⁻¹)
	match expression:
		case COR_Expressions.Dagger(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.EmptyRelation():
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
	# (𝟎) ∘ ((𝟏) ∪ ((B)⁻¹)) = 𝟎
	match expression:
		case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.EmptyRelation():
					match arg2:
						case COR_Expressions.Union(argument1=arg1, argument2=arg2):
							match arg1:
								case COR_Expressions.IdentityRelation:
									match arg2:
										case COR_Expressions.Converse(argument=arg):
											match arg:
												case _:
													B = arg
													return COR_Expressions.EmptyRelation()
	# (((C)⁻)⁻¹)⁻¹ = (C)⁻
	match expression:
		case COR_Expressions.Converse(argument=arg):
			match arg:
				case COR_Expressions.Converse(argument=arg):
					match arg:
						case COR_Expressions.Complement(argument=arg):
							match arg:
								case _:
									C = arg
									return COR_Expressions.Complement(C)
	# (𝟎) ∘ ((C) ∪ ((𝟏)⁻)) = 𝟎
	match expression:
		case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.EmptyRelation():
					match arg2:
						case COR_Expressions.Union(argument1=arg1, argument2=arg2):
							match arg1:
								case _:
									C = arg1
									match arg2:
										case COR_Expressions.Complement(argument=arg):
											match arg:
												case COR_Expressions.IdentityRelation:
													return COR_Expressions.EmptyRelation()
	# (𝟏) ∘ ((T) ∘ ((C)⁻¹)) = (T) ∘ ((C)⁻¹)
	match expression:
		case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.IdentityRelation:
					match arg2:
						case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
							match arg1:
								case COR_Expressions.UniversalRelation():
									match arg2:
										case COR_Expressions.Converse(argument=arg):
											match arg:
												case _:
													C = arg
													return COR_Expressions.Composition(COR_Expressions.UniversalRelation(), COR_Expressions.Converse(C))
	# (𝟏) ∘ ((𝟏) ∪ ((B)⁻¹)) = (𝟏) ∪ ((B)⁻¹)
	match expression:
		case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.IdentityRelation:
					match arg2:
						case COR_Expressions.Union(argument1=arg1, argument2=arg2):
							match arg1:
								case COR_Expressions.IdentityRelation:
									match arg2:
										case COR_Expressions.Converse(argument=arg):
											match arg:
												case _:
													B = arg
													return COR_Expressions.Union(COR_Expressions.IdentityRelation(), COR_Expressions.Converse(B))
	# (T) ∪ ((A) ∪ ((𝟏)⁻)) = T
	match expression:
		case COR_Expressions.Union(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.UniversalRelation():
					match arg2:
						case COR_Expressions.Union(argument1=arg1, argument2=arg2):
							match arg1:
								case _:
									A = arg1
									match arg2:
										case COR_Expressions.Complement(argument=arg):
											match arg:
												case COR_Expressions.IdentityRelation:
													return COR_Expressions.UniversalRelation()
	# (T) ∪ ((C) ∪ ((B)⁻)) = T
	match expression:
		case COR_Expressions.Union(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.UniversalRelation():
					match arg2:
						case COR_Expressions.Union(argument1=arg1, argument2=arg2):
							match arg1:
								case _:
									C = arg1
									match arg2:
										case COR_Expressions.Complement(argument=arg):
											match arg:
												case _:
													B = arg
													return COR_Expressions.UniversalRelation()
	# (T) ∪ ((𝟎) † ((A)⁻)) = T
	match expression:
		case COR_Expressions.Union(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.UniversalRelation():
					match arg2:
						case COR_Expressions.Dagger(argument1=arg1, argument2=arg2):
							match arg1:
								case COR_Expressions.EmptyRelation():
									match arg2:
										case COR_Expressions.Complement(argument=arg):
											match arg:
												case _:
													A = arg
													return COR_Expressions.UniversalRelation()
	# (𝟎) ∪ ((C) ∪ ((A)⁻)) = (C) ∪ ((A)⁻)
	match expression:
		case COR_Expressions.Union(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.EmptyRelation():
					match arg2:
						case COR_Expressions.Union(argument1=arg1, argument2=arg2):
							match arg1:
								case _:
									C = arg1
									match arg2:
										case COR_Expressions.Complement(argument=arg):
											match arg:
												case _:
													A = arg
													return COR_Expressions.Union(C, COR_Expressions.Complement(A))
	# (𝟎) † ((𝟎) † ((A)⁻)) = (𝟎) † ((A)⁻)
	match expression:
		case COR_Expressions.Dagger(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.EmptyRelation():
					match arg2:
						case COR_Expressions.Dagger(argument1=arg1, argument2=arg2):
							match arg1:
								case COR_Expressions.EmptyRelation():
									match arg2:
										case COR_Expressions.Complement(argument=arg):
											match arg:
												case _:
													A = arg
													return COR_Expressions.Dagger(COR_Expressions.EmptyRelation(), COR_Expressions.Complement(A))
	# (𝟎) ∘ ((C) ∘ ((C)⁻¹)) = 𝟎
	match expression:
		case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.EmptyRelation():
					match arg2:
						case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
							match arg1:
								case _:
									C = arg1
									match arg2:
										case COR_Expressions.Converse(argument=arg):
											match arg:
												case _:
													C = arg
													return COR_Expressions.EmptyRelation()
	# ((𝟏)⁻) ∪ ((B)⁻¹) = (B) ∪ ((𝟏)⁻)
	match expression:
		case COR_Expressions.Union(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.Complement(argument=arg):
					match arg:
						case COR_Expressions.IdentityRelation:
							match arg2:
								case COR_Expressions.Converse(argument=arg):
									match arg:
										case _:
											B = arg
											return COR_Expressions.Union(B, COR_Expressions.Complement(COR_Expressions.IdentityRelation()))
	# ((A) † ((A)⁻¹))⁻¹ = (A) † ((A)⁻¹)
	match expression:
		case COR_Expressions.Converse(argument=arg):
			match arg:
				case COR_Expressions.Dagger(argument1=arg1, argument2=arg2):
					match arg1:
						case _:
							A = arg1
							match arg2:
								case COR_Expressions.Converse(argument=arg):
									match arg:
										case _:
											A = arg
											return COR_Expressions.Dagger(A, COR_Expressions.Converse(A))
	# (𝟏) ∘ ((C) ∪ ((𝟏)⁻)) = (C) ∪ ((𝟏)⁻)
	match expression:
		case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.IdentityRelation:
					match arg2:
						case COR_Expressions.Union(argument1=arg1, argument2=arg2):
							match arg1:
								case _:
									C = arg1
									match arg2:
										case COR_Expressions.Complement(argument=arg):
											match arg:
												case COR_Expressions.IdentityRelation:
													return COR_Expressions.Union(C, COR_Expressions.Complement(COR_Expressions.IdentityRelation()))
	# (𝟎) ∪ ((A) ∘ ((B)⁻)) = (A) ∘ ((B)⁻)
	match expression:
		case COR_Expressions.Union(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.EmptyRelation():
					match arg2:
						case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
							match arg1:
								case _:
									A = arg1
									match arg2:
										case COR_Expressions.Complement(argument=arg):
											match arg:
												case _:
													B = arg
													return COR_Expressions.Composition(A, COR_Expressions.Complement(B))
	# ((𝟏)⁻) ∪ ((A)⁻¹) = (A) ∪ ((𝟏)⁻)
	match expression:
		case COR_Expressions.Union(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.Complement(argument=arg):
					match arg:
						case COR_Expressions.IdentityRelation:
							match arg2:
								case COR_Expressions.Converse(argument=arg):
									match arg:
										case _:
											A = arg
											return COR_Expressions.Union(A, COR_Expressions.Complement(COR_Expressions.IdentityRelation()))
	# (T) † ((𝟏) ∪ ((A)⁻¹)) = T
	match expression:
		case COR_Expressions.Dagger(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.UniversalRelation():
					match arg2:
						case COR_Expressions.Union(argument1=arg1, argument2=arg2):
							match arg1:
								case COR_Expressions.IdentityRelation:
									match arg2:
										case COR_Expressions.Converse(argument=arg):
											match arg:
												case _:
													A = arg
													return COR_Expressions.UniversalRelation()
	# (T) ∪ ((C) ∘ ((B)⁻)) = T
	match expression:
		case COR_Expressions.Union(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.UniversalRelation():
					match arg2:
						case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
							match arg1:
								case _:
									C = arg1
									match arg2:
										case COR_Expressions.Complement(argument=arg):
											match arg:
												case _:
													B = arg
													return COR_Expressions.UniversalRelation()
	# (𝟏) ∘ ((A) ∘ ((A)⁻¹)) = (A) ∘ ((A)⁻¹)
	match expression:
		case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.IdentityRelation:
					match arg2:
						case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
							match arg1:
								case _:
									A = arg1
									match arg2:
										case COR_Expressions.Converse(argument=arg):
											match arg:
												case _:
													A = arg
													return COR_Expressions.Composition(A, COR_Expressions.Converse(A))
	# (T) † ((A) ∘ ((A)⁻)) = T
	match expression:
		case COR_Expressions.Dagger(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.UniversalRelation():
					match arg2:
						case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
							match arg1:
								case _:
									A = arg1
									match arg2:
										case COR_Expressions.Complement(argument=arg):
											match arg:
												case _:
													A = arg
													return COR_Expressions.UniversalRelation()
	# (((C)⁻¹)⁻)⁻¹ = (C)⁻
	match expression:
		case COR_Expressions.Converse(argument=arg):
			match arg:
				case COR_Expressions.Complement(argument=arg):
					match arg:
						case COR_Expressions.Converse(argument=arg):
							match arg:
								case _:
									C = arg
									return COR_Expressions.Complement(C)
	# (T) ∪ ((A) ∘ ((B)⁻¹)) = T
	match expression:
		case COR_Expressions.Union(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.UniversalRelation():
					match arg2:
						case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
							match arg1:
								case _:
									A = arg1
									match arg2:
										case COR_Expressions.Converse(argument=arg):
											match arg:
												case _:
													B = arg
													return COR_Expressions.UniversalRelation()
	# (𝟏) ∘ ((𝟏) ∪ ((A)⁻)) = (𝟏) ∪ ((A)⁻)
	match expression:
		case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.IdentityRelation:
					match arg2:
						case COR_Expressions.Union(argument1=arg1, argument2=arg2):
							match arg1:
								case COR_Expressions.IdentityRelation:
									match arg2:
										case COR_Expressions.Complement(argument=arg):
											match arg:
												case _:
													A = arg
													return COR_Expressions.Union(COR_Expressions.IdentityRelation(), COR_Expressions.Complement(A))
	# (T) ∘ ((T) ∘ ((B)⁻)) = (T) ∘ ((B)⁻)
	match expression:
		case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.UniversalRelation():
					match arg2:
						case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
							match arg1:
								case COR_Expressions.UniversalRelation():
									match arg2:
										case COR_Expressions.Complement(argument=arg):
											match arg:
												case _:
													B = arg
													return COR_Expressions.Composition(COR_Expressions.UniversalRelation(), COR_Expressions.Complement(B))
	# (𝟎) ∘ ((C) ∪ ((A)⁻)) = 𝟎
	match expression:
		case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.EmptyRelation():
					match arg2:
						case COR_Expressions.Union(argument1=arg1, argument2=arg2):
							match arg1:
								case _:
									C = arg1
									match arg2:
										case COR_Expressions.Complement(argument=arg):
											match arg:
												case _:
													A = arg
													return COR_Expressions.EmptyRelation()
	# (B) ∪ ((B) ∪ ((C)⁻)) = (B) ∪ ((C)⁻)
	match expression:
		case COR_Expressions.Union(argument1=arg1, argument2=arg2):
			match arg1:
				case _:
					B = arg1
					match arg2:
						case COR_Expressions.Union(argument1=arg1, argument2=arg2):
							match arg1:
								case _:
									B = arg1
									match arg2:
										case COR_Expressions.Complement(argument=arg):
											match arg:
												case _:
													C = arg
													return COR_Expressions.Union(B, COR_Expressions.Complement(C))
	# (A) ∪ ((C) ∪ ((A)⁻)) = T
	match expression:
		case COR_Expressions.Union(argument1=arg1, argument2=arg2):
			match arg1:
				case _:
					A = arg1
					match arg2:
						case COR_Expressions.Union(argument1=arg1, argument2=arg2):
							match arg1:
								case _:
									C = arg1
									match arg2:
										case COR_Expressions.Complement(argument=arg):
											match arg:
												case _:
													A = arg
													return COR_Expressions.UniversalRelation()
	# (𝟎) ∘ ((C) ∪ ((B)⁻)) = 𝟎
	match expression:
		case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.EmptyRelation():
					match arg2:
						case COR_Expressions.Union(argument1=arg1, argument2=arg2):
							match arg1:
								case _:
									C = arg1
									match arg2:
										case COR_Expressions.Complement(argument=arg):
											match arg:
												case _:
													B = arg
													return COR_Expressions.EmptyRelation()
	# (𝟏) ∘ ((A) ∘ ((𝟏)⁻)) = (A) ∘ ((𝟏)⁻)
	match expression:
		case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.IdentityRelation:
					match arg2:
						case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
							match arg1:
								case _:
									A = arg1
									match arg2:
										case COR_Expressions.Complement(argument=arg):
											match arg:
												case COR_Expressions.IdentityRelation:
													return COR_Expressions.Composition(A, COR_Expressions.Complement(COR_Expressions.IdentityRelation()))
	# (𝟎) ∪ ((C) ∘ ((𝟏)⁻)) = (C) ∘ ((𝟏)⁻)
	match expression:
		case COR_Expressions.Union(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.EmptyRelation():
					match arg2:
						case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
							match arg1:
								case _:
									C = arg1
									match arg2:
										case COR_Expressions.Complement(argument=arg):
											match arg:
												case COR_Expressions.IdentityRelation:
													return COR_Expressions.Composition(C, COR_Expressions.Complement(COR_Expressions.IdentityRelation()))
	# (𝟏) † ((T) ∘ ((𝟏)⁻)) = T
	match expression:
		case COR_Expressions.Dagger(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.IdentityRelation:
					match arg2:
						case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
							match arg1:
								case COR_Expressions.UniversalRelation():
									match arg2:
										case COR_Expressions.Complement(argument=arg):
											match arg:
												case COR_Expressions.IdentityRelation:
													return COR_Expressions.UniversalRelation()
	# (𝟎) ∪ ((A) ∪ ((C)⁻)) = (A) ∪ ((C)⁻)
	match expression:
		case COR_Expressions.Union(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.EmptyRelation():
					match arg2:
						case COR_Expressions.Union(argument1=arg1, argument2=arg2):
							match arg1:
								case _:
									A = arg1
									match arg2:
										case COR_Expressions.Complement(argument=arg):
											match arg:
												case _:
													C = arg
													return COR_Expressions.Union(A, COR_Expressions.Complement(C))
	# (𝟏) ∪ ((B) ∪ ((𝟏)⁻)) = T
	match expression:
		case COR_Expressions.Union(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.IdentityRelation:
					match arg2:
						case COR_Expressions.Union(argument1=arg1, argument2=arg2):
							match arg1:
								case _:
									B = arg1
									match arg2:
										case COR_Expressions.Complement(argument=arg):
											match arg:
												case COR_Expressions.IdentityRelation:
													return COR_Expressions.UniversalRelation()
	# (C) ∪ ((A) ∪ ((C)⁻)) = T
	match expression:
		case COR_Expressions.Union(argument1=arg1, argument2=arg2):
			match arg1:
				case _:
					C = arg1
					match arg2:
						case COR_Expressions.Union(argument1=arg1, argument2=arg2):
							match arg1:
								case _:
									A = arg1
									match arg2:
										case COR_Expressions.Complement(argument=arg):
											match arg:
												case _:
													C = arg
													return COR_Expressions.UniversalRelation()
	# (𝟎) † ((C) † ((C)⁻¹)) = (𝟎) † ((C)⁻¹)
	match expression:
		case COR_Expressions.Dagger(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.EmptyRelation():
					match arg2:
						case COR_Expressions.Dagger(argument1=arg1, argument2=arg2):
							match arg1:
								case _:
									C = arg1
									match arg2:
										case COR_Expressions.Converse(argument=arg):
											match arg:
												case _:
													C = arg
													return COR_Expressions.Dagger(COR_Expressions.EmptyRelation(), COR_Expressions.Converse(C))
	# (T) ∪ ((A) ∪ ((B)⁻)) = T
	match expression:
		case COR_Expressions.Union(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.UniversalRelation():
					match arg2:
						case COR_Expressions.Union(argument1=arg1, argument2=arg2):
							match arg1:
								case _:
									A = arg1
									match arg2:
										case COR_Expressions.Complement(argument=arg):
											match arg:
												case _:
													B = arg
													return COR_Expressions.UniversalRelation()
	# (𝟏) ∘ ((A) ∪ ((B)⁻)) = (A) ∪ ((B)⁻)
	match expression:
		case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.IdentityRelation:
					match arg2:
						case COR_Expressions.Union(argument1=arg1, argument2=arg2):
							match arg1:
								case _:
									A = arg1
									match arg2:
										case COR_Expressions.Complement(argument=arg):
											match arg:
												case _:
													B = arg
													return COR_Expressions.Union(A, COR_Expressions.Complement(B))
	# ((B) † ((A)⁻¹))⁻¹ = (A) † ((B)⁻¹)
	match expression:
		case COR_Expressions.Converse(argument=arg):
			match arg:
				case COR_Expressions.Dagger(argument1=arg1, argument2=arg2):
					match arg1:
						case _:
							B = arg1
							match arg2:
								case COR_Expressions.Converse(argument=arg):
									match arg:
										case _:
											A = arg
											return COR_Expressions.Dagger(A, COR_Expressions.Converse(B))
	# (T) † ((B) † ((A)⁻¹)) = T
	match expression:
		case COR_Expressions.Dagger(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.UniversalRelation():
					match arg2:
						case COR_Expressions.Dagger(argument1=arg1, argument2=arg2):
							match arg1:
								case _:
									B = arg1
									match arg2:
										case COR_Expressions.Converse(argument=arg):
											match arg:
												case _:
													A = arg
													return COR_Expressions.UniversalRelation()
	# (𝟏) ∘ ((B) † ((A)⁻)) = (B) † ((A)⁻)
	match expression:
		case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.IdentityRelation:
					match arg2:
						case COR_Expressions.Dagger(argument1=arg1, argument2=arg2):
							match arg1:
								case _:
									B = arg1
									match arg2:
										case COR_Expressions.Complement(argument=arg):
											match arg:
												case _:
													A = arg
													return COR_Expressions.Dagger(B, COR_Expressions.Complement(A))
	# (𝟎) ∘ ((A) ∘ ((A)⁻¹)) = 𝟎
	match expression:
		case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.EmptyRelation():
					match arg2:
						case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
							match arg1:
								case _:
									A = arg1
									match arg2:
										case COR_Expressions.Converse(argument=arg):
											match arg:
												case _:
													A = arg
													return COR_Expressions.EmptyRelation()
	# (T) ∪ ((𝟎) † ((C)⁻)) = T
	match expression:
		case COR_Expressions.Union(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.UniversalRelation():
					match arg2:
						case COR_Expressions.Dagger(argument1=arg1, argument2=arg2):
							match arg1:
								case COR_Expressions.EmptyRelation():
									match arg2:
										case COR_Expressions.Complement(argument=arg):
											match arg:
												case _:
													C = arg
													return COR_Expressions.UniversalRelation()
	# (𝟎) ∘ ((A) ∪ ((𝟏)⁻)) = 𝟎
	match expression:
		case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.EmptyRelation():
					match arg2:
						case COR_Expressions.Union(argument1=arg1, argument2=arg2):
							match arg1:
								case _:
									A = arg1
									match arg2:
										case COR_Expressions.Complement(argument=arg):
											match arg:
												case COR_Expressions.IdentityRelation:
													return COR_Expressions.EmptyRelation()
	# (T) ∪ ((A) † ((B)⁻¹)) = T
	match expression:
		case COR_Expressions.Union(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.UniversalRelation():
					match arg2:
						case COR_Expressions.Dagger(argument1=arg1, argument2=arg2):
							match arg1:
								case _:
									A = arg1
									match arg2:
										case COR_Expressions.Converse(argument=arg):
											match arg:
												case _:
													B = arg
													return COR_Expressions.UniversalRelation()
	# (𝟎) ∘ ((A) ∘ ((A)⁻)) = 𝟎
	match expression:
		case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.EmptyRelation():
					match arg2:
						case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
							match arg1:
								case _:
									A = arg1
									match arg2:
										case COR_Expressions.Complement(argument=arg):
											match arg:
												case _:
													A = arg
													return COR_Expressions.EmptyRelation()
	# (𝟏) ∘ ((A) † ((A)⁻)) = (A) † ((A)⁻)
	match expression:
		case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.IdentityRelation:
					match arg2:
						case COR_Expressions.Dagger(argument1=arg1, argument2=arg2):
							match arg1:
								case _:
									A = arg1
									match arg2:
										case COR_Expressions.Complement(argument=arg):
											match arg:
												case _:
													A = arg
													return COR_Expressions.Dagger(A, COR_Expressions.Complement(A))
	# ((C) ∪ ((C)⁻¹))⁻¹ = (C) ∪ ((C)⁻¹)
	match expression:
		case COR_Expressions.Converse(argument=arg):
			match arg:
				case COR_Expressions.Union(argument1=arg1, argument2=arg2):
					match arg1:
						case _:
							C = arg1
							match arg2:
								case COR_Expressions.Converse(argument=arg):
									match arg:
										case _:
											C = arg
											return COR_Expressions.Union(C, COR_Expressions.Converse(C))
	# (𝟎) ∪ ((𝟏) ∪ ((B)⁻)) = (𝟏) ∪ ((B)⁻)
	match expression:
		case COR_Expressions.Union(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.EmptyRelation():
					match arg2:
						case COR_Expressions.Union(argument1=arg1, argument2=arg2):
							match arg1:
								case COR_Expressions.IdentityRelation:
									match arg2:
										case COR_Expressions.Complement(argument=arg):
											match arg:
												case _:
													B = arg
													return COR_Expressions.Union(COR_Expressions.IdentityRelation(), COR_Expressions.Complement(B))
	# (𝟎) ∪ ((C) † ((B)⁻¹)) = (C) † ((B)⁻¹)
	match expression:
		case COR_Expressions.Union(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.EmptyRelation():
					match arg2:
						case COR_Expressions.Dagger(argument1=arg1, argument2=arg2):
							match arg1:
								case _:
									C = arg1
									match arg2:
										case COR_Expressions.Converse(argument=arg):
											match arg:
												case _:
													B = arg
													return COR_Expressions.Dagger(C, COR_Expressions.Converse(B))
	# (T) † ((A) ∘ ((A)⁻¹)) = T
	match expression:
		case COR_Expressions.Dagger(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.UniversalRelation():
					match arg2:
						case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
							match arg1:
								case _:
									A = arg1
									match arg2:
										case COR_Expressions.Converse(argument=arg):
											match arg:
												case _:
													A = arg
													return COR_Expressions.UniversalRelation()
	# (((B)⁻)⁻¹)⁻ = (B)⁻¹
	match expression:
		case COR_Expressions.Complement(argument=arg):
			match arg:
				case COR_Expressions.Converse(argument=arg):
					match arg:
						case COR_Expressions.Complement(argument=arg):
							match arg:
								case _:
									B = arg
									return COR_Expressions.Converse(B)
	# (𝟏) ∘ ((C) ∘ ((B)⁻¹)) = (C) ∘ ((B)⁻¹)
	match expression:
		case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.IdentityRelation:
					match arg2:
						case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
							match arg1:
								case _:
									C = arg1
									match arg2:
										case COR_Expressions.Converse(argument=arg):
											match arg:
												case _:
													B = arg
													return COR_Expressions.Composition(C, COR_Expressions.Converse(B))
	# (T) ∘ ((𝟏) ∪ ((B)⁻¹)) = T
	match expression:
		case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.UniversalRelation():
					match arg2:
						case COR_Expressions.Union(argument1=arg1, argument2=arg2):
							match arg1:
								case COR_Expressions.IdentityRelation:
									match arg2:
										case COR_Expressions.Converse(argument=arg):
											match arg:
												case _:
													B = arg
													return COR_Expressions.UniversalRelation()
	# ((B) † ((B)⁻¹))⁻¹ = (B) † ((B)⁻¹)
	match expression:
		case COR_Expressions.Converse(argument=arg):
			match arg:
				case COR_Expressions.Dagger(argument1=arg1, argument2=arg2):
					match arg1:
						case _:
							B = arg1
							match arg2:
								case COR_Expressions.Converse(argument=arg):
									match arg:
										case _:
											B = arg
											return COR_Expressions.Dagger(B, COR_Expressions.Converse(B))
	# (𝟏) ∘ ((B) ∪ ((C)⁻¹)) = (B) ∪ ((C)⁻¹)
	match expression:
		case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.IdentityRelation:
					match arg2:
						case COR_Expressions.Union(argument1=arg1, argument2=arg2):
							match arg1:
								case _:
									B = arg1
									match arg2:
										case COR_Expressions.Converse(argument=arg):
											match arg:
												case _:
													C = arg
													return COR_Expressions.Union(B, COR_Expressions.Converse(C))
	# ((A) ∘ ((B)⁻¹))⁻¹ = (B) ∘ ((A)⁻¹)
	match expression:
		case COR_Expressions.Converse(argument=arg):
			match arg:
				case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
					match arg1:
						case _:
							A = arg1
							match arg2:
								case COR_Expressions.Converse(argument=arg):
									match arg:
										case _:
											B = arg
											return COR_Expressions.Composition(B, COR_Expressions.Converse(A))
	# (𝟎) ∘ ((A) ∪ ((B)⁻)) = 𝟎
	match expression:
		case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.EmptyRelation():
					match arg2:
						case COR_Expressions.Union(argument1=arg1, argument2=arg2):
							match arg1:
								case _:
									A = arg1
									match arg2:
										case COR_Expressions.Complement(argument=arg):
											match arg:
												case _:
													B = arg
													return COR_Expressions.EmptyRelation()
	# (T) ∘ ((T) ∘ ((𝟏)⁻)) = (T) ∘ ((𝟏)⁻)
	match expression:
		case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.UniversalRelation():
					match arg2:
						case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
							match arg1:
								case COR_Expressions.UniversalRelation():
									match arg2:
										case COR_Expressions.Complement(argument=arg):
											match arg:
												case COR_Expressions.IdentityRelation:
													return COR_Expressions.Composition(COR_Expressions.UniversalRelation(), COR_Expressions.Complement(COR_Expressions.IdentityRelation()))
	# (T) † ((C) ∘ ((B)⁻¹)) = T
	match expression:
		case COR_Expressions.Dagger(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.UniversalRelation():
					match arg2:
						case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
							match arg1:
								case _:
									C = arg1
									match arg2:
										case COR_Expressions.Converse(argument=arg):
											match arg:
												case _:
													B = arg
													return COR_Expressions.UniversalRelation()
	# (𝟏) ∘ ((B) ∘ ((𝟏)⁻)) = (B) ∘ ((𝟏)⁻)
	match expression:
		case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.IdentityRelation:
					match arg2:
						case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
							match arg1:
								case _:
									B = arg1
									match arg2:
										case COR_Expressions.Complement(argument=arg):
											match arg:
												case COR_Expressions.IdentityRelation:
													return COR_Expressions.Composition(B, COR_Expressions.Complement(COR_Expressions.IdentityRelation()))
	# (T) ∪ ((C) † ((A)⁻¹)) = T
	match expression:
		case COR_Expressions.Union(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.UniversalRelation():
					match arg2:
						case COR_Expressions.Dagger(argument1=arg1, argument2=arg2):
							match arg1:
								case _:
									C = arg1
									match arg2:
										case COR_Expressions.Converse(argument=arg):
											match arg:
												case _:
													A = arg
													return COR_Expressions.UniversalRelation()
	# (𝟏) ∘ ((A) ∘ ((B)⁻)) = (A) ∘ ((B)⁻)
	match expression:
		case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.IdentityRelation:
					match arg2:
						case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
							match arg1:
								case _:
									A = arg1
									match arg2:
										case COR_Expressions.Complement(argument=arg):
											match arg:
												case _:
													B = arg
													return COR_Expressions.Composition(A, COR_Expressions.Complement(B))
	# (𝟏) ∘ ((B) † ((B)⁻)) = (B) † ((B)⁻)
	match expression:
		case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.IdentityRelation:
					match arg2:
						case COR_Expressions.Dagger(argument1=arg1, argument2=arg2):
							match arg1:
								case _:
									B = arg1
									match arg2:
										case COR_Expressions.Complement(argument=arg):
											match arg:
												case _:
													B = arg
													return COR_Expressions.Dagger(B, COR_Expressions.Complement(B))
	# (𝟏) ∘ ((A) ∪ ((C)⁻¹)) = (A) ∪ ((C)⁻¹)
	match expression:
		case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.IdentityRelation:
					match arg2:
						case COR_Expressions.Union(argument1=arg1, argument2=arg2):
							match arg1:
								case _:
									A = arg1
									match arg2:
										case COR_Expressions.Converse(argument=arg):
											match arg:
												case _:
													C = arg
													return COR_Expressions.Union(A, COR_Expressions.Converse(C))
	# (𝟏) ∘ ((B) ∪ ((A)⁻)) = (B) ∪ ((A)⁻)
	match expression:
		case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.IdentityRelation:
					match arg2:
						case COR_Expressions.Union(argument1=arg1, argument2=arg2):
							match arg1:
								case _:
									B = arg1
									match arg2:
										case COR_Expressions.Complement(argument=arg):
											match arg:
												case _:
													A = arg
													return COR_Expressions.Union(B, COR_Expressions.Complement(A))
	# ((𝟏)⁻) † ((B)⁻¹) = (B)⁻¹
	match expression:
		case COR_Expressions.Dagger(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.Complement(argument=arg):
					match arg:
						case COR_Expressions.IdentityRelation:
							match arg2:
								case COR_Expressions.Converse(argument=arg):
									match arg:
										case _:
											B = arg
											return COR_Expressions.Converse(B)
	# (T) † ((B) † ((A)⁻)) = T
	match expression:
		case COR_Expressions.Dagger(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.UniversalRelation():
					match arg2:
						case COR_Expressions.Dagger(argument1=arg1, argument2=arg2):
							match arg1:
								case _:
									B = arg1
									match arg2:
										case COR_Expressions.Complement(argument=arg):
											match arg:
												case _:
													A = arg
													return COR_Expressions.UniversalRelation()
	# (𝟎) † ((𝟎) † ((A)⁻¹)) = (𝟎) † ((A)⁻¹)
	match expression:
		case COR_Expressions.Dagger(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.EmptyRelation():
					match arg2:
						case COR_Expressions.Dagger(argument1=arg1, argument2=arg2):
							match arg1:
								case COR_Expressions.EmptyRelation():
									match arg2:
										case COR_Expressions.Converse(argument=arg):
											match arg:
												case _:
													A = arg
													return COR_Expressions.Dagger(COR_Expressions.EmptyRelation(), COR_Expressions.Converse(A))
	# (𝟏) ∘ ((C) ∘ ((A)⁻)) = (C) ∘ ((A)⁻)
	match expression:
		case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.IdentityRelation:
					match arg2:
						case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
							match arg1:
								case _:
									C = arg1
									match arg2:
										case COR_Expressions.Complement(argument=arg):
											match arg:
												case _:
													A = arg
													return COR_Expressions.Composition(C, COR_Expressions.Complement(A))
	# (𝟎) ∘ ((B) ∘ ((C)⁻)) = 𝟎
	match expression:
		case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.EmptyRelation():
					match arg2:
						case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
							match arg1:
								case _:
									B = arg1
									match arg2:
										case COR_Expressions.Complement(argument=arg):
											match arg:
												case _:
													C = arg
													return COR_Expressions.EmptyRelation()
	# (𝟏) ∘ ((B) ∘ ((C)⁻)) = (B) ∘ ((C)⁻)
	match expression:
		case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.IdentityRelation:
					match arg2:
						case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
							match arg1:
								case _:
									B = arg1
									match arg2:
										case COR_Expressions.Complement(argument=arg):
											match arg:
												case _:
													C = arg
													return COR_Expressions.Composition(B, COR_Expressions.Complement(C))
	# ((C)⁻¹) † ((𝟏)⁻) = (C)⁻¹
	match expression:
		case COR_Expressions.Dagger(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.Converse(argument=arg):
					match arg:
						case _:
							C = arg
							match arg2:
								case COR_Expressions.Complement(argument=arg):
									match arg:
										case COR_Expressions.IdentityRelation:
											return COR_Expressions.Converse(C)
	# (𝟎) ∪ ((𝟏) ∪ ((A)⁻)) = (𝟏) ∪ ((A)⁻)
	match expression:
		case COR_Expressions.Union(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.EmptyRelation():
					match arg2:
						case COR_Expressions.Union(argument1=arg1, argument2=arg2):
							match arg1:
								case COR_Expressions.IdentityRelation:
									match arg2:
										case COR_Expressions.Complement(argument=arg):
											match arg:
												case _:
													A = arg
													return COR_Expressions.Union(COR_Expressions.IdentityRelation(), COR_Expressions.Complement(A))
	# (𝟎) ∪ ((𝟏) † ((A)⁻)) = (𝟏) † ((A)⁻)
	match expression:
		case COR_Expressions.Union(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.EmptyRelation():
					match arg2:
						case COR_Expressions.Dagger(argument1=arg1, argument2=arg2):
							match arg1:
								case COR_Expressions.IdentityRelation:
									match arg2:
										case COR_Expressions.Complement(argument=arg):
											match arg:
												case _:
													A = arg
													return COR_Expressions.Dagger(COR_Expressions.IdentityRelation(), COR_Expressions.Complement(A))
	# (((C)⁻)⁻¹)⁻ = (C)⁻¹
	match expression:
		case COR_Expressions.Complement(argument=arg):
			match arg:
				case COR_Expressions.Converse(argument=arg):
					match arg:
						case COR_Expressions.Complement(argument=arg):
							match arg:
								case _:
									C = arg
									return COR_Expressions.Converse(C)
	# (𝟎) ∪ ((C) ∘ ((B)⁻)) = (C) ∘ ((B)⁻)
	match expression:
		case COR_Expressions.Union(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.EmptyRelation():
					match arg2:
						case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
							match arg1:
								case _:
									C = arg1
									match arg2:
										case COR_Expressions.Complement(argument=arg):
											match arg:
												case _:
													B = arg
													return COR_Expressions.Composition(C, COR_Expressions.Complement(B))
	# (T) ∪ ((C) † ((B)⁻)) = T
	match expression:
		case COR_Expressions.Union(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.UniversalRelation():
					match arg2:
						case COR_Expressions.Dagger(argument1=arg1, argument2=arg2):
							match arg1:
								case _:
									C = arg1
									match arg2:
										case COR_Expressions.Complement(argument=arg):
											match arg:
												case _:
													B = arg
													return COR_Expressions.UniversalRelation()
	# (𝟏) ∘ ((C) ∘ ((C)⁻)) = (C) ∘ ((C)⁻)
	match expression:
		case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.IdentityRelation:
					match arg2:
						case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
							match arg1:
								case _:
									C = arg1
									match arg2:
										case COR_Expressions.Complement(argument=arg):
											match arg:
												case _:
													C = arg
													return COR_Expressions.Composition(C, COR_Expressions.Complement(C))
	# (T) † ((𝟏) ∪ ((C)⁻)) = T
	match expression:
		case COR_Expressions.Dagger(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.UniversalRelation():
					match arg2:
						case COR_Expressions.Union(argument1=arg1, argument2=arg2):
							match arg1:
								case COR_Expressions.IdentityRelation:
									match arg2:
										case COR_Expressions.Complement(argument=arg):
											match arg:
												case _:
													C = arg
													return COR_Expressions.UniversalRelation()
	# (T) † ((C) ∘ ((C)⁻)) = T
	match expression:
		case COR_Expressions.Dagger(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.UniversalRelation():
					match arg2:
						case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
							match arg1:
								case _:
									C = arg1
									match arg2:
										case COR_Expressions.Complement(argument=arg):
											match arg:
												case _:
													C = arg
													return COR_Expressions.UniversalRelation()
	# (𝟎) ∘ ((A) ∪ ((B)⁻¹)) = 𝟎
	match expression:
		case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.EmptyRelation():
					match arg2:
						case COR_Expressions.Union(argument1=arg1, argument2=arg2):
							match arg1:
								case _:
									A = arg1
									match arg2:
										case COR_Expressions.Converse(argument=arg):
											match arg:
												case _:
													B = arg
													return COR_Expressions.EmptyRelation()
	# (𝟏) ∘ ((B) ∪ ((B)⁻¹)) = (B) ∪ ((B)⁻¹)
	match expression:
		case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.IdentityRelation:
					match arg2:
						case COR_Expressions.Union(argument1=arg1, argument2=arg2):
							match arg1:
								case _:
									B = arg1
									match arg2:
										case COR_Expressions.Converse(argument=arg):
											match arg:
												case _:
													B = arg
													return COR_Expressions.Union(B, COR_Expressions.Converse(B))
	# (𝟏) ∪ ((T) ∘ ((𝟏)⁻)) = T
	match expression:
		case COR_Expressions.Union(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.IdentityRelation:
					match arg2:
						case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
							match arg1:
								case COR_Expressions.UniversalRelation():
									match arg2:
										case COR_Expressions.Complement(argument=arg):
											match arg:
												case COR_Expressions.IdentityRelation:
													return COR_Expressions.UniversalRelation()
	# (𝟎) ∘ ((C) ∘ ((B)⁻¹)) = 𝟎
	match expression:
		case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.EmptyRelation():
					match arg2:
						case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
							match arg1:
								case _:
									C = arg1
									match arg2:
										case COR_Expressions.Converse(argument=arg):
											match arg:
												case _:
													B = arg
													return COR_Expressions.EmptyRelation()
	# ((A)⁻) † ((𝟏)⁻) = (A)⁻
	match expression:
		case COR_Expressions.Dagger(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.Complement(argument=arg):
					match arg:
						case _:
							A = arg
							match arg2:
								case COR_Expressions.Complement(argument=arg):
									match arg:
										case COR_Expressions.IdentityRelation:
											return COR_Expressions.Complement(A)
	# (T) ∪ ((T) ∘ ((C)⁻)) = T
	match expression:
		case COR_Expressions.Union(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.UniversalRelation():
					match arg2:
						case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
							match arg1:
								case COR_Expressions.UniversalRelation():
									match arg2:
										case COR_Expressions.Complement(argument=arg):
											match arg:
												case _:
													C = arg
													return COR_Expressions.UniversalRelation()
	# (𝟎) ∘ ((B) ∪ ((C)⁻)) = 𝟎
	match expression:
		case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.EmptyRelation():
					match arg2:
						case COR_Expressions.Union(argument1=arg1, argument2=arg2):
							match arg1:
								case _:
									B = arg1
									match arg2:
										case COR_Expressions.Complement(argument=arg):
											match arg:
												case _:
													C = arg
													return COR_Expressions.EmptyRelation()
	# (𝟎) ∪ ((C) ∘ ((A)⁻¹)) = (C) ∘ ((A)⁻¹)
	match expression:
		case COR_Expressions.Union(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.EmptyRelation():
					match arg2:
						case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
							match arg1:
								case _:
									C = arg1
									match arg2:
										case COR_Expressions.Converse(argument=arg):
											match arg:
												case _:
													A = arg
													return COR_Expressions.Composition(C, COR_Expressions.Converse(A))
	# ((A) ∪ ((A)⁻¹))⁻¹ = (A) ∪ ((A)⁻¹)
	match expression:
		case COR_Expressions.Converse(argument=arg):
			match arg:
				case COR_Expressions.Union(argument1=arg1, argument2=arg2):
					match arg1:
						case _:
							A = arg1
							match arg2:
								case COR_Expressions.Converse(argument=arg):
									match arg:
										case _:
											A = arg
											return COR_Expressions.Union(A, COR_Expressions.Converse(A))
	# (T) † ((𝟏) † ((B)⁻)) = T
	match expression:
		case COR_Expressions.Dagger(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.UniversalRelation():
					match arg2:
						case COR_Expressions.Dagger(argument1=arg1, argument2=arg2):
							match arg1:
								case COR_Expressions.IdentityRelation:
									match arg2:
										case COR_Expressions.Complement(argument=arg):
											match arg:
												case _:
													B = arg
													return COR_Expressions.UniversalRelation()
	# (𝟏) ∘ ((A) ∘ ((C)⁻)) = (A) ∘ ((C)⁻)
	match expression:
		case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.IdentityRelation:
					match arg2:
						case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
							match arg1:
								case _:
									A = arg1
									match arg2:
										case COR_Expressions.Complement(argument=arg):
											match arg:
												case _:
													C = arg
													return COR_Expressions.Composition(A, COR_Expressions.Complement(C))
	# (T) ∪ ((B) ∘ ((A)⁻¹)) = T
	match expression:
		case COR_Expressions.Union(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.UniversalRelation():
					match arg2:
						case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
							match arg1:
								case _:
									B = arg1
									match arg2:
										case COR_Expressions.Converse(argument=arg):
											match arg:
												case _:
													A = arg
													return COR_Expressions.UniversalRelation()
	# (T) † ((T) ∘ ((C)⁻¹)) = T
	match expression:
		case COR_Expressions.Dagger(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.UniversalRelation():
					match arg2:
						case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
							match arg1:
								case COR_Expressions.UniversalRelation():
									match arg2:
										case COR_Expressions.Converse(argument=arg):
											match arg:
												case _:
													C = arg
													return COR_Expressions.UniversalRelation()
	# (𝟎) ∪ ((A) † ((C)⁻)) = (A) † ((C)⁻)
	match expression:
		case COR_Expressions.Union(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.EmptyRelation():
					match arg2:
						case COR_Expressions.Dagger(argument1=arg1, argument2=arg2):
							match arg1:
								case _:
									A = arg1
									match arg2:
										case COR_Expressions.Complement(argument=arg):
											match arg:
												case _:
													C = arg
													return COR_Expressions.Dagger(A, COR_Expressions.Complement(C))
	# (T) ∪ ((A) † ((C)⁻¹)) = T
	match expression:
		case COR_Expressions.Union(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.UniversalRelation():
					match arg2:
						case COR_Expressions.Dagger(argument1=arg1, argument2=arg2):
							match arg1:
								case _:
									A = arg1
									match arg2:
										case COR_Expressions.Converse(argument=arg):
											match arg:
												case _:
													C = arg
													return COR_Expressions.UniversalRelation()
	# (T) † ((C) † ((B)⁻)) = T
	match expression:
		case COR_Expressions.Dagger(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.UniversalRelation():
					match arg2:
						case COR_Expressions.Dagger(argument1=arg1, argument2=arg2):
							match arg1:
								case _:
									C = arg1
									match arg2:
										case COR_Expressions.Complement(argument=arg):
											match arg:
												case _:
													B = arg
													return COR_Expressions.UniversalRelation()
	# (𝟏) ∘ ((𝟎) † ((B)⁻¹)) = (𝟎) † ((B)⁻¹)
	match expression:
		case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.IdentityRelation:
					match arg2:
						case COR_Expressions.Dagger(argument1=arg1, argument2=arg2):
							match arg1:
								case COR_Expressions.EmptyRelation():
									match arg2:
										case COR_Expressions.Converse(argument=arg):
											match arg:
												case _:
													B = arg
													return COR_Expressions.Dagger(COR_Expressions.EmptyRelation(), COR_Expressions.Converse(B))
	# ((A)⁻) ∪ ((A)⁻) = (A)⁻
	match expression:
		case COR_Expressions.Union(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.Complement(argument=arg):
					match arg:
						case _:
							A = arg
							match arg2:
								case COR_Expressions.Complement(argument=arg):
									match arg:
										case _:
											A = arg
											return COR_Expressions.Complement(A)
	# (T) † (((A)⁻¹)⁻) = T
	match expression:
		case COR_Expressions.Dagger(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.UniversalRelation():
					match arg2:
						case COR_Expressions.Complement(argument=arg):
							match arg:
								case COR_Expressions.Converse(argument=arg):
									match arg:
										case _:
											A = arg
											return COR_Expressions.UniversalRelation()
	# (T) ∪ ((B) ∘ ((B)⁻¹)) = T
	match expression:
		case COR_Expressions.Union(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.UniversalRelation():
					match arg2:
						case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
							match arg1:
								case _:
									B = arg1
									match arg2:
										case COR_Expressions.Converse(argument=arg):
											match arg:
												case _:
													B = arg
													return COR_Expressions.UniversalRelation()
	# (𝟎) ∪ ((C) ∘ ((C)⁻)) = (C) ∘ ((C)⁻)
	match expression:
		case COR_Expressions.Union(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.EmptyRelation():
					match arg2:
						case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
							match arg1:
								case _:
									C = arg1
									match arg2:
										case COR_Expressions.Complement(argument=arg):
											match arg:
												case _:
													C = arg
													return COR_Expressions.Composition(C, COR_Expressions.Complement(C))
	# (T) ∪ ((B) ∘ ((𝟏)⁻)) = T
	match expression:
		case COR_Expressions.Union(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.UniversalRelation():
					match arg2:
						case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
							match arg1:
								case _:
									B = arg1
									match arg2:
										case COR_Expressions.Complement(argument=arg):
											match arg:
												case COR_Expressions.IdentityRelation:
													return COR_Expressions.UniversalRelation()
	# (𝟏) ∘ ((𝟏) ∪ ((B)⁻)) = (𝟏) ∪ ((B)⁻)
	match expression:
		case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.IdentityRelation:
					match arg2:
						case COR_Expressions.Union(argument1=arg1, argument2=arg2):
							match arg1:
								case COR_Expressions.IdentityRelation:
									match arg2:
										case COR_Expressions.Complement(argument=arg):
											match arg:
												case _:
													B = arg
													return COR_Expressions.Union(COR_Expressions.IdentityRelation(), COR_Expressions.Complement(B))
	# (T) ∘ ((T) ∘ ((B)⁻¹)) = (T) ∘ ((B)⁻¹)
	match expression:
		case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.UniversalRelation():
					match arg2:
						case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
							match arg1:
								case COR_Expressions.UniversalRelation():
									match arg2:
										case COR_Expressions.Converse(argument=arg):
											match arg:
												case _:
													B = arg
													return COR_Expressions.Composition(COR_Expressions.UniversalRelation(), COR_Expressions.Converse(B))
	# (T) † ((T) ∘ ((𝟏)⁻)) = T
	match expression:
		case COR_Expressions.Dagger(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.UniversalRelation():
					match arg2:
						case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
							match arg1:
								case COR_Expressions.UniversalRelation():
									match arg2:
										case COR_Expressions.Complement(argument=arg):
											match arg:
												case COR_Expressions.IdentityRelation:
													return COR_Expressions.UniversalRelation()
	# (𝟎) † ((T) ∘ ((C)⁻)) = (T) ∘ ((C)⁻)
	match expression:
		case COR_Expressions.Dagger(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.EmptyRelation():
					match arg2:
						case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
							match arg1:
								case COR_Expressions.UniversalRelation():
									match arg2:
										case COR_Expressions.Complement(argument=arg):
											match arg:
												case _:
													C = arg
													return COR_Expressions.Composition(COR_Expressions.UniversalRelation(), COR_Expressions.Complement(C))
	# (T) † ((A) † ((A)⁻)) = T
	match expression:
		case COR_Expressions.Dagger(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.UniversalRelation():
					match arg2:
						case COR_Expressions.Dagger(argument1=arg1, argument2=arg2):
							match arg1:
								case _:
									A = arg1
									match arg2:
										case COR_Expressions.Complement(argument=arg):
											match arg:
												case _:
													A = arg
													return COR_Expressions.UniversalRelation()
	# (𝟎) ∘ ((A) ∪ ((C)⁻¹)) = 𝟎
	match expression:
		case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.EmptyRelation():
					match arg2:
						case COR_Expressions.Union(argument1=arg1, argument2=arg2):
							match arg1:
								case _:
									A = arg1
									match arg2:
										case COR_Expressions.Converse(argument=arg):
											match arg:
												case _:
													C = arg
													return COR_Expressions.EmptyRelation()
	# (T) † ((B) ∘ ((C)⁻)) = T
	match expression:
		case COR_Expressions.Dagger(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.UniversalRelation():
					match arg2:
						case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
							match arg1:
								case _:
									B = arg1
									match arg2:
										case COR_Expressions.Complement(argument=arg):
											match arg:
												case _:
													C = arg
													return COR_Expressions.UniversalRelation()
	# (𝟎) † ((B) † ((B)⁻¹)) = (𝟎) † ((B)⁻¹)
	match expression:
		case COR_Expressions.Dagger(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.EmptyRelation():
					match arg2:
						case COR_Expressions.Dagger(argument1=arg1, argument2=arg2):
							match arg1:
								case _:
									B = arg1
									match arg2:
										case COR_Expressions.Converse(argument=arg):
											match arg:
												case _:
													B = arg
													return COR_Expressions.Dagger(COR_Expressions.EmptyRelation(), COR_Expressions.Converse(B))
	# (T) † ((𝟏) † ((B)⁻¹)) = T
	match expression:
		case COR_Expressions.Dagger(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.UniversalRelation():
					match arg2:
						case COR_Expressions.Dagger(argument1=arg1, argument2=arg2):
							match arg1:
								case COR_Expressions.IdentityRelation:
									match arg2:
										case COR_Expressions.Converse(argument=arg):
											match arg:
												case _:
													B = arg
													return COR_Expressions.UniversalRelation()
	# (𝟎) ∘ ((T) ∘ ((A)⁻)) = 𝟎
	match expression:
		case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.EmptyRelation():
					match arg2:
						case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
							match arg1:
								case COR_Expressions.UniversalRelation():
									match arg2:
										case COR_Expressions.Complement(argument=arg):
											match arg:
												case _:
													A = arg
													return COR_Expressions.EmptyRelation()
	# (𝟏) ∘ ((𝟏) † ((C)⁻¹)) = (𝟏) † ((C)⁻¹)
	match expression:
		case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.IdentityRelation:
					match arg2:
						case COR_Expressions.Dagger(argument1=arg1, argument2=arg2):
							match arg1:
								case COR_Expressions.IdentityRelation:
									match arg2:
										case COR_Expressions.Converse(argument=arg):
											match arg:
												case _:
													C = arg
													return COR_Expressions.Dagger(COR_Expressions.IdentityRelation(), COR_Expressions.Converse(C))
	# (T) ∪ ((𝟏) † ((A)⁻)) = T
	match expression:
		case COR_Expressions.Union(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.UniversalRelation():
					match arg2:
						case COR_Expressions.Dagger(argument1=arg1, argument2=arg2):
							match arg1:
								case COR_Expressions.IdentityRelation:
									match arg2:
										case COR_Expressions.Complement(argument=arg):
											match arg:
												case _:
													A = arg
													return COR_Expressions.UniversalRelation()
	# (((C)⁻¹)⁻)⁻ = (C)⁻¹
	match expression:
		case COR_Expressions.Complement(argument=arg):
			match arg:
				case COR_Expressions.Complement(argument=arg):
					match arg:
						case COR_Expressions.Converse(argument=arg):
							match arg:
								case _:
									C = arg
									return COR_Expressions.Converse(C)
	# (((B)⁻)⁻¹)⁻¹ = (B)⁻
	match expression:
		case COR_Expressions.Converse(argument=arg):
			match arg:
				case COR_Expressions.Converse(argument=arg):
					match arg:
						case COR_Expressions.Complement(argument=arg):
							match arg:
								case _:
									B = arg
									return COR_Expressions.Complement(B)
	# (𝟎) ∪ ((A) ∪ ((B)⁻¹)) = (A) ∪ ((B)⁻¹)
	match expression:
		case COR_Expressions.Union(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.EmptyRelation():
					match arg2:
						case COR_Expressions.Union(argument1=arg1, argument2=arg2):
							match arg1:
								case _:
									A = arg1
									match arg2:
										case COR_Expressions.Converse(argument=arg):
											match arg:
												case _:
													B = arg
													return COR_Expressions.Union(A, COR_Expressions.Converse(B))
	# (T) † ((B) ∪ ((𝟏)⁻)) = T
	match expression:
		case COR_Expressions.Dagger(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.UniversalRelation():
					match arg2:
						case COR_Expressions.Union(argument1=arg1, argument2=arg2):
							match arg1:
								case _:
									B = arg1
									match arg2:
										case COR_Expressions.Complement(argument=arg):
											match arg:
												case COR_Expressions.IdentityRelation:
													return COR_Expressions.UniversalRelation()
	# (T) ∪ ((𝟏) † ((A)⁻¹)) = T
	match expression:
		case COR_Expressions.Union(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.UniversalRelation():
					match arg2:
						case COR_Expressions.Dagger(argument1=arg1, argument2=arg2):
							match arg1:
								case COR_Expressions.IdentityRelation:
									match arg2:
										case COR_Expressions.Converse(argument=arg):
											match arg:
												case _:
													A = arg
													return COR_Expressions.UniversalRelation()
	# (𝟎) ∘ ((C) † ((B)⁻)) = 𝟎
	match expression:
		case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.EmptyRelation():
					match arg2:
						case COR_Expressions.Dagger(argument1=arg1, argument2=arg2):
							match arg1:
								case _:
									C = arg1
									match arg2:
										case COR_Expressions.Complement(argument=arg):
											match arg:
												case _:
													B = arg
													return COR_Expressions.EmptyRelation()
	# (T) ∪ ((𝟎) † ((B)⁻)) = T
	match expression:
		case COR_Expressions.Union(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.UniversalRelation():
					match arg2:
						case COR_Expressions.Dagger(argument1=arg1, argument2=arg2):
							match arg1:
								case COR_Expressions.EmptyRelation():
									match arg2:
										case COR_Expressions.Complement(argument=arg):
											match arg:
												case _:
													B = arg
													return COR_Expressions.UniversalRelation()
	# (T) † ((C) ∘ ((B)⁻)) = T
	match expression:
		case COR_Expressions.Dagger(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.UniversalRelation():
					match arg2:
						case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
							match arg1:
								case _:
									C = arg1
									match arg2:
										case COR_Expressions.Complement(argument=arg):
											match arg:
												case _:
													B = arg
													return COR_Expressions.UniversalRelation()
	# (T) ∪ ((B) ∘ ((C)⁻¹)) = T
	match expression:
		case COR_Expressions.Union(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.UniversalRelation():
					match arg2:
						case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
							match arg1:
								case _:
									B = arg1
									match arg2:
										case COR_Expressions.Converse(argument=arg):
											match arg:
												case _:
													C = arg
													return COR_Expressions.UniversalRelation()
	# (T) ∪ ((𝟏) † ((B)⁻)) = T
	match expression:
		case COR_Expressions.Union(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.UniversalRelation():
					match arg2:
						case COR_Expressions.Dagger(argument1=arg1, argument2=arg2):
							match arg1:
								case COR_Expressions.IdentityRelation:
									match arg2:
										case COR_Expressions.Complement(argument=arg):
											match arg:
												case _:
													B = arg
													return COR_Expressions.UniversalRelation()
	# (T) ∪ ((A) ∘ ((B)⁻)) = T
	match expression:
		case COR_Expressions.Union(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.UniversalRelation():
					match arg2:
						case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
							match arg1:
								case _:
									A = arg1
									match arg2:
										case COR_Expressions.Complement(argument=arg):
											match arg:
												case _:
													B = arg
													return COR_Expressions.UniversalRelation()
	# ((C)⁻) † ((𝟏)⁻) = (C)⁻
	match expression:
		case COR_Expressions.Dagger(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.Complement(argument=arg):
					match arg:
						case _:
							C = arg
							match arg2:
								case COR_Expressions.Complement(argument=arg):
									match arg:
										case COR_Expressions.IdentityRelation:
											return COR_Expressions.Complement(C)
	# (A) ∪ ((𝟏) ∪ ((A)⁻)) = T
	match expression:
		case COR_Expressions.Union(argument1=arg1, argument2=arg2):
			match arg1:
				case _:
					A = arg1
					match arg2:
						case COR_Expressions.Union(argument1=arg1, argument2=arg2):
							match arg1:
								case COR_Expressions.IdentityRelation:
									match arg2:
										case COR_Expressions.Complement(argument=arg):
											match arg:
												case _:
													A = arg
													return COR_Expressions.UniversalRelation()
	# (𝟎) ∪ ((𝟎) † ((C)⁻)) = (𝟎) † ((C)⁻)
	match expression:
		case COR_Expressions.Union(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.EmptyRelation():
					match arg2:
						case COR_Expressions.Dagger(argument1=arg1, argument2=arg2):
							match arg1:
								case COR_Expressions.EmptyRelation():
									match arg2:
										case COR_Expressions.Complement(argument=arg):
											match arg:
												case _:
													C = arg
													return COR_Expressions.Dagger(COR_Expressions.EmptyRelation(), COR_Expressions.Complement(C))
	# (T) ∪ ((𝟏) ∪ ((C)⁻)) = T
	match expression:
		case COR_Expressions.Union(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.UniversalRelation():
					match arg2:
						case COR_Expressions.Union(argument1=arg1, argument2=arg2):
							match arg1:
								case COR_Expressions.IdentityRelation:
									match arg2:
										case COR_Expressions.Complement(argument=arg):
											match arg:
												case _:
													C = arg
													return COR_Expressions.UniversalRelation()
	# (T) ∘ ((𝟏) ∪ ((B)⁻)) = T
	match expression:
		case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.UniversalRelation():
					match arg2:
						case COR_Expressions.Union(argument1=arg1, argument2=arg2):
							match arg1:
								case COR_Expressions.IdentityRelation:
									match arg2:
										case COR_Expressions.Complement(argument=arg):
											match arg:
												case _:
													B = arg
													return COR_Expressions.UniversalRelation()
	# (𝟎) ∪ ((B) ∪ ((A)⁻¹)) = (B) ∪ ((A)⁻¹)
	match expression:
		case COR_Expressions.Union(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.EmptyRelation():
					match arg2:
						case COR_Expressions.Union(argument1=arg1, argument2=arg2):
							match arg1:
								case _:
									B = arg1
									match arg2:
										case COR_Expressions.Converse(argument=arg):
											match arg:
												case _:
													A = arg
													return COR_Expressions.Union(B, COR_Expressions.Converse(A))
	# (T) † ((A) † ((A)⁻¹)) = T
	match expression:
		case COR_Expressions.Dagger(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.UniversalRelation():
					match arg2:
						case COR_Expressions.Dagger(argument1=arg1, argument2=arg2):
							match arg1:
								case _:
									A = arg1
									match arg2:
										case COR_Expressions.Converse(argument=arg):
											match arg:
												case _:
													A = arg
													return COR_Expressions.UniversalRelation()
	# (((A) † ((B)⁻¹))⁻)⁻ = (A) † ((B)⁻¹)
	match expression:
		case COR_Expressions.Complement(argument=arg):
			match arg:
				case COR_Expressions.Complement(argument=arg):
					match arg:
						case COR_Expressions.Dagger(argument1=arg1, argument2=arg2):
							match arg1:
								case _:
									A = arg1
									match arg2:
										case COR_Expressions.Converse(argument=arg):
											match arg:
												case _:
													B = arg
													return COR_Expressions.Dagger(A, COR_Expressions.Converse(B))
	# (𝟏) ∘ ((T) ∘ ((C) † ((B)⁻¹))) = (T) ∘ ((C) † ((B)⁻¹))
	match expression:
		case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.IdentityRelation:
					match arg2:
						case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
							match arg1:
								case COR_Expressions.UniversalRelation():
									match arg2:
										case COR_Expressions.Dagger(argument1=arg1, argument2=arg2):
											match arg1:
												case _:
													C = arg1
													match arg2:
														case COR_Expressions.Converse(argument=arg):
															match arg:
																case _:
																	B = arg
																	return COR_Expressions.Composition(COR_Expressions.UniversalRelation(), COR_Expressions.Dagger(C, COR_Expressions.Converse(B)))
	# (((𝟎) † ((B)⁻¹))⁻)⁻ = (𝟎) † ((B)⁻¹)
	match expression:
		case COR_Expressions.Complement(argument=arg):
			match arg:
				case COR_Expressions.Complement(argument=arg):
					match arg:
						case COR_Expressions.Dagger(argument1=arg1, argument2=arg2):
							match arg1:
								case COR_Expressions.EmptyRelation():
									match arg2:
										case COR_Expressions.Converse(argument=arg):
											match arg:
												case _:
													B = arg
													return COR_Expressions.Dagger(COR_Expressions.EmptyRelation(), COR_Expressions.Converse(B))
	# (((𝟎) † ((C)⁻))⁻)⁻ = (𝟎) † ((C)⁻)
	match expression:
		case COR_Expressions.Complement(argument=arg):
			match arg:
				case COR_Expressions.Complement(argument=arg):
					match arg:
						case COR_Expressions.Dagger(argument1=arg1, argument2=arg2):
							match arg1:
								case COR_Expressions.EmptyRelation():
									match arg2:
										case COR_Expressions.Complement(argument=arg):
											match arg:
												case _:
													C = arg
													return COR_Expressions.Dagger(COR_Expressions.EmptyRelation(), COR_Expressions.Complement(C))
	# (𝟏) ∘ ((T) ∘ ((B) ∘ ((A)⁻¹))) = (T) ∘ ((B) ∘ ((A)⁻¹))
	match expression:
		case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.IdentityRelation:
					match arg2:
						case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
							match arg1:
								case COR_Expressions.UniversalRelation():
									match arg2:
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
	# (((A) † ((A)⁻¹))⁻)⁻ = (A) † ((A)⁻¹)
	match expression:
		case COR_Expressions.Complement(argument=arg):
			match arg:
				case COR_Expressions.Complement(argument=arg):
					match arg:
						case COR_Expressions.Dagger(argument1=arg1, argument2=arg2):
							match arg1:
								case _:
									A = arg1
									match arg2:
										case COR_Expressions.Converse(argument=arg):
											match arg:
												case _:
													A = arg
													return COR_Expressions.Dagger(A, COR_Expressions.Converse(A))
	# (((𝟏) † ((B)⁻))⁻)⁻ = (𝟏) † ((B)⁻)
	match expression:
		case COR_Expressions.Complement(argument=arg):
			match arg:
				case COR_Expressions.Complement(argument=arg):
					match arg:
						case COR_Expressions.Dagger(argument1=arg1, argument2=arg2):
							match arg1:
								case COR_Expressions.IdentityRelation:
									match arg2:
										case COR_Expressions.Complement(argument=arg):
											match arg:
												case _:
													B = arg
													return COR_Expressions.Dagger(COR_Expressions.IdentityRelation(), COR_Expressions.Complement(B))
	# (𝟏) ∘ ((T) ∘ ((B) ∘ ((A)⁻))) = (T) ∘ ((B) ∘ ((A)⁻))
	match expression:
		case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.IdentityRelation:
					match arg2:
						case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
							match arg1:
								case COR_Expressions.UniversalRelation():
									match arg2:
										case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
											match arg1:
												case _:
													B = arg1
													match arg2:
														case COR_Expressions.Complement(argument=arg):
															match arg:
																case _:
																	A = arg
																	return COR_Expressions.Composition(COR_Expressions.UniversalRelation(), COR_Expressions.Composition(B, COR_Expressions.Complement(A)))
	# (A) ∪ ((𝟎) † ((A) ∪ ((𝟏)⁻))) = (A) † ((A) ∪ ((𝟏)⁻))
	match expression:
		case COR_Expressions.Union(argument1=arg1, argument2=arg2):
			match arg1:
				case _:
					A = arg1
					match arg2:
						case COR_Expressions.Dagger(argument1=arg1, argument2=arg2):
							match arg1:
								case COR_Expressions.EmptyRelation():
									match arg2:
										case COR_Expressions.Union(argument1=arg1, argument2=arg2):
											match arg1:
												case _:
													A = arg1
													match arg2:
														case COR_Expressions.Complement(argument=arg):
															match arg:
																case COR_Expressions.IdentityRelation:
																	return COR_Expressions.Dagger(A, COR_Expressions.Union(A, COR_Expressions.Complement(COR_Expressions.IdentityRelation())))
	# (𝟏) ∘ ((T) ∘ ((A) ∘ ((B)⁻))) = (T) ∘ ((A) ∘ ((B)⁻))
	match expression:
		case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.IdentityRelation:
					match arg2:
						case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
							match arg1:
								case COR_Expressions.UniversalRelation():
									match arg2:
										case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
											match arg1:
												case _:
													A = arg1
													match arg2:
														case COR_Expressions.Complement(argument=arg):
															match arg:
																case _:
																	B = arg
																	return COR_Expressions.Composition(COR_Expressions.UniversalRelation(), COR_Expressions.Composition(A, COR_Expressions.Complement(B)))
	# (((𝟎) † ((C)⁻¹))⁻)⁻ = (𝟎) † ((C)⁻¹)
	match expression:
		case COR_Expressions.Complement(argument=arg):
			match arg:
				case COR_Expressions.Complement(argument=arg):
					match arg:
						case COR_Expressions.Dagger(argument1=arg1, argument2=arg2):
							match arg1:
								case COR_Expressions.EmptyRelation():
									match arg2:
										case COR_Expressions.Converse(argument=arg):
											match arg:
												case _:
													C = arg
													return COR_Expressions.Dagger(COR_Expressions.EmptyRelation(), COR_Expressions.Converse(C))
	# ((A)⁻¹) ∘ ((𝟎) † ((A)⁻¹)) = (𝟎) † ((A)⁻¹)
	match expression:
		case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
			match arg1:
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
														case _:
															A = arg
															return COR_Expressions.Dagger(COR_Expressions.EmptyRelation(), COR_Expressions.Converse(A))
	# (((B) † ((A)⁻))⁻)⁻ = (B) † ((A)⁻)
	match expression:
		case COR_Expressions.Complement(argument=arg):
			match arg:
				case COR_Expressions.Complement(argument=arg):
					match arg:
						case COR_Expressions.Dagger(argument1=arg1, argument2=arg2):
							match arg1:
								case _:
									B = arg1
									match arg2:
										case COR_Expressions.Complement(argument=arg):
											match arg:
												case _:
													A = arg
													return COR_Expressions.Dagger(B, COR_Expressions.Complement(A))
	# (𝟏) ∘ ((T) ∘ ((C) † ((B)⁻))) = (T) ∘ ((C) † ((B)⁻))
	match expression:
		case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.IdentityRelation:
					match arg2:
						case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
							match arg1:
								case COR_Expressions.UniversalRelation():
									match arg2:
										case COR_Expressions.Dagger(argument1=arg1, argument2=arg2):
											match arg1:
												case _:
													C = arg1
													match arg2:
														case COR_Expressions.Complement(argument=arg):
															match arg:
																case _:
																	B = arg
																	return COR_Expressions.Composition(COR_Expressions.UniversalRelation(), COR_Expressions.Dagger(C, COR_Expressions.Complement(B)))
	# (A) ∪ ((𝟎) † ((B) ∪ ((𝟏)⁻))) = (A) † ((B) ∪ ((𝟏)⁻))
	match expression:
		case COR_Expressions.Union(argument1=arg1, argument2=arg2):
			match arg1:
				case _:
					A = arg1
					match arg2:
						case COR_Expressions.Dagger(argument1=arg1, argument2=arg2):
							match arg1:
								case COR_Expressions.EmptyRelation():
									match arg2:
										case COR_Expressions.Union(argument1=arg1, argument2=arg2):
											match arg1:
												case _:
													B = arg1
													match arg2:
														case COR_Expressions.Complement(argument=arg):
															match arg:
																case COR_Expressions.IdentityRelation:
																	return COR_Expressions.Dagger(A, COR_Expressions.Union(B, COR_Expressions.Complement(COR_Expressions.IdentityRelation())))
	# (𝟏) ∘ ((T) ∘ ((A) ∘ ((A)⁻))) = (T) ∘ ((A) ∘ ((A)⁻))
	match expression:
		case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.IdentityRelation:
					match arg2:
						case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
							match arg1:
								case COR_Expressions.UniversalRelation():
									match arg2:
										case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
											match arg1:
												case _:
													A = arg1
													match arg2:
														case COR_Expressions.Complement(argument=arg):
															match arg:
																case _:
																	A = arg
																	return COR_Expressions.Composition(COR_Expressions.UniversalRelation(), COR_Expressions.Composition(A, COR_Expressions.Complement(A)))
	# (((𝟏) † ((B)⁻¹))⁻)⁻ = (𝟏) † ((B)⁻¹)
	match expression:
		case COR_Expressions.Complement(argument=arg):
			match arg:
				case COR_Expressions.Complement(argument=arg):
					match arg:
						case COR_Expressions.Dagger(argument1=arg1, argument2=arg2):
							match arg1:
								case COR_Expressions.IdentityRelation:
									match arg2:
										case COR_Expressions.Converse(argument=arg):
											match arg:
												case _:
													B = arg
													return COR_Expressions.Dagger(COR_Expressions.IdentityRelation(), COR_Expressions.Converse(B))
	# (𝟏) ∘ ((T) ∘ ((A) ∘ ((C)⁻))) = (T) ∘ ((A) ∘ ((C)⁻))
	match expression:
		case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.IdentityRelation:
					match arg2:
						case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
							match arg1:
								case COR_Expressions.UniversalRelation():
									match arg2:
										case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
											match arg1:
												case _:
													A = arg1
													match arg2:
														case COR_Expressions.Complement(argument=arg):
															match arg:
																case _:
																	C = arg
																	return COR_Expressions.Composition(COR_Expressions.UniversalRelation(), COR_Expressions.Composition(A, COR_Expressions.Complement(C)))
	# (𝟏) ∘ ((T) ∘ ((A) ∘ ((𝟏)⁻))) = (T) ∘ ((A) ∘ ((𝟏)⁻))
	match expression:
		case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.IdentityRelation:
					match arg2:
						case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
							match arg1:
								case COR_Expressions.UniversalRelation():
									match arg2:
										case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
											match arg1:
												case _:
													A = arg1
													match arg2:
														case COR_Expressions.Complement(argument=arg):
															match arg:
																case COR_Expressions.IdentityRelation:
																	return COR_Expressions.Composition(COR_Expressions.UniversalRelation(), COR_Expressions.Composition(A, COR_Expressions.Complement(COR_Expressions.IdentityRelation())))
	# (𝟏) ∘ ((T) ∘ ((B) ∘ ((B)⁻))) = (T) ∘ ((B) ∘ ((B)⁻))
	match expression:
		case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.IdentityRelation:
					match arg2:
						case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
							match arg1:
								case COR_Expressions.UniversalRelation():
									match arg2:
										case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
											match arg1:
												case _:
													B = arg1
													match arg2:
														case COR_Expressions.Complement(argument=arg):
															match arg:
																case _:
																	B = arg
																	return COR_Expressions.Composition(COR_Expressions.UniversalRelation(), COR_Expressions.Composition(B, COR_Expressions.Complement(B)))
	# (((A) † ((A)⁻))⁻)⁻ = (A) † ((A)⁻)
	match expression:
		case COR_Expressions.Complement(argument=arg):
			match arg:
				case COR_Expressions.Complement(argument=arg):
					match arg:
						case COR_Expressions.Dagger(argument1=arg1, argument2=arg2):
							match arg1:
								case _:
									A = arg1
									match arg2:
										case COR_Expressions.Complement(argument=arg):
											match arg:
												case _:
													A = arg
													return COR_Expressions.Dagger(A, COR_Expressions.Complement(A))
	# (𝟏) ∘ ((T) ∘ ((B) ∘ ((𝟏)⁻))) = (T) ∘ ((B) ∘ ((𝟏)⁻))
	match expression:
		case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.IdentityRelation:
					match arg2:
						case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
							match arg1:
								case COR_Expressions.UniversalRelation():
									match arg2:
										case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
											match arg1:
												case _:
													B = arg1
													match arg2:
														case COR_Expressions.Complement(argument=arg):
															match arg:
																case COR_Expressions.IdentityRelation:
																	return COR_Expressions.Composition(COR_Expressions.UniversalRelation(), COR_Expressions.Composition(B, COR_Expressions.Complement(COR_Expressions.IdentityRelation())))
	# (((A) † ((C)⁻))⁻)⁻ = (A) † ((C)⁻)
	match expression:
		case COR_Expressions.Complement(argument=arg):
			match arg:
				case COR_Expressions.Complement(argument=arg):
					match arg:
						case COR_Expressions.Dagger(argument1=arg1, argument2=arg2):
							match arg1:
								case _:
									A = arg1
									match arg2:
										case COR_Expressions.Complement(argument=arg):
											match arg:
												case _:
													C = arg
													return COR_Expressions.Dagger(A, COR_Expressions.Complement(C))
	# (𝟏) ∘ ((T) ∘ ((C) ∘ ((A)⁻))) = (T) ∘ ((C) ∘ ((A)⁻))
	match expression:
		case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.IdentityRelation:
					match arg2:
						case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
							match arg1:
								case COR_Expressions.UniversalRelation():
									match arg2:
										case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
											match arg1:
												case _:
													C = arg1
													match arg2:
														case COR_Expressions.Complement(argument=arg):
															match arg:
																case _:
																	A = arg
																	return COR_Expressions.Composition(COR_Expressions.UniversalRelation(), COR_Expressions.Composition(C, COR_Expressions.Complement(A)))
	# (𝟏) ∘ ((T) ∘ ((A) ∘ ((C)⁻¹))) = (T) ∘ ((A) ∘ ((C)⁻¹))
	match expression:
		case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.IdentityRelation:
					match arg2:
						case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
							match arg1:
								case COR_Expressions.UniversalRelation():
									match arg2:
										case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
											match arg1:
												case _:
													A = arg1
													match arg2:
														case COR_Expressions.Converse(argument=arg):
															match arg:
																case _:
																	C = arg
																	return COR_Expressions.Composition(COR_Expressions.UniversalRelation(), COR_Expressions.Composition(A, COR_Expressions.Converse(C)))
	# (𝟏) ∘ ((T) ∘ ((C) † ((C)⁻¹))) = (T) ∘ ((C) † ((C)⁻¹))
	match expression:
		case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.IdentityRelation:
					match arg2:
						case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
							match arg1:
								case COR_Expressions.UniversalRelation():
									match arg2:
										case COR_Expressions.Dagger(argument1=arg1, argument2=arg2):
											match arg1:
												case _:
													C = arg1
													match arg2:
														case COR_Expressions.Converse(argument=arg):
															match arg:
																case _:
																	C = arg
																	return COR_Expressions.Composition(COR_Expressions.UniversalRelation(), COR_Expressions.Dagger(C, COR_Expressions.Converse(C)))
	# (((B) † ((A)⁻¹))⁻)⁻ = (B) † ((A)⁻¹)
	match expression:
		case COR_Expressions.Complement(argument=arg):
			match arg:
				case COR_Expressions.Complement(argument=arg):
					match arg:
						case COR_Expressions.Dagger(argument1=arg1, argument2=arg2):
							match arg1:
								case _:
									B = arg1
									match arg2:
										case COR_Expressions.Converse(argument=arg):
											match arg:
												case _:
													A = arg
													return COR_Expressions.Dagger(B, COR_Expressions.Converse(A))
	# (((𝟎) † ((A)⁻))⁻)⁻ = (𝟎) † ((A)⁻)
	match expression:
		case COR_Expressions.Complement(argument=arg):
			match arg:
				case COR_Expressions.Complement(argument=arg):
					match arg:
						case COR_Expressions.Dagger(argument1=arg1, argument2=arg2):
							match arg1:
								case COR_Expressions.EmptyRelation():
									match arg2:
										case COR_Expressions.Complement(argument=arg):
											match arg:
												case _:
													A = arg
													return COR_Expressions.Dagger(COR_Expressions.EmptyRelation(), COR_Expressions.Complement(A))
	# (((A) † ((C)⁻¹))⁻)⁻ = (A) † ((C)⁻¹)
	match expression:
		case COR_Expressions.Complement(argument=arg):
			match arg:
				case COR_Expressions.Complement(argument=arg):
					match arg:
						case COR_Expressions.Dagger(argument1=arg1, argument2=arg2):
							match arg1:
								case _:
									A = arg1
									match arg2:
										case COR_Expressions.Converse(argument=arg):
											match arg:
												case _:
													C = arg
													return COR_Expressions.Dagger(A, COR_Expressions.Converse(C))
	# (((A) † ((B)⁻))⁻)⁻ = (A) † ((B)⁻)
	match expression:
		case COR_Expressions.Complement(argument=arg):
			match arg:
				case COR_Expressions.Complement(argument=arg):
					match arg:
						case COR_Expressions.Dagger(argument1=arg1, argument2=arg2):
							match arg1:
								case _:
									A = arg1
									match arg2:
										case COR_Expressions.Complement(argument=arg):
											match arg:
												case _:
													B = arg
													return COR_Expressions.Dagger(A, COR_Expressions.Complement(B))
	# (𝟏) ∘ ((T) ∘ ((C) † ((C)⁻))) = (T) ∘ ((C) † ((C)⁻))
	match expression:
		case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.IdentityRelation:
					match arg2:
						case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
							match arg1:
								case COR_Expressions.UniversalRelation():
									match arg2:
										case COR_Expressions.Dagger(argument1=arg1, argument2=arg2):
											match arg1:
												case _:
													C = arg1
													match arg2:
														case COR_Expressions.Complement(argument=arg):
															match arg:
																case _:
																	C = arg
																	return COR_Expressions.Composition(COR_Expressions.UniversalRelation(), COR_Expressions.Dagger(C, COR_Expressions.Complement(C)))
	# (((𝟎) † ((B)⁻))⁻)⁻ = (𝟎) † ((B)⁻)
	match expression:
		case COR_Expressions.Complement(argument=arg):
			match arg:
				case COR_Expressions.Complement(argument=arg):
					match arg:
						case COR_Expressions.Dagger(argument1=arg1, argument2=arg2):
							match arg1:
								case COR_Expressions.EmptyRelation():
									match arg2:
										case COR_Expressions.Complement(argument=arg):
											match arg:
												case _:
													B = arg
													return COR_Expressions.Dagger(COR_Expressions.EmptyRelation(), COR_Expressions.Complement(B))
	# (𝟏) ∘ ((T) ∘ ((B) ∘ ((C)⁻))) = (T) ∘ ((B) ∘ ((C)⁻))
	match expression:
		case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.IdentityRelation:
					match arg2:
						case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
							match arg1:
								case COR_Expressions.UniversalRelation():
									match arg2:
										case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
											match arg1:
												case _:
													B = arg1
													match arg2:
														case COR_Expressions.Complement(argument=arg):
															match arg:
																case _:
																	C = arg
																	return COR_Expressions.Composition(COR_Expressions.UniversalRelation(), COR_Expressions.Composition(B, COR_Expressions.Complement(C)))
	# (((𝟏) † ((C)⁻))⁻)⁻ = (𝟏) † ((C)⁻)
	match expression:
		case COR_Expressions.Complement(argument=arg):
			match arg:
				case COR_Expressions.Complement(argument=arg):
					match arg:
						case COR_Expressions.Dagger(argument1=arg1, argument2=arg2):
							match arg1:
								case COR_Expressions.IdentityRelation:
									match arg2:
										case COR_Expressions.Complement(argument=arg):
											match arg:
												case _:
													C = arg
													return COR_Expressions.Dagger(COR_Expressions.IdentityRelation(), COR_Expressions.Complement(C))
	# (𝟏) ∘ ((T) ∘ ((C) ∘ ((𝟏)⁻))) = (T) ∘ ((C) ∘ ((𝟏)⁻))
	match expression:
		case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.IdentityRelation:
					match arg2:
						case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
							match arg1:
								case COR_Expressions.UniversalRelation():
									match arg2:
										case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
											match arg1:
												case _:
													C = arg1
													match arg2:
														case COR_Expressions.Complement(argument=arg):
															match arg:
																case COR_Expressions.IdentityRelation:
																	return COR_Expressions.Composition(COR_Expressions.UniversalRelation(), COR_Expressions.Composition(C, COR_Expressions.Complement(COR_Expressions.IdentityRelation())))
	# (𝟏) ∘ ((T) ∘ ((C) ∘ ((B)⁻))) = (T) ∘ ((C) ∘ ((B)⁻))
	match expression:
		case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.IdentityRelation:
					match arg2:
						case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
							match arg1:
								case COR_Expressions.UniversalRelation():
									match arg2:
										case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
											match arg1:
												case _:
													C = arg1
													match arg2:
														case COR_Expressions.Complement(argument=arg):
															match arg:
																case _:
																	B = arg
																	return COR_Expressions.Composition(COR_Expressions.UniversalRelation(), COR_Expressions.Composition(C, COR_Expressions.Complement(B)))
	# (𝟏) ∘ ((T) ∘ ((C) † ((A)⁻¹))) = (T) ∘ ((C) † ((A)⁻¹))
	match expression:
		case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.IdentityRelation:
					match arg2:
						case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
							match arg1:
								case COR_Expressions.UniversalRelation():
									match arg2:
										case COR_Expressions.Dagger(argument1=arg1, argument2=arg2):
											match arg1:
												case _:
													C = arg1
													match arg2:
														case COR_Expressions.Converse(argument=arg):
															match arg:
																case _:
																	A = arg
																	return COR_Expressions.Composition(COR_Expressions.UniversalRelation(), COR_Expressions.Dagger(C, COR_Expressions.Converse(A)))
	# (((𝟎) † ((A)⁻¹))⁻)⁻ = (𝟎) † ((A)⁻¹)
	match expression:
		case COR_Expressions.Complement(argument=arg):
			match arg:
				case COR_Expressions.Complement(argument=arg):
					match arg:
						case COR_Expressions.Dagger(argument1=arg1, argument2=arg2):
							match arg1:
								case COR_Expressions.EmptyRelation():
									match arg2:
										case COR_Expressions.Converse(argument=arg):
											match arg:
												case _:
													A = arg
													return COR_Expressions.Dagger(COR_Expressions.EmptyRelation(), COR_Expressions.Converse(A))
	# (𝟏) ∘ ((T) ∘ ((A) ∘ ((B)⁻¹))) = (T) ∘ ((A) ∘ ((B)⁻¹))
	match expression:
		case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.IdentityRelation:
					match arg2:
						case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
							match arg1:
								case COR_Expressions.UniversalRelation():
									match arg2:
										case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
											match arg1:
												case _:
													A = arg1
													match arg2:
														case COR_Expressions.Converse(argument=arg):
															match arg:
																case _:
																	B = arg
																	return COR_Expressions.Composition(COR_Expressions.UniversalRelation(), COR_Expressions.Composition(A, COR_Expressions.Converse(B)))
	# (((𝟏) † ((A)⁻¹))⁻)⁻ = (𝟏) † ((A)⁻¹)
	match expression:
		case COR_Expressions.Complement(argument=arg):
			match arg:
				case COR_Expressions.Complement(argument=arg):
					match arg:
						case COR_Expressions.Dagger(argument1=arg1, argument2=arg2):
							match arg1:
								case COR_Expressions.IdentityRelation:
									match arg2:
										case COR_Expressions.Converse(argument=arg):
											match arg:
												case _:
													A = arg
													return COR_Expressions.Dagger(COR_Expressions.IdentityRelation(), COR_Expressions.Converse(A))
	# (((B) † ((C)⁻))⁻)⁻ = (B) † ((C)⁻)
	match expression:
		case COR_Expressions.Complement(argument=arg):
			match arg:
				case COR_Expressions.Complement(argument=arg):
					match arg:
						case COR_Expressions.Dagger(argument1=arg1, argument2=arg2):
							match arg1:
								case _:
									B = arg1
									match arg2:
										case COR_Expressions.Complement(argument=arg):
											match arg:
												case _:
													C = arg
													return COR_Expressions.Dagger(B, COR_Expressions.Complement(C))
	# (((B) † ((B)⁻))⁻)⁻ = (B) † ((B)⁻)
	match expression:
		case COR_Expressions.Complement(argument=arg):
			match arg:
				case COR_Expressions.Complement(argument=arg):
					match arg:
						case COR_Expressions.Dagger(argument1=arg1, argument2=arg2):
							match arg1:
								case _:
									B = arg1
									match arg2:
										case COR_Expressions.Complement(argument=arg):
											match arg:
												case _:
													B = arg
													return COR_Expressions.Dagger(B, COR_Expressions.Complement(B))
	# (((𝟏) † ((C)⁻¹))⁻)⁻ = (𝟏) † ((C)⁻¹)
	match expression:
		case COR_Expressions.Complement(argument=arg):
			match arg:
				case COR_Expressions.Complement(argument=arg):
					match arg:
						case COR_Expressions.Dagger(argument1=arg1, argument2=arg2):
							match arg1:
								case COR_Expressions.IdentityRelation:
									match arg2:
										case COR_Expressions.Converse(argument=arg):
											match arg:
												case _:
													C = arg
													return COR_Expressions.Dagger(COR_Expressions.IdentityRelation(), COR_Expressions.Converse(C))
	# (𝟏) ∘ ((T) ∘ ((B) ∘ ((C)⁻¹))) = (T) ∘ ((B) ∘ ((C)⁻¹))
	match expression:
		case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.IdentityRelation:
					match arg2:
						case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
							match arg1:
								case COR_Expressions.UniversalRelation():
									match arg2:
										case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
											match arg1:
												case _:
													B = arg1
													match arg2:
														case COR_Expressions.Converse(argument=arg):
															match arg:
																case _:
																	C = arg
																	return COR_Expressions.Composition(COR_Expressions.UniversalRelation(), COR_Expressions.Composition(B, COR_Expressions.Converse(C)))
	# (((𝟏) † ((A)⁻))⁻)⁻ = (𝟏) † ((A)⁻)
	match expression:
		case COR_Expressions.Complement(argument=arg):
			match arg:
				case COR_Expressions.Complement(argument=arg):
					match arg:
						case COR_Expressions.Dagger(argument1=arg1, argument2=arg2):
							match arg1:
								case COR_Expressions.IdentityRelation:
									match arg2:
										case COR_Expressions.Complement(argument=arg):
											match arg:
												case _:
													A = arg
													return COR_Expressions.Dagger(COR_Expressions.IdentityRelation(), COR_Expressions.Complement(A))
	# (𝟎) ∪ (C) = C
	match expression:
		case COR_Expressions.Union(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.EmptyRelation():
					match arg2:
						case _:
							C = arg2
							return C
	# (𝟏) ∘ (T) = T
	match expression:
		case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.IdentityRelation:
					match arg2:
						case COR_Expressions.UniversalRelation():
							return COR_Expressions.UniversalRelation()
	# (𝟏) ∪ (T) = T
	match expression:
		case COR_Expressions.Union(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.IdentityRelation:
					match arg2:
						case COR_Expressions.UniversalRelation():
							return COR_Expressions.UniversalRelation()
	# (𝟏) ∘ (B) = B
	match expression:
		case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.IdentityRelation:
					match arg2:
						case _:
							B = arg2
							return B
	# (T) ∪ (𝟏) = T
	match expression:
		case COR_Expressions.Union(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.UniversalRelation():
					match arg2:
						case COR_Expressions.IdentityRelation:
							return COR_Expressions.UniversalRelation()
	# (B) ∘ (𝟏) = B
	match expression:
		case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
			match arg1:
				case _:
					B = arg1
					match arg2:
						case COR_Expressions.IdentityRelation:
							return B
	# (𝟏) ∪ (𝟎) = 𝟏
	match expression:
		case COR_Expressions.Union(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.IdentityRelation:
					match arg2:
						case COR_Expressions.EmptyRelation():
							return COR_Expressions.IdentityRelation()
	# (𝟎) † (T) = T
	match expression:
		case COR_Expressions.Dagger(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.EmptyRelation():
					match arg2:
						case COR_Expressions.UniversalRelation():
							return COR_Expressions.UniversalRelation()
	# (T) ∘ (𝟏) = T
	match expression:
		case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.UniversalRelation():
					match arg2:
						case COR_Expressions.IdentityRelation:
							return COR_Expressions.UniversalRelation()
	# (A) † (T) = T
	match expression:
		case COR_Expressions.Dagger(argument1=arg1, argument2=arg2):
			match arg1:
				case _:
					A = arg1
					match arg2:
						case COR_Expressions.UniversalRelation():
							return COR_Expressions.UniversalRelation()
	# (A) ∘ (𝟎) = 𝟎
	match expression:
		case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
			match arg1:
				case _:
					A = arg1
					match arg2:
						case COR_Expressions.EmptyRelation():
							return COR_Expressions.EmptyRelation()
	# (𝟏) ∘ (C) = C
	match expression:
		case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.IdentityRelation:
					match arg2:
						case _:
							C = arg2
							return C
	# (T) ∘ (T) = T
	match expression:
		case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.UniversalRelation():
					match arg2:
						case COR_Expressions.UniversalRelation():
							return COR_Expressions.UniversalRelation()
	# (𝟎) ∪ (𝟏) = 𝟏
	match expression:
		case COR_Expressions.Union(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.EmptyRelation():
					match arg2:
						case COR_Expressions.IdentityRelation:
							return COR_Expressions.IdentityRelation()
	# (T) ∪ (C) = T
	match expression:
		case COR_Expressions.Union(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.UniversalRelation():
					match arg2:
						case _:
							C = arg2
							return COR_Expressions.UniversalRelation()
	# (𝟏) ∘ (𝟎) = 𝟎
	match expression:
		case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.IdentityRelation:
					match arg2:
						case COR_Expressions.EmptyRelation():
							return COR_Expressions.EmptyRelation()
	# (T) † (𝟎) = T
	match expression:
		case COR_Expressions.Dagger(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.UniversalRelation():
					match arg2:
						case COR_Expressions.EmptyRelation():
							return COR_Expressions.UniversalRelation()
	# (B) ∘ (𝟎) = 𝟎
	match expression:
		case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
			match arg1:
				case _:
					B = arg1
					match arg2:
						case COR_Expressions.EmptyRelation():
							return COR_Expressions.EmptyRelation()
	# (T) ∪ (T) = T
	match expression:
		case COR_Expressions.Union(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.UniversalRelation():
					match arg2:
						case COR_Expressions.UniversalRelation():
							return COR_Expressions.UniversalRelation()
	# (𝟎) ∘ (B) = 𝟎
	match expression:
		case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.EmptyRelation():
					match arg2:
						case _:
							B = arg2
							return COR_Expressions.EmptyRelation()
	# (𝟏) ∪ (𝟏) = 𝟏
	match expression:
		case COR_Expressions.Union(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.IdentityRelation:
					match arg2:
						case COR_Expressions.IdentityRelation:
							return COR_Expressions.IdentityRelation()
	# (C) ∪ (T) = T
	match expression:
		case COR_Expressions.Union(argument1=arg1, argument2=arg2):
			match arg1:
				case _:
					C = arg1
					match arg2:
						case COR_Expressions.UniversalRelation():
							return COR_Expressions.UniversalRelation()
	# (T) ∘ (𝟎) = 𝟎
	match expression:
		case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.UniversalRelation():
					match arg2:
						case COR_Expressions.EmptyRelation():
							return COR_Expressions.EmptyRelation()
	# (B) † (T) = T
	match expression:
		case COR_Expressions.Dagger(argument1=arg1, argument2=arg2):
			match arg1:
				case _:
					B = arg1
					match arg2:
						case COR_Expressions.UniversalRelation():
							return COR_Expressions.UniversalRelation()
	# (A) ∪ (A) = A
	match expression:
		case COR_Expressions.Union(argument1=arg1, argument2=arg2):
			match arg1:
				case _:
					A = arg1
					match arg2:
						case _:
							A = arg2
							return A
	# (B) ∪ (𝟎) = B
	match expression:
		case COR_Expressions.Union(argument1=arg1, argument2=arg2):
			match arg1:
				case _:
					B = arg1
					match arg2:
						case COR_Expressions.EmptyRelation():
							return B
	# (A) ∪ (T) = T
	match expression:
		case COR_Expressions.Union(argument1=arg1, argument2=arg2):
			match arg1:
				case _:
					A = arg1
					match arg2:
						case COR_Expressions.UniversalRelation():
							return COR_Expressions.UniversalRelation()
	# (𝟎) ∘ (C) = 𝟎
	match expression:
		case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.EmptyRelation():
					match arg2:
						case _:
							C = arg2
							return COR_Expressions.EmptyRelation()
	# (T) † (𝟏) = T
	match expression:
		case COR_Expressions.Dagger(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.UniversalRelation():
					match arg2:
						case COR_Expressions.IdentityRelation:
							return COR_Expressions.UniversalRelation()
	# (T) ∪ (B) = T
	match expression:
		case COR_Expressions.Union(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.UniversalRelation():
					match arg2:
						case _:
							B = arg2
							return COR_Expressions.UniversalRelation()
	# (T) † (C) = T
	match expression:
		case COR_Expressions.Dagger(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.UniversalRelation():
					match arg2:
						case _:
							C = arg2
							return COR_Expressions.UniversalRelation()
	# (𝟎) ∪ (𝟎) = 𝟎
	match expression:
		case COR_Expressions.Union(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.EmptyRelation():
					match arg2:
						case COR_Expressions.EmptyRelation():
							return COR_Expressions.EmptyRelation()
	# (𝟎) ∘ (A) = 𝟎
	match expression:
		case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.EmptyRelation():
					match arg2:
						case _:
							A = arg2
							return COR_Expressions.EmptyRelation()
	# (𝟏) ∘ (A) = A
	match expression:
		case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.IdentityRelation:
					match arg2:
						case _:
							A = arg2
							return A
	# (A) ∘ (𝟏) = A
	match expression:
		case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
			match arg1:
				case _:
					A = arg1
					match arg2:
						case COR_Expressions.IdentityRelation:
							return A
	# (𝟎) ∪ (A) = A
	match expression:
		case COR_Expressions.Union(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.EmptyRelation():
					match arg2:
						case _:
							A = arg2
							return A
	# (𝟏) † (T) = T
	match expression:
		case COR_Expressions.Dagger(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.IdentityRelation:
					match arg2:
						case COR_Expressions.UniversalRelation():
							return COR_Expressions.UniversalRelation()
	# (B) ∪ (B) = B
	match expression:
		case COR_Expressions.Union(argument1=arg1, argument2=arg2):
			match arg1:
				case _:
					B = arg1
					match arg2:
						case _:
							B = arg2
							return B
	# (T) † (T) = T
	match expression:
		case COR_Expressions.Dagger(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.UniversalRelation():
					match arg2:
						case COR_Expressions.UniversalRelation():
							return COR_Expressions.UniversalRelation()
	# (𝟏) ∘ (𝟏) = 𝟏
	match expression:
		case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.IdentityRelation:
					match arg2:
						case COR_Expressions.IdentityRelation:
							return COR_Expressions.IdentityRelation()
	# (𝟎) ∘ (𝟎) = 𝟎
	match expression:
		case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.EmptyRelation():
					match arg2:
						case COR_Expressions.EmptyRelation():
							return COR_Expressions.EmptyRelation()
	# (B) ∪ (T) = T
	match expression:
		case COR_Expressions.Union(argument1=arg1, argument2=arg2):
			match arg1:
				case _:
					B = arg1
					match arg2:
						case COR_Expressions.UniversalRelation():
							return COR_Expressions.UniversalRelation()
	# (C) ∘ (𝟏) = C
	match expression:
		case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
			match arg1:
				case _:
					C = arg1
					match arg2:
						case COR_Expressions.IdentityRelation:
							return C
	# (𝟎) ∪ (B) = B
	match expression:
		case COR_Expressions.Union(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.EmptyRelation():
					match arg2:
						case _:
							B = arg2
							return B
	# (C) † (T) = T
	match expression:
		case COR_Expressions.Dagger(argument1=arg1, argument2=arg2):
			match arg1:
				case _:
					C = arg1
					match arg2:
						case COR_Expressions.UniversalRelation():
							return COR_Expressions.UniversalRelation()
	# (𝟎) ∘ (T) = 𝟎
	match expression:
		case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.EmptyRelation():
					match arg2:
						case COR_Expressions.UniversalRelation():
							return COR_Expressions.EmptyRelation()
	# (𝟎) ∪ (T) = T
	match expression:
		case COR_Expressions.Union(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.EmptyRelation():
					match arg2:
						case COR_Expressions.UniversalRelation():
							return COR_Expressions.UniversalRelation()
	# (C) ∘ (𝟎) = 𝟎
	match expression:
		case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
			match arg1:
				case _:
					C = arg1
					match arg2:
						case COR_Expressions.EmptyRelation():
							return COR_Expressions.EmptyRelation()
	# (T) ∪ (𝟎) = T
	match expression:
		case COR_Expressions.Union(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.UniversalRelation():
					match arg2:
						case COR_Expressions.EmptyRelation():
							return COR_Expressions.UniversalRelation()
	# (T) † (A) = T
	match expression:
		case COR_Expressions.Dagger(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.UniversalRelation():
					match arg2:
						case _:
							A = arg2
							return COR_Expressions.UniversalRelation()
	# (T) ∪ (A) = T
	match expression:
		case COR_Expressions.Union(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.UniversalRelation():
					match arg2:
						case _:
							A = arg2
							return COR_Expressions.UniversalRelation()
	# (C) ∪ (C) = C
	match expression:
		case COR_Expressions.Union(argument1=arg1, argument2=arg2):
			match arg1:
				case _:
					C = arg1
					match arg2:
						case _:
							C = arg2
							return C
	# (A) ∪ (𝟎) = A
	match expression:
		case COR_Expressions.Union(argument1=arg1, argument2=arg2):
			match arg1:
				case _:
					A = arg1
					match arg2:
						case COR_Expressions.EmptyRelation():
							return A
	# (𝟎) † (𝟎) = 𝟎
	match expression:
		case COR_Expressions.Dagger(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.EmptyRelation():
					match arg2:
						case COR_Expressions.EmptyRelation():
							return COR_Expressions.EmptyRelation()
	# (T) † (B) = T
	match expression:
		case COR_Expressions.Dagger(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.UniversalRelation():
					match arg2:
						case _:
							B = arg2
							return COR_Expressions.UniversalRelation()
	# (𝟎) ∘ (𝟏) = 𝟎
	match expression:
		case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.EmptyRelation():
					match arg2:
						case COR_Expressions.IdentityRelation:
							return COR_Expressions.EmptyRelation()
	# (C) ∪ (𝟎) = C
	match expression:
		case COR_Expressions.Union(argument1=arg1, argument2=arg2):
			match arg1:
				case _:
					C = arg1
					match arg2:
						case COR_Expressions.EmptyRelation():
							return C
	# (T) ∩ (𝟎) = 𝟎
	match expression:
		case COR_Expressions.Intersection(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.UniversalRelation():
					match arg2:
						case COR_Expressions.EmptyRelation():
							return COR_Expressions.EmptyRelation()
	# (𝟏) ∩ (𝟏) = 𝟏
	match expression:
		case COR_Expressions.Intersection(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.IdentityRelation:
					match arg2:
						case COR_Expressions.IdentityRelation:
							return COR_Expressions.IdentityRelation()
	# (𝟎) ∩ (T) = 𝟎
	match expression:
		case COR_Expressions.Intersection(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.EmptyRelation():
					match arg2:
						case COR_Expressions.UniversalRelation():
							return COR_Expressions.EmptyRelation()
	# (𝟎) ∩ (B) = 𝟎
	match expression:
		case COR_Expressions.Intersection(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.EmptyRelation():
					match arg2:
						case _:
							B = arg2
							return COR_Expressions.EmptyRelation()
	# (𝟎) ∩ (𝟎) = 𝟎
	match expression:
		case COR_Expressions.Intersection(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.EmptyRelation():
					match arg2:
						case COR_Expressions.EmptyRelation():
							return COR_Expressions.EmptyRelation()
	# (C) ∩ (𝟎) = 𝟎
	match expression:
		case COR_Expressions.Intersection(argument1=arg1, argument2=arg2):
			match arg1:
				case _:
					C = arg1
					match arg2:
						case COR_Expressions.EmptyRelation():
							return COR_Expressions.EmptyRelation()
	# (T) ∩ (𝟏) = 𝟏
	match expression:
		case COR_Expressions.Intersection(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.UniversalRelation():
					match arg2:
						case COR_Expressions.IdentityRelation:
							return COR_Expressions.IdentityRelation()
	# (C) ∩ (C) = C
	match expression:
		case COR_Expressions.Intersection(argument1=arg1, argument2=arg2):
			match arg1:
				case _:
					C = arg1
					match arg2:
						case _:
							C = arg2
							return C
	# (T) ∩ (A) = A
	match expression:
		case COR_Expressions.Intersection(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.UniversalRelation():
					match arg2:
						case _:
							A = arg2
							return A
	# (A) ∩ (A) = A
	match expression:
		case COR_Expressions.Intersection(argument1=arg1, argument2=arg2):
			match arg1:
				case _:
					A = arg1
					match arg2:
						case _:
							A = arg2
							return A
	# (B) ∩ (𝟎) = 𝟎
	match expression:
		case COR_Expressions.Intersection(argument1=arg1, argument2=arg2):
			match arg1:
				case _:
					B = arg1
					match arg2:
						case COR_Expressions.EmptyRelation():
							return COR_Expressions.EmptyRelation()
	# (A) ∩ (𝟎) = 𝟎
	match expression:
		case COR_Expressions.Intersection(argument1=arg1, argument2=arg2):
			match arg1:
				case _:
					A = arg1
					match arg2:
						case COR_Expressions.EmptyRelation():
							return COR_Expressions.EmptyRelation()
	# (B) ∩ (T) = B
	match expression:
		case COR_Expressions.Intersection(argument1=arg1, argument2=arg2):
			match arg1:
				case _:
					B = arg1
					match arg2:
						case COR_Expressions.UniversalRelation():
							return B
	# (𝟎) ∩ (𝟏) = 𝟎
	match expression:
		case COR_Expressions.Intersection(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.EmptyRelation():
					match arg2:
						case COR_Expressions.IdentityRelation:
							return COR_Expressions.EmptyRelation()
	# (𝟏) ∩ (𝟎) = 𝟎
	match expression:
		case COR_Expressions.Intersection(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.IdentityRelation:
					match arg2:
						case COR_Expressions.EmptyRelation():
							return COR_Expressions.EmptyRelation()
	# (𝟏) ∩ (T) = 𝟏
	match expression:
		case COR_Expressions.Intersection(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.IdentityRelation:
					match arg2:
						case COR_Expressions.UniversalRelation():
							return COR_Expressions.IdentityRelation()
	# (A) ∩ (T) = A
	match expression:
		case COR_Expressions.Intersection(argument1=arg1, argument2=arg2):
			match arg1:
				case _:
					A = arg1
					match arg2:
						case COR_Expressions.UniversalRelation():
							return A
	# (T) ∩ (T) = T
	match expression:
		case COR_Expressions.Intersection(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.UniversalRelation():
					match arg2:
						case COR_Expressions.UniversalRelation():
							return COR_Expressions.UniversalRelation()
	# (𝟎) ∩ (A) = 𝟎
	match expression:
		case COR_Expressions.Intersection(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.EmptyRelation():
					match arg2:
						case _:
							A = arg2
							return COR_Expressions.EmptyRelation()
	# (T) ∩ (B) = B
	match expression:
		case COR_Expressions.Intersection(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.UniversalRelation():
					match arg2:
						case _:
							B = arg2
							return B
	# (𝟎) ∩ (C) = 𝟎
	match expression:
		case COR_Expressions.Intersection(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.EmptyRelation():
					match arg2:
						case _:
							C = arg2
							return COR_Expressions.EmptyRelation()
	# (T) ∩ (C) = C
	match expression:
		case COR_Expressions.Intersection(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.UniversalRelation():
					match arg2:
						case _:
							C = arg2
							return C
	# (B) ∩ (B) = B
	match expression:
		case COR_Expressions.Intersection(argument1=arg1, argument2=arg2):
			match arg1:
				case _:
					B = arg1
					match arg2:
						case _:
							B = arg2
							return B
	# (C) ∩ (T) = C
	match expression:
		case COR_Expressions.Intersection(argument1=arg1, argument2=arg2):
			match arg1:
				case _:
					C = arg1
					match arg2:
						case COR_Expressions.UniversalRelation():
							return C
	# ((C)⁻) ∩ (C) = 𝟎
	match expression:
		case COR_Expressions.Intersection(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.Complement(argument=arg):
					match arg:
						case _:
							C = arg
							match arg2:
								case _:
									C = arg2
									return COR_Expressions.EmptyRelation()
	# ((𝟏) ∩ (C))⁻¹ = (C) ∩ (𝟏)
	match expression:
		case COR_Expressions.Converse(argument=arg):
			match arg:
				case COR_Expressions.Intersection(argument1=arg1, argument2=arg2):
					match arg1:
						case COR_Expressions.IdentityRelation:
							match arg2:
								case _:
									C = arg2
									return COR_Expressions.Intersection(C, COR_Expressions.IdentityRelation())
	# ((𝟏) † (𝟎))⁻¹ = (𝟎) † (𝟏)
	match expression:
		case COR_Expressions.Converse(argument=arg):
			match arg:
				case COR_Expressions.Dagger(argument1=arg1, argument2=arg2):
					match arg1:
						case COR_Expressions.IdentityRelation:
							match arg2:
								case COR_Expressions.EmptyRelation():
									return COR_Expressions.Dagger(COR_Expressions.EmptyRelation(), COR_Expressions.IdentityRelation())
	# ((A) ∩ (𝟏))⁻¹ = (𝟏) ∩ (A)
	match expression:
		case COR_Expressions.Converse(argument=arg):
			match arg:
				case COR_Expressions.Intersection(argument1=arg1, argument2=arg2):
					match arg1:
						case _:
							A = arg1
							match arg2:
								case COR_Expressions.IdentityRelation:
									return COR_Expressions.Intersection(COR_Expressions.IdentityRelation(), A)
	# ((C)⁻¹) † (T) = T
	match expression:
		case COR_Expressions.Dagger(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.Converse(argument=arg):
					match arg:
						case _:
							C = arg
							match arg2:
								case COR_Expressions.UniversalRelation():
									return COR_Expressions.UniversalRelation()
	# (𝟎) ∩ ((C)⁻) = 𝟎
	match expression:
		case COR_Expressions.Intersection(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.EmptyRelation():
					match arg2:
						case COR_Expressions.Complement(argument=arg):
							match arg:
								case _:
									C = arg
									return COR_Expressions.EmptyRelation()
	# ((B)⁻) † (T) = T
	match expression:
		case COR_Expressions.Dagger(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.Complement(argument=arg):
					match arg:
						case _:
							B = arg
							match arg2:
								case COR_Expressions.UniversalRelation():
									return COR_Expressions.UniversalRelation()
	# (T) ∩ ((B)⁻¹) = (B)⁻¹
	match expression:
		case COR_Expressions.Intersection(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.UniversalRelation():
					match arg2:
						case COR_Expressions.Converse(argument=arg):
							match arg:
								case _:
									B = arg
									return COR_Expressions.Converse(B)
	# ((C)⁻) ∪ (𝟎) = (C)⁻
	match expression:
		case COR_Expressions.Union(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.Complement(argument=arg):
					match arg:
						case _:
							C = arg
							match arg2:
								case COR_Expressions.EmptyRelation():
									return COR_Expressions.Complement(C)
	# (𝟎) ∩ ((A)⁻¹) = 𝟎
	match expression:
		case COR_Expressions.Intersection(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.EmptyRelation():
					match arg2:
						case COR_Expressions.Converse(argument=arg):
							match arg:
								case _:
									A = arg
									return COR_Expressions.EmptyRelation()
	# ((𝟏) † (𝟏))⁻¹ = (𝟏) † (𝟏)
	match expression:
		case COR_Expressions.Converse(argument=arg):
			match arg:
				case COR_Expressions.Dagger(argument1=arg1, argument2=arg2):
					match arg1:
						case COR_Expressions.IdentityRelation:
							match arg2:
								case COR_Expressions.IdentityRelation:
									return COR_Expressions.Dagger(COR_Expressions.IdentityRelation(), COR_Expressions.IdentityRelation())
	# ((B)⁻¹) ∪ (T) = T
	match expression:
		case COR_Expressions.Union(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.Converse(argument=arg):
					match arg:
						case _:
							B = arg
							match arg2:
								case COR_Expressions.UniversalRelation():
									return COR_Expressions.UniversalRelation()
	# ((𝟏)⁻) † (T) = T
	match expression:
		case COR_Expressions.Dagger(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.Complement(argument=arg):
					match arg:
						case COR_Expressions.IdentityRelation:
							match arg2:
								case COR_Expressions.UniversalRelation():
									return COR_Expressions.UniversalRelation()
	# ((B)⁻¹) ∩ (T) = (B)⁻¹
	match expression:
		case COR_Expressions.Intersection(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.Converse(argument=arg):
					match arg:
						case _:
							B = arg
							match arg2:
								case COR_Expressions.UniversalRelation():
									return COR_Expressions.Converse(B)
	# ((C)⁻) ∩ (T) = (C)⁻
	match expression:
		case COR_Expressions.Intersection(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.Complement(argument=arg):
					match arg:
						case _:
							C = arg
							match arg2:
								case COR_Expressions.UniversalRelation():
									return COR_Expressions.Complement(C)
	# (𝟎) ∩ ((A)⁻) = 𝟎
	match expression:
		case COR_Expressions.Intersection(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.EmptyRelation():
					match arg2:
						case COR_Expressions.Complement(argument=arg):
							match arg:
								case _:
									A = arg
									return COR_Expressions.EmptyRelation()
	# ((A)⁻¹) ∘ (𝟏) = (A)⁻¹
	match expression:
		case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.Converse(argument=arg):
					match arg:
						case _:
							A = arg
							match arg2:
								case COR_Expressions.IdentityRelation:
									return COR_Expressions.Converse(A)
	# ((A)⁻¹) ∪ (T) = T
	match expression:
		case COR_Expressions.Union(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.Converse(argument=arg):
					match arg:
						case _:
							A = arg
							match arg2:
								case COR_Expressions.UniversalRelation():
									return COR_Expressions.UniversalRelation()
	# (𝟏) ∩ ((A)⁻¹) = (𝟏) ∩ (A)
	match expression:
		case COR_Expressions.Intersection(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.IdentityRelation:
					match arg2:
						case COR_Expressions.Converse(argument=arg):
							match arg:
								case _:
									A = arg
									return COR_Expressions.Intersection(COR_Expressions.IdentityRelation(), A)
	# ((𝟏)⁻) † (B) = B
	match expression:
		case COR_Expressions.Dagger(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.Complement(argument=arg):
					match arg:
						case COR_Expressions.IdentityRelation:
							match arg2:
								case _:
									B = arg2
									return B
	# ((C)⁻) ∪ (C) = T
	match expression:
		case COR_Expressions.Union(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.Complement(argument=arg):
					match arg:
						case _:
							C = arg
							match arg2:
								case _:
									C = arg2
									return COR_Expressions.UniversalRelation()
	# (𝟏) ∩ ((𝟏)⁻) = 𝟎
	match expression:
		case COR_Expressions.Intersection(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.IdentityRelation:
					match arg2:
						case COR_Expressions.Complement(argument=arg):
							match arg:
								case COR_Expressions.IdentityRelation:
									return COR_Expressions.EmptyRelation()
	# (T) ∩ ((𝟏)⁻) = (𝟏)⁻
	match expression:
		case COR_Expressions.Intersection(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.UniversalRelation():
					match arg2:
						case COR_Expressions.Complement(argument=arg):
							match arg:
								case COR_Expressions.IdentityRelation:
									return COR_Expressions.Complement(COR_Expressions.IdentityRelation())
	# (B) ∩ ((B)⁻) = 𝟎
	match expression:
		case COR_Expressions.Intersection(argument1=arg1, argument2=arg2):
			match arg1:
				case _:
					B = arg1
					match arg2:
						case COR_Expressions.Complement(argument=arg):
							match arg:
								case _:
									B = arg
									return COR_Expressions.EmptyRelation()
	# ((A)⁻¹) ∘ (𝟎) = 𝟎
	match expression:
		case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.Converse(argument=arg):
					match arg:
						case _:
							A = arg
							match arg2:
								case COR_Expressions.EmptyRelation():
									return COR_Expressions.EmptyRelation()
	# ((A)⁻¹) ∩ (𝟎) = 𝟎
	match expression:
		case COR_Expressions.Intersection(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.Converse(argument=arg):
					match arg:
						case _:
							A = arg
							match arg2:
								case COR_Expressions.EmptyRelation():
									return COR_Expressions.EmptyRelation()
	# (𝟎) ∩ ((𝟏)⁻) = 𝟎
	match expression:
		case COR_Expressions.Intersection(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.EmptyRelation():
					match arg2:
						case COR_Expressions.Complement(argument=arg):
							match arg:
								case COR_Expressions.IdentityRelation:
									return COR_Expressions.EmptyRelation()
	# (𝟎) ∩ ((B)⁻¹) = 𝟎
	match expression:
		case COR_Expressions.Intersection(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.EmptyRelation():
					match arg2:
						case COR_Expressions.Converse(argument=arg):
							match arg:
								case _:
									B = arg
									return COR_Expressions.EmptyRelation()
	# ((C)⁻¹) ∩ (𝟎) = 𝟎
	match expression:
		case COR_Expressions.Intersection(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.Converse(argument=arg):
					match arg:
						case _:
							C = arg
							match arg2:
								case COR_Expressions.EmptyRelation():
									return COR_Expressions.EmptyRelation()
	# ((B)⁻¹) ∘ (𝟎) = 𝟎
	match expression:
		case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.Converse(argument=arg):
					match arg:
						case _:
							B = arg
							match arg2:
								case COR_Expressions.EmptyRelation():
									return COR_Expressions.EmptyRelation()
	# ((B)⁻¹) ∘ (𝟏) = (B)⁻¹
	match expression:
		case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.Converse(argument=arg):
					match arg:
						case _:
							B = arg
							match arg2:
								case COR_Expressions.IdentityRelation:
									return COR_Expressions.Converse(B)
	# ((A)⁻¹) ∪ (𝟎) = (A)⁻¹
	match expression:
		case COR_Expressions.Union(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.Converse(argument=arg):
					match arg:
						case _:
							A = arg
							match arg2:
								case COR_Expressions.EmptyRelation():
									return COR_Expressions.Converse(A)
	# ((C)⁻¹) ∪ (T) = T
	match expression:
		case COR_Expressions.Union(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.Converse(argument=arg):
					match arg:
						case _:
							C = arg
							match arg2:
								case COR_Expressions.UniversalRelation():
									return COR_Expressions.UniversalRelation()
	# ((C)⁻) ∘ (𝟏) = (C)⁻
	match expression:
		case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.Complement(argument=arg):
					match arg:
						case _:
							C = arg
							match arg2:
								case COR_Expressions.IdentityRelation:
									return COR_Expressions.Complement(C)
	# (𝟏) ∩ ((B)⁻¹) = (B) ∩ (𝟏)
	match expression:
		case COR_Expressions.Intersection(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.IdentityRelation:
					match arg2:
						case COR_Expressions.Converse(argument=arg):
							match arg:
								case _:
									B = arg
									return COR_Expressions.Intersection(B, COR_Expressions.IdentityRelation())
	# ((C)⁻¹) ∩ (𝟏) = (C) ∩ (𝟏)
	match expression:
		case COR_Expressions.Intersection(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.Converse(argument=arg):
					match arg:
						case _:
							C = arg
							match arg2:
								case COR_Expressions.IdentityRelation:
									return COR_Expressions.Intersection(C, COR_Expressions.IdentityRelation())
	# ((C)⁻¹) ∪ (𝟎) = (C)⁻¹
	match expression:
		case COR_Expressions.Union(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.Converse(argument=arg):
					match arg:
						case _:
							C = arg
							match arg2:
								case COR_Expressions.EmptyRelation():
									return COR_Expressions.Converse(C)
	# ((𝟏)⁻) † (A) = A
	match expression:
		case COR_Expressions.Dagger(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.Complement(argument=arg):
					match arg:
						case COR_Expressions.IdentityRelation:
							match arg2:
								case _:
									A = arg2
									return A
	# ((B)⁻) ∪ (T) = T
	match expression:
		case COR_Expressions.Union(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.Complement(argument=arg):
					match arg:
						case _:
							B = arg
							match arg2:
								case COR_Expressions.UniversalRelation():
									return COR_Expressions.UniversalRelation()
	# ((B)⁻) ∘ (𝟏) = (B)⁻
	match expression:
		case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.Complement(argument=arg):
					match arg:
						case _:
							B = arg
							match arg2:
								case COR_Expressions.IdentityRelation:
									return COR_Expressions.Complement(B)
	# (T) ∩ ((A)⁻) = (A)⁻
	match expression:
		case COR_Expressions.Intersection(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.UniversalRelation():
					match arg2:
						case COR_Expressions.Complement(argument=arg):
							match arg:
								case _:
									A = arg
									return COR_Expressions.Complement(A)
	# ((B)⁻) ∪ (B) = T
	match expression:
		case COR_Expressions.Union(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.Complement(argument=arg):
					match arg:
						case _:
							B = arg
							match arg2:
								case _:
									B = arg2
									return COR_Expressions.UniversalRelation()
	# ((𝟎) † (𝟏))⁻¹ = (𝟎) † (𝟏)
	match expression:
		case COR_Expressions.Converse(argument=arg):
			match arg:
				case COR_Expressions.Dagger(argument1=arg1, argument2=arg2):
					match arg1:
						case COR_Expressions.EmptyRelation():
							match arg2:
								case COR_Expressions.IdentityRelation:
									return COR_Expressions.Dagger(COR_Expressions.EmptyRelation(), COR_Expressions.IdentityRelation())
	# ((C)⁻) ∘ (𝟎) = 𝟎
	match expression:
		case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.Complement(argument=arg):
					match arg:
						case _:
							C = arg
							match arg2:
								case COR_Expressions.EmptyRelation():
									return COR_Expressions.EmptyRelation()
	# ((A)⁻) † (T) = T
	match expression:
		case COR_Expressions.Dagger(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.Complement(argument=arg):
					match arg:
						case _:
							A = arg
							match arg2:
								case COR_Expressions.UniversalRelation():
									return COR_Expressions.UniversalRelation()
	# ((C)⁻) ∪ (T) = T
	match expression:
		case COR_Expressions.Union(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.Complement(argument=arg):
					match arg:
						case _:
							C = arg
							match arg2:
								case COR_Expressions.UniversalRelation():
									return COR_Expressions.UniversalRelation()
	# ((B)⁻) ∩ (𝟎) = 𝟎
	match expression:
		case COR_Expressions.Intersection(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.Complement(argument=arg):
					match arg:
						case _:
							B = arg
							match arg2:
								case COR_Expressions.EmptyRelation():
									return COR_Expressions.EmptyRelation()
	# ((𝟏) ∩ (A))⁻¹ = (𝟏) ∩ (A)
	match expression:
		case COR_Expressions.Converse(argument=arg):
			match arg:
				case COR_Expressions.Intersection(argument1=arg1, argument2=arg2):
					match arg1:
						case COR_Expressions.IdentityRelation:
							match arg2:
								case _:
									A = arg2
									return COR_Expressions.Intersection(COR_Expressions.IdentityRelation(), A)
	# (T) ∩ ((A)⁻¹) = (A)⁻¹
	match expression:
		case COR_Expressions.Intersection(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.UniversalRelation():
					match arg2:
						case COR_Expressions.Converse(argument=arg):
							match arg:
								case _:
									A = arg
									return COR_Expressions.Converse(A)
	# ((𝟏)⁻) ∩ (T) = (𝟏)⁻
	match expression:
		case COR_Expressions.Intersection(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.Complement(argument=arg):
					match arg:
						case COR_Expressions.IdentityRelation:
							match arg2:
								case COR_Expressions.UniversalRelation():
									return COR_Expressions.Complement(COR_Expressions.IdentityRelation())
	# ((A)⁻) ∩ (𝟎) = 𝟎
	match expression:
		case COR_Expressions.Intersection(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.Complement(argument=arg):
					match arg:
						case _:
							A = arg
							match arg2:
								case COR_Expressions.EmptyRelation():
									return COR_Expressions.EmptyRelation()
	# ((𝟏)⁻) † (𝟏) = 𝟏
	match expression:
		case COR_Expressions.Dagger(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.Complement(argument=arg):
					match arg:
						case COR_Expressions.IdentityRelation:
							match arg2:
								case COR_Expressions.IdentityRelation:
									return COR_Expressions.IdentityRelation()
	# (T) ∩ ((B)⁻) = (B)⁻
	match expression:
		case COR_Expressions.Intersection(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.UniversalRelation():
					match arg2:
						case COR_Expressions.Complement(argument=arg):
							match arg:
								case _:
									B = arg
									return COR_Expressions.Complement(B)
	# ((𝟏)⁻) † (𝟎) = 𝟎
	match expression:
		case COR_Expressions.Dagger(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.Complement(argument=arg):
					match arg:
						case COR_Expressions.IdentityRelation:
							match arg2:
								case COR_Expressions.EmptyRelation():
									return COR_Expressions.EmptyRelation()
	# (𝟎) ∩ ((B)⁻) = 𝟎
	match expression:
		case COR_Expressions.Intersection(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.EmptyRelation():
					match arg2:
						case COR_Expressions.Complement(argument=arg):
							match arg:
								case _:
									B = arg
									return COR_Expressions.EmptyRelation()
	# (C) ∩ ((C)⁻) = 𝟎
	match expression:
		case COR_Expressions.Intersection(argument1=arg1, argument2=arg2):
			match arg1:
				case _:
					C = arg1
					match arg2:
						case COR_Expressions.Complement(argument=arg):
							match arg:
								case _:
									C = arg
									return COR_Expressions.EmptyRelation()
	# ((C) ∩ (𝟏))⁻¹ = (𝟏) ∩ (C)
	match expression:
		case COR_Expressions.Converse(argument=arg):
			match arg:
				case COR_Expressions.Intersection(argument1=arg1, argument2=arg2):
					match arg1:
						case _:
							C = arg1
							match arg2:
								case COR_Expressions.IdentityRelation:
									return COR_Expressions.Intersection(COR_Expressions.IdentityRelation(), C)
	# (𝟏) ∩ ((C)⁻¹) = (𝟏) ∩ (C)
	match expression:
		case COR_Expressions.Intersection(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.IdentityRelation:
					match arg2:
						case COR_Expressions.Converse(argument=arg):
							match arg:
								case _:
									C = arg
									return COR_Expressions.Intersection(COR_Expressions.IdentityRelation(), C)
	# ((A)⁻) ∘ (𝟏) = (A)⁻
	match expression:
		case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.Complement(argument=arg):
					match arg:
						case _:
							A = arg
							match arg2:
								case COR_Expressions.IdentityRelation:
									return COR_Expressions.Complement(A)
	# ((A)⁻¹) ∩ (T) = (A)⁻¹
	match expression:
		case COR_Expressions.Intersection(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.Converse(argument=arg):
					match arg:
						case _:
							A = arg
							match arg2:
								case COR_Expressions.UniversalRelation():
									return COR_Expressions.Converse(A)
	# ((B)⁻) ∘ (𝟎) = 𝟎
	match expression:
		case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.Complement(argument=arg):
					match arg:
						case _:
							B = arg
							match arg2:
								case COR_Expressions.EmptyRelation():
									return COR_Expressions.EmptyRelation()
	# ((B)⁻¹) ∪ (𝟎) = (B)⁻¹
	match expression:
		case COR_Expressions.Union(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.Converse(argument=arg):
					match arg:
						case _:
							B = arg
							match arg2:
								case COR_Expressions.EmptyRelation():
									return COR_Expressions.Converse(B)
	# ((𝟏)⁻) † (C) = C
	match expression:
		case COR_Expressions.Dagger(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.Complement(argument=arg):
					match arg:
						case COR_Expressions.IdentityRelation:
							match arg2:
								case _:
									C = arg2
									return C
	# ((A)⁻) ∩ (T) = (A)⁻
	match expression:
		case COR_Expressions.Intersection(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.Complement(argument=arg):
					match arg:
						case _:
							A = arg
							match arg2:
								case COR_Expressions.UniversalRelation():
									return COR_Expressions.Complement(A)
	# ((B)⁻) ∩ (T) = (B)⁻
	match expression:
		case COR_Expressions.Intersection(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.Complement(argument=arg):
					match arg:
						case _:
							B = arg
							match arg2:
								case COR_Expressions.UniversalRelation():
									return COR_Expressions.Complement(B)
	# ((C)⁻¹) ∩ (T) = (C)⁻¹
	match expression:
		case COR_Expressions.Intersection(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.Converse(argument=arg):
					match arg:
						case _:
							C = arg
							match arg2:
								case COR_Expressions.UniversalRelation():
									return COR_Expressions.Converse(C)
	# ((𝟏)⁻) ∘ (𝟏) = (𝟏)⁻
	match expression:
		case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.Complement(argument=arg):
					match arg:
						case COR_Expressions.IdentityRelation:
							match arg2:
								case COR_Expressions.IdentityRelation:
									return COR_Expressions.Complement(COR_Expressions.IdentityRelation())
	# ((A)⁻) ∪ (A) = T
	match expression:
		case COR_Expressions.Union(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.Complement(argument=arg):
					match arg:
						case _:
							A = arg
							match arg2:
								case _:
									A = arg2
									return COR_Expressions.UniversalRelation()
	# ((𝟏)⁻) ∪ (𝟏) = T
	match expression:
		case COR_Expressions.Union(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.Complement(argument=arg):
					match arg:
						case COR_Expressions.IdentityRelation:
							match arg2:
								case COR_Expressions.IdentityRelation:
									return COR_Expressions.UniversalRelation()
	# ((B)⁻¹) ∩ (𝟏) = (B) ∩ (𝟏)
	match expression:
		case COR_Expressions.Intersection(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.Converse(argument=arg):
					match arg:
						case _:
							B = arg
							match arg2:
								case COR_Expressions.IdentityRelation:
									return COR_Expressions.Intersection(B, COR_Expressions.IdentityRelation())
	# (𝟎) ∩ ((C)⁻¹) = 𝟎
	match expression:
		case COR_Expressions.Intersection(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.EmptyRelation():
					match arg2:
						case COR_Expressions.Converse(argument=arg):
							match arg:
								case _:
									C = arg
									return COR_Expressions.EmptyRelation()
	# ((𝟏) ∩ (B))⁻¹ = (𝟏) ∩ (B)
	match expression:
		case COR_Expressions.Converse(argument=arg):
			match arg:
				case COR_Expressions.Intersection(argument1=arg1, argument2=arg2):
					match arg1:
						case COR_Expressions.IdentityRelation:
							match arg2:
								case _:
									B = arg2
									return COR_Expressions.Intersection(COR_Expressions.IdentityRelation(), B)
	# ((A)⁻¹) ∩ (𝟏) = (A) ∩ (𝟏)
	match expression:
		case COR_Expressions.Intersection(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.Converse(argument=arg):
					match arg:
						case _:
							A = arg
							match arg2:
								case COR_Expressions.IdentityRelation:
									return COR_Expressions.Intersection(A, COR_Expressions.IdentityRelation())
	# ((A)⁻) ∘ (𝟎) = 𝟎
	match expression:
		case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.Complement(argument=arg):
					match arg:
						case _:
							A = arg
							match arg2:
								case COR_Expressions.EmptyRelation():
									return COR_Expressions.EmptyRelation()
	# ((𝟏)⁻) ∘ (𝟎) = 𝟎
	match expression:
		case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.Complement(argument=arg):
					match arg:
						case COR_Expressions.IdentityRelation:
							match arg2:
								case COR_Expressions.EmptyRelation():
									return COR_Expressions.EmptyRelation()
	# ((B) ∩ (𝟏))⁻¹ = (𝟏) ∩ (B)
	match expression:
		case COR_Expressions.Converse(argument=arg):
			match arg:
				case COR_Expressions.Intersection(argument1=arg1, argument2=arg2):
					match arg1:
						case _:
							B = arg1
							match arg2:
								case COR_Expressions.IdentityRelation:
									return COR_Expressions.Intersection(COR_Expressions.IdentityRelation(), B)
	# (T) ∩ ((C)⁻¹) = (C)⁻¹
	match expression:
		case COR_Expressions.Intersection(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.UniversalRelation():
					match arg2:
						case COR_Expressions.Converse(argument=arg):
							match arg:
								case _:
									C = arg
									return COR_Expressions.Converse(C)
	# ((C)⁻) ∩ (𝟎) = 𝟎
	match expression:
		case COR_Expressions.Intersection(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.Complement(argument=arg):
					match arg:
						case _:
							C = arg
							match arg2:
								case COR_Expressions.EmptyRelation():
									return COR_Expressions.EmptyRelation()
	# ((A)⁻) ∩ (A) = 𝟎
	match expression:
		case COR_Expressions.Intersection(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.Complement(argument=arg):
					match arg:
						case _:
							A = arg
							match arg2:
								case _:
									A = arg2
									return COR_Expressions.EmptyRelation()
	# ((C)⁻) † (T) = T
	match expression:
		case COR_Expressions.Dagger(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.Complement(argument=arg):
					match arg:
						case _:
							C = arg
							match arg2:
								case COR_Expressions.UniversalRelation():
									return COR_Expressions.UniversalRelation()
	# ((𝟏)⁻) ∪ (T) = T
	match expression:
		case COR_Expressions.Union(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.Complement(argument=arg):
					match arg:
						case COR_Expressions.IdentityRelation:
							match arg2:
								case COR_Expressions.UniversalRelation():
									return COR_Expressions.UniversalRelation()
	# ((B)⁻) ∪ (𝟎) = (B)⁻
	match expression:
		case COR_Expressions.Union(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.Complement(argument=arg):
					match arg:
						case _:
							B = arg
							match arg2:
								case COR_Expressions.EmptyRelation():
									return COR_Expressions.Complement(B)
	# ((𝟏)⁻) ∩ (𝟏) = 𝟎
	match expression:
		case COR_Expressions.Intersection(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.Complement(argument=arg):
					match arg:
						case COR_Expressions.IdentityRelation:
							match arg2:
								case COR_Expressions.IdentityRelation:
									return COR_Expressions.EmptyRelation()
	# ((A)⁻¹) † (T) = T
	match expression:
		case COR_Expressions.Dagger(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.Converse(argument=arg):
					match arg:
						case _:
							A = arg
							match arg2:
								case COR_Expressions.UniversalRelation():
									return COR_Expressions.UniversalRelation()
	# (A) ∩ ((A)⁻) = 𝟎
	match expression:
		case COR_Expressions.Intersection(argument1=arg1, argument2=arg2):
			match arg1:
				case _:
					A = arg1
					match arg2:
						case COR_Expressions.Complement(argument=arg):
							match arg:
								case _:
									A = arg
									return COR_Expressions.EmptyRelation()
	# ((𝟏)⁻) ∪ (𝟎) = (𝟏)⁻
	match expression:
		case COR_Expressions.Union(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.Complement(argument=arg):
					match arg:
						case COR_Expressions.IdentityRelation:
							match arg2:
								case COR_Expressions.EmptyRelation():
									return COR_Expressions.Complement(COR_Expressions.IdentityRelation())
	# ((A)⁻) ∪ (𝟎) = (A)⁻
	match expression:
		case COR_Expressions.Union(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.Complement(argument=arg):
					match arg:
						case _:
							A = arg
							match arg2:
								case COR_Expressions.EmptyRelation():
									return COR_Expressions.Complement(A)
	# ((B)⁻) ∩ (B) = 𝟎
	match expression:
		case COR_Expressions.Intersection(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.Complement(argument=arg):
					match arg:
						case _:
							B = arg
							match arg2:
								case _:
									B = arg2
									return COR_Expressions.EmptyRelation()
	# ((B)⁻¹) ∩ (𝟎) = 𝟎
	match expression:
		case COR_Expressions.Intersection(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.Converse(argument=arg):
					match arg:
						case _:
							B = arg
							match arg2:
								case COR_Expressions.EmptyRelation():
									return COR_Expressions.EmptyRelation()
	# ((C)⁻¹) ∘ (𝟏) = (C)⁻¹
	match expression:
		case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.Converse(argument=arg):
					match arg:
						case _:
							C = arg
							match arg2:
								case COR_Expressions.IdentityRelation:
									return COR_Expressions.Converse(C)
	# ((C)⁻¹) ∘ (𝟎) = 𝟎
	match expression:
		case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.Converse(argument=arg):
					match arg:
						case _:
							C = arg
							match arg2:
								case COR_Expressions.EmptyRelation():
									return COR_Expressions.EmptyRelation()
	# ((B)⁻¹) † (T) = T
	match expression:
		case COR_Expressions.Dagger(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.Converse(argument=arg):
					match arg:
						case _:
							B = arg
							match arg2:
								case COR_Expressions.UniversalRelation():
									return COR_Expressions.UniversalRelation()
	# ((𝟏)⁻) ∩ (𝟎) = 𝟎
	match expression:
		case COR_Expressions.Intersection(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.Complement(argument=arg):
					match arg:
						case COR_Expressions.IdentityRelation:
							match arg2:
								case COR_Expressions.EmptyRelation():
									return COR_Expressions.EmptyRelation()
	# ((A)⁻) ∪ (T) = T
	match expression:
		case COR_Expressions.Union(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.Complement(argument=arg):
					match arg:
						case _:
							A = arg
							match arg2:
								case COR_Expressions.UniversalRelation():
									return COR_Expressions.UniversalRelation()
	# (T) ∩ ((C)⁻) = (C)⁻
	match expression:
		case COR_Expressions.Intersection(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.UniversalRelation():
					match arg2:
						case COR_Expressions.Complement(argument=arg):
							match arg:
								case _:
									C = arg
									return COR_Expressions.Complement(C)
	return expression # The given expression was unable to be simplified