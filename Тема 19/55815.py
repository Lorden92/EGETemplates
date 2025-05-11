def game(heap, moves, to):
    if heap>=78:
        return moves%2 == to%2
    if moves ==to:
        return 0
    h = [game(heap+1, moves+1, to),
         game(heap+4, moves+1, to),
         game(heap*4, moves+1, to)]
    return any(h)

def game2(heap, moves, to):
    if heap>=78:
        return moves%2 == to%2
    if moves ==to:
        return 0
    h = [game2(heap+1, moves+1, to),
         game2(heap+4, moves+1, to),
         game2(heap*4, moves+1, to)]
    return any(h) if (moves + 1) % 2 == to % 2 else all(h)

print('19:', min(s for s in range(1,78) if game2(s, 0, 2)))
print('20:', [s for s in range(1,78) if not game2(s, 0, 1) and game2(s,0,3)])
print('21', [s for s in range(1,78) if not game2(s, 0, 2) and game2(s, 0, 4)])
