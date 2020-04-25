'''
Project #1: 14 Puzzle Project
Artificial Intelligence Class
Simay Yazicioglu
Fall 2019
'''
#global variables
L1 = "L1"
R1 = "R1"
U1 = "U1"
D1 = "D1"
L2 = "L2"
R2 = "R2"
U2 = "U2"
D2 = "D2"

GOAL_STATE = []

class Puzzle14_problem:
    class Node:
        def __init__(self ,state, action =None, parent = None):
            '''Node initialization'''
            self.state = state #state of the node, 1-D list
            self.parent = parent #parent of the node
            self.action = action #action that produced the node
            self.f = self.calculate_f() #f value of the node
            if not self.parent: #if no parent, self.d is 0
                self.d = 0
            else:
                self.d = self.parent.d +1

        def calculate_h(self):
            '''
            None ->int
            returns the h value for the node
            '''
            self.h =self.man_distance(self.state)
            return self.h

        def  calculate_f(self):
            '''
            None ->int
            returns the f value for the node
            '''
            if not self.parent: #if no parent, g is 1
                self.g = 0
                h = self.calculate_h()
                return self.g+h
                
            else:#if has parent
                self.g = self.parent.g +1
                h = self.calculate_h()
                return  self.g+h
        def find_row(self, i):
            '''
            int->int
            returns row of index i in the 4x4 board
            '''
            if i <4:
                return 0
            elif i<8:
                return 1
            elif i<12:
                return 2
            else:
                return 3
            
        def find_col(self, i):
            '''
            int->int
            returns column of index i in the 4x4 board
            '''
            return i%4

        def man_distance(self, node_state):
            '''
            list->int
            given node_state (1-d list), returns the manhattan distance between node_state and goal state 
            '''
            m_dis = 0
            for  i in range(len(node_state)):
            #if not equal to a or b representing zeroes , check manhattan distance
                if isinstance(node_state[i], int): 
                    #find row and column for i
                    i_col = self.find_col(i)
                    i_row = self.find_row(i)

                    pos_in_goal = GOAL_STATE.index(node_state[i])
                    #find row and column for the position in goal
                    g_col = self.find_col(pos_in_goal)
                    g_row = self.find_row(pos_in_goal)
                    #add the differences in cols and row to find manhattan distance
                    m_dis += abs(g_col  - i_col) 
                    m_dis += abs(g_row - i_row )
            return m_dis

    def __init__(self):
        '''
        14Puzzle Problem initialization
        '''
        self.initial_state =[]  #physical representation of initial state, 1D
        self.root = None #root node
        self.frontier = []#priortiy queue contains nodes, sorted based on f value of each node, initially only contains explored
        self.explored =[] #contains states explored, initially empty
        self.N=  0 #total number of nodes generated

    def swap(self,lst, i , j):
        '''
        list, int, int -> None
        given a list and 2 indexes, swap the values of the list at given indexes
        '''
        lst[i] , lst[j]  = lst[j] , lst[i]
    
    def check_neighborhood(self,a_row, a_col,  b_row, b_col):
        ''' 
            int, int, int, int -> bool, bool, bool. bool
            given row and column information of both zeros (a and b), 
            checks if given indexes are nighbor
            returns a list of  booleans 
                representing locations of a and b with respect to each other
        '''
        a_above_b , a_left_of_b  = 0,0
        b_above_a, b_left_of_a  =0,0
        if a_col == b_col:
            #are tehy on top of each other?
            if a_row +1 == b_row: # a is on top of b
                a_above_b = 1
            elif b_row +1 == a_row : #b is in top of a 
                b_above_a = 1
        elif a_row == b_row:
            #are tehy next to each oteher?
            if a_col +1 == b_col: #b is on the right of a
                a_left_of_b = 1
            elif b_col +1 == a_col : # a is on the right of b
                b_left_of_a = 1
        return [a_above_b , a_left_of_b, b_above_a, b_left_of_a]
        
    def find_possible_actions(self, p_node):
        '''
        Node -> lst
        based on the state of the node p_node, returns a list of possible actions
        zero 'a' can have the following actions [R1, L1, U1, D1] as default
        zero 'b' can have the following actions [R2, L2, U2, D2] as defailt
        '''
        curr_state = p_node.state
        poss_actions = [] #possible actions
        #for a (first zero)
        a_ind = curr_state.index('a')
        a_row, a_col = p_node.find_row(a_ind), p_node.find_col(a_ind)
        #for b (second zero)
        b_ind = curr_state.index('b')
        b_row, b_col = p_node.find_row(b_ind), p_node.find_col(b_ind)

        #ACTIONS FOR A
        if a_row ==0: #first row: cant go up
            if a_col ==0: #cant go left
                poss_actions.extend([R1, D1])
            elif a_col ==3:# cant go right
                poss_actions.extend([L1, D1])
            else:
                poss_actions.extend([R1, L1, D1])

        elif a_row==3: #last row, cant go down
            if a_col ==0: #cant go left
                poss_actions.extend([R1, U1])
            elif a_col ==3:# cant go right
                poss_actions.extend([L1, U1])
            else:
                poss_actions.extend([R1, L1, U1])
        else: #rows 1 and 2, can go UP and DOWN
            if a_col ==0: #cant go left
                poss_actions.extend([R1, D1 ,U1])
            elif a_col ==3:# cant go right
                poss_actions.extend([L1, D1, U1])
            else:
                poss_actions.extend([R1, L1, D1, U1])
        #ACTIONS FOR B
        if b_row ==0: #first row: cant go up
            if b_col ==0: #cant go left
                poss_actions.extend([R2, D2])
            elif b_col ==3:# cant go right
                poss_actions.extend([L2, D2])
            else:
                poss_actions.extend([R2, L2, D2])

        elif b_row==3: #last row, cant go down
            if b_col ==0: #cant go left
                poss_actions.extend([R2, U2])
            elif b_col ==3:# cant go right
                poss_actions.extend([L2, U2])
            else:
                poss_actions.extend([R2, L2, U2])

        else: #rows 1 and 2, can go UP and DOWN
            if b_col ==0: #cant go left
                poss_actions.extend([R2, D2 ,U2])
            elif b_col ==3:# cant go right
                poss_actions.extend([L2, D2, U2])
            else:
                poss_actions.extend([R2, L2, D2, U2])

        # if a and b are neigbhors, remove some of the actions
        neighbor_data = self.check_neighborhood(a_row, a_col,  b_row, b_col)

        if neighbor_data[0]: #if a above b
            #a cannot go down, b canot go up
            if D1 in poss_actions:
                poss_actions.pop(poss_actions.index(D1))
            if U2 in poss_actions:
                poss_actions.pop(poss_actions.index(U2))
            
        elif neighbor_data[1]: #if a left of b
            #a cannot go right, b cannot go left
            if R1 in poss_actions:
                poss_actions.pop(poss_actions.index(R1))
            if L2 in poss_actions:
                poss_actions.pop(poss_actions.index(L2))

        elif neighbor_data[2]: #if b above a
            #b cannot go down, a cannot go up
            if D2 in poss_actions:
                poss_actions.pop(poss_actions.index(D2))
            if U1 in poss_actions:
                poss_actions.pop(poss_actions.index(U1))

        elif neighbor_data[3]: #if b left of a
            #b cannot go right, a cannot go left
            if R2 in poss_actions:
                poss_actions.pop(poss_actions.index(R2))
            if L1 in poss_actions:
                poss_actions.pop(poss_actions.index(L1))
        return poss_actions

    
   
    def produce_new_state(self, state, action, zero):
        '''
        list, str, str -> list
        based on the state, action, and which zero we are moving, 
        this function produces a new state with given action and zero
        '''
        # zero =='a' represents the 'a' zero in the matrix
        # zero =='b' represents the 'b' zero in the matrix
        cop_state = state[:] #copy state
        ind = cop_state.index(zero)
        
        if action == L1 or action == L2:
            self.swap(cop_state, ind, ind-1)
        elif action == R1 or action == R2:
            self.swap(cop_state, ind, ind+1)
        elif action == U1 or action == U2:
            self.swap(cop_state, ind, ind-4)
        elif action == D1 or action == D2:
            self.swap(cop_state, ind, ind+4)

        return cop_state
    

    def expand(self, parent_node):
        '''
        Node -> list(Node)
        finds possible actions for parent_node and applies these functions to it
        returns the list of resulting nodes after each action is applied to the parent_node
        '''
        resulting_nodes = []
        #find possible actions
        actions = self.find_possible_actions(parent_node)
        #for each action, generate a new state, pass it into a Node and add the Node to the frontier
        for action in actions:
            if action[-1] == "1": #if action ends with string 1 , we will move first Zero ('a')
                # do the action , produce a node with the new state, append it to the resulting_nodes
                new_state = self.produce_new_state(parent_node.state, action ,'a')
                new_node = self.Node(new_state, action , parent_node)
                self.N +=1 
                resulting_nodes.append(new_node)
            else:#if action ends with string 1 , we will move first Zero ('a')
               # do the action , produce a node with the new state, append it to the resulting_nodes
                new_state = self.produce_new_state(parent_node.state, action ,'b')
                new_node = self.Node(new_state, action , parent_node)
                self.N +=1
                resulting_nodes.append(new_node)
        return resulting_nodes

    def contains(self, lst_to_look_in, state_to_look, node=False):
        '''
        list, list, bool-> bool
        returns True if state_to_look is in the list lst_to_look_in
        returns False otherwise
        '''
        if not node: #if lst_to_look_in is a list of lists (for example explored list)
            #removes 'a' and 'b' from state_to_look
            state = [l if isinstance(l, int) else 0 for l in state_to_look]
            for i in range(len(lst_to_look_in)):
                lst_to_look_in[i]= [l if isinstance(l, int) else 0 for l in lst_to_look_in[i]]
            return state in lst_to_look_in
            
        else: #if lst_to_look_in contains Nodes (for example self.frontier)
            for node in self.frontier:
                if state_to_look == node.state: #state found in frontier
                    return True
            return False

    def check_goal_state(self, node_state):
        ''' 
        list -> bool
        returns true if node_state and GOAL_STATE represent the same state
        '''
        #removes 'a' and 'b' from goal state and node_state
        state = [l if isinstance(l, int) else 0 for l in node_state]
        g_state = [l if isinstance(l, int) else 0 for l in GOAL_STATE]
        
        return state == g_state

    def solve(self): 
        '''
        None -> Node
        main loop for the A* algorithm
        if there's no solution returns -1, 
        if there is a solution returns the node where algorithm finds the goal state
        '''
        while True:
            if len(self.frontier) == 0: #failure
                return -1
            #get the first leaf from frontier, which naturally has the highest f value
            node = self.frontier.pop(0)
            #check if node has the goal state
            if self.check_goal_state(node.state): #returns True if success
                print('SUCCESS!')
                return node
            # if node.state is not the goal state, add node.state to the explored set
            self.explored.append(node.state)
            resulting_nodes = self.expand(node) #expand the node and get the resulting nodes
            for r_node in resulting_nodes:
                if not self.contains(self.explored , r_node.state) and not self.contains(self.frontier, r_node.state, True):
                    #add resulting nodes o the frontier 
                    # #only if the state isnt at frontier or at explored set
                    self.frontier.append(r_node)
                    self.update_frontier()
        return -1 #failure

    def update_frontier(self):
        '''
        None -> None
        sorts the frontier based on eahc nodes f value
        '''
        self.frontier.sort(key = lambda n : n.f) 
    
    def read_file(self, in_file):
        '''
        str -> None
        reads the file with name in_file
        updates initial state, goal state, root node and frontier
        '''
        global GOAL_STATE
        GOAL_STATE =[]
        file = open(in_file, 'r')
        first_zero_found = False #first zero not yet found
        for i in range(4): 
            line = file.readline()
            row = [int(elem) for elem in line.strip().split(" ")]
            #change 0 values to a and b to differentiate between 2 zeros
            for i in range(len(row)):
                if row[i] ==0:
                    if not first_zero_found:
                        first_zero_found = True
                        row[i] = 'a'
                    else:
                        row[i] ='b'
                        first_zero_found = False
            self.initial_state.append(row)
        #skip blank line
        line = file.readline()
        #read the goal state
        for i in range(4): 
            line = file.readline()
            row = [int(elem) for elem in line.strip().split(" ")]
            #change 0 values to a and b to differentiate
            for i in range(len(row)):
                if row[i] ==0:
                    if not first_zero_found:
                        first_zero_found = True
                        row[i] = 'a'
                    else:
                        row[i] ='b'
                        first_zero_found = False
            GOAL_STATE.append(row)
        file.close()

        #flatten the 2D arrays, thats how we will store them
        self.initial_state = [elem for row in self.initial_state for elem in row]
        GOAL_STATE = [elem for row in GOAL_STATE for elem in row]

        #self.root is a Node with initial state
        self.root = self.Node(self.initial_state) 
        #frontier  initially has only root node
        self.frontier = [self.root]

    def track_solution(self, node):
        """
        Node -> lst, lst, int, int
        takes the node as argument
        return list of actions (solution), 
                        list of f values on solution path ,
                        node.d and self.N
        """
        f_values = []
        actions =[]
        curr_node = node
        #trace back the actions
        while curr_node: #while curr node has a parent
            f_values.append(curr_node.f)
            actions.append(curr_node.action)
            curr_node = curr_node.parent

        actions.reverse() #reverse so it goes from root to leaf
        actions.pop(0) #pop the first action, which is None bcs it is root node's action
        f_values.reverse() #reverse so it goes from root to leaf
        return actions, f_values, node.d, self.N

    def print_board(self, lst, out_file):
        ''' 
        list -> None
        takes a list and prints it as a board in the out-file handle given
        '''
        #replace of 'a' and 'b' in the lst with 0
        state = [l if isinstance(l, int) else 0 for l in lst] 
        #make a matrix out of state
        matrix = [ state[i:i+4] for i in range(0,len(state),4) ]
            
        for elem in matrix:
            elem = [str(k) for k in elem]
            print(' '.join(elem) , file=out_file )
            
    def display_result(self, node , file_name):
        '''
        Node, str -> None
        calls the track solution, and displays the solution in the wanted format in output file
        '''
        out_file = open(file_name, 'w')
        actions, f_values, d, N = self.track_solution(node)
        self.print_board(self.initial_state, out_file)
        print(file=out_file)
        self.print_board(GOAL_STATE, out_file)
        print(file=out_file)
        print(d, file=out_file)
        print(N, file=out_file)
        for action in actions:
            print(action, end= ' ', file=out_file)
        print('', file=out_file)
        for f in f_values:
            print(f, end=' ', file=out_file)

        out_file.close()

def main():
    puzzle = Puzzle14_problem()
    in_file = "Input1.txt" #input file name
    puzzle.read_file(in_file)
    solution = puzzle.solve()
    if solution == -1: #puzzle has no solution
        print("cannot be solved")
    else: #puzzle has solution
        out_file = "Output_of_"+ in_file
        puzzle.display_result(solution, out_file)
main()