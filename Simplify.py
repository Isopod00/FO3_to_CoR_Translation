import COR_Expressions
def simplify(expression):
	match expression:
		# (𝟏) ∪ ((T)⁻¹) = T
		case COR_Expressions.Union(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.IdentityRelation:
					match arg2:
						case COR_Expressions.Converse(argument=arg):
							match arg:
								case COR_Expressions.UniversalRelation():
									return COR_Expressions.UniversalRelation()
		# (𝟎) ∘ ((C)⁻¹) = (𝟎)⁻¹
		case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.EmptyRelation():
					match arg2:
						case COR_Expressions.Converse(argument=arg):
							match arg:
								case _:
									C = arg
									return COR_Expressions.Converse(COR_Expressions.EmptyRelation())
		# (𝟏) ∘ ((B)⁻) = (B)⁻
		case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.IdentityRelation:
					match arg2:
						case COR_Expressions.Complement(argument=arg):
							match arg:
								case _:
									B = arg
									return COR_Expressions.Complement(B)
		# ((C)⁻¹)⁻¹ = C
		case COR_Expressions.Converse(argument=arg):
			match arg:
				case COR_Expressions.Converse(argument=arg):
					match arg:
						case _:
							C = arg
							return C
		# (𝟏) ∘ ((B)⁻¹) = (B)⁻¹
		case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.IdentityRelation:
					match arg2:
						case COR_Expressions.Converse(argument=arg):
							match arg:
								case _:
									B = arg
									return COR_Expressions.Converse(B)
		# (𝟎) ∘ ((T)⁻¹) = (T)⁻
		case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.EmptyRelation():
					match arg2:
						case COR_Expressions.Converse(argument=arg):
							match arg:
								case COR_Expressions.UniversalRelation():
									return COR_Expressions.Complement(COR_Expressions.UniversalRelation())
		# (T) ∘ ((T)⁻) = 𝟎
		case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.UniversalRelation():
					match arg2:
						case COR_Expressions.Complement(argument=arg):
							match arg:
								case COR_Expressions.UniversalRelation():
									return COR_Expressions.EmptyRelation()
		# (C) † ((T)⁻¹) = (T)⁻¹
		case COR_Expressions.Dagger(argument1=arg1, argument2=arg2):
			match arg1:
				case _:
					C = arg1
					match arg2:
						case COR_Expressions.Converse(argument=arg):
							match arg:
								case COR_Expressions.UniversalRelation():
									return COR_Expressions.Converse(COR_Expressions.UniversalRelation())
		# (T) ∪ ((C)⁻¹) = (T)⁻¹
		case COR_Expressions.Union(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.UniversalRelation():
					match arg2:
						case COR_Expressions.Converse(argument=arg):
							match arg:
								case _:
									C = arg
									return COR_Expressions.Converse(COR_Expressions.UniversalRelation())
		# (T) ∪ ((T)⁻) = (T)⁻¹
		case COR_Expressions.Union(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.UniversalRelation():
					match arg2:
						case COR_Expressions.Complement(argument=arg):
							match arg:
								case COR_Expressions.UniversalRelation():
									return COR_Expressions.Converse(COR_Expressions.UniversalRelation())
		# (𝟎) ∘ ((𝟎)⁻) = (𝟎)⁻¹
		case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.EmptyRelation():
					match arg2:
						case COR_Expressions.Complement(argument=arg):
							match arg:
								case COR_Expressions.EmptyRelation():
									return COR_Expressions.Converse(COR_Expressions.EmptyRelation())
		# (𝟎) † ((T)⁻) = 𝟎
		case COR_Expressions.Dagger(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.EmptyRelation():
					match arg2:
						case COR_Expressions.Complement(argument=arg):
							match arg:
								case COR_Expressions.UniversalRelation():
									return COR_Expressions.EmptyRelation()
		# (𝟎) ∘ ((𝟎)⁻¹) = (T)⁻
		case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.EmptyRelation():
					match arg2:
						case COR_Expressions.Converse(argument=arg):
							match arg:
								case COR_Expressions.EmptyRelation():
									return COR_Expressions.Complement(COR_Expressions.UniversalRelation())
		# (𝟎) ∘ ((B)⁻) = (T)⁻
		case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.EmptyRelation():
					match arg2:
						case COR_Expressions.Complement(argument=arg):
							match arg:
								case _:
									B = arg
									return COR_Expressions.Complement(COR_Expressions.UniversalRelation())
		# ((𝟎)⁻)⁻ = 𝟎
		case COR_Expressions.Complement(argument=arg):
			match arg:
				case COR_Expressions.Complement(argument=arg):
					match arg:
						case COR_Expressions.EmptyRelation():
							return COR_Expressions.EmptyRelation()
		# (T) ∘ ((𝟎)⁻) = (𝟎)⁻
		case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.UniversalRelation():
					match arg2:
						case COR_Expressions.Complement(argument=arg):
							match arg:
								case COR_Expressions.EmptyRelation():
									return COR_Expressions.Complement(COR_Expressions.EmptyRelation())
		# (T) † ((T)⁻¹) = (T)⁻¹
		case COR_Expressions.Dagger(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.UniversalRelation():
					match arg2:
						case COR_Expressions.Converse(argument=arg):
							match arg:
								case COR_Expressions.UniversalRelation():
									return COR_Expressions.Converse(COR_Expressions.UniversalRelation())
		# (T) † ((C)⁻¹) = T
		case COR_Expressions.Dagger(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.UniversalRelation():
					match arg2:
						case COR_Expressions.Converse(argument=arg):
							match arg:
								case _:
									C = arg
									return COR_Expressions.UniversalRelation()
		# (A) † ((𝟏)⁻) = A
		case COR_Expressions.Dagger(argument1=arg1, argument2=arg2):
			match arg1:
				case _:
					A = arg1
					match arg2:
						case COR_Expressions.Complement(argument=arg):
							match arg:
								case COR_Expressions.IdentityRelation:
									return A
		# (𝟎) ∪ ((T)⁻¹) = T
		case COR_Expressions.Union(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.EmptyRelation():
					match arg2:
						case COR_Expressions.Converse(argument=arg):
							match arg:
								case COR_Expressions.UniversalRelation():
									return COR_Expressions.UniversalRelation()
		# (𝟎) ∪ ((C)⁻) = (C)⁻
		case COR_Expressions.Union(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.EmptyRelation():
					match arg2:
						case COR_Expressions.Complement(argument=arg):
							match arg:
								case _:
									C = arg
									return COR_Expressions.Complement(C)
		# (T) ∪ ((B)⁻) = (T)⁻¹
		case COR_Expressions.Union(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.UniversalRelation():
					match arg2:
						case COR_Expressions.Complement(argument=arg):
							match arg:
								case _:
									B = arg
									return COR_Expressions.Converse(COR_Expressions.UniversalRelation())
		# (𝟎) ∘ ((A)⁻) = (𝟎)⁻¹
		case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.EmptyRelation():
					match arg2:
						case COR_Expressions.Complement(argument=arg):
							match arg:
								case _:
									A = arg
									return COR_Expressions.Converse(COR_Expressions.EmptyRelation())
		# (B) ∪ ((𝟎)⁻) = T
		case COR_Expressions.Union(argument1=arg1, argument2=arg2):
			match arg1:
				case _:
					B = arg1
					match arg2:
						case COR_Expressions.Complement(argument=arg):
							match arg:
								case COR_Expressions.EmptyRelation():
									return COR_Expressions.UniversalRelation()
		# (𝟎) † ((T)⁻¹) = (T)⁻¹
		case COR_Expressions.Dagger(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.EmptyRelation():
					match arg2:
						case COR_Expressions.Converse(argument=arg):
							match arg:
								case COR_Expressions.UniversalRelation():
									return COR_Expressions.Converse(COR_Expressions.UniversalRelation())
		# (B) † ((T)⁻¹) = (T)⁻¹
		case COR_Expressions.Dagger(argument1=arg1, argument2=arg2):
			match arg1:
				case _:
					B = arg1
					match arg2:
						case COR_Expressions.Converse(argument=arg):
							match arg:
								case COR_Expressions.UniversalRelation():
									return COR_Expressions.Converse(COR_Expressions.UniversalRelation())
		# ((T)⁻)⁻¹ = 𝟎
		case COR_Expressions.Converse(argument=arg):
			match arg:
				case COR_Expressions.Complement(argument=arg):
					match arg:
						case COR_Expressions.UniversalRelation():
							return COR_Expressions.EmptyRelation()
		# (A) ∪ ((𝟎)⁻) = (𝟎)⁻
		case COR_Expressions.Union(argument1=arg1, argument2=arg2):
			match arg1:
				case _:
					A = arg1
					match arg2:
						case COR_Expressions.Complement(argument=arg):
							match arg:
								case COR_Expressions.EmptyRelation():
									return COR_Expressions.Complement(COR_Expressions.EmptyRelation())
		# (A) ∪ ((T)⁻) = A
		case COR_Expressions.Union(argument1=arg1, argument2=arg2):
			match arg1:
				case _:
					A = arg1
					match arg2:
						case COR_Expressions.Complement(argument=arg):
							match arg:
								case COR_Expressions.UniversalRelation():
									return A
		# (𝟎) ∘ ((A)⁻¹) = (T)⁻
		case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.EmptyRelation():
					match arg2:
						case COR_Expressions.Converse(argument=arg):
							match arg:
								case _:
									A = arg
									return COR_Expressions.Complement(COR_Expressions.UniversalRelation())
		# (T) ∪ ((𝟏)⁻¹) = T
		case COR_Expressions.Union(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.UniversalRelation():
					match arg2:
						case COR_Expressions.Converse(argument=arg):
							match arg:
								case COR_Expressions.IdentityRelation:
									return COR_Expressions.UniversalRelation()
		# (B) ∘ ((𝟎)⁻¹) = (T)⁻
		case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
			match arg1:
				case _:
					B = arg1
					match arg2:
						case COR_Expressions.Converse(argument=arg):
							match arg:
								case COR_Expressions.EmptyRelation():
									return COR_Expressions.Complement(COR_Expressions.UniversalRelation())
		# (B) ∘ ((T)⁻) = (T)⁻
		case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
			match arg1:
				case _:
					B = arg1
					match arg2:
						case COR_Expressions.Complement(argument=arg):
							match arg:
								case COR_Expressions.UniversalRelation():
									return COR_Expressions.Complement(COR_Expressions.UniversalRelation())
		# (B) ∪ ((𝟎)⁻¹) = B
		case COR_Expressions.Union(argument1=arg1, argument2=arg2):
			match arg1:
				case _:
					B = arg1
					match arg2:
						case COR_Expressions.Converse(argument=arg):
							match arg:
								case COR_Expressions.EmptyRelation():
									return B
		# (A) † ((T)⁻¹) = (T)⁻¹
		case COR_Expressions.Dagger(argument1=arg1, argument2=arg2):
			match arg1:
				case _:
					A = arg1
					match arg2:
						case COR_Expressions.Converse(argument=arg):
							match arg:
								case COR_Expressions.UniversalRelation():
									return COR_Expressions.Converse(COR_Expressions.UniversalRelation())
		# (A) ∘ ((𝟎)⁻¹) = (T)⁻
		case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
			match arg1:
				case _:
					A = arg1
					match arg2:
						case COR_Expressions.Converse(argument=arg):
							match arg:
								case COR_Expressions.EmptyRelation():
									return COR_Expressions.Complement(COR_Expressions.UniversalRelation())
		# (C) ∪ ((C)⁻) = (𝟎)⁻
		case COR_Expressions.Union(argument1=arg1, argument2=arg2):
			match arg1:
				case _:
					C = arg1
					match arg2:
						case COR_Expressions.Complement(argument=arg):
							match arg:
								case _:
									C = arg
									return COR_Expressions.Complement(COR_Expressions.EmptyRelation())
		# (𝟎) ∘ ((B)⁻¹) = 𝟎
		case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.EmptyRelation():
					match arg2:
						case COR_Expressions.Converse(argument=arg):
							match arg:
								case _:
									B = arg
									return COR_Expressions.EmptyRelation()
		# (B) ∪ ((B)⁻) = (𝟎)⁻
		case COR_Expressions.Union(argument1=arg1, argument2=arg2):
			match arg1:
				case _:
					B = arg1
					match arg2:
						case COR_Expressions.Complement(argument=arg):
							match arg:
								case _:
									B = arg
									return COR_Expressions.Complement(COR_Expressions.EmptyRelation())
		# ((T)⁻¹)⁻ = 𝟎
		case COR_Expressions.Complement(argument=arg):
			match arg:
				case COR_Expressions.Converse(argument=arg):
					match arg:
						case COR_Expressions.UniversalRelation():
							return COR_Expressions.EmptyRelation()
		# (𝟏) ∘ ((T)⁻) = (𝟎)⁻¹
		case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.IdentityRelation:
					match arg2:
						case COR_Expressions.Complement(argument=arg):
							match arg:
								case COR_Expressions.UniversalRelation():
									return COR_Expressions.Converse(COR_Expressions.EmptyRelation())
		# (T) † ((𝟏)⁻¹) = (𝟎)⁻
		case COR_Expressions.Dagger(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.UniversalRelation():
					match arg2:
						case COR_Expressions.Converse(argument=arg):
							match arg:
								case COR_Expressions.IdentityRelation:
									return COR_Expressions.Complement(COR_Expressions.EmptyRelation())
		# (T) ∪ ((𝟎)⁻) = (T)⁻¹
		case COR_Expressions.Union(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.UniversalRelation():
					match arg2:
						case COR_Expressions.Complement(argument=arg):
							match arg:
								case COR_Expressions.EmptyRelation():
									return COR_Expressions.Converse(COR_Expressions.UniversalRelation())
		# (T) † ((A)⁻¹) = (T)⁻¹
		case COR_Expressions.Dagger(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.UniversalRelation():
					match arg2:
						case COR_Expressions.Converse(argument=arg):
							match arg:
								case _:
									A = arg
									return COR_Expressions.Converse(COR_Expressions.UniversalRelation())
		# (T) † ((B)⁻) = (𝟎)⁻
		case COR_Expressions.Dagger(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.UniversalRelation():
					match arg2:
						case COR_Expressions.Complement(argument=arg):
							match arg:
								case _:
									B = arg
									return COR_Expressions.Complement(COR_Expressions.EmptyRelation())
		# (𝟏) ∪ ((𝟎)⁻) = (T)⁻¹
		case COR_Expressions.Union(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.IdentityRelation:
					match arg2:
						case COR_Expressions.Complement(argument=arg):
							match arg:
								case COR_Expressions.EmptyRelation():
									return COR_Expressions.Converse(COR_Expressions.UniversalRelation())
		# (𝟏) † ((T)⁻¹) = T
		case COR_Expressions.Dagger(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.IdentityRelation:
					match arg2:
						case COR_Expressions.Converse(argument=arg):
							match arg:
								case COR_Expressions.UniversalRelation():
									return COR_Expressions.UniversalRelation()
		# (T) ∪ ((A)⁻¹) = (T)⁻¹
		case COR_Expressions.Union(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.UniversalRelation():
					match arg2:
						case COR_Expressions.Converse(argument=arg):
							match arg:
								case _:
									A = arg
									return COR_Expressions.Converse(COR_Expressions.UniversalRelation())
		# (A) ∪ ((𝟎)⁻¹) = A
		case COR_Expressions.Union(argument1=arg1, argument2=arg2):
			match arg1:
				case _:
					A = arg1
					match arg2:
						case COR_Expressions.Converse(argument=arg):
							match arg:
								case COR_Expressions.EmptyRelation():
									return A
		# (𝟎) ∪ ((𝟏)⁻) = (𝟏)⁻
		case COR_Expressions.Union(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.EmptyRelation():
					match arg2:
						case COR_Expressions.Complement(argument=arg):
							match arg:
								case COR_Expressions.IdentityRelation:
									return COR_Expressions.Complement(COR_Expressions.IdentityRelation())
		# ((𝟎)⁻)⁻¹ = (T)⁻¹
		case COR_Expressions.Converse(argument=arg):
			match arg:
				case COR_Expressions.Complement(argument=arg):
					match arg:
						case COR_Expressions.EmptyRelation():
							return COR_Expressions.Converse(COR_Expressions.UniversalRelation())
		# (B) ∪ ((T)⁻¹) = (T)⁻¹
		case COR_Expressions.Union(argument1=arg1, argument2=arg2):
			match arg1:
				case _:
					B = arg1
					match arg2:
						case COR_Expressions.Converse(argument=arg):
							match arg:
								case COR_Expressions.UniversalRelation():
									return COR_Expressions.Converse(COR_Expressions.UniversalRelation())
		# (𝟏) ∪ ((𝟎)⁻¹) = 𝟏
		case COR_Expressions.Union(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.IdentityRelation:
					match arg2:
						case COR_Expressions.Converse(argument=arg):
							match arg:
								case COR_Expressions.EmptyRelation():
									return COR_Expressions.IdentityRelation()
		# (A) ∪ ((T)⁻¹) = T
		case COR_Expressions.Union(argument1=arg1, argument2=arg2):
			match arg1:
				case _:
					A = arg1
					match arg2:
						case COR_Expressions.Converse(argument=arg):
							match arg:
								case COR_Expressions.UniversalRelation():
									return COR_Expressions.UniversalRelation()
		# (C) † ((𝟏)⁻) = C
		case COR_Expressions.Dagger(argument1=arg1, argument2=arg2):
			match arg1:
				case _:
					C = arg1
					match arg2:
						case COR_Expressions.Complement(argument=arg):
							match arg:
								case COR_Expressions.IdentityRelation:
									return C
		# (T) † ((𝟏)⁻) = (𝟎)⁻
		case COR_Expressions.Dagger(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.UniversalRelation():
					match arg2:
						case COR_Expressions.Complement(argument=arg):
							match arg:
								case COR_Expressions.IdentityRelation:
									return COR_Expressions.Complement(COR_Expressions.EmptyRelation())
		# (𝟎) † ((𝟎)⁻) = (𝟎)⁻
		case COR_Expressions.Dagger(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.EmptyRelation():
					match arg2:
						case COR_Expressions.Complement(argument=arg):
							match arg:
								case COR_Expressions.EmptyRelation():
									return COR_Expressions.Complement(COR_Expressions.EmptyRelation())
		# (𝟎) ∘ ((𝟏)⁻¹) = 𝟎
		case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.EmptyRelation():
					match arg2:
						case COR_Expressions.Converse(argument=arg):
							match arg:
								case COR_Expressions.IdentityRelation:
									return COR_Expressions.EmptyRelation()
		# (C) ∪ ((𝟎)⁻¹) = C
		case COR_Expressions.Union(argument1=arg1, argument2=arg2):
			match arg1:
				case _:
					C = arg1
					match arg2:
						case COR_Expressions.Converse(argument=arg):
							match arg:
								case COR_Expressions.EmptyRelation():
									return C
		# (C) ∘ ((T)⁻) = (𝟎)⁻¹
		case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
			match arg1:
				case _:
					C = arg1
					match arg2:
						case COR_Expressions.Complement(argument=arg):
							match arg:
								case COR_Expressions.UniversalRelation():
									return COR_Expressions.Converse(COR_Expressions.EmptyRelation())
		# ((C)⁻)⁻ = C
		case COR_Expressions.Complement(argument=arg):
			match arg:
				case COR_Expressions.Complement(argument=arg):
					match arg:
						case _:
							C = arg
							return C
		# (𝟎) † ((𝟏)⁻) = (𝟎)⁻¹
		case COR_Expressions.Dagger(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.EmptyRelation():
					match arg2:
						case COR_Expressions.Complement(argument=arg):
							match arg:
								case COR_Expressions.IdentityRelation:
									return COR_Expressions.Converse(COR_Expressions.EmptyRelation())
		# (T) † ((T)⁻) = (𝟎)⁻
		case COR_Expressions.Dagger(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.UniversalRelation():
					match arg2:
						case COR_Expressions.Complement(argument=arg):
							match arg:
								case COR_Expressions.UniversalRelation():
									return COR_Expressions.Complement(COR_Expressions.EmptyRelation())
		# (T) ∪ ((C)⁻) = (T)⁻¹
		case COR_Expressions.Union(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.UniversalRelation():
					match arg2:
						case COR_Expressions.Complement(argument=arg):
							match arg:
								case _:
									C = arg
									return COR_Expressions.Converse(COR_Expressions.UniversalRelation())
		# (B) † ((𝟎)⁻) = (T)⁻¹
		case COR_Expressions.Dagger(argument1=arg1, argument2=arg2):
			match arg1:
				case _:
					B = arg1
					match arg2:
						case COR_Expressions.Complement(argument=arg):
							match arg:
								case COR_Expressions.EmptyRelation():
									return COR_Expressions.Converse(COR_Expressions.UniversalRelation())
		# (T) † ((𝟎)⁻) = (𝟎)⁻
		case COR_Expressions.Dagger(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.UniversalRelation():
					match arg2:
						case COR_Expressions.Complement(argument=arg):
							match arg:
								case COR_Expressions.EmptyRelation():
									return COR_Expressions.Complement(COR_Expressions.EmptyRelation())
		# (𝟏) ∘ ((𝟏)⁻) = (𝟏)⁻
		case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.IdentityRelation:
					match arg2:
						case COR_Expressions.Complement(argument=arg):
							match arg:
								case COR_Expressions.IdentityRelation:
									return COR_Expressions.Complement(COR_Expressions.IdentityRelation())
		# (C) † ((𝟎)⁻) = (𝟎)⁻
		case COR_Expressions.Dagger(argument1=arg1, argument2=arg2):
			match arg1:
				case _:
					C = arg1
					match arg2:
						case COR_Expressions.Complement(argument=arg):
							match arg:
								case COR_Expressions.EmptyRelation():
									return COR_Expressions.Complement(COR_Expressions.EmptyRelation())
		# ((A)⁻)⁻ = A
		case COR_Expressions.Complement(argument=arg):
			match arg:
				case COR_Expressions.Complement(argument=arg):
					match arg:
						case _:
							A = arg
							return A
		# (T) † ((C)⁻) = T
		case COR_Expressions.Dagger(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.UniversalRelation():
					match arg2:
						case COR_Expressions.Complement(argument=arg):
							match arg:
								case _:
									C = arg
									return COR_Expressions.UniversalRelation()
		# (T) ∪ ((B)⁻¹) = (T)⁻¹
		case COR_Expressions.Union(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.UniversalRelation():
					match arg2:
						case COR_Expressions.Converse(argument=arg):
							match arg:
								case _:
									B = arg
									return COR_Expressions.Converse(COR_Expressions.UniversalRelation())
		# (𝟏) ∘ ((𝟎)⁻¹) = (T)⁻
		case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.IdentityRelation:
					match arg2:
						case COR_Expressions.Converse(argument=arg):
							match arg:
								case COR_Expressions.EmptyRelation():
									return COR_Expressions.Complement(COR_Expressions.UniversalRelation())
		# ((𝟏)⁻¹)⁻¹ = (𝟏)⁻¹
		case COR_Expressions.Converse(argument=arg):
			match arg:
				case COR_Expressions.Converse(argument=arg):
					match arg:
						case COR_Expressions.IdentityRelation:
							return COR_Expressions.Converse(COR_Expressions.IdentityRelation())
		# ((T)⁻¹)⁻¹ = T
		case COR_Expressions.Converse(argument=arg):
			match arg:
				case COR_Expressions.Converse(argument=arg):
					match arg:
						case COR_Expressions.UniversalRelation():
							return COR_Expressions.UniversalRelation()
		# (A) ∪ ((A)⁻) = T
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
		# (T) ∪ ((𝟏)⁻) = T
		case COR_Expressions.Union(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.UniversalRelation():
					match arg2:
						case COR_Expressions.Complement(argument=arg):
							match arg:
								case COR_Expressions.IdentityRelation:
									return COR_Expressions.UniversalRelation()
		# (𝟎) ∪ ((𝟎)⁻¹) = 𝟎
		case COR_Expressions.Union(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.EmptyRelation():
					match arg2:
						case COR_Expressions.Converse(argument=arg):
							match arg:
								case COR_Expressions.EmptyRelation():
									return COR_Expressions.EmptyRelation()
		# (𝟏) † ((𝟎)⁻) = T
		case COR_Expressions.Dagger(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.IdentityRelation:
					match arg2:
						case COR_Expressions.Complement(argument=arg):
							match arg:
								case COR_Expressions.EmptyRelation():
									return COR_Expressions.UniversalRelation()
		# (T) ∪ ((T)⁻¹) = (𝟎)⁻
		case COR_Expressions.Union(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.UniversalRelation():
					match arg2:
						case COR_Expressions.Converse(argument=arg):
							match arg:
								case COR_Expressions.UniversalRelation():
									return COR_Expressions.Complement(COR_Expressions.EmptyRelation())
		# ((𝟏)⁻)⁻¹ = (𝟏)⁻
		case COR_Expressions.Converse(argument=arg):
			match arg:
				case COR_Expressions.Complement(argument=arg):
					match arg:
						case COR_Expressions.IdentityRelation:
							return COR_Expressions.Complement(COR_Expressions.IdentityRelation())
		# ((𝟎)⁻¹)⁻ = (T)⁻¹
		case COR_Expressions.Complement(argument=arg):
			match arg:
				case COR_Expressions.Converse(argument=arg):
					match arg:
						case COR_Expressions.EmptyRelation():
							return COR_Expressions.Converse(COR_Expressions.UniversalRelation())
		# (𝟏) ∘ ((𝟎)⁻) = T
		case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.IdentityRelation:
					match arg2:
						case COR_Expressions.Complement(argument=arg):
							match arg:
								case COR_Expressions.EmptyRelation():
									return COR_Expressions.UniversalRelation()
		# (𝟎) ∪ ((B)⁻¹) = (B)⁻¹
		case COR_Expressions.Union(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.EmptyRelation():
					match arg2:
						case COR_Expressions.Converse(argument=arg):
							match arg:
								case _:
									B = arg
									return COR_Expressions.Converse(B)
		# (𝟎) ∘ ((T)⁻) = (𝟎)⁻¹
		case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.EmptyRelation():
					match arg2:
						case COR_Expressions.Complement(argument=arg):
							match arg:
								case COR_Expressions.UniversalRelation():
									return COR_Expressions.Converse(COR_Expressions.EmptyRelation())
		# (T) ∘ ((𝟏)⁻¹) = T
		case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.UniversalRelation():
					match arg2:
						case COR_Expressions.Converse(argument=arg):
							match arg:
								case COR_Expressions.IdentityRelation:
									return COR_Expressions.UniversalRelation()
		# (C) ∪ ((T)⁻¹) = T
		case COR_Expressions.Union(argument1=arg1, argument2=arg2):
			match arg1:
				case _:
					C = arg1
					match arg2:
						case COR_Expressions.Converse(argument=arg):
							match arg:
								case COR_Expressions.UniversalRelation():
									return COR_Expressions.UniversalRelation()
		# (T) ∪ ((𝟎)⁻¹) = (𝟎)⁻
		case COR_Expressions.Union(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.UniversalRelation():
					match arg2:
						case COR_Expressions.Converse(argument=arg):
							match arg:
								case COR_Expressions.EmptyRelation():
									return COR_Expressions.Complement(COR_Expressions.EmptyRelation())
		# ((𝟎)⁻¹)⁻¹ = (𝟎)⁻¹
		case COR_Expressions.Converse(argument=arg):
			match arg:
				case COR_Expressions.Converse(argument=arg):
					match arg:
						case COR_Expressions.EmptyRelation():
							return COR_Expressions.Converse(COR_Expressions.EmptyRelation())
		# ((B)⁻)⁻ = B
		case COR_Expressions.Complement(argument=arg):
			match arg:
				case COR_Expressions.Complement(argument=arg):
					match arg:
						case _:
							B = arg
							return B
		# (𝟏) ∘ ((A)⁻¹) = (A)⁻¹
		case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.IdentityRelation:
					match arg2:
						case COR_Expressions.Converse(argument=arg):
							match arg:
								case _:
									A = arg
									return COR_Expressions.Converse(A)
		# (𝟏) ∘ ((T)⁻¹) = T
		case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.IdentityRelation:
					match arg2:
						case COR_Expressions.Converse(argument=arg):
							match arg:
								case COR_Expressions.UniversalRelation():
									return COR_Expressions.UniversalRelation()
		# (𝟏) ∘ ((C)⁻) = (C)⁻
		case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.IdentityRelation:
					match arg2:
						case COR_Expressions.Complement(argument=arg):
							match arg:
								case _:
									C = arg
									return COR_Expressions.Complement(C)
		# (A) † ((𝟎)⁻) = (T)⁻¹
		case COR_Expressions.Dagger(argument1=arg1, argument2=arg2):
			match arg1:
				case _:
					A = arg1
					match arg2:
						case COR_Expressions.Complement(argument=arg):
							match arg:
								case COR_Expressions.EmptyRelation():
									return COR_Expressions.Converse(COR_Expressions.UniversalRelation())
		# (𝟎) ∪ ((B)⁻) = (B)⁻
		case COR_Expressions.Union(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.EmptyRelation():
					match arg2:
						case COR_Expressions.Complement(argument=arg):
							match arg:
								case _:
									B = arg
									return COR_Expressions.Complement(B)
		# (𝟎) ∘ ((C)⁻) = (T)⁻
		case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.EmptyRelation():
					match arg2:
						case COR_Expressions.Complement(argument=arg):
							match arg:
								case _:
									C = arg
									return COR_Expressions.Complement(COR_Expressions.UniversalRelation())
		# (𝟏) ∪ ((𝟏)⁻) = (T)⁻¹
		case COR_Expressions.Union(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.IdentityRelation:
					match arg2:
						case COR_Expressions.Complement(argument=arg):
							match arg:
								case COR_Expressions.IdentityRelation:
									return COR_Expressions.Converse(COR_Expressions.UniversalRelation())
		# (T) ∘ ((T)⁻¹) = T
		case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.UniversalRelation():
					match arg2:
						case COR_Expressions.Converse(argument=arg):
							match arg:
								case COR_Expressions.UniversalRelation():
									return COR_Expressions.UniversalRelation()
		# (T) ∘ ((𝟎)⁻¹) = 𝟎
		case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.UniversalRelation():
					match arg2:
						case COR_Expressions.Converse(argument=arg):
							match arg:
								case COR_Expressions.EmptyRelation():
									return COR_Expressions.EmptyRelation()
		# (𝟏) † ((𝟏)⁻) = 𝟏
		case COR_Expressions.Dagger(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.IdentityRelation:
					match arg2:
						case COR_Expressions.Complement(argument=arg):
							match arg:
								case COR_Expressions.IdentityRelation:
									return COR_Expressions.IdentityRelation()
		# (𝟏) ∪ ((𝟏)⁻¹) = 𝟏
		case COR_Expressions.Union(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.IdentityRelation:
					match arg2:
						case COR_Expressions.Converse(argument=arg):
							match arg:
								case COR_Expressions.IdentityRelation:
									return COR_Expressions.IdentityRelation()
		# (C) ∪ ((T)⁻) = C
		case COR_Expressions.Union(argument1=arg1, argument2=arg2):
			match arg1:
				case _:
					C = arg1
					match arg2:
						case COR_Expressions.Complement(argument=arg):
							match arg:
								case COR_Expressions.UniversalRelation():
									return C
		# (𝟏) ∘ ((A)⁻) = (A)⁻
		case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.IdentityRelation:
					match arg2:
						case COR_Expressions.Complement(argument=arg):
							match arg:
								case _:
									A = arg
									return COR_Expressions.Complement(A)
		# (A) ∘ ((T)⁻) = 𝟎
		case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
			match arg1:
				case _:
					A = arg1
					match arg2:
						case COR_Expressions.Complement(argument=arg):
							match arg:
								case COR_Expressions.UniversalRelation():
									return COR_Expressions.EmptyRelation()
		# (𝟎) ∪ ((T)⁻) = 𝟎
		case COR_Expressions.Union(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.EmptyRelation():
					match arg2:
						case COR_Expressions.Complement(argument=arg):
							match arg:
								case COR_Expressions.UniversalRelation():
									return COR_Expressions.EmptyRelation()
		# ((𝟏)⁻)⁻ = (𝟏)⁻¹
		case COR_Expressions.Complement(argument=arg):
			match arg:
				case COR_Expressions.Complement(argument=arg):
					match arg:
						case COR_Expressions.IdentityRelation:
							return COR_Expressions.Converse(COR_Expressions.IdentityRelation())
		# (T) ∪ ((A)⁻) = (𝟎)⁻
		case COR_Expressions.Union(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.UniversalRelation():
					match arg2:
						case COR_Expressions.Complement(argument=arg):
							match arg:
								case _:
									A = arg
									return COR_Expressions.Complement(COR_Expressions.EmptyRelation())
		# (𝟏) ∘ ((𝟏)⁻¹) = 𝟏
		case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.IdentityRelation:
					match arg2:
						case COR_Expressions.Converse(argument=arg):
							match arg:
								case COR_Expressions.IdentityRelation:
									return COR_Expressions.IdentityRelation()
		# (T) † ((𝟎)⁻¹) = (𝟎)⁻
		case COR_Expressions.Dagger(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.UniversalRelation():
					match arg2:
						case COR_Expressions.Converse(argument=arg):
							match arg:
								case COR_Expressions.EmptyRelation():
									return COR_Expressions.Complement(COR_Expressions.EmptyRelation())
		# (C) ∘ ((𝟏)⁻¹) = C
		case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
			match arg1:
				case _:
					C = arg1
					match arg2:
						case COR_Expressions.Converse(argument=arg):
							match arg:
								case COR_Expressions.IdentityRelation:
									return C
		# ((T)⁻)⁻ = (T)⁻¹
		case COR_Expressions.Complement(argument=arg):
			match arg:
				case COR_Expressions.Complement(argument=arg):
					match arg:
						case COR_Expressions.UniversalRelation():
							return COR_Expressions.Converse(COR_Expressions.UniversalRelation())
		# (𝟎) ∪ ((𝟎)⁻) = (T)⁻¹
		case COR_Expressions.Union(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.EmptyRelation():
					match arg2:
						case COR_Expressions.Complement(argument=arg):
							match arg:
								case COR_Expressions.EmptyRelation():
									return COR_Expressions.Converse(COR_Expressions.UniversalRelation())
		# (𝟎) † ((𝟎)⁻¹) = (T)⁻
		case COR_Expressions.Dagger(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.EmptyRelation():
					match arg2:
						case COR_Expressions.Converse(argument=arg):
							match arg:
								case COR_Expressions.EmptyRelation():
									return COR_Expressions.Complement(COR_Expressions.UniversalRelation())
		# (𝟏) ∘ ((C)⁻¹) = (C)⁻¹
		case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.IdentityRelation:
					match arg2:
						case COR_Expressions.Converse(argument=arg):
							match arg:
								case _:
									C = arg
									return COR_Expressions.Converse(C)
		# ((B)⁻¹)⁻¹ = B
		case COR_Expressions.Converse(argument=arg):
			match arg:
				case COR_Expressions.Converse(argument=arg):
					match arg:
						case _:
							B = arg
							return B
		# (B) † ((𝟏)⁻) = B
		case COR_Expressions.Dagger(argument1=arg1, argument2=arg2):
			match arg1:
				case _:
					B = arg1
					match arg2:
						case COR_Expressions.Complement(argument=arg):
							match arg:
								case COR_Expressions.IdentityRelation:
									return B
		# (𝟎) ∘ ((𝟏)⁻) = 𝟎
		case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.EmptyRelation():
					match arg2:
						case COR_Expressions.Complement(argument=arg):
							match arg:
								case COR_Expressions.IdentityRelation:
									return COR_Expressions.EmptyRelation()
		# (C) ∘ ((𝟎)⁻¹) = (T)⁻
		case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
			match arg1:
				case _:
					C = arg1
					match arg2:
						case COR_Expressions.Converse(argument=arg):
							match arg:
								case COR_Expressions.EmptyRelation():
									return COR_Expressions.Complement(COR_Expressions.UniversalRelation())
		# (𝟏) ∪ ((T)⁻) = (𝟏)⁻¹
		case COR_Expressions.Union(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.IdentityRelation:
					match arg2:
						case COR_Expressions.Complement(argument=arg):
							match arg:
								case COR_Expressions.UniversalRelation():
									return COR_Expressions.Converse(COR_Expressions.IdentityRelation())
		# (T) † ((A)⁻) = (T)⁻¹
		case COR_Expressions.Dagger(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.UniversalRelation():
					match arg2:
						case COR_Expressions.Complement(argument=arg):
							match arg:
								case _:
									A = arg
									return COR_Expressions.Converse(COR_Expressions.UniversalRelation())
		# (T) † ((B)⁻¹) = T
		case COR_Expressions.Dagger(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.UniversalRelation():
					match arg2:
						case COR_Expressions.Converse(argument=arg):
							match arg:
								case _:
									B = arg
									return COR_Expressions.UniversalRelation()
		# (𝟎) ∪ ((𝟏)⁻¹) = 𝟏
		case COR_Expressions.Union(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.EmptyRelation():
					match arg2:
						case COR_Expressions.Converse(argument=arg):
							match arg:
								case COR_Expressions.IdentityRelation:
									return COR_Expressions.IdentityRelation()
		# (C) ∪ ((𝟎)⁻) = T
		case COR_Expressions.Union(argument1=arg1, argument2=arg2):
			match arg1:
				case _:
					C = arg1
					match arg2:
						case COR_Expressions.Complement(argument=arg):
							match arg:
								case COR_Expressions.EmptyRelation():
									return COR_Expressions.UniversalRelation()
		# (𝟎) ∪ ((A)⁻) = (A)⁻
		case COR_Expressions.Union(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.EmptyRelation():
					match arg2:
						case COR_Expressions.Complement(argument=arg):
							match arg:
								case _:
									A = arg
									return COR_Expressions.Complement(A)
		# ((𝟏)⁻¹)⁻ = (𝟏)⁻
		case COR_Expressions.Complement(argument=arg):
			match arg:
				case COR_Expressions.Converse(argument=arg):
					match arg:
						case COR_Expressions.IdentityRelation:
							return COR_Expressions.Complement(COR_Expressions.IdentityRelation())
		# (𝟎) ∪ ((A)⁻¹) = (A)⁻¹
		case COR_Expressions.Union(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.EmptyRelation():
					match arg2:
						case COR_Expressions.Converse(argument=arg):
							match arg:
								case _:
									A = arg
									return COR_Expressions.Converse(A)
		# (𝟎) ∪ ((C)⁻¹) = (C)⁻¹
		case COR_Expressions.Union(argument1=arg1, argument2=arg2):
			match arg1:
				case COR_Expressions.EmptyRelation():
					match arg2:
						case COR_Expressions.Converse(argument=arg):
							match arg:
								case _:
									C = arg
									return COR_Expressions.Converse(C)
		# ((A)⁻¹)⁻¹ = A
		case COR_Expressions.Converse(argument=arg):
			match arg:
				case COR_Expressions.Converse(argument=arg):
					match arg:
						case _:
							A = arg
							return A
		# (B) ∪ ((T)⁻) = B
		case COR_Expressions.Union(argument1=arg1, argument2=arg2):
			match arg1:
				case _:
					B = arg1
					match arg2:
						case COR_Expressions.Complement(argument=arg):
							match arg:
								case COR_Expressions.UniversalRelation():
									return B
		# (A) ∘ ((𝟏)⁻¹) = A
		case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
			match arg1:
				case _:
					A = arg1
					match arg2:
						case COR_Expressions.Converse(argument=arg):
							match arg:
								case COR_Expressions.IdentityRelation:
									return A
		# (B) ∘ ((𝟏)⁻¹) = B
		case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
			match arg1:
				case _:
					B = arg1
					match arg2:
						case COR_Expressions.Converse(argument=arg):
							match arg:
								case COR_Expressions.IdentityRelation:
									return B
		# (𝟏)⁻¹ = 𝟏
		case COR_Expressions.Converse(argument=arg):
			match arg:
				case COR_Expressions.IdentityRelation:
					return COR_Expressions.IdentityRelation()
		# (T)⁻¹ = T
		case COR_Expressions.Converse(argument=arg):
			match arg:
				case COR_Expressions.UniversalRelation():
					return COR_Expressions.UniversalRelation()
		# (𝟎)⁻ = T
		case COR_Expressions.Complement(argument=arg):
			match arg:
				case COR_Expressions.EmptyRelation():
					return COR_Expressions.UniversalRelation()
		# (T)⁻ = 𝟎
		case COR_Expressions.Complement(argument=arg):
			match arg:
				case COR_Expressions.UniversalRelation():
					return COR_Expressions.EmptyRelation()
		# (𝟎)⁻¹ = 𝟎
		case COR_Expressions.Converse(argument=arg):
			match arg:
				case COR_Expressions.EmptyRelation():
					return COR_Expressions.EmptyRelation()
		# (𝟎) † ((C) ∘ ((T)⁻)) = (T)⁻
		case COR_Expressions.Dagger(argument1=arg1, argument2=arg2):
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
												case COR_Expressions.UniversalRelation():
													return COR_Expressions.Complement(COR_Expressions.UniversalRelation())
		# (𝟏) ∪ ((C) ∪ ((T)⁻¹)) = (C) † ((T)⁻¹)
		case COR_Expressions.Union(argument1=arg1, argument2=arg2):
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
												case COR_Expressions.UniversalRelation():
													return COR_Expressions.Dagger(C, COR_Expressions.Converse(COR_Expressions.UniversalRelation()))
		# (C) † ((A) † ((T)⁻¹)) = ((𝟎)⁻)⁻¹
		case COR_Expressions.Dagger(argument1=arg1, argument2=arg2):
			match arg1:
				case _:
					C = arg1
					match arg2:
						case COR_Expressions.Dagger(argument1=arg1, argument2=arg2):
							match arg1:
								case _:
									A = arg1
									match arg2:
										case COR_Expressions.Converse(argument=arg):
											match arg:
												case COR_Expressions.UniversalRelation():
													return COR_Expressions.Converse(COR_Expressions.Complement(COR_Expressions.EmptyRelation()))
		# (((T)⁻)⁻)⁻ = (𝟎) † ((𝟎)⁻¹)
		case COR_Expressions.Complement(argument=arg):
			match arg:
				case COR_Expressions.Complement(argument=arg):
					match arg:
						case COR_Expressions.Complement(argument=arg):
							match arg:
								case COR_Expressions.UniversalRelation():
									return COR_Expressions.Dagger(COR_Expressions.EmptyRelation(), COR_Expressions.Converse(COR_Expressions.EmptyRelation()))
		# (((𝟎)⁻)⁻)⁻ = (B) † ((𝟎)⁻)
		case COR_Expressions.Complement(argument=arg):
			match arg:
				case COR_Expressions.Complement(argument=arg):
					match arg:
						case COR_Expressions.Complement(argument=arg):
							match arg:
								case COR_Expressions.EmptyRelation():
									return COR_Expressions.Dagger(B, COR_Expressions.Complement(COR_Expressions.EmptyRelation()))
		# (𝟏) ∘ ((B) † ((𝟎)⁻)) = (𝟎)⁻
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
												case COR_Expressions.EmptyRelation():
													return COR_Expressions.Complement(COR_Expressions.EmptyRelation())
		# (𝟏) ∪ ((C) ∪ ((C)⁻)) = (C) ∪ ((C)⁻)
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
												case _:
													C = arg
													return COR_Expressions.Union(C, COR_Expressions.Complement(C))
		# (𝟏) ∘ ((B) † ((𝟏)⁻)) = (B) ∪ ((𝟎)⁻¹)
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
												case COR_Expressions.IdentityRelation:
													return COR_Expressions.Union(B, COR_Expressions.Converse(COR_Expressions.EmptyRelation()))
		# (((B)⁻)⁻)⁻ = (B)⁻
		case COR_Expressions.Complement(argument=arg):
			match arg:
				case COR_Expressions.Complement(argument=arg):
					match arg:
						case COR_Expressions.Complement(argument=arg):
							match arg:
								case _:
									B = arg
									return COR_Expressions.Complement(B)
		# (𝟏) ∪ ((C) ∪ ((𝟎)⁻¹)) = (C) ∪ ((𝟏)⁻¹)
		case COR_Expressions.Union(argument1=arg1, argument2=arg2):
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
												case COR_Expressions.EmptyRelation():
													return COR_Expressions.Union(C, COR_Expressions.Converse(COR_Expressions.IdentityRelation()))
		# (((𝟏)⁻)⁻)⁻ = (𝟎) ∪ ((𝟏)⁻)
		case COR_Expressions.Complement(argument=arg):
			match arg:
				case COR_Expressions.Complement(argument=arg):
					match arg:
						case COR_Expressions.Complement(argument=arg):
							match arg:
								case COR_Expressions.IdentityRelation:
									return COR_Expressions.Union(COR_Expressions.EmptyRelation(), COR_Expressions.Complement(COR_Expressions.IdentityRelation()))
		# (𝟏) ∘ ((B) † ((T)⁻)) = (B) † ((T)⁻)
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
												case COR_Expressions.UniversalRelation():
													return COR_Expressions.Dagger(B, COR_Expressions.Complement(COR_Expressions.UniversalRelation()))
		# (((A)⁻)⁻)⁻ = (𝟎) ∪ ((A)⁻)
		case COR_Expressions.Complement(argument=arg):
			match arg:
				case COR_Expressions.Complement(argument=arg):
					match arg:
						case COR_Expressions.Complement(argument=arg):
							match arg:
								case _:
									A = arg
									return COR_Expressions.Union(COR_Expressions.EmptyRelation(), COR_Expressions.Complement(A))
		# (𝟏) ∘ ((B) † ((A)⁻)) = (B) † ((A)⁻)
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
		# (((𝟎)⁻¹)⁻)⁻ = (𝟎) ∘ ((T)⁻¹)
		case COR_Expressions.Complement(argument=arg):
			match arg:
				case COR_Expressions.Complement(argument=arg):
					match arg:
						case COR_Expressions.Converse(argument=arg):
							match arg:
								case COR_Expressions.EmptyRelation():
									return COR_Expressions.Composition(COR_Expressions.EmptyRelation(), COR_Expressions.Converse(COR_Expressions.UniversalRelation()))
		# (𝟏) ∘ ((B) † ((T)⁻¹)) = (A) ∪ ((𝟎)⁻)
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
												case COR_Expressions.UniversalRelation():
													return COR_Expressions.Union(A, COR_Expressions.Complement(COR_Expressions.EmptyRelation()))
		# (((T)⁻¹)⁻)⁻ = (𝟏) ∪ ((𝟎)⁻)
		case COR_Expressions.Complement(argument=arg):
			match arg:
				case COR_Expressions.Complement(argument=arg):
					match arg:
						case COR_Expressions.Converse(argument=arg):
							match arg:
								case COR_Expressions.UniversalRelation():
									return COR_Expressions.Union(COR_Expressions.IdentityRelation(), COR_Expressions.Complement(COR_Expressions.EmptyRelation()))
		# (((C)⁻)⁻)⁻ = (𝟎) ∪ ((C)⁻)
		case COR_Expressions.Complement(argument=arg):
			match arg:
				case COR_Expressions.Complement(argument=arg):
					match arg:
						case COR_Expressions.Complement(argument=arg):
							match arg:
								case _:
									C = arg
									return COR_Expressions.Union(COR_Expressions.EmptyRelation(), COR_Expressions.Complement(C))
		# (((𝟏)⁻¹)⁻)⁻ = ((𝟏)⁻¹)⁻¹
		case COR_Expressions.Complement(argument=arg):
			match arg:
				case COR_Expressions.Complement(argument=arg):
					match arg:
						case COR_Expressions.Converse(argument=arg):
							match arg:
								case COR_Expressions.IdentityRelation:
									return COR_Expressions.Converse(COR_Expressions.Converse(COR_Expressions.IdentityRelation()))
		# (C) ∘ ((C) ∪ ((𝟎)⁻)) = (C) ∘ ((𝟎)⁻)
		case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
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
												case COR_Expressions.EmptyRelation():
													return COR_Expressions.Composition(C, COR_Expressions.Complement(COR_Expressions.EmptyRelation()))
		# (𝟏) ∘ ((B) † ((𝟏)⁻¹)) = (B) † ((𝟏)⁻¹)
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
												case COR_Expressions.IdentityRelation:
													return COR_Expressions.Dagger(B, COR_Expressions.Converse(COR_Expressions.IdentityRelation()))
		# (𝟏) ∘ ((B) † ((𝟎)⁻¹)) = (B) † ((T)⁻)
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
												case COR_Expressions.EmptyRelation():
													return COR_Expressions.Dagger(B, COR_Expressions.Complement(COR_Expressions.UniversalRelation()))
		# (((A)⁻¹)⁻)⁻ = (A)⁻¹
		case COR_Expressions.Complement(argument=arg):
			match arg:
				case COR_Expressions.Complement(argument=arg):
					match arg:
						case COR_Expressions.Converse(argument=arg):
							match arg:
								case _:
									A = arg
									return COR_Expressions.Converse(A)
		# (𝟏) ∘ ((B) † ((C)⁻)) = (B) † ((C)⁻)
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
		# (𝟏) ∪ ((C) ∪ ((𝟏)⁻¹)) = (C) ∪ ((𝟏)⁻¹)
		case COR_Expressions.Union(argument1=arg1, argument2=arg2):
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
												case COR_Expressions.IdentityRelation:
													return COR_Expressions.Union(C, COR_Expressions.Converse(COR_Expressions.IdentityRelation()))
		case _:
			return expression