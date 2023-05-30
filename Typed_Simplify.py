import Typed_COR_Expressions

def simplify(expression):
	P = expression.type()[0]
	Q = expression.type()[1]
	if isinstance(expression, Typed_COR_Expressions.Typed_Union):
		lhs1, rhs1 = expression.argument1, expression.argument2
		if P==lhs1.type()[0]:
			if Q==lhs1.type()[1]:
				A = lhs1
				if P==rhs1.type()[0]:
					if Q==rhs1.type()[1]:
						if str(A)==str(rhs1):
							return ("(A[P*Q]) ∪ (A[P*Q]) = A[P*Q]", A)
						if isinstance(rhs1, Typed_COR_Expressions.Typed_Intersection):
							lhs6, rhs6 = rhs1.argument1, rhs1.argument2
							if P==lhs6.type()[0]:
								if Q==lhs6.type()[1]:
									B = lhs6
									if P==rhs6.type()[0]:
										if Q==rhs6.type()[1]:
											if str(A)==str(rhs6):
												return ("(A[P*Q]) ∪ ((B[P*Q]) ∩ (A[P*Q])) = A[P*Q]", A)
											if isinstance(rhs6, Typed_COR_Expressions.Typed_Complement):
												arg = rhs6.argument
												if P==arg.type()[0]:
													if Q==arg.type()[1]:
														if str(A)==str(arg):
															return ("(A[P*Q]) ∪ ((B[P*Q]) ∩ ((A[P*Q])⁻)) = (A[P*Q]) ∪ (B[P*Q])", Typed_COR_Expressions.Typed_Union(A, B))
											if isinstance(rhs6, Typed_COR_Expressions.Typed_Union):
												lhs11, rhs11 = rhs6.argument1, rhs6.argument2
												if P==lhs11.type()[0]:
													if Q==lhs11.type()[1]:
														if str(A)==str(lhs11):
															if P==rhs11.type()[0]:
																if Q==rhs11.type()[1]:
																	C = rhs11
																	return ("(A[P*Q]) ∪ ((B[P*Q]) ∩ ((A[P*Q]) ∪ (C[P*Q]))) = (A[P*Q]) ∪ ((C[P*Q]) ∩ (B[P*Q]))", Typed_COR_Expressions.Typed_Union(A, Typed_COR_Expressions.Typed_Intersection(C, B)))
														C = lhs11
														if P==rhs11.type()[0]:
															if Q==rhs11.type()[1]:
																if str(A)==str(rhs11):
																	return ("(A[P*Q]) ∪ ((B[P*Q]) ∩ ((C[P*Q]) ∪ (A[P*Q]))) = (A[P*Q]) ∪ ((B[P*Q]) ∩ (C[P*Q]))", Typed_COR_Expressions.Typed_Union(A, Typed_COR_Expressions.Typed_Intersection(B, C)))
											if isinstance(rhs6, Typed_COR_Expressions.Typed_Intersection):
												lhs11, rhs11 = rhs6.argument1, rhs6.argument2
												if P==lhs11.type()[0]:
													if Q==lhs11.type()[1]:
														C = lhs11
														if P==rhs11.type()[0]:
															if Q==rhs11.type()[1]:
																if str(A)==str(rhs11):
																	return ("(A[P*Q]) ∪ ((B[P*Q]) ∩ ((C[P*Q]) ∩ (A[P*Q]))) = A[P*Q]", A)
														if str(A)==str(lhs11):
															if P==rhs11.type()[0]:
																if Q==rhs11.type()[1]:
																	C = rhs11
																	return ("(A[P*Q]) ∪ ((B[P*Q]) ∩ ((A[P*Q]) ∩ (C[P*Q]))) = A[P*Q]", A)
									if str(A)==str(lhs6):
										if P==rhs6.type()[0]:
											if Q==rhs6.type()[1]:
												B = rhs6
												return ("(A[P*Q]) ∪ ((A[P*Q]) ∩ (B[P*Q])) = A[P*Q]", A)
									if isinstance(lhs6, Typed_COR_Expressions.Typed_Union):
										lhs9, rhs9 = lhs6.argument1, lhs6.argument2
										if P==lhs9.type()[0]:
											if Q==lhs9.type()[1]:
												if str(A)==str(lhs9):
													if P==rhs9.type()[0]:
														if Q==rhs9.type()[1]:
															B = rhs9
															if P==rhs6.type()[0]:
																if Q==rhs6.type()[1]:
																	C = rhs6
																	return ("(A[P*Q]) ∪ (((A[P*Q]) ∪ (B[P*Q])) ∩ (C[P*Q])) = (A[P*Q]) ∪ ((B[P*Q]) ∩ (C[P*Q]))", Typed_COR_Expressions.Typed_Union(A, Typed_COR_Expressions.Typed_Intersection(B, C)))
												B = lhs9
												if P==rhs9.type()[0]:
													if Q==rhs9.type()[1]:
														if str(A)==str(rhs9):
															if P==rhs6.type()[0]:
																if Q==rhs6.type()[1]:
																	C = rhs6
																	return ("(A[P*Q]) ∪ (((B[P*Q]) ∪ (A[P*Q])) ∩ (C[P*Q])) = ((B[P*Q]) ∩ (C[P*Q])) ∪ (A[P*Q])", Typed_COR_Expressions.Typed_Union(Typed_COR_Expressions.Typed_Intersection(B, C), A))
									if isinstance(lhs6, Typed_COR_Expressions.Typed_Intersection):
										lhs9, rhs9 = lhs6.argument1, lhs6.argument2
										if P==lhs9.type()[0]:
											if Q==lhs9.type()[1]:
												B = lhs9
												if P==rhs9.type()[0]:
													if Q==rhs9.type()[1]:
														if str(A)==str(rhs9):
															if P==rhs6.type()[0]:
																if Q==rhs6.type()[1]:
																	C = rhs6
																	return ("(A[P*Q]) ∪ (((B[P*Q]) ∩ (A[P*Q])) ∩ (C[P*Q])) = A[P*Q]", A)
												if str(A)==str(lhs9):
													if P==rhs9.type()[0]:
														if Q==rhs9.type()[1]:
															B = rhs9
															if P==rhs6.type()[0]:
																if Q==rhs6.type()[1]:
																	C = rhs6
																	return ("(A[P*Q]) ∪ (((A[P*Q]) ∩ (B[P*Q])) ∩ (C[P*Q])) = A[P*Q]", A)
									if isinstance(lhs6, Typed_COR_Expressions.Typed_Complement):
										arg = lhs6.argument
										if P==arg.type()[0]:
											if Q==arg.type()[1]:
												if str(A)==str(arg):
													if P==rhs6.type()[0]:
														if Q==rhs6.type()[1]:
															B = rhs6
															return ("(A[P*Q]) ∪ (((A[P*Q])⁻) ∩ (B[P*Q])) = (B[P*Q]) ∪ (A[P*Q])", Typed_COR_Expressions.Typed_Union(B, A))
						if isinstance(rhs1, Typed_COR_Expressions.Typed_UniversalRelation):
							return ("(A[P*Q]) ∪ (T[P*Q]) = T[P*Q]", Typed_COR_Expressions.Typed_UniversalRelation(expression.type()[0], expression.type()[1]))
						if isinstance(rhs1, Typed_COR_Expressions.Typed_Union):
							lhs6, rhs6 = rhs1.argument1, rhs1.argument2
							if P==lhs6.type()[0]:
								if Q==lhs6.type()[1]:
									if str(A)==str(lhs6):
										if P==rhs6.type()[0]:
											if Q==rhs6.type()[1]:
												B = rhs6
												return ("(A[P*Q]) ∪ ((A[P*Q]) ∪ (B[P*Q])) = (A[P*Q]) ∪ (B[P*Q])", Typed_COR_Expressions.Typed_Union(A, B))
									B = lhs6
									if P==rhs6.type()[0]:
										if Q==rhs6.type()[1]:
											if str(A)==str(rhs6):
												return ("(A[P*Q]) ∪ ((B[P*Q]) ∪ (A[P*Q])) = (B[P*Q]) ∪ (A[P*Q])", Typed_COR_Expressions.Typed_Union(B, A))
											if isinstance(rhs6, Typed_COR_Expressions.Typed_Union):
												lhs11, rhs11 = rhs6.argument1, rhs6.argument2
												if P==lhs11.type()[0]:
													if Q==lhs11.type()[1]:
														C = lhs11
														if P==rhs11.type()[0]:
															if Q==rhs11.type()[1]:
																if str(A)==str(rhs11):
																	return ("(A[P*Q]) ∪ ((B[P*Q]) ∪ ((C[P*Q]) ∪ (A[P*Q]))) = (C[P*Q]) ∪ ((A[P*Q]) ∪ (B[P*Q]))", Typed_COR_Expressions.Typed_Union(C, Typed_COR_Expressions.Typed_Union(A, B)))
														if str(A)==str(lhs11):
															if P==rhs11.type()[0]:
																if Q==rhs11.type()[1]:
																	C = rhs11
																	return ("(A[P*Q]) ∪ ((B[P*Q]) ∪ ((A[P*Q]) ∪ (C[P*Q]))) = (C[P*Q]) ∪ ((B[P*Q]) ∪ (A[P*Q]))", Typed_COR_Expressions.Typed_Union(C, Typed_COR_Expressions.Typed_Union(B, A)))
											if isinstance(rhs6, Typed_COR_Expressions.Typed_Intersection):
												lhs11, rhs11 = rhs6.argument1, rhs6.argument2
												if P==lhs11.type()[0]:
													if Q==lhs11.type()[1]:
														if str(A)==str(lhs11):
															if P==rhs11.type()[0]:
																if Q==rhs11.type()[1]:
																	C = rhs11
																	return ("(A[P*Q]) ∪ ((B[P*Q]) ∪ ((A[P*Q]) ∩ (C[P*Q]))) = (B[P*Q]) ∪ (A[P*Q])", Typed_COR_Expressions.Typed_Union(B, A))
														C = lhs11
														if P==rhs11.type()[0]:
															if Q==rhs11.type()[1]:
																if str(A)==str(rhs11):
																	return ("(A[P*Q]) ∪ ((B[P*Q]) ∪ ((C[P*Q]) ∩ (A[P*Q]))) = (A[P*Q]) ∪ (B[P*Q])", Typed_COR_Expressions.Typed_Union(A, B))
											if isinstance(rhs6, Typed_COR_Expressions.Typed_Complement):
												arg = rhs6.argument
												if P==arg.type()[0]:
													if Q==arg.type()[1]:
														if str(A)==str(arg):
															return ("(A[P*Q]) ∪ ((B[P*Q]) ∪ ((A[P*Q])⁻)) = T[P*Q]", Typed_COR_Expressions.Typed_UniversalRelation(expression.type()[0], expression.type()[1]))
									if isinstance(lhs6, Typed_COR_Expressions.Typed_Union):
										lhs9, rhs9 = lhs6.argument1, lhs6.argument2
										if P==lhs9.type()[0]:
											if Q==lhs9.type()[1]:
												B = lhs9
												if P==rhs9.type()[0]:
													if Q==rhs9.type()[1]:
														if str(A)==str(rhs9):
															if P==rhs6.type()[0]:
																if Q==rhs6.type()[1]:
																	C = rhs6
																	return ("(A[P*Q]) ∪ (((B[P*Q]) ∪ (A[P*Q])) ∪ (C[P*Q])) = (C[P*Q]) ∪ ((B[P*Q]) ∪ (A[P*Q]))", Typed_COR_Expressions.Typed_Union(C, Typed_COR_Expressions.Typed_Union(B, A)))
												if str(A)==str(lhs9):
													if P==rhs9.type()[0]:
														if Q==rhs9.type()[1]:
															B = rhs9
															if P==rhs6.type()[0]:
																if Q==rhs6.type()[1]:
																	C = rhs6
																	return ("(A[P*Q]) ∪ (((A[P*Q]) ∪ (B[P*Q])) ∪ (C[P*Q])) = (B[P*Q]) ∪ ((C[P*Q]) ∪ (A[P*Q]))", Typed_COR_Expressions.Typed_Union(B, Typed_COR_Expressions.Typed_Union(C, A)))
									if isinstance(lhs6, Typed_COR_Expressions.Typed_Intersection):
										lhs9, rhs9 = lhs6.argument1, lhs6.argument2
										if P==lhs9.type()[0]:
											if Q==lhs9.type()[1]:
												if str(A)==str(lhs9):
													if P==rhs9.type()[0]:
														if Q==rhs9.type()[1]:
															B = rhs9
															if P==rhs6.type()[0]:
																if Q==rhs6.type()[1]:
																	C = rhs6
																	return ("(A[P*Q]) ∪ (((A[P*Q]) ∩ (B[P*Q])) ∪ (C[P*Q])) = (C[P*Q]) ∪ (A[P*Q])", Typed_COR_Expressions.Typed_Union(C, A))
												B = lhs9
												if P==rhs9.type()[0]:
													if Q==rhs9.type()[1]:
														if str(A)==str(rhs9):
															if P==rhs6.type()[0]:
																if Q==rhs6.type()[1]:
																	C = rhs6
																	return ("(A[P*Q]) ∪ (((B[P*Q]) ∩ (A[P*Q])) ∪ (C[P*Q])) = (C[P*Q]) ∪ (A[P*Q])", Typed_COR_Expressions.Typed_Union(C, A))
									if isinstance(lhs6, Typed_COR_Expressions.Typed_Complement):
										arg = lhs6.argument
										if P==arg.type()[0]:
											if Q==arg.type()[1]:
												if str(A)==str(arg):
													if P==rhs6.type()[0]:
														if Q==rhs6.type()[1]:
															B = rhs6
															return ("(A[P*Q]) ∪ (((A[P*Q])⁻) ∪ (B[P*Q])) = T[P*Q]", Typed_COR_Expressions.Typed_UniversalRelation(expression.type()[0], expression.type()[1]))
						if isinstance(rhs1, Typed_COR_Expressions.Typed_Complement):
							arg = rhs1.argument
							if P==arg.type()[0]:
								if Q==arg.type()[1]:
									if str(A)==str(arg):
										return ("(A[P*Q]) ∪ ((A[P*Q])⁻) = T[P*Q]", Typed_COR_Expressions.Typed_UniversalRelation(expression.type()[0], expression.type()[1]))
									if isinstance(arg, Typed_COR_Expressions.Typed_Union):
										lhs9, rhs9 = arg.argument1, arg.argument2
										if P==lhs9.type()[0]:
											if Q==lhs9.type()[1]:
												if str(A)==str(lhs9):
													if P==rhs9.type()[0]:
														if Q==rhs9.type()[1]:
															B = rhs9
															return ("(A[P*Q]) ∪ (((A[P*Q]) ∪ (B[P*Q]))⁻) = (A[P*Q]) ∪ ((B[P*Q])⁻)", Typed_COR_Expressions.Typed_Union(A, Typed_COR_Expressions.Typed_Complement(B)))
												B = lhs9
												if P==rhs9.type()[0]:
													if Q==rhs9.type()[1]:
														if str(A)==str(rhs9):
															return ("(A[P*Q]) ∪ (((B[P*Q]) ∪ (A[P*Q]))⁻) = (A[P*Q]) ∪ ((B[P*Q])⁻)", Typed_COR_Expressions.Typed_Union(A, Typed_COR_Expressions.Typed_Complement(B)))
									if isinstance(arg, Typed_COR_Expressions.Typed_Intersection):
										lhs9, rhs9 = arg.argument1, arg.argument2
										if P==lhs9.type()[0]:
											if Q==lhs9.type()[1]:
												if str(A)==str(lhs9):
													if P==rhs9.type()[0]:
														if Q==rhs9.type()[1]:
															B = rhs9
															return ("(A[P*Q]) ∪ (((A[P*Q]) ∩ (B[P*Q]))⁻) = T[P*Q]", Typed_COR_Expressions.Typed_UniversalRelation(expression.type()[0], expression.type()[1]))
												B = lhs9
												if P==rhs9.type()[0]:
													if Q==rhs9.type()[1]:
														if str(A)==str(rhs9):
															return ("(A[P*Q]) ∪ (((B[P*Q]) ∩ (A[P*Q]))⁻) = T[P*Q]", Typed_COR_Expressions.Typed_UniversalRelation(expression.type()[0], expression.type()[1]))
						if isinstance(rhs1, Typed_COR_Expressions.Typed_EmptyRelation):
							return ("(A[P*Q]) ∪ (𝟎[P*Q]) = A[P*Q]", A)
						if isinstance(rhs1, Typed_COR_Expressions.Typed_Composition):
							lhs6, rhs6 = rhs1.argument1, rhs1.argument2
							if P==lhs6.type()[0]:
								if Q==lhs6.type()[1]:
									if str(A)==str(lhs6):
										if Q==rhs6.type()[0]:
											if Q==rhs6.type()[1]:
												if isinstance(rhs6, Typed_COR_Expressions.Typed_UniversalRelation):
													return ("(A[P*Q]) ∪ ((A[P*Q]) ∘ (T[Q*Q])) = (A[P*Q]) ∘ (T[Q*Q])", Typed_COR_Expressions.Typed_Composition(A, Typed_COR_Expressions.Typed_UniversalRelation(A.type()[1], expression.type()[1])))
								if P==lhs6.type()[1]:
									if isinstance(lhs6, Typed_COR_Expressions.Typed_UniversalRelation):
										if P==rhs6.type()[0]:
											if Q==rhs6.type()[1]:
												if str(A)==str(rhs6):
													return ("(A[P*Q]) ∪ ((T[P*P]) ∘ (A[P*Q])) = (T[P*P]) ∘ (A[P*Q])", Typed_COR_Expressions.Typed_Composition(Typed_COR_Expressions.Typed_UniversalRelation(expression.type()[0], A.type()[0]), A))
						if isinstance(rhs1, Typed_COR_Expressions.Typed_Dagger):
							lhs6, rhs6 = rhs1.argument1, rhs1.argument2
							if P==lhs6.type()[0]:
								if P==lhs6.type()[1]:
									if isinstance(lhs6, Typed_COR_Expressions.Typed_EmptyRelation):
										if P==rhs6.type()[0]:
											if Q==rhs6.type()[1]:
												if str(A)==str(rhs6):
													return ("(A[P*Q]) ∪ ((𝟎[P*P]) † (A[P*Q])) = A[P*Q]", A)
								if Q==lhs6.type()[1]:
									if str(A)==str(lhs6):
										if Q==rhs6.type()[0]:
											if Q==rhs6.type()[1]:
												if isinstance(rhs6, Typed_COR_Expressions.Typed_EmptyRelation):
													return ("(A[P*Q]) ∪ ((A[P*Q]) † (𝟎[Q*Q])) = A[P*Q]", A)
				if isinstance(lhs1, Typed_COR_Expressions.Typed_Union):
					lhs4, rhs4 = lhs1.argument1, lhs1.argument2
					if P==lhs4.type()[0]:
						if Q==lhs4.type()[1]:
							A = lhs4
							if P==rhs4.type()[0]:
								if Q==rhs4.type()[1]:
									B = rhs4
									if P==rhs1.type()[0]:
										if Q==rhs1.type()[1]:
											if str(B)==str(rhs1):
												return ("((A[P*Q]) ∪ (B[P*Q])) ∪ (B[P*Q]) = (B[P*Q]) ∪ (A[P*Q])", Typed_COR_Expressions.Typed_Union(B, A))
											if str(A)==str(rhs1):
												return ("((A[P*Q]) ∪ (B[P*Q])) ∪ (A[P*Q]) = (A[P*Q]) ∪ (B[P*Q])", Typed_COR_Expressions.Typed_Union(A, B))
											if isinstance(rhs1, Typed_COR_Expressions.Typed_Union):
												lhs11, rhs11 = rhs1.argument1, rhs1.argument2
												if P==lhs11.type()[0]:
													if Q==lhs11.type()[1]:
														if str(A)==str(lhs11):
															if P==rhs11.type()[0]:
																if Q==rhs11.type()[1]:
																	C = rhs11
																	return ("((A[P*Q]) ∪ (B[P*Q])) ∪ ((A[P*Q]) ∪ (C[P*Q])) = ((A[P*Q]) ∪ (B[P*Q])) ∪ (C[P*Q])", Typed_COR_Expressions.Typed_Union(Typed_COR_Expressions.Typed_Union(A, B), C))
														if str(B)==str(lhs11):
															if P==rhs11.type()[0]:
																if Q==rhs11.type()[1]:
																	C = rhs11
																	return ("((A[P*Q]) ∪ (B[P*Q])) ∪ ((B[P*Q]) ∪ (C[P*Q])) = (C[P*Q]) ∪ ((B[P*Q]) ∪ (A[P*Q]))", Typed_COR_Expressions.Typed_Union(C, Typed_COR_Expressions.Typed_Union(B, A)))
														C = lhs11
														if P==rhs11.type()[0]:
															if Q==rhs11.type()[1]:
																if str(B)==str(rhs11):
																	return ("((A[P*Q]) ∪ (B[P*Q])) ∪ ((C[P*Q]) ∪ (B[P*Q])) = ((A[P*Q]) ∪ (C[P*Q])) ∪ (B[P*Q])", Typed_COR_Expressions.Typed_Union(Typed_COR_Expressions.Typed_Union(A, C), B))
																if str(A)==str(rhs11):
																	return ("((A[P*Q]) ∪ (B[P*Q])) ∪ ((C[P*Q]) ∪ (A[P*Q])) = (B[P*Q]) ∪ ((A[P*Q]) ∪ (C[P*Q]))", Typed_COR_Expressions.Typed_Union(B, Typed_COR_Expressions.Typed_Union(A, C)))
											if isinstance(rhs1, Typed_COR_Expressions.Typed_Complement):
												arg = rhs1.argument
												if P==arg.type()[0]:
													if Q==arg.type()[1]:
														if str(B)==str(arg):
															return ("((A[P*Q]) ∪ (B[P*Q])) ∪ ((B[P*Q])⁻) = T[P*Q]", Typed_COR_Expressions.Typed_UniversalRelation(expression.type()[0], expression.type()[1]))
														if str(A)==str(arg):
															return ("((A[P*Q]) ∪ (B[P*Q])) ∪ ((A[P*Q])⁻) = T[P*Q]", Typed_COR_Expressions.Typed_UniversalRelation(expression.type()[0], expression.type()[1]))
											if isinstance(rhs1, Typed_COR_Expressions.Typed_Intersection):
												lhs11, rhs11 = rhs1.argument1, rhs1.argument2
												if P==lhs11.type()[0]:
													if Q==lhs11.type()[1]:
														if str(B)==str(lhs11):
															if P==rhs11.type()[0]:
																if Q==rhs11.type()[1]:
																	C = rhs11
																	return ("((A[P*Q]) ∪ (B[P*Q])) ∪ ((B[P*Q]) ∩ (C[P*Q])) = (A[P*Q]) ∪ (B[P*Q])", Typed_COR_Expressions.Typed_Union(A, B))
														if str(A)==str(lhs11):
															if P==rhs11.type()[0]:
																if Q==rhs11.type()[1]:
																	C = rhs11
																	return ("((A[P*Q]) ∪ (B[P*Q])) ∪ ((A[P*Q]) ∩ (C[P*Q])) = (A[P*Q]) ∪ (B[P*Q])", Typed_COR_Expressions.Typed_Union(A, B))
														C = lhs11
														if P==rhs11.type()[0]:
															if Q==rhs11.type()[1]:
																if str(A)==str(rhs11):
																	return ("((A[P*Q]) ∪ (B[P*Q])) ∪ ((C[P*Q]) ∩ (A[P*Q])) = (B[P*Q]) ∪ (A[P*Q])", Typed_COR_Expressions.Typed_Union(B, A))
																if str(B)==str(rhs11):
																	return ("((A[P*Q]) ∪ (B[P*Q])) ∪ ((C[P*Q]) ∩ (B[P*Q])) = (B[P*Q]) ∪ (A[P*Q])", Typed_COR_Expressions.Typed_Union(B, A))
									if isinstance(rhs4, Typed_COR_Expressions.Typed_Union):
										lhs9, rhs9 = rhs4.argument1, rhs4.argument2
										if P==lhs9.type()[0]:
											if Q==lhs9.type()[1]:
												B = lhs9
												if P==rhs9.type()[0]:
													if Q==rhs9.type()[1]:
														C = rhs9
														if P==rhs1.type()[0]:
															if Q==rhs1.type()[1]:
																if str(C)==str(rhs1):
																	return ("((A[P*Q]) ∪ ((B[P*Q]) ∪ (C[P*Q]))) ∪ (C[P*Q]) = (B[P*Q]) ∪ ((A[P*Q]) ∪ (C[P*Q]))", Typed_COR_Expressions.Typed_Union(B, Typed_COR_Expressions.Typed_Union(A, C)))
																if str(B)==str(rhs1):
																	return ("((A[P*Q]) ∪ ((B[P*Q]) ∪ (C[P*Q]))) ∪ (B[P*Q]) = (A[P*Q]) ∪ ((C[P*Q]) ∪ (B[P*Q]))", Typed_COR_Expressions.Typed_Union(A, Typed_COR_Expressions.Typed_Union(C, B)))
									if isinstance(rhs4, Typed_COR_Expressions.Typed_Intersection):
										lhs9, rhs9 = rhs4.argument1, rhs4.argument2
										if P==lhs9.type()[0]:
											if Q==lhs9.type()[1]:
												B = lhs9
												if P==rhs9.type()[0]:
													if Q==rhs9.type()[1]:
														C = rhs9
														if P==rhs1.type()[0]:
															if Q==rhs1.type()[1]:
																if str(B)==str(rhs1):
																	return ("((A[P*Q]) ∪ ((B[P*Q]) ∩ (C[P*Q]))) ∪ (B[P*Q]) = (A[P*Q]) ∪ (B[P*Q])", Typed_COR_Expressions.Typed_Union(A, B))
																if str(C)==str(rhs1):
																	return ("((A[P*Q]) ∪ ((B[P*Q]) ∩ (C[P*Q]))) ∪ (C[P*Q]) = (C[P*Q]) ∪ (A[P*Q])", Typed_COR_Expressions.Typed_Union(C, A))
									if isinstance(rhs4, Typed_COR_Expressions.Typed_Complement):
										arg = rhs4.argument
										if P==arg.type()[0]:
											if Q==arg.type()[1]:
												B = arg
												if P==rhs1.type()[0]:
													if Q==rhs1.type()[1]:
														if str(B)==str(rhs1):
															return ("((A[P*Q]) ∪ ((B[P*Q])⁻)) ∪ (B[P*Q]) = T[P*Q]", Typed_COR_Expressions.Typed_UniversalRelation(expression.type()[0], expression.type()[1]))
							if isinstance(lhs4, Typed_COR_Expressions.Typed_Union):
								lhs7, rhs7 = lhs4.argument1, lhs4.argument2
								if P==lhs7.type()[0]:
									if Q==lhs7.type()[1]:
										A = lhs7
										if P==rhs7.type()[0]:
											if Q==rhs7.type()[1]:
												B = rhs7
												if P==rhs4.type()[0]:
													if Q==rhs4.type()[1]:
														C = rhs4
														if P==rhs1.type()[0]:
															if Q==rhs1.type()[1]:
																if str(B)==str(rhs1):
																	return ("(((A[P*Q]) ∪ (B[P*Q])) ∪ (C[P*Q])) ∪ (B[P*Q]) = (A[P*Q]) ∪ ((C[P*Q]) ∪ (B[P*Q]))", Typed_COR_Expressions.Typed_Union(A, Typed_COR_Expressions.Typed_Union(C, B)))
																if str(A)==str(rhs1):
																	return ("(((A[P*Q]) ∪ (B[P*Q])) ∪ (C[P*Q])) ∪ (A[P*Q]) = (C[P*Q]) ∪ ((A[P*Q]) ∪ (B[P*Q]))", Typed_COR_Expressions.Typed_Union(C, Typed_COR_Expressions.Typed_Union(A, B)))
							if isinstance(lhs4, Typed_COR_Expressions.Typed_Complement):
								arg = lhs4.argument
								if P==arg.type()[0]:
									if Q==arg.type()[1]:
										A = arg
										if P==rhs4.type()[0]:
											if Q==rhs4.type()[1]:
												B = rhs4
												if P==rhs1.type()[0]:
													if Q==rhs1.type()[1]:
														if str(A)==str(rhs1):
															return ("(((A[P*Q])⁻) ∪ (B[P*Q])) ∪ (A[P*Q]) = T[P*Q]", Typed_COR_Expressions.Typed_UniversalRelation(expression.type()[0], expression.type()[1]))
							if isinstance(lhs4, Typed_COR_Expressions.Typed_Intersection):
								lhs7, rhs7 = lhs4.argument1, lhs4.argument2
								if P==lhs7.type()[0]:
									if Q==lhs7.type()[1]:
										A = lhs7
										if P==rhs7.type()[0]:
											if Q==rhs7.type()[1]:
												B = rhs7
												if P==rhs4.type()[0]:
													if Q==rhs4.type()[1]:
														C = rhs4
														if P==rhs1.type()[0]:
															if Q==rhs1.type()[1]:
																if str(B)==str(rhs1):
																	return ("(((A[P*Q]) ∩ (B[P*Q])) ∪ (C[P*Q])) ∪ (B[P*Q]) = (C[P*Q]) ∪ (B[P*Q])", Typed_COR_Expressions.Typed_Union(C, B))
																if str(A)==str(rhs1):
																	return ("(((A[P*Q]) ∩ (B[P*Q])) ∪ (C[P*Q])) ∪ (A[P*Q]) = (C[P*Q]) ∪ (A[P*Q])", Typed_COR_Expressions.Typed_Union(C, A))
				if isinstance(lhs1, Typed_COR_Expressions.Typed_Complement):
					arg = lhs1.argument
					if P==arg.type()[0]:
						if Q==arg.type()[1]:
							A = arg
							if P==rhs1.type()[0]:
								if Q==rhs1.type()[1]:
									if str(A)==str(rhs1):
										return ("((A[P*Q])⁻) ∪ (A[P*Q]) = T[P*Q]", Typed_COR_Expressions.Typed_UniversalRelation(expression.type()[0], expression.type()[1]))
									if isinstance(rhs1, Typed_COR_Expressions.Typed_Union):
										lhs9, rhs9 = rhs1.argument1, rhs1.argument2
										if P==lhs9.type()[0]:
											if Q==lhs9.type()[1]:
												B = lhs9
												if P==rhs9.type()[0]:
													if Q==rhs9.type()[1]:
														if str(A)==str(rhs9):
															return ("((A[P*Q])⁻) ∪ ((B[P*Q]) ∪ (A[P*Q])) = T[P*Q]", Typed_COR_Expressions.Typed_UniversalRelation(expression.type()[0], expression.type()[1]))
												if str(A)==str(lhs9):
													if P==rhs9.type()[0]:
														if Q==rhs9.type()[1]:
															B = rhs9
															return ("((A[P*Q])⁻) ∪ ((A[P*Q]) ∪ (B[P*Q])) = T[P*Q]", Typed_COR_Expressions.Typed_UniversalRelation(expression.type()[0], expression.type()[1]))
									if isinstance(rhs1, Typed_COR_Expressions.Typed_Complement):
										arg = rhs1.argument
										if P==arg.type()[0]:
											if Q==arg.type()[1]:
												B = arg
												return ("((A[P*Q])⁻) ∪ ((B[P*Q])⁻) = ((A[P*Q]) ∩ (B[P*Q]))⁻", Typed_COR_Expressions.Typed_Complement(Typed_COR_Expressions.Typed_Intersection(A, B)))
									if isinstance(rhs1, Typed_COR_Expressions.Typed_Intersection):
										lhs9, rhs9 = rhs1.argument1, rhs1.argument2
										if P==lhs9.type()[0]:
											if Q==lhs9.type()[1]:
												if str(A)==str(lhs9):
													if P==rhs9.type()[0]:
														if Q==rhs9.type()[1]:
															B = rhs9
															return ("((A[P*Q])⁻) ∪ ((A[P*Q]) ∩ (B[P*Q])) = (B[P*Q]) ∪ ((A[P*Q])⁻)", Typed_COR_Expressions.Typed_Union(B, Typed_COR_Expressions.Typed_Complement(A)))
												B = lhs9
												if P==rhs9.type()[0]:
													if Q==rhs9.type()[1]:
														if str(A)==str(rhs9):
															return ("((A[P*Q])⁻) ∪ ((B[P*Q]) ∩ (A[P*Q])) = (B[P*Q]) ∪ ((A[P*Q])⁻)", Typed_COR_Expressions.Typed_Union(B, Typed_COR_Expressions.Typed_Complement(A)))
							if isinstance(arg, Typed_COR_Expressions.Typed_Union):
								lhs7, rhs7 = arg.argument1, arg.argument2
								if P==lhs7.type()[0]:
									if Q==lhs7.type()[1]:
										A = lhs7
										if P==rhs7.type()[0]:
											if Q==rhs7.type()[1]:
												B = rhs7
												if P==rhs1.type()[0]:
													if Q==rhs1.type()[1]:
														if str(B)==str(rhs1):
															return ("(((A[P*Q]) ∪ (B[P*Q]))⁻) ∪ (B[P*Q]) = ((A[P*Q])⁻) ∪ (B[P*Q])", Typed_COR_Expressions.Typed_Union(Typed_COR_Expressions.Typed_Complement(A), B))
														if str(A)==str(rhs1):
															return ("(((A[P*Q]) ∪ (B[P*Q]))⁻) ∪ (A[P*Q]) = ((B[P*Q])⁻) ∪ (A[P*Q])", Typed_COR_Expressions.Typed_Union(Typed_COR_Expressions.Typed_Complement(B), A))
							if isinstance(arg, Typed_COR_Expressions.Typed_Intersection):
								lhs7, rhs7 = arg.argument1, arg.argument2
								if P==lhs7.type()[0]:
									if Q==lhs7.type()[1]:
										A = lhs7
										if P==rhs7.type()[0]:
											if Q==rhs7.type()[1]:
												B = rhs7
												if P==rhs1.type()[0]:
													if Q==rhs1.type()[1]:
														if str(B)==str(rhs1):
															return ("(((A[P*Q]) ∩ (B[P*Q]))⁻) ∪ (B[P*Q]) = T[P*Q]", Typed_COR_Expressions.Typed_UniversalRelation(expression.type()[0], expression.type()[1]))
														if str(A)==str(rhs1):
															return ("(((A[P*Q]) ∩ (B[P*Q]))⁻) ∪ (A[P*Q]) = T[P*Q]", Typed_COR_Expressions.Typed_UniversalRelation(expression.type()[0], expression.type()[1]))
				if isinstance(lhs1, Typed_COR_Expressions.Typed_UniversalRelation):
					if P==rhs1.type()[0]:
						if Q==rhs1.type()[1]:
							A = rhs1
							return ("(T[P*Q]) ∪ (A[P*Q]) = T[P*Q]", Typed_COR_Expressions.Typed_UniversalRelation(expression.type()[0], expression.type()[1]))
				if isinstance(lhs1, Typed_COR_Expressions.Typed_Intersection):
					lhs4, rhs4 = lhs1.argument1, lhs1.argument2
					if P==lhs4.type()[0]:
						if Q==lhs4.type()[1]:
							A = lhs4
							if P==rhs4.type()[0]:
								if Q==rhs4.type()[1]:
									B = rhs4
									if P==rhs1.type()[0]:
										if Q==rhs1.type()[1]:
											if str(A)==str(rhs1):
												return ("((A[P*Q]) ∩ (B[P*Q])) ∪ (A[P*Q]) = A[P*Q]", A)
											if str(B)==str(rhs1):
												return ("((A[P*Q]) ∩ (B[P*Q])) ∪ (B[P*Q]) = B[P*Q]", B)
											if isinstance(rhs1, Typed_COR_Expressions.Typed_Intersection):
												lhs11, rhs11 = rhs1.argument1, rhs1.argument2
												if P==lhs11.type()[0]:
													if Q==lhs11.type()[1]:
														if str(B)==str(lhs11):
															if P==rhs11.type()[0]:
																if Q==rhs11.type()[1]:
																	C = rhs11
																	return ("((A[P*Q]) ∩ (B[P*Q])) ∪ ((B[P*Q]) ∩ (C[P*Q])) = ((C[P*Q]) ∪ (A[P*Q])) ∩ (B[P*Q])", Typed_COR_Expressions.Typed_Intersection(Typed_COR_Expressions.Typed_Union(C, A), B))
														if str(A)==str(lhs11):
															if P==rhs11.type()[0]:
																if Q==rhs11.type()[1]:
																	C = rhs11
																	return ("((A[P*Q]) ∩ (B[P*Q])) ∪ ((A[P*Q]) ∩ (C[P*Q])) = ((B[P*Q]) ∪ (C[P*Q])) ∩ (A[P*Q])", Typed_COR_Expressions.Typed_Intersection(Typed_COR_Expressions.Typed_Union(B, C), A))
														C = lhs11
														if P==rhs11.type()[0]:
															if Q==rhs11.type()[1]:
																if str(B)==str(rhs11):
																	return ("((A[P*Q]) ∩ (B[P*Q])) ∪ ((C[P*Q]) ∩ (B[P*Q])) = (B[P*Q]) ∩ ((C[P*Q]) ∪ (A[P*Q]))", Typed_COR_Expressions.Typed_Intersection(B, Typed_COR_Expressions.Typed_Union(C, A)))
																if str(A)==str(rhs11):
																	return ("((A[P*Q]) ∩ (B[P*Q])) ∪ ((C[P*Q]) ∩ (A[P*Q])) = (A[P*Q]) ∩ ((B[P*Q]) ∪ (C[P*Q]))", Typed_COR_Expressions.Typed_Intersection(A, Typed_COR_Expressions.Typed_Union(B, C)))
											if isinstance(rhs1, Typed_COR_Expressions.Typed_Union):
												lhs11, rhs11 = rhs1.argument1, rhs1.argument2
												if P==lhs11.type()[0]:
													if Q==lhs11.type()[1]:
														C = lhs11
														if P==rhs11.type()[0]:
															if Q==rhs11.type()[1]:
																if str(B)==str(rhs11):
																	return ("((A[P*Q]) ∩ (B[P*Q])) ∪ ((C[P*Q]) ∪ (B[P*Q])) = (B[P*Q]) ∪ (C[P*Q])", Typed_COR_Expressions.Typed_Union(B, C))
																if str(A)==str(rhs11):
																	return ("((A[P*Q]) ∩ (B[P*Q])) ∪ ((C[P*Q]) ∪ (A[P*Q])) = (A[P*Q]) ∪ (C[P*Q])", Typed_COR_Expressions.Typed_Union(A, C))
														if str(B)==str(lhs11):
															if P==rhs11.type()[0]:
																if Q==rhs11.type()[1]:
																	C = rhs11
																	return ("((A[P*Q]) ∩ (B[P*Q])) ∪ ((B[P*Q]) ∪ (C[P*Q])) = (B[P*Q]) ∪ (C[P*Q])", Typed_COR_Expressions.Typed_Union(B, C))
														if str(A)==str(lhs11):
															if P==rhs11.type()[0]:
																if Q==rhs11.type()[1]:
																	C = rhs11
																	return ("((A[P*Q]) ∩ (B[P*Q])) ∪ ((A[P*Q]) ∪ (C[P*Q])) = (C[P*Q]) ∪ (A[P*Q])", Typed_COR_Expressions.Typed_Union(C, A))
											if isinstance(rhs1, Typed_COR_Expressions.Typed_Complement):
												arg = rhs1.argument
												if P==arg.type()[0]:
													if Q==arg.type()[1]:
														if str(B)==str(arg):
															return ("((A[P*Q]) ∩ (B[P*Q])) ∪ ((B[P*Q])⁻) = ((B[P*Q])⁻) ∪ (A[P*Q])", Typed_COR_Expressions.Typed_Union(Typed_COR_Expressions.Typed_Complement(B), A))
														if str(A)==str(arg):
															return ("((A[P*Q]) ∩ (B[P*Q])) ∪ ((A[P*Q])⁻) = ((A[P*Q])⁻) ∪ (B[P*Q])", Typed_COR_Expressions.Typed_Union(Typed_COR_Expressions.Typed_Complement(A), B))
									if isinstance(rhs4, Typed_COR_Expressions.Typed_Union):
										lhs9, rhs9 = rhs4.argument1, rhs4.argument2
										if P==lhs9.type()[0]:
											if Q==lhs9.type()[1]:
												B = lhs9
												if P==rhs9.type()[0]:
													if Q==rhs9.type()[1]:
														C = rhs9
														if P==rhs1.type()[0]:
															if Q==rhs1.type()[1]:
																if str(B)==str(rhs1):
																	return ("((A[P*Q]) ∩ ((B[P*Q]) ∪ (C[P*Q]))) ∪ (B[P*Q]) = (B[P*Q]) ∪ ((C[P*Q]) ∩ (A[P*Q]))", Typed_COR_Expressions.Typed_Union(B, Typed_COR_Expressions.Typed_Intersection(C, A)))
																if str(C)==str(rhs1):
																	return ("((A[P*Q]) ∩ ((B[P*Q]) ∪ (C[P*Q]))) ∪ (C[P*Q]) = ((B[P*Q]) ∩ (A[P*Q])) ∪ (C[P*Q])", Typed_COR_Expressions.Typed_Union(Typed_COR_Expressions.Typed_Intersection(B, A), C))
									if isinstance(rhs4, Typed_COR_Expressions.Typed_Complement):
										arg = rhs4.argument
										if P==arg.type()[0]:
											if Q==arg.type()[1]:
												B = arg
												if P==rhs1.type()[0]:
													if Q==rhs1.type()[1]:
														if str(B)==str(rhs1):
															return ("((A[P*Q]) ∩ ((B[P*Q])⁻)) ∪ (B[P*Q]) = (B[P*Q]) ∪ (A[P*Q])", Typed_COR_Expressions.Typed_Union(B, A))
									if isinstance(rhs4, Typed_COR_Expressions.Typed_Intersection):
										lhs9, rhs9 = rhs4.argument1, rhs4.argument2
										if P==lhs9.type()[0]:
											if Q==lhs9.type()[1]:
												B = lhs9
												if P==rhs9.type()[0]:
													if Q==rhs9.type()[1]:
														C = rhs9
														if P==rhs1.type()[0]:
															if Q==rhs1.type()[1]:
																if str(B)==str(rhs1):
																	return ("((A[P*Q]) ∩ ((B[P*Q]) ∩ (C[P*Q]))) ∪ (B[P*Q]) = B[P*Q]", B)
																if str(C)==str(rhs1):
																	return ("((A[P*Q]) ∩ ((B[P*Q]) ∩ (C[P*Q]))) ∪ (C[P*Q]) = C[P*Q]", C)
							if isinstance(lhs4, Typed_COR_Expressions.Typed_Union):
								lhs7, rhs7 = lhs4.argument1, lhs4.argument2
								if P==lhs7.type()[0]:
									if Q==lhs7.type()[1]:
										A = lhs7
										if P==rhs7.type()[0]:
											if Q==rhs7.type()[1]:
												B = rhs7
												if P==rhs4.type()[0]:
													if Q==rhs4.type()[1]:
														C = rhs4
														if P==rhs1.type()[0]:
															if Q==rhs1.type()[1]:
																if str(B)==str(rhs1):
																	return ("(((A[P*Q]) ∪ (B[P*Q])) ∩ (C[P*Q])) ∪ (B[P*Q]) = (B[P*Q]) ∪ ((A[P*Q]) ∩ (C[P*Q]))", Typed_COR_Expressions.Typed_Union(B, Typed_COR_Expressions.Typed_Intersection(A, C)))
																if str(A)==str(rhs1):
																	return ("(((A[P*Q]) ∪ (B[P*Q])) ∩ (C[P*Q])) ∪ (A[P*Q]) = ((B[P*Q]) ∩ (C[P*Q])) ∪ (A[P*Q])", Typed_COR_Expressions.Typed_Union(Typed_COR_Expressions.Typed_Intersection(B, C), A))
							if isinstance(lhs4, Typed_COR_Expressions.Typed_Intersection):
								lhs7, rhs7 = lhs4.argument1, lhs4.argument2
								if P==lhs7.type()[0]:
									if Q==lhs7.type()[1]:
										A = lhs7
										if P==rhs7.type()[0]:
											if Q==rhs7.type()[1]:
												B = rhs7
												if P==rhs4.type()[0]:
													if Q==rhs4.type()[1]:
														C = rhs4
														if P==rhs1.type()[0]:
															if Q==rhs1.type()[1]:
																if str(B)==str(rhs1):
																	return ("(((A[P*Q]) ∩ (B[P*Q])) ∩ (C[P*Q])) ∪ (B[P*Q]) = B[P*Q]", B)
																if str(A)==str(rhs1):
																	return ("(((A[P*Q]) ∩ (B[P*Q])) ∩ (C[P*Q])) ∪ (A[P*Q]) = A[P*Q]", A)
							if isinstance(lhs4, Typed_COR_Expressions.Typed_Complement):
								arg = lhs4.argument
								if P==arg.type()[0]:
									if Q==arg.type()[1]:
										A = arg
										if P==rhs4.type()[0]:
											if Q==rhs4.type()[1]:
												B = rhs4
												if P==rhs1.type()[0]:
													if Q==rhs1.type()[1]:
														if str(A)==str(rhs1):
															return ("(((A[P*Q])⁻) ∩ (B[P*Q])) ∪ (A[P*Q]) = (A[P*Q]) ∪ (B[P*Q])", Typed_COR_Expressions.Typed_Union(A, B))
				if isinstance(lhs1, Typed_COR_Expressions.Typed_EmptyRelation):
					if P==rhs1.type()[0]:
						if Q==rhs1.type()[1]:
							A = rhs1
							return ("(𝟎[P*Q]) ∪ (A[P*Q]) = A[P*Q]", A)
				if isinstance(lhs1, Typed_COR_Expressions.Typed_Composition):
					lhs4, rhs4 = lhs1.argument1, lhs1.argument2
					if P==lhs4.type()[0]:
						if P==lhs4.type()[1]:
							A = lhs4
							if P==rhs4.type()[0]:
								if Q==rhs4.type()[1]:
									B = rhs4
									if P==rhs1.type()[0]:
										if Q==rhs1.type()[1]:
											if isinstance(rhs1, Typed_COR_Expressions.Typed_Composition):
												lhs11, rhs11 = rhs1.argument1, rhs1.argument2
												if P==lhs11.type()[0]:
													if P==lhs11.type()[1]:
														if str(A)==str(lhs11):
															if P==rhs11.type()[0]:
																if Q==rhs11.type()[1]:
																	C = rhs11
																	return ("((A[P*P]) ∘ (B[P*Q])) ∪ ((A[P*P]) ∘ (C[P*Q])) = (A[P*P]) ∘ ((B[P*Q]) ∪ (C[P*Q]))", Typed_COR_Expressions.Typed_Composition(A, Typed_COR_Expressions.Typed_Union(B, C)))
														C = lhs11
														if P==rhs11.type()[0]:
															if Q==rhs11.type()[1]:
																if str(B)==str(rhs11):
																	return ("((A[P*P]) ∘ (B[P*Q])) ∪ ((C[P*P]) ∘ (B[P*Q])) = ((C[P*P]) ∪ (A[P*P])) ∘ (B[P*Q])", Typed_COR_Expressions.Typed_Composition(Typed_COR_Expressions.Typed_Union(C, A), B))
							if isinstance(lhs4, Typed_COR_Expressions.Typed_UniversalRelation):
								if P==rhs4.type()[0]:
									if Q==rhs4.type()[1]:
										A = rhs4
										if P==rhs1.type()[0]:
											if Q==rhs1.type()[1]:
												if str(A)==str(rhs1):
													return ("((T[P*P]) ∘ (A[P*Q])) ∪ (A[P*Q]) = (T[P*P]) ∘ (A[P*Q])", Typed_COR_Expressions.Typed_Composition(Typed_COR_Expressions.Typed_UniversalRelation(expression.type()[0], A.type()[0]), A))
						if Q==lhs4.type()[1]:
							A = lhs4
							if Q==rhs4.type()[0]:
								if Q==rhs4.type()[1]:
									B = rhs4
									if P==rhs1.type()[0]:
										if Q==rhs1.type()[1]:
											if isinstance(rhs1, Typed_COR_Expressions.Typed_Composition):
												lhs11, rhs11 = rhs1.argument1, rhs1.argument2
												if P==lhs11.type()[0]:
													if Q==lhs11.type()[1]:
														if str(A)==str(lhs11):
															if Q==rhs11.type()[0]:
																if Q==rhs11.type()[1]:
																	C = rhs11
																	return ("((A[P*Q]) ∘ (B[Q*Q])) ∪ ((A[P*Q]) ∘ (C[Q*Q])) = (A[P*Q]) ∘ ((B[Q*Q]) ∪ (C[Q*Q]))", Typed_COR_Expressions.Typed_Composition(A, Typed_COR_Expressions.Typed_Union(B, C)))
														C = lhs11
														if Q==rhs11.type()[0]:
															if Q==rhs11.type()[1]:
																if str(B)==str(rhs11):
																	return ("((A[P*Q]) ∘ (B[Q*Q])) ∪ ((C[P*Q]) ∘ (B[Q*Q])) = ((C[P*Q]) ∪ (A[P*Q])) ∘ (B[Q*Q])", Typed_COR_Expressions.Typed_Composition(Typed_COR_Expressions.Typed_Union(C, A), B))
									if isinstance(rhs4, Typed_COR_Expressions.Typed_UniversalRelation):
										if P==rhs1.type()[0]:
											if Q==rhs1.type()[1]:
												if str(A)==str(rhs1):
													return ("((A[P*Q]) ∘ (T[Q*Q])) ∪ (A[P*Q]) = (A[P*Q]) ∘ (T[Q*Q])", Typed_COR_Expressions.Typed_Composition(A, Typed_COR_Expressions.Typed_UniversalRelation(A.type()[1], expression.type()[1])))
						R = lhs4.type()[1]
						A = lhs4
						if R==rhs4.type()[0]:
							if Q==rhs4.type()[1]:
								B = rhs4
								if P==rhs1.type()[0]:
									if Q==rhs1.type()[1]:
										if isinstance(rhs1, Typed_COR_Expressions.Typed_Composition):
											lhs10, rhs10 = rhs1.argument1, rhs1.argument2
											if P==lhs10.type()[0]:
												if R==lhs10.type()[1]:
													if str(A)==str(lhs10):
														if R==rhs10.type()[0]:
															if Q==rhs10.type()[1]:
																C = rhs10
																return ("((A[P*R]) ∘ (B[R*Q])) ∪ ((A[P*R]) ∘ (C[R*Q])) = (A[P*R]) ∘ ((B[R*Q]) ∪ (C[R*Q]))", Typed_COR_Expressions.Typed_Composition(A, Typed_COR_Expressions.Typed_Union(B, C)))
													C = lhs10
													if R==rhs10.type()[0]:
														if Q==rhs10.type()[1]:
															if str(B)==str(rhs10):
																return ("((A[P*R]) ∘ (B[R*Q])) ∪ ((C[P*R]) ∘ (B[R*Q])) = ((C[P*R]) ∪ (A[P*R])) ∘ (B[R*Q])", Typed_COR_Expressions.Typed_Composition(Typed_COR_Expressions.Typed_Union(C, A), B))
				if isinstance(lhs1, Typed_COR_Expressions.Typed_Dagger):
					lhs4, rhs4 = lhs1.argument1, lhs1.argument2
					if P==lhs4.type()[0]:
						if Q==lhs4.type()[1]:
							A = lhs4
							if Q==rhs4.type()[0]:
								if Q==rhs4.type()[1]:
									if isinstance(rhs4, Typed_COR_Expressions.Typed_EmptyRelation):
										if P==rhs1.type()[0]:
											if Q==rhs1.type()[1]:
												if str(A)==str(rhs1):
													return ("((A[P*Q]) † (𝟎[Q*Q])) ∪ (A[P*Q]) = A[P*Q]", A)
						if P==lhs4.type()[1]:
							if isinstance(lhs4, Typed_COR_Expressions.Typed_EmptyRelation):
								if P==rhs4.type()[0]:
									if Q==rhs4.type()[1]:
										A = rhs4
										if P==rhs1.type()[0]:
											if Q==rhs1.type()[1]:
												if str(A)==str(rhs1):
													return ("((𝟎[P*P]) † (A[P*Q])) ∪ (A[P*Q]) = A[P*Q]", A)
	if isinstance(expression, Typed_COR_Expressions.Typed_Intersection):
		lhs1, rhs1 = expression.argument1, expression.argument2
		if P==lhs1.type()[0]:
			if Q==lhs1.type()[1]:
				A = lhs1
				if P==rhs1.type()[0]:
					if Q==rhs1.type()[1]:
						if str(A)==str(rhs1):
							return ("(A[P*Q]) ∩ (A[P*Q]) = A[P*Q]", A)
						if isinstance(rhs1, Typed_COR_Expressions.Typed_Complement):
							arg = rhs1.argument
							if P==arg.type()[0]:
								if Q==arg.type()[1]:
									if str(A)==str(arg):
										return ("(A[P*Q]) ∩ ((A[P*Q])⁻) = 𝟎[P*Q]", Typed_COR_Expressions.Typed_EmptyRelation(expression.type()[0], expression.type()[1]))
									if isinstance(arg, Typed_COR_Expressions.Typed_Intersection):
										lhs9, rhs9 = arg.argument1, arg.argument2
										if P==lhs9.type()[0]:
											if Q==lhs9.type()[1]:
												if str(A)==str(lhs9):
													if P==rhs9.type()[0]:
														if Q==rhs9.type()[1]:
															B = rhs9
															return ("(A[P*Q]) ∩ (((A[P*Q]) ∩ (B[P*Q]))⁻) = (A[P*Q]) ∩ ((B[P*Q])⁻)", Typed_COR_Expressions.Typed_Intersection(A, Typed_COR_Expressions.Typed_Complement(B)))
												B = lhs9
												if P==rhs9.type()[0]:
													if Q==rhs9.type()[1]:
														if str(A)==str(rhs9):
															return ("(A[P*Q]) ∩ (((B[P*Q]) ∩ (A[P*Q]))⁻) = (A[P*Q]) ∩ ((B[P*Q])⁻)", Typed_COR_Expressions.Typed_Intersection(A, Typed_COR_Expressions.Typed_Complement(B)))
									if isinstance(arg, Typed_COR_Expressions.Typed_Union):
										lhs9, rhs9 = arg.argument1, arg.argument2
										if P==lhs9.type()[0]:
											if Q==lhs9.type()[1]:
												if str(A)==str(lhs9):
													if P==rhs9.type()[0]:
														if Q==rhs9.type()[1]:
															B = rhs9
															return ("(A[P*Q]) ∩ (((A[P*Q]) ∪ (B[P*Q]))⁻) = 𝟎[P*Q]", Typed_COR_Expressions.Typed_EmptyRelation(expression.type()[0], expression.type()[1]))
												B = lhs9
												if P==rhs9.type()[0]:
													if Q==rhs9.type()[1]:
														if str(A)==str(rhs9):
															return ("(A[P*Q]) ∩ (((B[P*Q]) ∪ (A[P*Q]))⁻) = 𝟎[P*Q]", Typed_COR_Expressions.Typed_EmptyRelation(expression.type()[0], expression.type()[1]))
						if isinstance(rhs1, Typed_COR_Expressions.Typed_UniversalRelation):
							return ("(A[P*Q]) ∩ (T[P*Q]) = A[P*Q]", A)
						if isinstance(rhs1, Typed_COR_Expressions.Typed_Intersection):
							lhs6, rhs6 = rhs1.argument1, rhs1.argument2
							if P==lhs6.type()[0]:
								if Q==lhs6.type()[1]:
									B = lhs6
									if P==rhs6.type()[0]:
										if Q==rhs6.type()[1]:
											if str(A)==str(rhs6):
												return ("(A[P*Q]) ∩ ((B[P*Q]) ∩ (A[P*Q])) = (B[P*Q]) ∩ (A[P*Q])", Typed_COR_Expressions.Typed_Intersection(B, A))
											if isinstance(rhs6, Typed_COR_Expressions.Typed_Intersection):
												lhs11, rhs11 = rhs6.argument1, rhs6.argument2
												if P==lhs11.type()[0]:
													if Q==lhs11.type()[1]:
														C = lhs11
														if P==rhs11.type()[0]:
															if Q==rhs11.type()[1]:
																if str(A)==str(rhs11):
																	return ("(A[P*Q]) ∩ ((B[P*Q]) ∩ ((C[P*Q]) ∩ (A[P*Q]))) = ((B[P*Q]) ∩ (A[P*Q])) ∩ (C[P*Q])", Typed_COR_Expressions.Typed_Intersection(Typed_COR_Expressions.Typed_Intersection(B, A), C))
														if str(A)==str(lhs11):
															if P==rhs11.type()[0]:
																if Q==rhs11.type()[1]:
																	C = rhs11
																	return ("(A[P*Q]) ∩ ((B[P*Q]) ∩ ((A[P*Q]) ∩ (C[P*Q]))) = ((B[P*Q]) ∩ (C[P*Q])) ∩ (A[P*Q])", Typed_COR_Expressions.Typed_Intersection(Typed_COR_Expressions.Typed_Intersection(B, C), A))
											if isinstance(rhs6, Typed_COR_Expressions.Typed_Union):
												lhs11, rhs11 = rhs6.argument1, rhs6.argument2
												if P==lhs11.type()[0]:
													if Q==lhs11.type()[1]:
														C = lhs11
														if P==rhs11.type()[0]:
															if Q==rhs11.type()[1]:
																if str(A)==str(rhs11):
																	return ("(A[P*Q]) ∩ ((B[P*Q]) ∩ ((C[P*Q]) ∪ (A[P*Q]))) = (A[P*Q]) ∩ (B[P*Q])", Typed_COR_Expressions.Typed_Intersection(A, B))
														if str(A)==str(lhs11):
															if P==rhs11.type()[0]:
																if Q==rhs11.type()[1]:
																	C = rhs11
																	return ("(A[P*Q]) ∩ ((B[P*Q]) ∩ ((A[P*Q]) ∪ (C[P*Q]))) = (A[P*Q]) ∩ (B[P*Q])", Typed_COR_Expressions.Typed_Intersection(A, B))
											if isinstance(rhs6, Typed_COR_Expressions.Typed_Complement):
												arg = rhs6.argument
												if P==arg.type()[0]:
													if Q==arg.type()[1]:
														if str(A)==str(arg):
															return ("(A[P*Q]) ∩ ((B[P*Q]) ∩ ((A[P*Q])⁻)) = 𝟎[P*Q]", Typed_COR_Expressions.Typed_EmptyRelation(expression.type()[0], expression.type()[1]))
									if str(A)==str(lhs6):
										if P==rhs6.type()[0]:
											if Q==rhs6.type()[1]:
												B = rhs6
												return ("(A[P*Q]) ∩ ((A[P*Q]) ∩ (B[P*Q])) = (A[P*Q]) ∩ (B[P*Q])", Typed_COR_Expressions.Typed_Intersection(A, B))
									if isinstance(lhs6, Typed_COR_Expressions.Typed_Intersection):
										lhs9, rhs9 = lhs6.argument1, lhs6.argument2
										if P==lhs9.type()[0]:
											if Q==lhs9.type()[1]:
												B = lhs9
												if P==rhs9.type()[0]:
													if Q==rhs9.type()[1]:
														if str(A)==str(rhs9):
															if P==rhs6.type()[0]:
																if Q==rhs6.type()[1]:
																	C = rhs6
																	return ("(A[P*Q]) ∩ (((B[P*Q]) ∩ (A[P*Q])) ∩ (C[P*Q])) = ((A[P*Q]) ∩ (C[P*Q])) ∩ (B[P*Q])", Typed_COR_Expressions.Typed_Intersection(Typed_COR_Expressions.Typed_Intersection(A, C), B))
												if str(A)==str(lhs9):
													if P==rhs9.type()[0]:
														if Q==rhs9.type()[1]:
															B = rhs9
															if P==rhs6.type()[0]:
																if Q==rhs6.type()[1]:
																	C = rhs6
																	return ("(A[P*Q]) ∩ (((A[P*Q]) ∩ (B[P*Q])) ∩ (C[P*Q])) = ((A[P*Q]) ∩ (B[P*Q])) ∩ (C[P*Q])", Typed_COR_Expressions.Typed_Intersection(Typed_COR_Expressions.Typed_Intersection(A, B), C))
									if isinstance(lhs6, Typed_COR_Expressions.Typed_Union):
										lhs9, rhs9 = lhs6.argument1, lhs6.argument2
										if P==lhs9.type()[0]:
											if Q==lhs9.type()[1]:
												B = lhs9
												if P==rhs9.type()[0]:
													if Q==rhs9.type()[1]:
														if str(A)==str(rhs9):
															if P==rhs6.type()[0]:
																if Q==rhs6.type()[1]:
																	C = rhs6
																	return ("(A[P*Q]) ∩ (((B[P*Q]) ∪ (A[P*Q])) ∩ (C[P*Q])) = (C[P*Q]) ∩ (A[P*Q])", Typed_COR_Expressions.Typed_Intersection(C, A))
												if str(A)==str(lhs9):
													if P==rhs9.type()[0]:
														if Q==rhs9.type()[1]:
															B = rhs9
															if P==rhs6.type()[0]:
																if Q==rhs6.type()[1]:
																	C = rhs6
																	return ("(A[P*Q]) ∩ (((A[P*Q]) ∪ (B[P*Q])) ∩ (C[P*Q])) = (C[P*Q]) ∩ (A[P*Q])", Typed_COR_Expressions.Typed_Intersection(C, A))
									if isinstance(lhs6, Typed_COR_Expressions.Typed_Complement):
										arg = lhs6.argument
										if P==arg.type()[0]:
											if Q==arg.type()[1]:
												if str(A)==str(arg):
													if P==rhs6.type()[0]:
														if Q==rhs6.type()[1]:
															B = rhs6
															return ("(A[P*Q]) ∩ (((A[P*Q])⁻) ∩ (B[P*Q])) = 𝟎[P*Q]", Typed_COR_Expressions.Typed_EmptyRelation(expression.type()[0], expression.type()[1]))
						if isinstance(rhs1, Typed_COR_Expressions.Typed_Union):
							lhs6, rhs6 = rhs1.argument1, rhs1.argument2
							if P==lhs6.type()[0]:
								if Q==lhs6.type()[1]:
									B = lhs6
									if P==rhs6.type()[0]:
										if Q==rhs6.type()[1]:
											if str(A)==str(rhs6):
												return ("(A[P*Q]) ∩ ((B[P*Q]) ∪ (A[P*Q])) = A[P*Q]", A)
											if isinstance(rhs6, Typed_COR_Expressions.Typed_Intersection):
												lhs11, rhs11 = rhs6.argument1, rhs6.argument2
												if P==lhs11.type()[0]:
													if Q==lhs11.type()[1]:
														C = lhs11
														if P==rhs11.type()[0]:
															if Q==rhs11.type()[1]:
																if str(A)==str(rhs11):
																	return ("(A[P*Q]) ∩ ((B[P*Q]) ∪ ((C[P*Q]) ∩ (A[P*Q]))) = ((C[P*Q]) ∪ (B[P*Q])) ∩ (A[P*Q])", Typed_COR_Expressions.Typed_Intersection(Typed_COR_Expressions.Typed_Union(C, B), A))
														if str(A)==str(lhs11):
															if P==rhs11.type()[0]:
																if Q==rhs11.type()[1]:
																	C = rhs11
																	return ("(A[P*Q]) ∩ ((B[P*Q]) ∪ ((A[P*Q]) ∩ (C[P*Q]))) = ((B[P*Q]) ∪ (C[P*Q])) ∩ (A[P*Q])", Typed_COR_Expressions.Typed_Intersection(Typed_COR_Expressions.Typed_Union(B, C), A))
											if isinstance(rhs6, Typed_COR_Expressions.Typed_Union):
												lhs11, rhs11 = rhs6.argument1, rhs6.argument2
												if P==lhs11.type()[0]:
													if Q==lhs11.type()[1]:
														if str(A)==str(lhs11):
															if P==rhs11.type()[0]:
																if Q==rhs11.type()[1]:
																	C = rhs11
																	return ("(A[P*Q]) ∩ ((B[P*Q]) ∪ ((A[P*Q]) ∪ (C[P*Q]))) = A[P*Q]", A)
														C = lhs11
														if P==rhs11.type()[0]:
															if Q==rhs11.type()[1]:
																if str(A)==str(rhs11):
																	return ("(A[P*Q]) ∩ ((B[P*Q]) ∪ ((C[P*Q]) ∪ (A[P*Q]))) = A[P*Q]", A)
											if isinstance(rhs6, Typed_COR_Expressions.Typed_Complement):
												arg = rhs6.argument
												if P==arg.type()[0]:
													if Q==arg.type()[1]:
														if str(A)==str(arg):
															return ("(A[P*Q]) ∩ ((B[P*Q]) ∪ ((A[P*Q])⁻)) = (B[P*Q]) ∩ (A[P*Q])", Typed_COR_Expressions.Typed_Intersection(B, A))
									if str(A)==str(lhs6):
										if P==rhs6.type()[0]:
											if Q==rhs6.type()[1]:
												B = rhs6
												return ("(A[P*Q]) ∩ ((A[P*Q]) ∪ (B[P*Q])) = A[P*Q]", A)
									if isinstance(lhs6, Typed_COR_Expressions.Typed_Intersection):
										lhs9, rhs9 = lhs6.argument1, lhs6.argument2
										if P==lhs9.type()[0]:
											if Q==lhs9.type()[1]:
												B = lhs9
												if P==rhs9.type()[0]:
													if Q==rhs9.type()[1]:
														if str(A)==str(rhs9):
															if P==rhs6.type()[0]:
																if Q==rhs6.type()[1]:
																	C = rhs6
																	return ("(A[P*Q]) ∩ (((B[P*Q]) ∩ (A[P*Q])) ∪ (C[P*Q])) = ((C[P*Q]) ∪ (B[P*Q])) ∩ (A[P*Q])", Typed_COR_Expressions.Typed_Intersection(Typed_COR_Expressions.Typed_Union(C, B), A))
												if str(A)==str(lhs9):
													if P==rhs9.type()[0]:
														if Q==rhs9.type()[1]:
															B = rhs9
															if P==rhs6.type()[0]:
																if Q==rhs6.type()[1]:
																	C = rhs6
																	return ("(A[P*Q]) ∩ (((A[P*Q]) ∩ (B[P*Q])) ∪ (C[P*Q])) = ((C[P*Q]) ∪ (B[P*Q])) ∩ (A[P*Q])", Typed_COR_Expressions.Typed_Intersection(Typed_COR_Expressions.Typed_Union(C, B), A))
									if isinstance(lhs6, Typed_COR_Expressions.Typed_Complement):
										arg = lhs6.argument
										if P==arg.type()[0]:
											if Q==arg.type()[1]:
												if str(A)==str(arg):
													if P==rhs6.type()[0]:
														if Q==rhs6.type()[1]:
															B = rhs6
															return ("(A[P*Q]) ∩ (((A[P*Q])⁻) ∪ (B[P*Q])) = (A[P*Q]) ∩ (B[P*Q])", Typed_COR_Expressions.Typed_Intersection(A, B))
									if isinstance(lhs6, Typed_COR_Expressions.Typed_Union):
										lhs9, rhs9 = lhs6.argument1, lhs6.argument2
										if P==lhs9.type()[0]:
											if Q==lhs9.type()[1]:
												if str(A)==str(lhs9):
													if P==rhs9.type()[0]:
														if Q==rhs9.type()[1]:
															B = rhs9
															if P==rhs6.type()[0]:
																if Q==rhs6.type()[1]:
																	C = rhs6
																	return ("(A[P*Q]) ∩ (((A[P*Q]) ∪ (B[P*Q])) ∪ (C[P*Q])) = A[P*Q]", A)
												B = lhs9
												if P==rhs9.type()[0]:
													if Q==rhs9.type()[1]:
														if str(A)==str(rhs9):
															if P==rhs6.type()[0]:
																if Q==rhs6.type()[1]:
																	C = rhs6
																	return ("(A[P*Q]) ∩ (((B[P*Q]) ∪ (A[P*Q])) ∪ (C[P*Q])) = A[P*Q]", A)
						if isinstance(rhs1, Typed_COR_Expressions.Typed_EmptyRelation):
							return ("(A[P*Q]) ∩ (𝟎[P*Q]) = 𝟎[P*Q]", Typed_COR_Expressions.Typed_EmptyRelation(expression.type()[0], expression.type()[1]))
						if isinstance(rhs1, Typed_COR_Expressions.Typed_Dagger):
							lhs6, rhs6 = rhs1.argument1, rhs1.argument2
							if P==lhs6.type()[0]:
								if Q==lhs6.type()[1]:
									if str(A)==str(lhs6):
										if Q==rhs6.type()[0]:
											if Q==rhs6.type()[1]:
												if isinstance(rhs6, Typed_COR_Expressions.Typed_IdentityRelation):
													return ("(A[P*Q]) ∩ ((A[P*Q]) † (𝟏[Q*Q])) = (A[P*Q]) † (𝟎[Q*Q])", Typed_COR_Expressions.Typed_Dagger(A, Typed_COR_Expressions.Typed_EmptyRelation(A.type()[1], expression.type()[1])))
												if isinstance(rhs6, Typed_COR_Expressions.Typed_EmptyRelation):
													return ("(A[P*Q]) ∩ ((A[P*Q]) † (𝟎[Q*Q])) = (A[P*Q]) † (𝟎[Q*Q])", Typed_COR_Expressions.Typed_Dagger(A, Typed_COR_Expressions.Typed_EmptyRelation(A.type()[1], expression.type()[1])))
								if P==lhs6.type()[1]:
									if isinstance(lhs6, Typed_COR_Expressions.Typed_EmptyRelation):
										if P==rhs6.type()[0]:
											if Q==rhs6.type()[1]:
												if str(A)==str(rhs6):
													return ("(A[P*Q]) ∩ ((𝟎[P*P]) † (A[P*Q])) = (𝟎[P*P]) † (A[P*Q])", Typed_COR_Expressions.Typed_Dagger(Typed_COR_Expressions.Typed_EmptyRelation(expression.type()[0], A.type()[0]), A))
									if isinstance(lhs6, Typed_COR_Expressions.Typed_IdentityRelation):
										if P==rhs6.type()[0]:
											if Q==rhs6.type()[1]:
												if str(A)==str(rhs6):
													return ("(A[P*Q]) ∩ ((𝟏[P*P]) † (A[P*Q])) = (𝟎[P*P]) † (A[P*Q])", Typed_COR_Expressions.Typed_Dagger(Typed_COR_Expressions.Typed_EmptyRelation(expression.type()[0], A.type()[0]), A))
						if isinstance(rhs1, Typed_COR_Expressions.Typed_Composition):
							lhs6, rhs6 = rhs1.argument1, rhs1.argument2
							if P==lhs6.type()[0]:
								if Q==lhs6.type()[1]:
									if str(A)==str(lhs6):
										if Q==rhs6.type()[0]:
											if Q==rhs6.type()[1]:
												if isinstance(rhs6, Typed_COR_Expressions.Typed_UniversalRelation):
													return ("(A[P*Q]) ∩ ((A[P*Q]) ∘ (T[Q*Q])) = A[P*Q]", A)
								if P==lhs6.type()[1]:
									if isinstance(lhs6, Typed_COR_Expressions.Typed_UniversalRelation):
										if P==rhs6.type()[0]:
											if Q==rhs6.type()[1]:
												if str(A)==str(rhs6):
													return ("(A[P*Q]) ∩ ((T[P*P]) ∘ (A[P*Q])) = A[P*Q]", A)
				if isinstance(lhs1, Typed_COR_Expressions.Typed_Intersection):
					lhs4, rhs4 = lhs1.argument1, lhs1.argument2
					if P==lhs4.type()[0]:
						if Q==lhs4.type()[1]:
							A = lhs4
							if P==rhs4.type()[0]:
								if Q==rhs4.type()[1]:
									B = rhs4
									if P==rhs1.type()[0]:
										if Q==rhs1.type()[1]:
											if str(B)==str(rhs1):
												return ("((A[P*Q]) ∩ (B[P*Q])) ∩ (B[P*Q]) = (A[P*Q]) ∩ (B[P*Q])", Typed_COR_Expressions.Typed_Intersection(A, B))
											if str(A)==str(rhs1):
												return ("((A[P*Q]) ∩ (B[P*Q])) ∩ (A[P*Q]) = (B[P*Q]) ∩ (A[P*Q])", Typed_COR_Expressions.Typed_Intersection(B, A))
											if isinstance(rhs1, Typed_COR_Expressions.Typed_Intersection):
												lhs11, rhs11 = rhs1.argument1, rhs1.argument2
												if P==lhs11.type()[0]:
													if Q==lhs11.type()[1]:
														C = lhs11
														if P==rhs11.type()[0]:
															if Q==rhs11.type()[1]:
																if str(B)==str(rhs11):
																	return ("((A[P*Q]) ∩ (B[P*Q])) ∩ ((C[P*Q]) ∩ (B[P*Q])) = ((C[P*Q]) ∩ (B[P*Q])) ∩ (A[P*Q])", Typed_COR_Expressions.Typed_Intersection(Typed_COR_Expressions.Typed_Intersection(C, B), A))
																if str(A)==str(rhs11):
																	return ("((A[P*Q]) ∩ (B[P*Q])) ∩ ((C[P*Q]) ∩ (A[P*Q])) = ((C[P*Q]) ∩ (B[P*Q])) ∩ (A[P*Q])", Typed_COR_Expressions.Typed_Intersection(Typed_COR_Expressions.Typed_Intersection(C, B), A))
														if str(B)==str(lhs11):
															if P==rhs11.type()[0]:
																if Q==rhs11.type()[1]:
																	C = rhs11
																	return ("((A[P*Q]) ∩ (B[P*Q])) ∩ ((B[P*Q]) ∩ (C[P*Q])) = ((A[P*Q]) ∩ (C[P*Q])) ∩ (B[P*Q])", Typed_COR_Expressions.Typed_Intersection(Typed_COR_Expressions.Typed_Intersection(A, C), B))
														if str(A)==str(lhs11):
															if P==rhs11.type()[0]:
																if Q==rhs11.type()[1]:
																	C = rhs11
																	return ("((A[P*Q]) ∩ (B[P*Q])) ∩ ((A[P*Q]) ∩ (C[P*Q])) = ((A[P*Q]) ∩ (B[P*Q])) ∩ (C[P*Q])", Typed_COR_Expressions.Typed_Intersection(Typed_COR_Expressions.Typed_Intersection(A, B), C))
											if isinstance(rhs1, Typed_COR_Expressions.Typed_Union):
												lhs11, rhs11 = rhs1.argument1, rhs1.argument2
												if P==lhs11.type()[0]:
													if Q==lhs11.type()[1]:
														C = lhs11
														if P==rhs11.type()[0]:
															if Q==rhs11.type()[1]:
																if str(A)==str(rhs11):
																	return ("((A[P*Q]) ∩ (B[P*Q])) ∩ ((C[P*Q]) ∪ (A[P*Q])) = (B[P*Q]) ∩ (A[P*Q])", Typed_COR_Expressions.Typed_Intersection(B, A))
																if str(B)==str(rhs11):
																	return ("((A[P*Q]) ∩ (B[P*Q])) ∩ ((C[P*Q]) ∪ (B[P*Q])) = (B[P*Q]) ∩ (A[P*Q])", Typed_COR_Expressions.Typed_Intersection(B, A))
														if str(B)==str(lhs11):
															if P==rhs11.type()[0]:
																if Q==rhs11.type()[1]:
																	C = rhs11
																	return ("((A[P*Q]) ∩ (B[P*Q])) ∩ ((B[P*Q]) ∪ (C[P*Q])) = (A[P*Q]) ∩ (B[P*Q])", Typed_COR_Expressions.Typed_Intersection(A, B))
														if str(A)==str(lhs11):
															if P==rhs11.type()[0]:
																if Q==rhs11.type()[1]:
																	C = rhs11
																	return ("((A[P*Q]) ∩ (B[P*Q])) ∩ ((A[P*Q]) ∪ (C[P*Q])) = (B[P*Q]) ∩ (A[P*Q])", Typed_COR_Expressions.Typed_Intersection(B, A))
											if isinstance(rhs1, Typed_COR_Expressions.Typed_Complement):
												arg = rhs1.argument
												if P==arg.type()[0]:
													if Q==arg.type()[1]:
														if str(B)==str(arg):
															return ("((A[P*Q]) ∩ (B[P*Q])) ∩ ((B[P*Q])⁻) = 𝟎[P*Q]", Typed_COR_Expressions.Typed_EmptyRelation(expression.type()[0], expression.type()[1]))
														if str(A)==str(arg):
															return ("((A[P*Q]) ∩ (B[P*Q])) ∩ ((A[P*Q])⁻) = 𝟎[P*Q]", Typed_COR_Expressions.Typed_EmptyRelation(expression.type()[0], expression.type()[1]))
									if isinstance(rhs4, Typed_COR_Expressions.Typed_Intersection):
										lhs9, rhs9 = rhs4.argument1, rhs4.argument2
										if P==lhs9.type()[0]:
											if Q==lhs9.type()[1]:
												B = lhs9
												if P==rhs9.type()[0]:
													if Q==rhs9.type()[1]:
														C = rhs9
														if P==rhs1.type()[0]:
															if Q==rhs1.type()[1]:
																if str(C)==str(rhs1):
																	return ("((A[P*Q]) ∩ ((B[P*Q]) ∩ (C[P*Q]))) ∩ (C[P*Q]) = ((B[P*Q]) ∩ (A[P*Q])) ∩ (C[P*Q])", Typed_COR_Expressions.Typed_Intersection(Typed_COR_Expressions.Typed_Intersection(B, A), C))
																if str(B)==str(rhs1):
																	return ("((A[P*Q]) ∩ ((B[P*Q]) ∩ (C[P*Q]))) ∩ (B[P*Q]) = ((C[P*Q]) ∩ (A[P*Q])) ∩ (B[P*Q])", Typed_COR_Expressions.Typed_Intersection(Typed_COR_Expressions.Typed_Intersection(C, A), B))
									if isinstance(rhs4, Typed_COR_Expressions.Typed_Union):
										lhs9, rhs9 = rhs4.argument1, rhs4.argument2
										if P==lhs9.type()[0]:
											if Q==lhs9.type()[1]:
												B = lhs9
												if P==rhs9.type()[0]:
													if Q==rhs9.type()[1]:
														C = rhs9
														if P==rhs1.type()[0]:
															if Q==rhs1.type()[1]:
																if str(B)==str(rhs1):
																	return ("((A[P*Q]) ∩ ((B[P*Q]) ∪ (C[P*Q]))) ∩ (B[P*Q]) = (B[P*Q]) ∩ (A[P*Q])", Typed_COR_Expressions.Typed_Intersection(B, A))
																if str(C)==str(rhs1):
																	return ("((A[P*Q]) ∩ ((B[P*Q]) ∪ (C[P*Q]))) ∩ (C[P*Q]) = (C[P*Q]) ∩ (A[P*Q])", Typed_COR_Expressions.Typed_Intersection(C, A))
									if isinstance(rhs4, Typed_COR_Expressions.Typed_Complement):
										arg = rhs4.argument
										if P==arg.type()[0]:
											if Q==arg.type()[1]:
												B = arg
												if P==rhs1.type()[0]:
													if Q==rhs1.type()[1]:
														if str(B)==str(rhs1):
															return ("((A[P*Q]) ∩ ((B[P*Q])⁻)) ∩ (B[P*Q]) = 𝟎[P*Q]", Typed_COR_Expressions.Typed_EmptyRelation(expression.type()[0], expression.type()[1]))
							if isinstance(lhs4, Typed_COR_Expressions.Typed_Intersection):
								lhs7, rhs7 = lhs4.argument1, lhs4.argument2
								if P==lhs7.type()[0]:
									if Q==lhs7.type()[1]:
										A = lhs7
										if P==rhs7.type()[0]:
											if Q==rhs7.type()[1]:
												B = rhs7
												if P==rhs4.type()[0]:
													if Q==rhs4.type()[1]:
														C = rhs4
														if P==rhs1.type()[0]:
															if Q==rhs1.type()[1]:
																if str(B)==str(rhs1):
																	return ("(((A[P*Q]) ∩ (B[P*Q])) ∩ (C[P*Q])) ∩ (B[P*Q]) = (B[P*Q]) ∩ ((A[P*Q]) ∩ (C[P*Q]))", Typed_COR_Expressions.Typed_Intersection(B, Typed_COR_Expressions.Typed_Intersection(A, C)))
																if str(A)==str(rhs1):
																	return ("(((A[P*Q]) ∩ (B[P*Q])) ∩ (C[P*Q])) ∩ (A[P*Q]) = ((C[P*Q]) ∩ (A[P*Q])) ∩ (B[P*Q])", Typed_COR_Expressions.Typed_Intersection(Typed_COR_Expressions.Typed_Intersection(C, A), B))
							if isinstance(lhs4, Typed_COR_Expressions.Typed_Union):
								lhs7, rhs7 = lhs4.argument1, lhs4.argument2
								if P==lhs7.type()[0]:
									if Q==lhs7.type()[1]:
										A = lhs7
										if P==rhs7.type()[0]:
											if Q==rhs7.type()[1]:
												B = rhs7
												if P==rhs4.type()[0]:
													if Q==rhs4.type()[1]:
														C = rhs4
														if P==rhs1.type()[0]:
															if Q==rhs1.type()[1]:
																if str(B)==str(rhs1):
																	return ("(((A[P*Q]) ∪ (B[P*Q])) ∩ (C[P*Q])) ∩ (B[P*Q]) = (C[P*Q]) ∩ (B[P*Q])", Typed_COR_Expressions.Typed_Intersection(C, B))
																if str(A)==str(rhs1):
																	return ("(((A[P*Q]) ∪ (B[P*Q])) ∩ (C[P*Q])) ∩ (A[P*Q]) = (C[P*Q]) ∩ (A[P*Q])", Typed_COR_Expressions.Typed_Intersection(C, A))
							if isinstance(lhs4, Typed_COR_Expressions.Typed_Complement):
								arg = lhs4.argument
								if P==arg.type()[0]:
									if Q==arg.type()[1]:
										A = arg
										if P==rhs4.type()[0]:
											if Q==rhs4.type()[1]:
												B = rhs4
												if P==rhs1.type()[0]:
													if Q==rhs1.type()[1]:
														if str(A)==str(rhs1):
															return ("(((A[P*Q])⁻) ∩ (B[P*Q])) ∩ (A[P*Q]) = 𝟎[P*Q]", Typed_COR_Expressions.Typed_EmptyRelation(expression.type()[0], expression.type()[1]))
				if isinstance(lhs1, Typed_COR_Expressions.Typed_Union):
					lhs4, rhs4 = lhs1.argument1, lhs1.argument2
					if P==lhs4.type()[0]:
						if Q==lhs4.type()[1]:
							A = lhs4
							if P==rhs4.type()[0]:
								if Q==rhs4.type()[1]:
									B = rhs4
									if P==rhs1.type()[0]:
										if Q==rhs1.type()[1]:
											if str(B)==str(rhs1):
												return ("((A[P*Q]) ∪ (B[P*Q])) ∩ (B[P*Q]) = B[P*Q]", B)
											if str(A)==str(rhs1):
												return ("((A[P*Q]) ∪ (B[P*Q])) ∩ (A[P*Q]) = A[P*Q]", A)
											if isinstance(rhs1, Typed_COR_Expressions.Typed_Union):
												lhs11, rhs11 = rhs1.argument1, rhs1.argument2
												if P==lhs11.type()[0]:
													if Q==lhs11.type()[1]:
														C = lhs11
														if P==rhs11.type()[0]:
															if Q==rhs11.type()[1]:
																if str(A)==str(rhs11):
																	return ("((A[P*Q]) ∪ (B[P*Q])) ∩ ((C[P*Q]) ∪ (A[P*Q])) = (A[P*Q]) ∪ ((C[P*Q]) ∩ (B[P*Q]))", Typed_COR_Expressions.Typed_Union(A, Typed_COR_Expressions.Typed_Intersection(C, B)))
																if str(B)==str(rhs11):
																	return ("((A[P*Q]) ∪ (B[P*Q])) ∩ ((C[P*Q]) ∪ (B[P*Q])) = (B[P*Q]) ∪ ((A[P*Q]) ∩ (C[P*Q]))", Typed_COR_Expressions.Typed_Union(B, Typed_COR_Expressions.Typed_Intersection(A, C)))
														if str(B)==str(lhs11):
															if P==rhs11.type()[0]:
																if Q==rhs11.type()[1]:
																	C = rhs11
																	return ("((A[P*Q]) ∪ (B[P*Q])) ∩ ((B[P*Q]) ∪ (C[P*Q])) = ((C[P*Q]) ∩ (A[P*Q])) ∪ (B[P*Q])", Typed_COR_Expressions.Typed_Union(Typed_COR_Expressions.Typed_Intersection(C, A), B))
														if str(A)==str(lhs11):
															if P==rhs11.type()[0]:
																if Q==rhs11.type()[1]:
																	C = rhs11
																	return ("((A[P*Q]) ∪ (B[P*Q])) ∩ ((A[P*Q]) ∪ (C[P*Q])) = (A[P*Q]) ∪ ((B[P*Q]) ∩ (C[P*Q]))", Typed_COR_Expressions.Typed_Union(A, Typed_COR_Expressions.Typed_Intersection(B, C)))
											if isinstance(rhs1, Typed_COR_Expressions.Typed_Intersection):
												lhs11, rhs11 = rhs1.argument1, rhs1.argument2
												if P==lhs11.type()[0]:
													if Q==lhs11.type()[1]:
														C = lhs11
														if P==rhs11.type()[0]:
															if Q==rhs11.type()[1]:
																if str(A)==str(rhs11):
																	return ("((A[P*Q]) ∪ (B[P*Q])) ∩ ((C[P*Q]) ∩ (A[P*Q])) = (A[P*Q]) ∩ (C[P*Q])", Typed_COR_Expressions.Typed_Intersection(A, C))
																if str(B)==str(rhs11):
																	return ("((A[P*Q]) ∪ (B[P*Q])) ∩ ((C[P*Q]) ∩ (B[P*Q])) = (C[P*Q]) ∩ (B[P*Q])", Typed_COR_Expressions.Typed_Intersection(C, B))
														if str(B)==str(lhs11):
															if P==rhs11.type()[0]:
																if Q==rhs11.type()[1]:
																	C = rhs11
																	return ("((A[P*Q]) ∪ (B[P*Q])) ∩ ((B[P*Q]) ∩ (C[P*Q])) = (C[P*Q]) ∩ (B[P*Q])", Typed_COR_Expressions.Typed_Intersection(C, B))
														if str(A)==str(lhs11):
															if P==rhs11.type()[0]:
																if Q==rhs11.type()[1]:
																	C = rhs11
																	return ("((A[P*Q]) ∪ (B[P*Q])) ∩ ((A[P*Q]) ∩ (C[P*Q])) = (C[P*Q]) ∩ (A[P*Q])", Typed_COR_Expressions.Typed_Intersection(C, A))
											if isinstance(rhs1, Typed_COR_Expressions.Typed_Complement):
												arg = rhs1.argument
												if P==arg.type()[0]:
													if Q==arg.type()[1]:
														if str(A)==str(arg):
															return ("((A[P*Q]) ∪ (B[P*Q])) ∩ ((A[P*Q])⁻) = ((A[P*Q])⁻) ∩ (B[P*Q])", Typed_COR_Expressions.Typed_Intersection(Typed_COR_Expressions.Typed_Complement(A), B))
														if str(B)==str(arg):
															return ("((A[P*Q]) ∪ (B[P*Q])) ∩ ((B[P*Q])⁻) = ((B[P*Q])⁻) ∩ (A[P*Q])", Typed_COR_Expressions.Typed_Intersection(Typed_COR_Expressions.Typed_Complement(B), A))
									if isinstance(rhs4, Typed_COR_Expressions.Typed_Complement):
										arg = rhs4.argument
										if P==arg.type()[0]:
											if Q==arg.type()[1]:
												B = arg
												if P==rhs1.type()[0]:
													if Q==rhs1.type()[1]:
														if str(B)==str(rhs1):
															return ("((A[P*Q]) ∪ ((B[P*Q])⁻)) ∩ (B[P*Q]) = (A[P*Q]) ∩ (B[P*Q])", Typed_COR_Expressions.Typed_Intersection(A, B))
									if isinstance(rhs4, Typed_COR_Expressions.Typed_Intersection):
										lhs9, rhs9 = rhs4.argument1, rhs4.argument2
										if P==lhs9.type()[0]:
											if Q==lhs9.type()[1]:
												B = lhs9
												if P==rhs9.type()[0]:
													if Q==rhs9.type()[1]:
														C = rhs9
														if P==rhs1.type()[0]:
															if Q==rhs1.type()[1]:
																if str(B)==str(rhs1):
																	return ("((A[P*Q]) ∪ ((B[P*Q]) ∩ (C[P*Q]))) ∩ (B[P*Q]) = (B[P*Q]) ∩ ((C[P*Q]) ∪ (A[P*Q]))", Typed_COR_Expressions.Typed_Intersection(B, Typed_COR_Expressions.Typed_Union(C, A)))
																if str(C)==str(rhs1):
																	return ("((A[P*Q]) ∪ ((B[P*Q]) ∩ (C[P*Q]))) ∩ (C[P*Q]) = ((B[P*Q]) ∪ (A[P*Q])) ∩ (C[P*Q])", Typed_COR_Expressions.Typed_Intersection(Typed_COR_Expressions.Typed_Union(B, A), C))
									if isinstance(rhs4, Typed_COR_Expressions.Typed_Union):
										lhs9, rhs9 = rhs4.argument1, rhs4.argument2
										if P==lhs9.type()[0]:
											if Q==lhs9.type()[1]:
												B = lhs9
												if P==rhs9.type()[0]:
													if Q==rhs9.type()[1]:
														C = rhs9
														if P==rhs1.type()[0]:
															if Q==rhs1.type()[1]:
																if str(B)==str(rhs1):
																	return ("((A[P*Q]) ∪ ((B[P*Q]) ∪ (C[P*Q]))) ∩ (B[P*Q]) = B[P*Q]", B)
																if str(C)==str(rhs1):
																	return ("((A[P*Q]) ∪ ((B[P*Q]) ∪ (C[P*Q]))) ∩ (C[P*Q]) = C[P*Q]", C)
							if isinstance(lhs4, Typed_COR_Expressions.Typed_Intersection):
								lhs7, rhs7 = lhs4.argument1, lhs4.argument2
								if P==lhs7.type()[0]:
									if Q==lhs7.type()[1]:
										A = lhs7
										if P==rhs7.type()[0]:
											if Q==rhs7.type()[1]:
												B = rhs7
												if P==rhs4.type()[0]:
													if Q==rhs4.type()[1]:
														C = rhs4
														if P==rhs1.type()[0]:
															if Q==rhs1.type()[1]:
																if str(A)==str(rhs1):
																	return ("(((A[P*Q]) ∩ (B[P*Q])) ∪ (C[P*Q])) ∩ (A[P*Q]) = (A[P*Q]) ∩ ((C[P*Q]) ∪ (B[P*Q]))", Typed_COR_Expressions.Typed_Intersection(A, Typed_COR_Expressions.Typed_Union(C, B)))
																if str(B)==str(rhs1):
																	return ("(((A[P*Q]) ∩ (B[P*Q])) ∪ (C[P*Q])) ∩ (B[P*Q]) = (B[P*Q]) ∩ ((A[P*Q]) ∪ (C[P*Q]))", Typed_COR_Expressions.Typed_Intersection(B, Typed_COR_Expressions.Typed_Union(A, C)))
							if isinstance(lhs4, Typed_COR_Expressions.Typed_Complement):
								arg = lhs4.argument
								if P==arg.type()[0]:
									if Q==arg.type()[1]:
										A = arg
										if P==rhs4.type()[0]:
											if Q==rhs4.type()[1]:
												B = rhs4
												if P==rhs1.type()[0]:
													if Q==rhs1.type()[1]:
														if str(A)==str(rhs1):
															return ("(((A[P*Q])⁻) ∪ (B[P*Q])) ∩ (A[P*Q]) = (A[P*Q]) ∩ (B[P*Q])", Typed_COR_Expressions.Typed_Intersection(A, B))
							if isinstance(lhs4, Typed_COR_Expressions.Typed_Union):
								lhs7, rhs7 = lhs4.argument1, lhs4.argument2
								if P==lhs7.type()[0]:
									if Q==lhs7.type()[1]:
										A = lhs7
										if P==rhs7.type()[0]:
											if Q==rhs7.type()[1]:
												B = rhs7
												if P==rhs4.type()[0]:
													if Q==rhs4.type()[1]:
														C = rhs4
														if P==rhs1.type()[0]:
															if Q==rhs1.type()[1]:
																if str(A)==str(rhs1):
																	return ("(((A[P*Q]) ∪ (B[P*Q])) ∪ (C[P*Q])) ∩ (A[P*Q]) = A[P*Q]", A)
																if str(B)==str(rhs1):
																	return ("(((A[P*Q]) ∪ (B[P*Q])) ∪ (C[P*Q])) ∩ (B[P*Q]) = B[P*Q]", B)
				if isinstance(lhs1, Typed_COR_Expressions.Typed_EmptyRelation):
					if P==rhs1.type()[0]:
						if Q==rhs1.type()[1]:
							A = rhs1
							return ("(𝟎[P*Q]) ∩ (A[P*Q]) = 𝟎[P*Q]", Typed_COR_Expressions.Typed_EmptyRelation(expression.type()[0], expression.type()[1]))
				if isinstance(lhs1, Typed_COR_Expressions.Typed_UniversalRelation):
					if P==rhs1.type()[0]:
						if Q==rhs1.type()[1]:
							A = rhs1
							return ("(T[P*Q]) ∩ (A[P*Q]) = A[P*Q]", A)
				if isinstance(lhs1, Typed_COR_Expressions.Typed_Complement):
					arg = lhs1.argument
					if P==arg.type()[0]:
						if Q==arg.type()[1]:
							A = arg
							if P==rhs1.type()[0]:
								if Q==rhs1.type()[1]:
									if str(A)==str(rhs1):
										return ("((A[P*Q])⁻) ∩ (A[P*Q]) = 𝟎[P*Q]", Typed_COR_Expressions.Typed_EmptyRelation(expression.type()[0], expression.type()[1]))
									if isinstance(rhs1, Typed_COR_Expressions.Typed_Intersection):
										lhs9, rhs9 = rhs1.argument1, rhs1.argument2
										if P==lhs9.type()[0]:
											if Q==lhs9.type()[1]:
												if str(A)==str(lhs9):
													if P==rhs9.type()[0]:
														if Q==rhs9.type()[1]:
															B = rhs9
															return ("((A[P*Q])⁻) ∩ ((A[P*Q]) ∩ (B[P*Q])) = 𝟎[P*Q]", Typed_COR_Expressions.Typed_EmptyRelation(expression.type()[0], expression.type()[1]))
												B = lhs9
												if P==rhs9.type()[0]:
													if Q==rhs9.type()[1]:
														if str(A)==str(rhs9):
															return ("((A[P*Q])⁻) ∩ ((B[P*Q]) ∩ (A[P*Q])) = 𝟎[P*Q]", Typed_COR_Expressions.Typed_EmptyRelation(expression.type()[0], expression.type()[1]))
									if isinstance(rhs1, Typed_COR_Expressions.Typed_Union):
										lhs9, rhs9 = rhs1.argument1, rhs1.argument2
										if P==lhs9.type()[0]:
											if Q==lhs9.type()[1]:
												B = lhs9
												if P==rhs9.type()[0]:
													if Q==rhs9.type()[1]:
														if str(A)==str(rhs9):
															return ("((A[P*Q])⁻) ∩ ((B[P*Q]) ∪ (A[P*Q])) = (B[P*Q]) ∩ ((A[P*Q])⁻)", Typed_COR_Expressions.Typed_Intersection(B, Typed_COR_Expressions.Typed_Complement(A)))
												if str(A)==str(lhs9):
													if P==rhs9.type()[0]:
														if Q==rhs9.type()[1]:
															B = rhs9
															return ("((A[P*Q])⁻) ∩ ((A[P*Q]) ∪ (B[P*Q])) = ((A[P*Q])⁻) ∩ (B[P*Q])", Typed_COR_Expressions.Typed_Intersection(Typed_COR_Expressions.Typed_Complement(A), B))
									if isinstance(rhs1, Typed_COR_Expressions.Typed_Complement):
										arg = rhs1.argument
										if P==arg.type()[0]:
											if Q==arg.type()[1]:
												B = arg
												return ("((A[P*Q])⁻) ∩ ((B[P*Q])⁻) = ((B[P*Q]) ∪ (A[P*Q]))⁻", Typed_COR_Expressions.Typed_Complement(Typed_COR_Expressions.Typed_Union(B, A)))
							if isinstance(arg, Typed_COR_Expressions.Typed_Intersection):
								lhs7, rhs7 = arg.argument1, arg.argument2
								if P==lhs7.type()[0]:
									if Q==lhs7.type()[1]:
										A = lhs7
										if P==rhs7.type()[0]:
											if Q==rhs7.type()[1]:
												B = rhs7
												if P==rhs1.type()[0]:
													if Q==rhs1.type()[1]:
														if str(A)==str(rhs1):
															return ("(((A[P*Q]) ∩ (B[P*Q]))⁻) ∩ (A[P*Q]) = ((B[P*Q])⁻) ∩ (A[P*Q])", Typed_COR_Expressions.Typed_Intersection(Typed_COR_Expressions.Typed_Complement(B), A))
														if str(B)==str(rhs1):
															return ("(((A[P*Q]) ∩ (B[P*Q]))⁻) ∩ (B[P*Q]) = (B[P*Q]) ∩ ((A[P*Q])⁻)", Typed_COR_Expressions.Typed_Intersection(B, Typed_COR_Expressions.Typed_Complement(A)))
							if isinstance(arg, Typed_COR_Expressions.Typed_Union):
								lhs7, rhs7 = arg.argument1, arg.argument2
								if P==lhs7.type()[0]:
									if Q==lhs7.type()[1]:
										A = lhs7
										if P==rhs7.type()[0]:
											if Q==rhs7.type()[1]:
												B = rhs7
												if P==rhs1.type()[0]:
													if Q==rhs1.type()[1]:
														if str(A)==str(rhs1):
															return ("(((A[P*Q]) ∪ (B[P*Q]))⁻) ∩ (A[P*Q]) = 𝟎[P*Q]", Typed_COR_Expressions.Typed_EmptyRelation(expression.type()[0], expression.type()[1]))
														if str(B)==str(rhs1):
															return ("(((A[P*Q]) ∪ (B[P*Q]))⁻) ∩ (B[P*Q]) = 𝟎[P*Q]", Typed_COR_Expressions.Typed_EmptyRelation(expression.type()[0], expression.type()[1]))
				if isinstance(lhs1, Typed_COR_Expressions.Typed_Dagger):
					lhs4, rhs4 = lhs1.argument1, lhs1.argument2
					if P==lhs4.type()[0]:
						if P==lhs4.type()[1]:
							A = lhs4
							if P==rhs4.type()[0]:
								if Q==rhs4.type()[1]:
									B = rhs4
									if P==rhs1.type()[0]:
										if Q==rhs1.type()[1]:
											if isinstance(rhs1, Typed_COR_Expressions.Typed_Dagger):
												lhs11, rhs11 = rhs1.argument1, rhs1.argument2
												if P==lhs11.type()[0]:
													if P==lhs11.type()[1]:
														C = lhs11
														if P==rhs11.type()[0]:
															if Q==rhs11.type()[1]:
																if str(B)==str(rhs11):
																	return ("((A[P*P]) † (B[P*Q])) ∩ ((C[P*P]) † (B[P*Q])) = ((A[P*P]) ∩ (C[P*P])) † (B[P*Q])", Typed_COR_Expressions.Typed_Dagger(Typed_COR_Expressions.Typed_Intersection(A, C), B))
														if str(A)==str(lhs11):
															if P==rhs11.type()[0]:
																if Q==rhs11.type()[1]:
																	C = rhs11
																	return ("((A[P*P]) † (B[P*Q])) ∩ ((A[P*P]) † (C[P*Q])) = (A[P*P]) † ((B[P*Q]) ∩ (C[P*Q]))", Typed_COR_Expressions.Typed_Dagger(A, Typed_COR_Expressions.Typed_Intersection(B, C)))
							if isinstance(lhs4, Typed_COR_Expressions.Typed_IdentityRelation):
								if P==rhs4.type()[0]:
									if Q==rhs4.type()[1]:
										A = rhs4
										if P==rhs1.type()[0]:
											if Q==rhs1.type()[1]:
												if str(A)==str(rhs1):
													return ("((𝟏[P*P]) † (A[P*Q])) ∩ (A[P*Q]) = (𝟎[P*P]) † (A[P*Q])", Typed_COR_Expressions.Typed_Dagger(Typed_COR_Expressions.Typed_EmptyRelation(expression.type()[0], A.type()[0]), A))
							if isinstance(lhs4, Typed_COR_Expressions.Typed_EmptyRelation):
								if P==rhs4.type()[0]:
									if Q==rhs4.type()[1]:
										A = rhs4
										if P==rhs1.type()[0]:
											if Q==rhs1.type()[1]:
												if str(A)==str(rhs1):
													return ("((𝟎[P*P]) † (A[P*Q])) ∩ (A[P*Q]) = (𝟎[P*P]) † (A[P*Q])", Typed_COR_Expressions.Typed_Dagger(Typed_COR_Expressions.Typed_EmptyRelation(expression.type()[0], A.type()[0]), A))
						if Q==lhs4.type()[1]:
							A = lhs4
							if Q==rhs4.type()[0]:
								if Q==rhs4.type()[1]:
									B = rhs4
									if P==rhs1.type()[0]:
										if Q==rhs1.type()[1]:
											if isinstance(rhs1, Typed_COR_Expressions.Typed_Dagger):
												lhs11, rhs11 = rhs1.argument1, rhs1.argument2
												if P==lhs11.type()[0]:
													if Q==lhs11.type()[1]:
														C = lhs11
														if Q==rhs11.type()[0]:
															if Q==rhs11.type()[1]:
																if str(B)==str(rhs11):
																	return ("((A[P*Q]) † (B[Q*Q])) ∩ ((C[P*Q]) † (B[Q*Q])) = ((A[P*Q]) ∩ (C[P*Q])) † (B[Q*Q])", Typed_COR_Expressions.Typed_Dagger(Typed_COR_Expressions.Typed_Intersection(A, C), B))
														if str(A)==str(lhs11):
															if Q==rhs11.type()[0]:
																if Q==rhs11.type()[1]:
																	C = rhs11
																	return ("((A[P*Q]) † (B[Q*Q])) ∩ ((A[P*Q]) † (C[Q*Q])) = (A[P*Q]) † ((B[Q*Q]) ∩ (C[Q*Q]))", Typed_COR_Expressions.Typed_Dagger(A, Typed_COR_Expressions.Typed_Intersection(B, C)))
									if isinstance(rhs4, Typed_COR_Expressions.Typed_IdentityRelation):
										if P==rhs1.type()[0]:
											if Q==rhs1.type()[1]:
												if str(A)==str(rhs1):
													return ("((A[P*Q]) † (𝟏[Q*Q])) ∩ (A[P*Q]) = (A[P*Q]) † (𝟎[Q*Q])", Typed_COR_Expressions.Typed_Dagger(A, Typed_COR_Expressions.Typed_EmptyRelation(A.type()[1], expression.type()[1])))
									if isinstance(rhs4, Typed_COR_Expressions.Typed_EmptyRelation):
										if P==rhs1.type()[0]:
											if Q==rhs1.type()[1]:
												if str(A)==str(rhs1):
													return ("((A[P*Q]) † (𝟎[Q*Q])) ∩ (A[P*Q]) = (A[P*Q]) † (𝟎[Q*Q])", Typed_COR_Expressions.Typed_Dagger(A, Typed_COR_Expressions.Typed_EmptyRelation(A.type()[1], expression.type()[1])))
						R = lhs4.type()[1]
						A = lhs4
						if R==rhs4.type()[0]:
							if Q==rhs4.type()[1]:
								B = rhs4
								if P==rhs1.type()[0]:
									if Q==rhs1.type()[1]:
										if isinstance(rhs1, Typed_COR_Expressions.Typed_Dagger):
											lhs10, rhs10 = rhs1.argument1, rhs1.argument2
											if P==lhs10.type()[0]:
												if R==lhs10.type()[1]:
													C = lhs10
													if R==rhs10.type()[0]:
														if Q==rhs10.type()[1]:
															if str(B)==str(rhs10):
																return ("((A[P*R]) † (B[R*Q])) ∩ ((C[P*R]) † (B[R*Q])) = ((A[P*R]) ∩ (C[P*R])) † (B[R*Q])", Typed_COR_Expressions.Typed_Dagger(Typed_COR_Expressions.Typed_Intersection(A, C), B))
													if str(A)==str(lhs10):
														if R==rhs10.type()[0]:
															if Q==rhs10.type()[1]:
																C = rhs10
																return ("((A[P*R]) † (B[R*Q])) ∩ ((A[P*R]) † (C[R*Q])) = (A[P*R]) † ((B[R*Q]) ∩ (C[R*Q]))", Typed_COR_Expressions.Typed_Dagger(A, Typed_COR_Expressions.Typed_Intersection(B, C)))
				if isinstance(lhs1, Typed_COR_Expressions.Typed_Composition):
					lhs4, rhs4 = lhs1.argument1, lhs1.argument2
					if P==lhs4.type()[0]:
						if Q==lhs4.type()[1]:
							A = lhs4
							if Q==rhs4.type()[0]:
								if Q==rhs4.type()[1]:
									if isinstance(rhs4, Typed_COR_Expressions.Typed_UniversalRelation):
										if P==rhs1.type()[0]:
											if Q==rhs1.type()[1]:
												if str(A)==str(rhs1):
													return ("((A[P*Q]) ∘ (T[Q*Q])) ∩ (A[P*Q]) = A[P*Q]", A)
						if P==lhs4.type()[1]:
							if isinstance(lhs4, Typed_COR_Expressions.Typed_UniversalRelation):
								if P==rhs4.type()[0]:
									if Q==rhs4.type()[1]:
										A = rhs4
										if P==rhs1.type()[0]:
											if Q==rhs1.type()[1]:
												if str(A)==str(rhs1):
													return ("((T[P*P]) ∘ (A[P*Q])) ∩ (A[P*Q]) = A[P*Q]", A)
	if isinstance(expression, Typed_COR_Expressions.Typed_Converse):
		arg = expression.argument
		if Q==arg.type()[0]:
			if P==arg.type()[1]:
				if isinstance(arg, Typed_COR_Expressions.Typed_Converse):
					arg = arg.argument
					if P==arg.type()[0]:
						if Q==arg.type()[1]:
							A = arg
							return ("((A[P*Q])⁻¹)⁻¹ = A[P*Q]", A)
				if isinstance(arg, Typed_COR_Expressions.Typed_EmptyRelation):
					return ("(𝟎[Q*P])⁻¹ = 𝟎[P*Q]", Typed_COR_Expressions.Typed_EmptyRelation(expression.type()[0], expression.type()[1]))
				if isinstance(arg, Typed_COR_Expressions.Typed_UniversalRelation):
					return ("(T[Q*P])⁻¹ = T[P*Q]", Typed_COR_Expressions.Typed_UniversalRelation(expression.type()[0], expression.type()[1]))
				if isinstance(arg, Typed_COR_Expressions.Typed_Complement):
					arg = arg.argument
					if Q==arg.type()[0]:
						if P==arg.type()[1]:
							if isinstance(arg, Typed_COR_Expressions.Typed_Converse):
								arg = arg.argument
								if P==arg.type()[0]:
									if Q==arg.type()[1]:
										A = arg
										return ("(((A[P*Q])⁻¹)⁻)⁻¹ = (A[P*Q])⁻", Typed_COR_Expressions.Typed_Complement(A))
	if isinstance(expression, Typed_COR_Expressions.Typed_Composition):
		lhs1, rhs1 = expression.argument1, expression.argument2
		if P==lhs1.type()[0]:
			R = lhs1.type()[1]
			A = lhs1
			if R==rhs1.type()[0]:
				if Q==rhs1.type()[1]:
					if isinstance(rhs1, Typed_COR_Expressions.Typed_EmptyRelation):
						return ("(A[P*R]) ∘ (𝟎[R*Q]) = 𝟎[P*Q]", Typed_COR_Expressions.Typed_EmptyRelation(expression.type()[0], expression.type()[1]))
			if isinstance(lhs1, Typed_COR_Expressions.Typed_EmptyRelation):
				if R==rhs1.type()[0]:
					if Q==rhs1.type()[1]:
						A = rhs1
						return ("(𝟎[P*R]) ∘ (A[R*Q]) = 𝟎[P*Q]", Typed_COR_Expressions.Typed_EmptyRelation(expression.type()[0], expression.type()[1]))
			if isinstance(lhs1, Typed_COR_Expressions.Typed_Complement):
				arg = lhs1.argument
				if P==arg.type()[0]:
					if R==arg.type()[1]:
						A = arg
						if R==rhs1.type()[0]:
							if Q==rhs1.type()[1]:
								if isinstance(rhs1, Typed_COR_Expressions.Typed_Complement):
									arg = rhs1.argument
									if R==arg.type()[0]:
										if Q==arg.type()[1]:
											B = arg
											return ("((A[P*R])⁻) ∘ ((B[R*Q])⁻) = ((A[P*R]) † (B[R*Q]))⁻", Typed_COR_Expressions.Typed_Complement(Typed_COR_Expressions.Typed_Dagger(A, B)))
			if isinstance(lhs1, Typed_COR_Expressions.Typed_UniversalRelation):
				if R==rhs1.type()[0]:
					if Q==rhs1.type()[1]:
						if isinstance(rhs1, Typed_COR_Expressions.Typed_UniversalRelation):
							return ("(T[P*R]) ∘ (T[R*Q]) = T[P*Q]", Typed_COR_Expressions.Typed_UniversalRelation(expression.type()[0], expression.type()[1]))
			if P==lhs1.type()[1]:
				if isinstance(lhs1, Typed_COR_Expressions.Typed_IdentityRelation):
					if P==rhs1.type()[0]:
						if Q==rhs1.type()[1]:
							A = rhs1
							return ("(𝟏[P*P]) ∘ (A[P*Q]) = A[P*Q]", A)
				if isinstance(lhs1, Typed_COR_Expressions.Typed_Dagger):
					lhs4, rhs4 = lhs1.argument1, lhs1.argument2
					if P==lhs4.type()[0]:
						if Q==lhs4.type()[1]:
							A = lhs4
							if Q==rhs4.type()[0]:
								if P==rhs4.type()[1]:
									if isinstance(rhs4, Typed_COR_Expressions.Typed_EmptyRelation):
										if P==rhs1.type()[0]:
											if Q==rhs1.type()[1]:
												if str(A)==str(rhs1):
													return ("((A[P*Q]) † (𝟎[Q*P])) ∘ (A[P*Q]) = (A[P*Q]) † (𝟎[Q*Q])", Typed_COR_Expressions.Typed_Dagger(A, Typed_COR_Expressions.Typed_EmptyRelation(A.type()[1], expression.type()[1])))
			if Q==lhs1.type()[1]:
				A = lhs1
				if Q==rhs1.type()[0]:
					if Q==rhs1.type()[1]:
						if isinstance(rhs1, Typed_COR_Expressions.Typed_IdentityRelation):
							return ("(A[P*Q]) ∘ (𝟏[Q*Q]) = A[P*Q]", A)
						if isinstance(rhs1, Typed_COR_Expressions.Typed_Dagger):
							lhs6, rhs6 = rhs1.argument1, rhs1.argument2
							if Q==lhs6.type()[0]:
								if P==lhs6.type()[1]:
									if isinstance(lhs6, Typed_COR_Expressions.Typed_EmptyRelation):
										if P==rhs6.type()[0]:
											if Q==rhs6.type()[1]:
												if str(A)==str(rhs6):
													return ("(A[P*Q]) ∘ ((𝟎[Q*P]) † (A[P*Q])) = (𝟎[P*P]) † (A[P*Q])", Typed_COR_Expressions.Typed_Dagger(Typed_COR_Expressions.Typed_EmptyRelation(expression.type()[0], A.type()[0]), A))
	if isinstance(expression, Typed_COR_Expressions.Typed_Dagger):
		lhs1, rhs1 = expression.argument1, expression.argument2
		if P==lhs1.type()[0]:
			if P==lhs1.type()[1]:
				A = lhs1
				if P==rhs1.type()[0]:
					if Q==rhs1.type()[1]:
						if isinstance(rhs1, Typed_COR_Expressions.Typed_UniversalRelation):
							return ("(A[P*P]) † (T[P*Q]) = T[P*Q]", Typed_COR_Expressions.Typed_UniversalRelation(expression.type()[0], expression.type()[1]))
				if isinstance(lhs1, Typed_COR_Expressions.Typed_UniversalRelation):
					if P==rhs1.type()[0]:
						if Q==rhs1.type()[1]:
							A = rhs1
							return ("(T[P*P]) † (A[P*Q]) = T[P*Q]", Typed_COR_Expressions.Typed_UniversalRelation(expression.type()[0], expression.type()[1]))
				if isinstance(lhs1, Typed_COR_Expressions.Typed_Complement):
					arg = lhs1.argument
					if P==arg.type()[0]:
						if P==arg.type()[1]:
							if isinstance(arg, Typed_COR_Expressions.Typed_IdentityRelation):
								if P==rhs1.type()[0]:
									if Q==rhs1.type()[1]:
										A = rhs1
										return ("((𝟏[P*P])⁻) † (A[P*Q]) = A[P*Q]", A)
							A = arg
							if P==rhs1.type()[0]:
								if Q==rhs1.type()[1]:
									if isinstance(rhs1, Typed_COR_Expressions.Typed_Complement):
										arg = rhs1.argument
										if P==arg.type()[0]:
											if Q==arg.type()[1]:
												B = arg
												return ("((A[P*P])⁻) † ((B[P*Q])⁻) = ((A[P*P]) ∘ (B[P*Q]))⁻", Typed_COR_Expressions.Typed_Complement(Typed_COR_Expressions.Typed_Composition(A, B)))
				if isinstance(lhs1, Typed_COR_Expressions.Typed_EmptyRelation):
					if P==rhs1.type()[0]:
						if Q==rhs1.type()[1]:
							if isinstance(rhs1, Typed_COR_Expressions.Typed_EmptyRelation):
								return ("(𝟎[P*P]) † (𝟎[P*Q]) = 𝟎[P*Q]", Typed_COR_Expressions.Typed_EmptyRelation(expression.type()[0], expression.type()[1]))
				if isinstance(lhs1, Typed_COR_Expressions.Typed_Composition):
					lhs4, rhs4 = lhs1.argument1, lhs1.argument2
					if P==lhs4.type()[0]:
						if Q==lhs4.type()[1]:
							A = lhs4
							if Q==rhs4.type()[0]:
								if P==rhs4.type()[1]:
									if isinstance(rhs4, Typed_COR_Expressions.Typed_UniversalRelation):
										if P==rhs1.type()[0]:
											if Q==rhs1.type()[1]:
												if str(A)==str(rhs1):
													return ("((A[P*Q]) ∘ (T[Q*P])) † (A[P*Q]) = (A[P*Q]) ∘ (T[Q*Q])", Typed_COR_Expressions.Typed_Composition(A, Typed_COR_Expressions.Typed_UniversalRelation(A.type()[1], expression.type()[1])))
			R = lhs1.type()[1]
			A = lhs1
			if R==rhs1.type()[0]:
				if Q==rhs1.type()[1]:
					if isinstance(rhs1, Typed_COR_Expressions.Typed_UniversalRelation):
						return ("(A[P*R]) † (T[R*Q]) = T[P*Q]", Typed_COR_Expressions.Typed_UniversalRelation(expression.type()[0], expression.type()[1]))
			if isinstance(lhs1, Typed_COR_Expressions.Typed_UniversalRelation):
				if R==rhs1.type()[0]:
					if Q==rhs1.type()[1]:
						A = rhs1
						return ("(T[P*R]) † (A[R*Q]) = T[P*Q]", Typed_COR_Expressions.Typed_UniversalRelation(expression.type()[0], expression.type()[1]))
			if isinstance(lhs1, Typed_COR_Expressions.Typed_Complement):
				arg = lhs1.argument
				if P==arg.type()[0]:
					if R==arg.type()[1]:
						A = arg
						if R==rhs1.type()[0]:
							if Q==rhs1.type()[1]:
								if isinstance(rhs1, Typed_COR_Expressions.Typed_Complement):
									arg = rhs1.argument
									if R==arg.type()[0]:
										if Q==arg.type()[1]:
											B = arg
											return ("((A[P*R])⁻) † ((B[R*Q])⁻) = ((A[P*R]) ∘ (B[R*Q]))⁻", Typed_COR_Expressions.Typed_Complement(Typed_COR_Expressions.Typed_Composition(A, B)))
			if isinstance(lhs1, Typed_COR_Expressions.Typed_EmptyRelation):
				if R==rhs1.type()[0]:
					if Q==rhs1.type()[1]:
						if isinstance(rhs1, Typed_COR_Expressions.Typed_EmptyRelation):
							return ("(𝟎[P*R]) † (𝟎[R*Q]) = 𝟎[P*Q]", Typed_COR_Expressions.Typed_EmptyRelation(expression.type()[0], expression.type()[1]))
			if Q==lhs1.type()[1]:
				A = lhs1
				if Q==rhs1.type()[0]:
					if Q==rhs1.type()[1]:
						if isinstance(rhs1, Typed_COR_Expressions.Typed_Composition):
							lhs6, rhs6 = rhs1.argument1, rhs1.argument2
							if Q==lhs6.type()[0]:
								if P==lhs6.type()[1]:
									if isinstance(lhs6, Typed_COR_Expressions.Typed_UniversalRelation):
										if P==rhs6.type()[0]:
											if Q==rhs6.type()[1]:
												if str(A)==str(rhs6):
													return ("(A[P*Q]) † ((T[Q*P]) ∘ (A[P*Q])) = (T[P*P]) ∘ (A[P*Q])", Typed_COR_Expressions.Typed_Composition(Typed_COR_Expressions.Typed_UniversalRelation(expression.type()[0], A.type()[0]), A))
						if isinstance(rhs1, Typed_COR_Expressions.Typed_Complement):
							arg = rhs1.argument
							if Q==arg.type()[0]:
								if Q==arg.type()[1]:
									if isinstance(arg, Typed_COR_Expressions.Typed_IdentityRelation):
										return ("(A[P*Q]) † ((𝟏[Q*Q])⁻) = A[P*Q]", A)
	if isinstance(expression, Typed_COR_Expressions.Typed_Complement):
		arg = expression.argument
		if P==arg.type()[0]:
			if Q==arg.type()[1]:
				if isinstance(arg, Typed_COR_Expressions.Typed_UniversalRelation):
					return ("(T[P*Q])⁻ = 𝟎[P*Q]", Typed_COR_Expressions.Typed_EmptyRelation(expression.type()[0], expression.type()[1]))
				if isinstance(arg, Typed_COR_Expressions.Typed_EmptyRelation):
					return ("(𝟎[P*Q])⁻ = T[P*Q]", Typed_COR_Expressions.Typed_UniversalRelation(expression.type()[0], expression.type()[1]))
				if isinstance(arg, Typed_COR_Expressions.Typed_Complement):
					arg = arg.argument
					if P==arg.type()[0]:
						if Q==arg.type()[1]:
							A = arg
							return ("((A[P*Q])⁻)⁻ = A[P*Q]", A)
				if isinstance(arg, Typed_COR_Expressions.Typed_Union):
					lhs4, rhs4 = arg.argument1, arg.argument2
					if P==lhs4.type()[0]:
						if Q==lhs4.type()[1]:
							A = lhs4
							if P==rhs4.type()[0]:
								if Q==rhs4.type()[1]:
									if isinstance(rhs4, Typed_COR_Expressions.Typed_Complement):
										arg = rhs4.argument
										if P==arg.type()[0]:
											if Q==arg.type()[1]:
												B = arg
												return ("((A[P*Q]) ∪ ((B[P*Q])⁻))⁻ = ((A[P*Q])⁻) ∩ (B[P*Q])", Typed_COR_Expressions.Typed_Intersection(Typed_COR_Expressions.Typed_Complement(A), B))
							if isinstance(lhs4, Typed_COR_Expressions.Typed_Complement):
								arg = lhs4.argument
								if P==arg.type()[0]:
									if Q==arg.type()[1]:
										A = arg
										if P==rhs4.type()[0]:
											if Q==rhs4.type()[1]:
												B = rhs4
												return ("(((A[P*Q])⁻) ∪ (B[P*Q]))⁻ = (A[P*Q]) ∩ ((B[P*Q])⁻)", Typed_COR_Expressions.Typed_Intersection(A, Typed_COR_Expressions.Typed_Complement(B)))
				if isinstance(arg, Typed_COR_Expressions.Typed_Intersection):
					lhs4, rhs4 = arg.argument1, arg.argument2
					if P==lhs4.type()[0]:
						if Q==lhs4.type()[1]:
							if isinstance(lhs4, Typed_COR_Expressions.Typed_Complement):
								arg = lhs4.argument
								if P==arg.type()[0]:
									if Q==arg.type()[1]:
										A = arg
										if P==rhs4.type()[0]:
											if Q==rhs4.type()[1]:
												B = rhs4
												return ("(((A[P*Q])⁻) ∩ (B[P*Q]))⁻ = ((B[P*Q])⁻) ∪ (A[P*Q])", Typed_COR_Expressions.Typed_Union(Typed_COR_Expressions.Typed_Complement(B), A))
							A = lhs4
							if P==rhs4.type()[0]:
								if Q==rhs4.type()[1]:
									if isinstance(rhs4, Typed_COR_Expressions.Typed_Complement):
										arg = rhs4.argument
										if P==arg.type()[0]:
											if Q==arg.type()[1]:
												B = arg
												return ("((A[P*Q]) ∩ ((B[P*Q])⁻))⁻ = (B[P*Q]) ∪ ((A[P*Q])⁻)", Typed_COR_Expressions.Typed_Union(B, Typed_COR_Expressions.Typed_Complement(A)))
				if isinstance(arg, Typed_COR_Expressions.Typed_Composition):
					lhs4, rhs4 = arg.argument1, arg.argument2
					if P==lhs4.type()[0]:
						R = lhs4.type()[1]
						if isinstance(lhs4, Typed_COR_Expressions.Typed_Complement):
							arg = lhs4.argument
							if P==arg.type()[0]:
								if R==arg.type()[1]:
									A = arg
									if R==rhs4.type()[0]:
										if Q==rhs4.type()[1]:
											B = rhs4
											return ("(((A[P*R])⁻) ∘ (B[R*Q]))⁻ = (A[P*R]) † ((B[R*Q])⁻)", Typed_COR_Expressions.Typed_Dagger(A, Typed_COR_Expressions.Typed_Complement(B)))
						A = lhs4
						if R==rhs4.type()[0]:
							if Q==rhs4.type()[1]:
								if isinstance(rhs4, Typed_COR_Expressions.Typed_Complement):
									arg = rhs4.argument
									if R==arg.type()[0]:
										if Q==arg.type()[1]:
											B = arg
											return ("((A[P*R]) ∘ ((B[R*Q])⁻))⁻ = ((A[P*R])⁻) † (B[R*Q])", Typed_COR_Expressions.Typed_Dagger(Typed_COR_Expressions.Typed_Complement(A), B))
				if isinstance(arg, Typed_COR_Expressions.Typed_Dagger):
					lhs4, rhs4 = arg.argument1, arg.argument2
					if P==lhs4.type()[0]:
						R = lhs4.type()[1]
						if isinstance(lhs4, Typed_COR_Expressions.Typed_Complement):
							arg = lhs4.argument
							if P==arg.type()[0]:
								if R==arg.type()[1]:
									A = arg
									if R==rhs4.type()[0]:
										if Q==rhs4.type()[1]:
											B = rhs4
											return ("(((A[P*R])⁻) † (B[R*Q]))⁻ = (A[P*R]) ∘ ((B[R*Q])⁻)", Typed_COR_Expressions.Typed_Composition(A, Typed_COR_Expressions.Typed_Complement(B)))
						A = lhs4
						if R==rhs4.type()[0]:
							if Q==rhs4.type()[1]:
								if isinstance(rhs4, Typed_COR_Expressions.Typed_Complement):
									arg = rhs4.argument
									if R==arg.type()[0]:
										if Q==arg.type()[1]:
											B = arg
											return ("((A[P*R]) † ((B[R*Q])⁻))⁻ = ((A[P*R])⁻) ∘ (B[R*Q])", Typed_COR_Expressions.Typed_Composition(Typed_COR_Expressions.Typed_Complement(A), B))
	if P==expression.type()[1]:
		if isinstance(expression, Typed_COR_Expressions.Typed_Converse):
			arg = expression.argument
			if P==arg.type()[0]:
				if P==arg.type()[1]:
					if isinstance(arg, Typed_COR_Expressions.Typed_IdentityRelation):
						return ("(𝟏[P*P])⁻¹ = 𝟏[P*P]", Typed_COR_Expressions.Typed_IdentityRelation(expression.type()[0], expression.type()[1]))
					if isinstance(arg, Typed_COR_Expressions.Typed_Union):
						lhs5, rhs5 = arg.argument1, arg.argument2
						if P==lhs5.type()[0]:
							if P==lhs5.type()[1]:
								A = lhs5
								if P==rhs5.type()[0]:
									if P==rhs5.type()[1]:
										if isinstance(rhs5, Typed_COR_Expressions.Typed_Converse):
											arg = rhs5.argument
											if P==arg.type()[0]:
												if P==arg.type()[1]:
													B = arg
													return ("((A[P*P]) ∪ ((B[P*P])⁻¹))⁻¹ = ((A[P*P])⁻¹) ∪ (B[P*P])", Typed_COR_Expressions.Typed_Union(Typed_COR_Expressions.Typed_Converse(A), B))
								if isinstance(lhs5, Typed_COR_Expressions.Typed_Converse):
									arg = lhs5.argument
									if P==arg.type()[0]:
										if P==arg.type()[1]:
											A = arg
											if P==rhs5.type()[0]:
												if P==rhs5.type()[1]:
													B = rhs5
													return ("(((A[P*P])⁻¹) ∪ (B[P*P]))⁻¹ = ((B[P*P])⁻¹) ∪ (A[P*P])", Typed_COR_Expressions.Typed_Union(Typed_COR_Expressions.Typed_Converse(B), A))
					if isinstance(arg, Typed_COR_Expressions.Typed_Intersection):
						lhs5, rhs5 = arg.argument1, arg.argument2
						if P==lhs5.type()[0]:
							if P==lhs5.type()[1]:
								A = lhs5
								if P==rhs5.type()[0]:
									if P==rhs5.type()[1]:
										if isinstance(rhs5, Typed_COR_Expressions.Typed_IdentityRelation):
											return ("((A[P*P]) ∩ (𝟏[P*P]))⁻¹ = (𝟏[P*P]) ∩ (A[P*P])", Typed_COR_Expressions.Typed_Intersection(Typed_COR_Expressions.Typed_IdentityRelation(expression.type()[0], expression.type()[1]), A))
										if isinstance(rhs5, Typed_COR_Expressions.Typed_Converse):
											arg = rhs5.argument
											if P==arg.type()[0]:
												if P==arg.type()[1]:
													B = arg
													return ("((A[P*P]) ∩ ((B[P*P])⁻¹))⁻¹ = ((A[P*P])⁻¹) ∩ (B[P*P])", Typed_COR_Expressions.Typed_Intersection(Typed_COR_Expressions.Typed_Converse(A), B))
								if isinstance(lhs5, Typed_COR_Expressions.Typed_Converse):
									arg = lhs5.argument
									if P==arg.type()[0]:
										if P==arg.type()[1]:
											A = arg
											if P==rhs5.type()[0]:
												if P==rhs5.type()[1]:
													B = rhs5
													return ("(((A[P*P])⁻¹) ∩ (B[P*P]))⁻¹ = ((B[P*P])⁻¹) ∩ (A[P*P])", Typed_COR_Expressions.Typed_Intersection(Typed_COR_Expressions.Typed_Converse(B), A))
								if isinstance(lhs5, Typed_COR_Expressions.Typed_IdentityRelation):
									if P==rhs5.type()[0]:
										if P==rhs5.type()[1]:
											A = rhs5
											return ("((𝟏[P*P]) ∩ (A[P*P]))⁻¹ = (A[P*P]) ∩ (𝟏[P*P])", Typed_COR_Expressions.Typed_Intersection(A, Typed_COR_Expressions.Typed_IdentityRelation(expression.type()[0], expression.type()[1])))
					if isinstance(arg, Typed_COR_Expressions.Typed_Complement):
						arg = arg.argument
						if P==arg.type()[0]:
							if P==arg.type()[1]:
								if isinstance(arg, Typed_COR_Expressions.Typed_IdentityRelation):
									return ("((𝟏[P*P])⁻)⁻¹ = (𝟏[P*P])⁻", Typed_COR_Expressions.Typed_Complement(Typed_COR_Expressions.Typed_IdentityRelation(expression.type()[0], expression.type()[1])))
		if isinstance(expression, Typed_COR_Expressions.Typed_Composition):
			lhs2, rhs2 = expression.argument1, expression.argument2
			if P==lhs2.type()[0]:
				Q = lhs2.type()[1]
				if isinstance(lhs2, Typed_COR_Expressions.Typed_Converse):
					arg = lhs2.argument
					if Q==arg.type()[0]:
						if P==arg.type()[1]:
							A = arg
							if Q==rhs2.type()[0]:
								if P==rhs2.type()[1]:
									if isinstance(rhs2, Typed_COR_Expressions.Typed_Converse):
										arg = rhs2.argument
										if P==arg.type()[0]:
											if Q==arg.type()[1]:
												B = arg
												return ("((A[Q*P])⁻¹) ∘ ((B[P*Q])⁻¹) = ((B[P*Q]) ∘ (A[Q*P]))⁻¹", Typed_COR_Expressions.Typed_Converse(Typed_COR_Expressions.Typed_Composition(B, A)))
		if isinstance(expression, Typed_COR_Expressions.Typed_Intersection):
			lhs2, rhs2 = expression.argument1, expression.argument2
			if P==lhs2.type()[0]:
				if P==lhs2.type()[1]:
					if isinstance(lhs2, Typed_COR_Expressions.Typed_Converse):
						arg = lhs2.argument
						if P==arg.type()[0]:
							if P==arg.type()[1]:
								A = arg
								if P==rhs2.type()[0]:
									if P==rhs2.type()[1]:
										if isinstance(rhs2, Typed_COR_Expressions.Typed_Converse):
											arg = rhs2.argument
											if P==arg.type()[0]:
												if P==arg.type()[1]:
													B = arg
													return ("((A[P*P])⁻¹) ∩ ((B[P*P])⁻¹) = ((A[P*P]) ∩ (B[P*P]))⁻¹", Typed_COR_Expressions.Typed_Converse(Typed_COR_Expressions.Typed_Intersection(A, B)))
										if isinstance(rhs2, Typed_COR_Expressions.Typed_IdentityRelation):
											return ("((A[P*P])⁻¹) ∩ (𝟏[P*P]) = (A[P*P]) ∩ (𝟏[P*P])", Typed_COR_Expressions.Typed_Intersection(A, Typed_COR_Expressions.Typed_IdentityRelation(expression.type()[0], expression.type()[1])))
					if isinstance(lhs2, Typed_COR_Expressions.Typed_IdentityRelation):
						if P==rhs2.type()[0]:
							if P==rhs2.type()[1]:
								if isinstance(rhs2, Typed_COR_Expressions.Typed_Converse):
									arg = rhs2.argument
									if P==arg.type()[0]:
										if P==arg.type()[1]:
											A = arg
											return ("(𝟏[P*P]) ∩ ((A[P*P])⁻¹) = (A[P*P]) ∩ (𝟏[P*P])", Typed_COR_Expressions.Typed_Intersection(A, Typed_COR_Expressions.Typed_IdentityRelation(expression.type()[0], expression.type()[1])))
		if isinstance(expression, Typed_COR_Expressions.Typed_Dagger):
			lhs2, rhs2 = expression.argument1, expression.argument2
			if P==lhs2.type()[0]:
				if P==lhs2.type()[1]:
					if isinstance(lhs2, Typed_COR_Expressions.Typed_Converse):
						arg = lhs2.argument
						if P==arg.type()[0]:
							if P==arg.type()[1]:
								A = arg
								if P==rhs2.type()[0]:
									if P==rhs2.type()[1]:
										if isinstance(rhs2, Typed_COR_Expressions.Typed_Converse):
											arg = rhs2.argument
											if P==arg.type()[0]:
												if P==arg.type()[1]:
													B = arg
													return ("((A[P*P])⁻¹) † ((B[P*P])⁻¹) = ((B[P*P]) † (A[P*P]))⁻¹", Typed_COR_Expressions.Typed_Converse(Typed_COR_Expressions.Typed_Dagger(B, A)))
				Q = lhs2.type()[1]
				if isinstance(lhs2, Typed_COR_Expressions.Typed_Converse):
					arg = lhs2.argument
					if Q==arg.type()[0]:
						if P==arg.type()[1]:
							A = arg
							if Q==rhs2.type()[0]:
								if P==rhs2.type()[1]:
									if isinstance(rhs2, Typed_COR_Expressions.Typed_Converse):
										arg = rhs2.argument
										if P==arg.type()[0]:
											if Q==arg.type()[1]:
												B = arg
												return ("((A[Q*P])⁻¹) † ((B[P*Q])⁻¹) = ((B[P*Q]) † (A[Q*P]))⁻¹", Typed_COR_Expressions.Typed_Converse(Typed_COR_Expressions.Typed_Dagger(B, A)))
		if isinstance(expression, Typed_COR_Expressions.Typed_Complement):
			arg = expression.argument
			if P==arg.type()[0]:
				if P==arg.type()[1]:
					if isinstance(arg, Typed_COR_Expressions.Typed_Converse):
						arg = arg.argument
						if P==arg.type()[0]:
							if P==arg.type()[1]:
								if isinstance(arg, Typed_COR_Expressions.Typed_Complement):
									arg = arg.argument
									if P==arg.type()[0]:
										if P==arg.type()[1]:
											A = arg
											return ("(((A[P*P])⁻)⁻¹)⁻ = (A[P*P])⁻¹", Typed_COR_Expressions.Typed_Converse(A))
		if isinstance(expression, Typed_COR_Expressions.Typed_Union):
			lhs2, rhs2 = expression.argument1, expression.argument2
			if P==lhs2.type()[0]:
				if P==lhs2.type()[1]:
					if isinstance(lhs2, Typed_COR_Expressions.Typed_Converse):
						arg = lhs2.argument
						if P==arg.type()[0]:
							if P==arg.type()[1]:
								A = arg
								if P==rhs2.type()[0]:
									if P==rhs2.type()[1]:
										if isinstance(rhs2, Typed_COR_Expressions.Typed_Converse):
											arg = rhs2.argument
											if P==arg.type()[0]:
												if P==arg.type()[1]:
													B = arg
													return ("((A[P*P])⁻¹) ∪ ((B[P*P])⁻¹) = ((A[P*P]) ∪ (B[P*P]))⁻¹", Typed_COR_Expressions.Typed_Converse(Typed_COR_Expressions.Typed_Union(A, B)))

	return (None, expression) # The given expression was unable to be simplified