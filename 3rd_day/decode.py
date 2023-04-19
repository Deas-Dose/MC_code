import time
# Create a helper function
def find_number_from_command(cmd, position):
    # create a map for the instructions
    # R and L should move horizontaly so we add and substract from the first index
    # U and D should move verticaly so we add and substract from the second one
    mouvements = {"U": [1, 0], "D": [-1, 0], "L": [0, -1], "R": [0, 1]}
    # loop through the given command 
    for k in cmd:
        # check whether the move sets us outside the padlock
        if 0 <= (position[0] + mouvements[k][0]) <= 2 and 0 <= (position[1] + mouvements[k][1]) <= 2:
            # if the move is U or D for example, only the first line will change the position because we set R[1] to be 0
            # if the move is R or L for example, only the second line will make changes to the position because of the same thing
            position[0] += mouvements[k][0]
            position[1] += mouvements[k][1]
    # return the position for the given command
    return position

# This is just to make the code inside of it run only when the script is executed directly, unlike being imported as a module
if __name__ == "__main__":
    start_time = time.time()
    # set the map of the padlock
    padlock = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    # We were told that the starting position is 5, which means it's the center of the padlock
    pos = [1, 1]
    # read the document to get the commands
    command = open("doc.txt").read().split()
    road = []
    # get all the positions of each command with the help of our helper function
    for i in command:
        # get the new position starting from the old position
        pos = find_number_from_command(i, pos)
        # append the new position to the road
        # note that i should use list method because else the road will append a reference of position and not the current value which will make the elements of road all the same with every iteration
        road.append(list(pos))
        
    # get what the position refers to in the padlock
    solution = [padlock[i][j] for i,j in road]
    # print the solution
    print(solution)

    # the following code is just to time the function
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"Elapsed time: {elapsed_time:.6f} seconds")