import numpy as np


def gram_schmidt(vectors):
    basis = []
    for v in vectors:
        w = v - np.sum(np.dot(v, b) * b for b in basis)
        if np.linalg.norm(w) > 1e-10:  # Избегаем добавления нулевых векторов
            basis.append(w / np.linalg.norm(w))
    return np.array(basis)


def input_vectors():
    vectors = []
    n = int(input("Number of vectors: "))
    dim = int(input("Size of vectors: "))

    for i in range(n):
        print(f"Vector {i + 1}: ")
        vec = list(map(float, input().split()))
        if len(vec) != dim:
            print("Error: Vector dimensionality mismatch")
            return None
        vectors.append(vec)

    return np.array(vectors)


vectors = input_vectors()
if vectors is not None:
    orthogonal_basis = gram_schmidt(vectors)
    print("Orthogonal basis: ")
    print(orthogonal_basis)
