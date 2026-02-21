def hanoi_solver(n):
    # Initialize the rods: source has disks n to 1, others are empty
    rods = {
        'source': list(range(n, 0, -1)),
        'auxiliary': [],
        'target': []
    }
    
    moves = []

    def get_state():
        # Returns the current arrangement of rods as a formatted string
        return f"{rods['source']} {rods['auxiliary']} {rods['target']}"

    # Record the starting arrangement
    moves.append(get_state())

    def solve(n, source, target, auxiliary):
        if n > 0:
            # Move n-1 disks to auxiliary
            solve(n - 1, source, auxiliary, target)
            
            # Move the largest disk from source to target
            disk = rods[source].pop()
            rods[target].append(disk)
            
            # Record the state after the move
            moves.append(get_state())
            
            # Move n-1 disks from auxiliary to target
            solve(n - 1, auxiliary, target, source)

    solve(n, 'source', 'target', 'auxiliary')
    
    return "\n".join(moves)