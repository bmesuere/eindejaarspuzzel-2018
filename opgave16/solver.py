import string

faces = [
        [
            ['x', 'd', 'c', 'b', 'a'],
            ['e', 6, 4, 5, 14],
            ['f', 0, 16, 2, 12],
            ['g', 0, 10, 8, 7],
            ['h', 0, 3, 1, 13]
            ],
        [
            ['x', 'd', 'c', 'b', 'a'],
            ['i', 4, 0, 3, 5],
            ['j', 13, 1, 12, 15],
            ['k', 14, 0, 0, 8],
            ['l', 16, 0, 0, 2]
            ],
        [
            ['x', 'h', 'g', 'f', 'e'],
            ['i', 0, 0, 0, 1],
            ['j', 14, 0, 0, 7],
            ['k', 0, 0, 4, 0],
            ['l', 6, 0, 0, 0]
            ],
        [
            ['x', 'h', 'g', 'f', 'e'],
            ['a', 4, 0, 0, 0],
            ['b', 0, 0, 0, 16],
            ['c', 0, 12, 0, 0],
            ['d', 2, 1, 0, 0]
            ],
        [
            ['x', 'l', 'k', 'j', 'i'],
            ['a', 1, 9, 10, 0],
            ['b', 4, 0, 0, 0],
            ['c', 0, 15, 0, 7],
            ['d', 0, 0, 0, 12],
            ],
        [
            ['x', 'l', 'k', 'j', 'i'],
            ['e', 12, 3, 9, 15],
            ['f', 0, 0, 5, 0],
            ['g', 0, 0, 0, 2],
            ['h', 0, 0, 0, 0]
            ]
        ]

def transpose(matrix):
    return list(map(list, zip(*matrix)))

def getLane(faces, lane):
    result = []
    for face in faces:
        transposed = transpose(face)
        for i in range(1,5):
            if face[i][0] == lane:
                result += face[i][1:5]
            if transposed[i][0] == lane:
                result += transposed[i][1:5]
    return result

def flattenFace(face):
    l = []
    for row in face[1:5]:
        l += row[1:5]
    return l

def unique(l):
    filtered = list(filter(lambda x: x != 0, l))
    return len(filtered) == len(set(filtered))

def isValid(faces):
    valid = True
    for c in string.ascii_lowercase[:12]:
        valid = valid and unique(getLane(faces, c))
    for face in faces:
        valid = valid and unique(flattenFace(face))
    return valid

def full(faces):
    for i in range(6):
        for j in range(1,5):
            for k in range(1,5):
                if faces[i][j][k] == 0:
                    return False
    return True

def openPositions(faces):
    positions = []
    for i in range(6):
        for j in range(1,5):
            for k in range(1,5):
                if faces[i][j][k] == 0:
                    positions.append((i, j, k))
    return positions


def solve(faces, positions, depth=0):
    i, j, k = positions[0]
    possible = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16}
    possible -= set(flattenFace(faces[i]))
    possible -= set(getLane(faces, faces[i][0][k]))
    possible -= set(getLane(faces, faces[i][j][0]))
    for val in possible:
        if depth <= 4:
            print(depth, i, faces[i][j][0], faces[i][0][k], val)
        faces[i][j][k] = val
        if isValid(faces):
            if full(faces):
                return faces
            else:
                res = solve(faces, positions[1:], depth + 1)
                if res is not None:
                    return res
        faces[i][j][k] = 0
    return None

print(solve(faces, openPositions(faces)))
