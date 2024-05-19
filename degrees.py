# We used breadth-first search algorithm in this project

def shortest_path(source, target):
    """
    Returns the shortest list of (movie_id, person_id) pairs
    that connect the source to the target.

    If no possible path, returns None.
    """

    visitedState = set()

    queue = []
    queue.append((source , []))

    # bfs algorithm starts
    while queue:
        
        personId, path = queue.pop(0)

        if personId == target:
            return path

        # visited person adding visited state
        visitedState.add(personId)

        for movieId, neighborId in neighbors_for_person(personId):
            if neighborId not in visitedState:
                queue.append((neighborId, path + [(movieId, neighborId)]))

    return None
