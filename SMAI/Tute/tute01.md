## Linear Independence
No trivial solution

# Generating Set and Span
Generating Set: set of vectors which when combined can in linear combination form entire space

Span: Minimal such Generating Set.

# Basis

# Norm
L1 Norm: Manhattan Distance
L2 Norm: Euclidian Distance
L<inf> Norm: 

L1: used in Text Retrieval
L2: used in KNN Applications etc

# Matrix
- Just a representation
- Rank of a matrix: least number of linearly independent columns representing matrix

# Properties of Determinants:
- det(A) = det(A')
- det(AB) = det(A).det(B)
-
-

# Trace
Sum of diagonal elements

# Representing equations

# *Important basics*
## Triangular Matrix
Lower triangular and Upper triangular
### Useful because?
Lx = b
L: Lower triangular matrix
Each addition/division/multiplication is 1 flop
Lesser the flops lesser the computations

- Flop counts increase as n^2
 
If not a triangular matrix, O(n^3)

### Positive Definite (PD) Matrix
- Symmetric
- x'Ax > 0 for all x
A'A is PD

### Cholesky Decomposition
A PD 'A' can be factorized into A = LL1 where L is a LT matrix with positive diagonal elements

#### Algo
1. Calculate l_11 = sqrt(a_11)
2. Calculate l_21 = A_21\l_11
3. Use cholesky to compute l_22 = (A_22-L_21L21') = L_22L_22'


# Eigenvectors and EigenValues



