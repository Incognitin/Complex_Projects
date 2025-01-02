from __future__ import annotations
class Player:
    """  Contains player information"""
    Name: str
    score_history: list[int]
    top_score: int
    avg_score: int
    all_scores: list[int]
    total_games: int

    def __init__(self, name: str) -> None:
        """
        """
        self.Name = name
        self.score_history = []
        self._top_score = 0
        self.avg_score = 0
        self.all_scores = []
        self.total_games = 0

    def top_score_of_player(self) -> None:

        for scores in self.all_scores:
            if scores > self._top_score:
                self._top_score = scores

    def avg_score_of_player(self) -> None:

        total_sum = 0
        for scores in self.all_scores:
            total_sum += scores

        self.avg_score = total_sum // len(self.all_scores)

    def get_recent_history(self) -> list[int]:

        return self.score_history

    def add_scores(self, score: int) -> None:

        self.score_history.append(score)
        self.all_scores.append(score)
        self.total_games += 1

    def update_history(self):

        while len(self.score_history) > 100:
            self.score_history.pop(0)


Player_1 = Player('Nithin')
Player_1.add_scores(100)
Player_1.add_scores(1033)
Player_1.add_scores(10309480)
Player_1.add_scores(13403400)
Player_1.add_scores(14400)
Player_1.add_scores(1348900)
Player_1.add_scores(1094280)
Player_1.add_scores(1904800)
Player_1.add_scores(17500)
Player_1.add_scores(549100)
Player_1.add_scores(859100)
Player_1.add_scores(58100)
#print(Player_1.get_recent_history())
Player_1.avg_score_of_player()
#print(Player_1.avg_score)
Player_1.top_score_of_player()
#print(Player_1._top_score)

from random import randint

class CandyLandBoard:

    def __init__(self):

        self.Player_1 = ""
        self.Player_2 = ""
        self.p1_position = 0
        self.p2_position = 0
        self.snake_list = {53: 22, 64: 36, 74: 51, 81: 75, 95: 83, 99: 89, 26: 11}
        self.ladder_list = {57: 68, 34: 59, 82: 91, 5: 17, 29: 46, 71: 80}

    def choose_your_character(self) -> None:
        character_list = ['(*^_^*)', '>_<', '(*_*)', '=^_^=', '[‘ᴥ’]']
        print(character_list)
        try:
            p1 = int(input("p1 pls choose your character from the list above. Enter a number from 1 to 5"))
            p2 = int(input("p2 pls choose your character from the list above. Enter a number from 1 to 5"))
        except ValueError:
            p1 = int(input("p1 pls choose your character from the list above. Enter a number from 1 to 5"))
            p2 = int(input("p2 pls choose your character from the list above. Enter a number from 1 to 5"))

        self.Player_1 = character_list[p1 - 1]
        self.Player_2 = character_list[p2 - 1]

    def who_goes_first(self) -> int:

        choose = randint(1,2)
        return choose

    def visualize(self):
        my_dict = {0: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
                   1: [11, 12, 13, 14, 15, 16, 17, 18, 19, 20],
                   2: [21, 22, 23, 24, 25, 26, 27, 28, 29, 30],
                   3: [31, 32, 33, 34, 35, 36, 37, 38, 39, 40],
                   4: [41, 42, 43, 44, 45, 46, 47, 48, 49, 50],
                   5: [51, 52, 53, 54, 55, 56, 57, 58, 59, 60],
                   6: [61, 62, 63, 64, 65, 66, 67, 68, 69, 70],
                   7: [71, 72, 73, 74, 75, 76, 77, 78, 79, 80],
                   8: [81, 82, 83, 84, 85, 86, 87, 88, 89, 90],
                   9: [91, 92, 93, 94, 95, 96, 97, 98, 99, 100]
                }
        rep_1 = str(self.p1_position)[0]
        rep_2 = str(self.p2_position)[0]
        if self.p1_position == 0 and self.p2_position == 0:
            my_dict[0][0] = [self.Player_1, self.Player_2]
        check = self.p1_position == 0 and self.p2_position == 0
        if self.p1_position <= 10 and self.p2_position <= 10:
            rep_1 = 0
            rep_2 = 0
        if self.p2_position <= 10:
            rep_2 = 0
        if self.p1_position <= 10:
            rep_1 = 0

        while not check:
            for x in range(len(my_dict[int(rep_1)])):
                if my_dict[int(rep_1)][x] == self.p1_position:
                    my_dict[int(rep_1)][x] = self.Player_1
                    break

            for y in range(len(my_dict[int(rep_2)])):
                if my_dict[int(rep_2)][y] == self.p2_position:
                    my_dict[int(rep_2)][y] = self.Player_2
                    break

            check = True

        if self.p1_position == self.p2_position and self.p2_position != 0:
            my_dict[int(rep_1)][abs(int(str(self.p1_position)[-1]) - 1)] = [self.Player_1, self.Player_2]


        return f'{my_dict[9]}\n'\
               f'{my_dict[8]}\n' \
               f'{my_dict[7]}\n' \
               f'{my_dict[6]}\n' \
               f'{my_dict[5]}\n' \
               f'{my_dict[4]}\n' \
               f'{my_dict[3]}\n' \
               f'{my_dict[2]}\n' \
               f'{my_dict[1]}\n' \
               f'{my_dict[0]}\n'

    def play_game(self):

        game = True
        if self.p1_position == 100 or self.p2_position == 100:
            game = False

        print(self.visualize())
        while game:
            first = str(input("p1 press r to roll the die"))
            turn_p1 = randint(1, 6)
            print(f'Player 1, You rolled a {turn_p1}!!')
            self.p1_position += turn_p1
            print(self.visualize())
            second = str(input("p2 press r to roll the die"))
            turn_p2 = randint(1, 6)
            print(f'Player 2, You rolled a {turn_p2}!!')
            self.p2_position += turn_p2
            print(self.visualize())


#snake_ladder = CandyLandBoard()
#print(snake_ladder.choose_your_character())
#print(snake_ladder.play_game())

class Vehicle :
    def __init__ ( self , name ) :
        self . name = name
    def drive ( self ) :
        print ( f"{ self . name } is being driven .")


class Car(Vehicle):
    def __init__ ( self , name , brand ) :
        super () . __init__ ( name )
        self . brand = brand

    def drive ( self ) :
        print ( f"{ self . brand } { self . name } is zooming on the road .")


class SportsCar ( Car ) :

    def __init__ ( self , name , brand , top_speed ) :
        super () . __init__ ( name , brand )
        self . top_speed = top_speed

    def drive ( self ) :
        print ( f"{ self . brand } { self . name } is racing at { self . top_speed } mph.")

new_class = Vehicle('Pizza Mobile')
new_class_2 = Vehicle('Model S')
second_class = Vehicle('F1')
Car_1 = Car('F1', 'Mclaren')
Car_2 = Car('Tesla', 'Model S')
Sports_car = SportsCar('F1', 'Mclaren', '200')
new_class.drive()
new_class_2.drive()
second_class.drive()
Car_1.drive()
Car_2.drive()
Sports_car.drive()


class _Node:

    def __init__(self, item):

        self.item = item
        self.next = None
        self.prev = None


class DoubleLinkedList:

    def __init__(self):

        self._head = None

    def __len__(self):

        curr = self._head
        count = 0
        while curr:
            count += 1
            curr = curr.next
        return count

    def append(self, item):
        """
        >>> final = DoubleLinkedList()
        >>> final.append('hello')
        >>> final.append('Soccer')
        >>> final.append('Exam')
        >>> final.append('Gym')
        >>> final.get_previous(2)
        'Soccer'

        """
        curr = self._head
        new_node = _Node(item)
        if curr is None:
            self._head = new_node
            self._head.next = new_node.next
            self._head.prev = new_node.prev
            return
        while curr.next:
            curr = curr.next

        new_node.prev = curr
        curr.next = new_node
        new_node.next = None

    def insert(self, index: int, item) -> None:
        """
        >>> new = DoubleLinkedList()
        >>> new.append('hello')
        >>> new.append('Soccer')
        >>> new.get_previous(1)
        'hello'
        """
        curr = self._head
        count = 0
        while curr:
            if count == index:
                return
            curr = curr.next

        new_node = _Node(item)
        new_node.prev = curr
        curr.next = new_node
        new_node.next = curr.next

    def get_previous(self, index: int) -> None:
        curr = self._head
        count = 0
        while curr:
            if count == index:
                return curr.prev.item
            count += 1
            curr = curr.next

def first_at_depth(obj, d: int):
    """
    >>> first_at_depth([3,[4, 5]], 1)
    3
    >>> first_at_depth([5, [7, 8], 10], 2)
    7
    """
    if isinstance(obj, int):
        if d == 0:
            return obj
        else:
            return None
    else:
        if d == 0:
            return None
        else:
            if d == 0:
                return None
            else:
                for sublist in obj:
                    item = first_at_depth(sublist, d - 1)
                    if item is not None:
                        return item



def count_odd(obj) -> int:
    """
    >>> count_odd([1, [2, 6, 5], [9, [8, 7]]])
    4

    """
    if isinstance(obj, int):
        if obj % 2 == 0:
            return 0
        else:
            return 1
    else:
        count = 0
        for sublist in obj:
            check = count_odd(sublist)
            count += check
        return count


###### MIDTERM 2 ###################################################################

from typing import Union

# LECTURE 6A ----------------------------------------------------------------

def flatten(obj: Union[int, list]) -> list[int]:
    """Return a (non-nested) list of the integers in <obj>.
    The integers are returned in the left-to-right order they appear
    in <obj>.
    >>> flatten(6)
    [6]
    >>> flatten([1, [-2, 3], -4])
    [1, -2, 3, -4]
    >>> flatten([[0, -1], -2, [[-3, [-5]]]])
    [0, -1, -2, -3, -5]
    """
    # Checks the case where the object is an integer
    if isinstance(obj, int):
        return [obj]
    else:
        # creates an empty list to store all the unpacked integers
        my_list = []
        for objects in obj:
            # Goes through each list/object in obj and recalls the function until
            # a list of a single integer is returned
            my_list.extend(flatten(objects))
        return my_list


def uniques(obj: Union[int, list]) -> list[int]:
    """Return a (non-nested) list of the integers in <obj>, with no duplicates.
    >>> uniques([13, [2, 13], 4])
    [13, 2, 4]
    >>> uniques([[10, 4], 10, 4])
    [10, 4]
    """
    seen = []
    checker = flatten(obj)
    if isinstance(obj, int):
        seen.append(obj)
        return [obj]
    else:
        final = []
        for sub in checker:
            if sub not in seen:
                final.append(sub)
            seen.append(sub)
        return final


def nested_list_contains(obj, item: int):
    """
    >>> nested_list_contains([1, 2,[4, 6], [8], 10], 6)
    True
    >>> nested_list_contains(12, 12)
    True
    >>> nested_list_contains([13, 14], 14)
    True
    >>> nested_list_contains([12, [19, 16]], 18)
    False
    """
    if isinstance(obj, int):
        return item == obj
    else:
        for sub_list in obj:
            if nested_list_contains(sub_list, item):
                return True
        return False


def first_at_depth(obj, d: int):
    """
    >>> first_at_depth([3,[4, 5]], 1)
    3
    >>> first_at_depth([5, [7, 8], 10], 2)
    7
    >>> first_at_depth(5, 1)

    >>> first_at_depth([7, 8], 1)
    7
    >>> first_at_depth([12, 14, [15, [16]], [17, [[18]]]], 4)
    18
    >>> first_at_depth([12, 14, [15, [16]], [17, [[18]]]], 3)
    16
    >>> first_at_depth([12, 14, [15, [16]], [17, [[18]]]], 2)
    15
    >>> first_at_depth(5, 0)
    5
    """
    if isinstance(obj, int):
        if d == 0:
            return obj

    else:
        for sublist in obj:
            if first_at_depth(sublist, d - 1):
                return first_at_depth(sublist, d - 1)
        return


def add_one(obj: Union[int, list]) -> None:
    """Add one to every number stored in <obj>. Do nothing if <obj> is an int.
    If <obj> is a list, *mutate* it to change the numbers stored.
    >>> lst0 = 1
    >>> add_one(lst0)
    >>> lst0
    1
    >>> lst1 = []
    >>> add_one(lst1)
    >>> lst1
    []
    >>> lst2 = [1, [2, 3], [[[5]]]]
    >>> add_one(lst2)
    >>> lst2
    [2, [3, 4], [[[6]]]]
    >>> lst4 = [6]
    >>> add_one(lst4)
    >>> lst4
    [7]
    """
    if isinstance(obj, int):
        return
    else:
        for i in range(len(obj)):
            if isinstance(obj[i], int):
                obj[i] += 1
            else:
                add_one(obj[i])


def fib(n: int) -> int:
    if n < 2:
        return 1
    else:
        for i in range(n):
            return fib(n - 2) + fib(n - 1)


#--------------------------WEEK 7------------------------------#

def semi_homogeneous(obj: Union[int, list]) -> bool:
    """Return whether the given nested list is semi-homogeneous.
    A single integer and empty list are semi-homogeneous.
    In general, a list is semi-homogeneous if and only if:
    - all of its sub-nested-lists are integers, or all of them are lists
    - all of its sub-nested-lists are semi-homogeneous
    >>> semi_homogeneous([1, 2, 3])
    True
    >>> semi_homogeneous([])
    True
    >>> semi_homogeneous(1)
    True
    >>> semi_homogeneous([[1, 9], [3, 8], [5, 7]])
    True
    >>> semi_homogeneous([1, 5, [6, 7], 9, 10])
    False
    >>> semi_homogeneous([[1, 4, 5, 6], 4, [5, 6, 7, 8]])
    False
    >>> semi_homogeneous([2, []])
    False
    """
    if obj == [] or isinstance(obj, int):
        return True
    else:
        first = False
        second = False
        third = False
        if isinstance(obj[0], int):
            first = all([isinstance(sublist, int) for sublist in obj])
        else:
            second = all([isinstance(sublist, list) for sublist in obj])
            third = all([semi_homogeneous(sublist) for sublist in obj])

        return first or (second and third)


#--------------------------WEEK 8------------------------------#


from typing import Any, Optional, Callable


class Tree:
    """A recursive tree data structure.

    Note the relationship between this class and RecursiveList; the only major
    difference is that _rest has been replaced by _subtrees to handle multiple
    recursive sub-parts.
    """
    # === Private Attributes ===
    # The item stored at this tree's root, or None if the tree is empty.
    _root: Optional[Any]
    # The list of all subtrees of this tree.
    _subtrees: list[Tree]

    # === Representation Invariants ===
    # - If self._root is None then self._subtrees is an empty list.
    #   This setting of attributes represents an empty Tree.
    #
    #   Note: self._subtrees may be empty when self._root is not None.
    #   This setting of attributes represents a tree consisting of just one
    #   node.

    def __init__(self, root: Any, subtrees: list[Tree]) -> None:
        """Initialize a new Tree with the given root value and subtrees.

        If <root> is None, the tree is empty.
        Precondition: if <root> is None, then <subtrees> is empty.
        """
        self._root = root
        self._subtrees = subtrees

    def is_empty(self) -> bool:
        """Return True if this tree is empty.

        >>> t1 = Tree(None, [])
        >>> t1.is_empty()
        True
        >>> t2 = Tree(3, [])
        >>> t2.is_empty()
        False
        """
        return self._root is None

    def __len__(self) -> int:
        """Return the number of items contained in this tree.

        >>> t1 = Tree(None, [])
        >>> len(t1)
        0
        >>> t2 = Tree(3, [Tree(4, []), Tree(1, [])])
        >>> len(t2)
        3
        """
        if self.is_empty():
            return 0
        else:
            size = 1  # count the root
            for subtree in self._subtrees:
                size += subtree.__len__()  # could also do len(subtree) here
            return size

    def leaves(self) -> list:
        """ Return all leaves pls and thank you
        >>> new = Tree(8, [Tree(5, [Tree(6, [])]), Tree(10, [Tree(11, [])])])
        >>> t1 = Tree(21, [Tree(70, []), Tree(80, [])])
        >>> t2 = Tree(41, [Tree(2, [Tree(3, [])]), Tree(4, [])])
        >>> final = Tree(100, [new, Tree(11, [t2, t1])])
        >>> new.leaves()
        [6, 11]
        >>> final.leaves()
        [6, 11, 3, 4, 70, 80]
        """
        if self.is_empty():
            return []
        elif self._subtrees == []:
            return [self._root]
        else:
            leafs = []
            for sublist in self._subtrees:
                leafs.extend(sublist.leaves())
            return leafs

    def average(self) -> float:
        """Return the average of all the values in this tree.
        Return 0.0 if this tree is empty.
        Precondition: this is a tree of numbers.
        """
        if self.is_empty():
            return 0.0
        elif self._subtrees == []:
            pass

    def avg_helper(self) -> tuple[int, int]:
        """ This function the returns the total number of nodes
        and the values of each node as a tuple where (total_nodes, values)
        >>> t2 = Tree(1, [Tree(-2, []), Tree(10, []), Tree(-30, [])])
        >>> t2.avg_helper()
        (4, -21)
        >>> t1 = Tree(5, [Tree(20, []), Tree(30, [])])
        >>> t2 = Tree(12, [Tree(8, []), Tree(5, [])])
        >>> t3 = Tree(18, [Tree(2, []), Tree(5, [])])
        >>> final = Tree(10,[t1, t2, t3])
        >>> final.avg_helper()
        (10, 115)
        """
        if self.is_empty():
            return 0, 0
        elif self._subtrees == []:
            return 1, self._root
        else:
            total_nodes = 1
            values = self._root
            for sublist in self._subtrees:
                total_nodes += sublist.avg_helper()[0]
                values += sublist.avg_helper()[1]
            return total_nodes, values

    def avg(self):
        """ Just returns the avg bud
        >>> t2 = Tree(1, [Tree(-2, []), Tree(10, []), Tree(-30, [])])
        >>> t2.avg()
        -5.25
        >>> t1 = Tree(5, [Tree(20, []), Tree(30, [])])
        >>> t2 = Tree(12, [Tree(8, []), Tree(5, [])])
        >>> t3 = Tree(18, [Tree(2, []), Tree(5, [])])
        >>> final = Tree(10,[t1, t2, t3])
        >>> final.avg()
        11.5
        """
        return self.avg_helper()[1]/self.avg_helper()[0]

    def delete_root(self) -> None:
        """ Delete the root and promote its rightmost subtree
        >>> t1 = Tree(8, [Tree(1,[]), Tree(2, []), Tree(3, [])])
        >>> t4 = Tree(1, [Tree(-2, []), Tree(10, []), Tree(-30, [t1])])
        >>> t6 = Tree(-30, [t1])
        >>> t1.delete_root()
        >>> t1._root
        3
        >>> t2 = Tree(11, [Tree(8, [Tree(10, [])])])
        >>> t2.delete_root()
        >>> t2._root
        8
        >>> t4.delete_root()
        >>> t4._root
        -30
        >>> t6.delete_root()
        >>> t6._root
        3
        >>> t4.delete_root()
        >>> t4._root
        3
        >>> t4.delete_root()
        >>> t4._root
        2
        """
        if self.is_empty():
            return
        elif self._subtrees == []:
            self._root = None
        else:
            current = self._subtrees.pop()
            self._subtrees.extend(current._subtrees)
            self._root = current._root


    def delete_item_strategy_2(self) -> None:
        """ Leftmost node becomes the root
        >>> t1 = Tree(8, [Tree(1,[]), Tree(2, []), Tree(3, [])])
        >>> t4 = Tree(1, [Tree(-2, []), Tree(10, []), Tree(-30, [t1])])
        >>> t6 = Tree(-30, [t1])
        >>> t11 = Tree(5, [Tree(20, []), Tree(30, [])])
        >>> t21 = Tree(12, [Tree(8, []), Tree(5, [])])
        >>> t31 = Tree(18, [Tree(2, []), Tree(5, [])])
        >>> t4.delete_item_strategy_2()
        >>> t4._root
        -2
        >>> t1.delete_item_strategy_2()
        >>> t1._root
        1
        >>> t10 = Tree(3, [t11, t21, t31])
        >>> t10.delete_item_strategy_2()
        >>> t10._root
        20
        """
        if self._subtrees == []:
            self._root = None
            return

        left = self._subtrees[0]
        while left._subtrees:
            left = left._subtrees[0]

        left._subtrees = self._subtrees
        self._root = left._root

    def to_nested_list(self):
        """ list rep
        >>> t1 = Tree('B', [Tree('E', []), Tree('F', [])])
        >>> t2 = Tree('C', [Tree('G', []), Tree('H', [Tree('J', [])])])
        >>> t3 = Tree('D', [Tree('I', [])])
        >>> hey = Tree('A', [t1, t2, t3])
        >>> hey.to_nested_list()
        ['A', ['B', ['E'], ['F']], ['C', ['G'], ['H', ['J']]], ['D', ['I']]]
        >>> lt = Tree(2, [Tree(4, []), Tree(5, [])])
        >>> rt = Tree(3, [Tree(6, []), Tree(7, []), Tree(8, []), Tree(9, []),\
                          Tree(10, [])])
        >>> t = Tree(1, [lt, rt])
        >>> t.to_nested_list()
        [1, [2, [4], [5]], [3, [6], [7], [8], [9], [10]]]
        >>> lt = Tree(2, [Tree(4, [Tree(32, [Tree(1, [])])]), Tree(5, [])])
        >>> rt = Tree(3, [Tree(6, []), Tree(7, []), Tree(8, []), Tree(9, []),\
                          Tree(10, [Tree(1, [])])])
        >>> t = Tree(1, [lt, rt])
        >>> t.to_nested_list()
        [1, [2, [4, [32, [1]]], [5]], [3, [6], [7], [8], [9], [10, [1]]]]
        """
        if self.is_empty():
            return []
        elif self._subtrees == []:
            return [self._root]
        else:
            final = [self._root]
            for sublist in self._subtrees:
                final.append(sublist.to_nested_list())
            return final
