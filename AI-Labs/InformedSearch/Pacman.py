import bisect

from sys import maxsize as infinity


def go_forward(pos_x, pos_y, side1, obstacles1):
    if side1 == 'sever' and pos_y < 9 and [pos_x, pos_y + 1] not in obstacles1:
        pos_y += 1
    elif side1 == 'jug' and pos_y > 0 and [pos_x, pos_y - 1] not in obstacles1:
        pos_y -= 1
    elif side1 == 'zapad' and pos_x > 0 and [pos_x - 1, pos_y] not in obstacles1:
        pos_x -= 1
    elif side1 == 'istok' and pos_x < 9 and [pos_x + 1, pos_y] not in obstacles1:
        pos_x += 1
    return [pos_x, pos_y, side1]


def go_backward(pos_x, pos_y, side1, obstacles1):
    if side1 == 'jug' and pos_y < 9 and [pos_x, pos_y + 1] not in obstacles1:
        pos_y += 1
        side1 = 'sever'
    elif side1 == 'sever' and pos_y > 0 and [pos_x, pos_y - 1] not in obstacles1:
        pos_y -= 1
        side1 = 'jug'
    elif side1 == 'istok' and pos_x > 0 and [pos_x - 1, pos_y] not in obstacles1:
        pos_x -= 1
        side1 = 'zapad'
    elif side1 == 'zapad' and pos_x < 9 and [pos_x + 1, pos_y] not in obstacles1:
        pos_x += 1
        side1 = 'istok'
    return [pos_x, pos_y, side1]


def go_left(pos_x, pos_y, side1, obstacles1):
    if side1 == 'jug' and pos_x < 9 and [pos_x + 1, pos_y] not in obstacles1:
        pos_x += 1
        side1 = 'istok'
    elif side1 == 'sever' and pos_x > 0 and [pos_x - 1, pos_y] not in obstacles1:
        pos_x -= 1
        side1 = 'zapad'
    elif side1 == 'zapad' and pos_y > 0 and [pos_x, pos_y - 1] not in obstacles1:
        pos_y -= 1
        side1 = 'jug'
    elif side1 == 'istok' and pos_y < 9 and [pos_x, pos_y + 1] not in obstacles1:
        pos_y += 1
        side1 = 'sever'
    return [pos_x, pos_y, side1]


def go_right(pos_x, pos_y, side1, obstacles1):
    if side1 == 'jug' and pos_x > 0 and [pos_x - 1, pos_y] not in obstacles1:
        pos_x -= 1
        side1 = 'zapad'
    elif side1 == 'sever' and pos_x < 9 and [pos_x + 1, pos_y] not in obstacles1:
        pos_x += 1
        side1 = 'istok'
    elif side1 == 'zapad' and pos_y < 9 and [pos_x, pos_y + 1] not in obstacles1:
        pos_y += 1
        side1 = 'sever'
    elif side1 == 'istok' and pos_y > 0 and [pos_x, pos_y - 1] not in obstacles1:
        pos_y -= 1
        side1 = 'jug'
    return [pos_x, pos_y, side1]


def delete_item(lista, position):
    lista1 = []
    for i in range(len(lista)):
        if lista[i] != position:
            lista1.append(lista[i])
    return lista1


"""
Информирано пребарување во рамки на граф
"""


def memoize(fn, slot=None):
    """ Запамети ја пресметаната вредност за која била листа од
    аргументи. Ако е специфициран slot, зачувај го резултатот во
    тој slot на првиот аргумент. Ако slot е None, зачувај ги
    резултатите во речник.

    :param fn: зададена функција
    :type fn: function
    :param slot: име на атрибут во кој се чуваат резултатите од функцијата
    :type slot: str
    :return: функција со модификација за зачувување на резултатите
    :rtype: function
    """
    if slot:
        def memoized_fn(obj, *args):
            if hasattr(obj, slot):
                return getattr(obj, slot)
            else:
                val = fn(obj, *args)
                setattr(obj, slot, val)
                return val
    else:
        def memoized_fn(*args):
            if args not in memoized_fn.cache:
                memoized_fn.cache[args] = fn(*args)
            return memoized_fn.cache[args]

        memoized_fn.cache = {}
    return memoized_fn


def best_first_graph_search(problem, f):
    """Пребарувај низ следбениците на даден проблем за да најдеш цел. Користи
     функција за евалуација за да се одлучи кој е сосед најмногу ветува и
     потоа да се истражи. Ако до дадена состојба стигнат два пата, употреби
     го најдобриот пат.

    :param problem: даден проблем
    :type problem: Problem
    :param f: дадена функција за евалуација (проценка)
    :type f: function
    :return: Node or None
    :rtype: Node
    """
    f = memoize(f, 'f')
    node = Node(problem.initial)
    if problem.goal_test(node.state):
        return node
    frontier = PriorityQueue(min, f)
    frontier.append(node)
    explored = set()
    while frontier:
        node = frontier.pop()
        if problem.goal_test(node.state):
            return node
        explored.add(node.state)
        for child in node.expand(problem):
            if child.state not in explored and child not in frontier:
                frontier.append(child)
            elif child in frontier:
                incumbent = frontier[child]
                if f(child) < f(incumbent):
                    del frontier[incumbent]
                    frontier.append(child)
    return None


def greedy_best_first_graph_search(problem, h=None):
    """ Greedy best-first пребарување се остварува ако се специфицира дека f(n) = h(n).

    :param problem: даден проблем
    :type problem: Problem
    :param h: дадена функција за хевристика
    :type h: function
    :return: Node or None
    """
    h = memoize(h or problem.h, 'h')
    return best_first_graph_search(problem, h)


def astar_search(problem, h=None):
    """ A* пребарување е best-first graph пребарување каде f(n) = g(n) + h(n).

    :param problem: даден проблем
    :type problem: Problem
    :param h: дадена функција за хевристика
    :type h: function
    :return: Node or None
    """
    h = memoize(h or problem.h, 'h')
    return best_first_graph_search(problem, lambda n: n.path_cost + h(n))


def recursive_best_first_search(problem, h=None):
    """Recursive best first search - ја ограничува рекурзијата
    преку следење на f-вредноста на најдобриот алтернативен пат
    од било кој јазел предок (еден чекор гледање нанапред).

    :param problem: даден проблем
    :type problem: Problem
    :param h: дадена функција за хевристика
    :type h: function
    :return: Node or None
    """
    h = memoize(h or problem.h, 'h')

    def RBFS(problem, node, flimit):
        if problem.goal_test(node.state):
            return node, 0  # (втората вредност е неважна)
        successors = node.expand(problem)
        if len(successors) == 0:
            return None, infinity
        for s in successors:
            s.f = max(s.path_cost + h(s), node.f)
        while True:
            # Подреди ги според најниската f вредност
            successors.sort(key=lambda x: x.f)
            best = successors[0]
            if best.f > flimit:
                return None, best.f
            if len(successors) > 1:
                alternative = successors[1].f
            else:
                alternative = infinity
            result, best.f = RBFS(problem, best, min(flimit, alternative))
            if result is not None:
                return result, best.f

    node = Node(problem.initial)
    node.f = h(node)
    result, bestf = RBFS(problem, node, infinity)
    return result


"""
Дефинирање на класа за структурата на проблемот кој ќе го решаваме со пребарување.
Класата Problem е апстрактна класа од која правиме наследување за дефинирање на основните 
карактеристики на секој проблем што сакаме да го решиме
"""


class Problem:
    def __init__(self, obstacles, initial, goal=None):
        self.initial = initial
        self.obstacles = obstacles
        self.goal = goal

    def successor(self, state):
        """За дадена состојба, врати речник од парови {акција : состојба}
        достапни од оваа состојба. Ако има многу следбеници, употребете
        итератор кој би ги генерирал следбениците еден по еден, наместо да
        ги генерирате сите одеднаш.
        :param state: дадена состојба
        :return:  речник од парови {акција : состојба} достапни од оваа
                  состојба
        :rtype: dict
        """
        possible_actions = dict()
        new = list(state)
        forward = go_forward(state[0], state[1], state[2], self.obstacles)
        backward = go_backward(state[0], state[1], state[2], self.obstacles)
        left = go_left(state[0], state[1], state[2], self.obstacles)
        right = go_right(state[0], state[1], state[2], self.obstacles)

        if (forward[0], forward[1]) in state:
            new[0], new[1], new[2] = forward[0], forward[1], forward[2]
            possible_actions['ProdolzhiPravo'] = tuple(delete_item(new, (forward[0], forward[1])))
        else:
            new[0], new[1], new[2] = forward[0], forward[1], forward[2]
            possible_actions['ProdolzhiPravo'] = tuple(new)

        if (backward[0], backward[1]) in state:
            new[0], new[1], new[2] = backward[0], backward[1], backward[2]
            possible_actions['ProdolzhiNazad'] = tuple(delete_item(new, (backward[0], backward[1])))
        else:
            new[0], new[1], new[2] = backward[0], backward[1], backward[2]
            possible_actions['ProdolzhiNazad'] = tuple(new)

        if (left[0], left[1]) in state:
            new[0], new[1], new[2] = left[0], left[1], left[2]
            possible_actions['SvrtiLevo'] = tuple(delete_item(new, (left[0], left[1])))
        else:
            new[0], new[1], new[2] = left[0], left[1], left[2]
            possible_actions['SvrtiLevo'] = tuple(new)

        if (right[0], right[1]) in state:
            new[0], new[1], new[2] = right[0], right[1], right[2]
            possible_actions['SvrtiDesno'] = tuple(delete_item(new, (right[0], right[1])))
        else:
            new[0], new[1], new[2] = right[0], right[1], right[2]
            possible_actions['SvrtiDesno'] = tuple(new)

        return possible_actions

    def actions(self, state):
        """За дадена состојба state, врати листа од сите акции што може да
        се применат над таа состојба
        :param state: дадена состојба
        :return: листа на акции
        :rtype: list
        """
        return self.successor(state).keys()

    def result(self, state, action):
        """За дадена состојба state и акција action, врати ја состојбата
        што се добива со примена на акцијата над состојбата
        :param state: дадена состојба
        :param action: дадена акција
        :return: резултантна состојба
        """
        return self.successor(state)[action]

    def goal_test(self, state):
        """Врати True ако state е целна состојба. Даденава имплементација
        на методот директно ја споредува state со self.goal, како што е
        специфицирана во конструкторот. Имплементирајте го овој метод ако
        проверката со една целна состојба self.goal не е доволна.
        :param state: дадена состојба
        :return: дали дадената состојба е целна состојба
        :rtype: bool
        """
        return len(list(state)) == 3

    def path_cost(self, c, state1, action, state2):
        """Врати ја цената на решавачкиот пат кој пристигнува во состојбата
        state2 од состојбата state1 преку акцијата action, претпоставувајќи
        дека цената на патот до состојбата state1 е c. Ако проблемот е таков
        што патот не е важен, оваа функција ќе ја разгледува само состојбата
        state2. Ако патот е важен, ќе ја разгледува цената c и можеби и
        state1 и action. Даденава имплементација му доделува цена 1 на секој
        чекор од патот.
        :param c: цена на патот до состојбата state1
        :param state1: дадена моментална состојба
        :param action: акција која треба да се изврши
        :param state2: состојба во која треба да се стигне
        :return: цена на патот по извршување на акцијата
        :rtype: float
        """
        return c + 1

    def value(self):
        """За проблеми на оптимизација, секоја состојба си има вредност.
        Hill-climbing и сличните алгоритми се обидуваат да ја максимизираат
        оваа вредност.
        :return: вредност на состојба
        :rtype: float
        """
        raise NotImplementedError

    def h(self, node):
        closest = 0
        now_state = list(node.state)
        for x in now_state:
            if x is tuple and abs(now_state[0] - x[0]) + abs(now_state[1] - x[1]) > closest:
                closest = abs(now_state[0] - x[0]) + abs(now_state[1] - x[1])
        return closest + (len(now_state) - 4)
        # for x in now_state:
        #     if x is tuple:
        #         closest += abs(now_state[0] - x[0]) + abs(now_state[1] - x[1])
        # return closest + (len(now_state) - 3)


"""
Дефинирање на класата за структурата на јазел од пребарување.
Класата Node не се наследува
"""


class Node:
    def __init__(self, state, parent=None, action=None, path_cost=0):
        """Креирај јазол од пребарувачкото дрво, добиен од parent со примена
        на акцијата action

        :param state: моментална состојба (current state)
        :param parent: родителска состојба (parent state)
        :param action: акција (action)
        :param path_cost: цена на патот (path cost)
        """
        self.state = state
        self.parent = parent
        self.action = action
        self.path_cost = path_cost
        self.depth = 0  # search depth
        if parent:
            self.depth = parent.depth + 1

    def __repr__(self):
        return "<Node %s>" % (self.state,)

    def __lt__(self, node):
        return self.state < node.state

    def expand(self, problem):
        """Излистај ги јазлите достапни во еден чекор од овој јазол.

        :param problem: даден проблем
        :return: листа на достапни јазли во еден чекор
        :rtype: list(Node)
        """

        return [self.child_node(problem, action)
                for action in problem.actions(self.state)]

    def child_node(self, problem, action):
        """Дете јазел

        :param problem: даден проблем
        :param action: дадена акција
        :return: достапен јазел според дадената акција
        :rtype: Node
        """
        next_state = problem.result(self.state, action)
        return Node(next_state, self, action,
                    problem.path_cost(self.path_cost, self.state,
                                      action, next_state))

    def solution(self):
        """Врати ја секвенцата од акции за да се стигне од коренот до овој јазол.

        :return: секвенцата од акции
        :rtype: list
        """
        return [node.action for node in self.path()[1:]]

    def solve(self):
        """Врати ја секвенцата од состојби за да се стигне од коренот до овој јазол.

        :return: листа од состојби
        :rtype: list
        """
        return [node.state for node in self.path()[0:]]

    def path(self):
        """Врати ја листата од јазли што го формираат патот од коренот до овој јазол.

        :return: листа од јазли од патот
        :rtype: list(Node)
        """
        x, result = self, []
        while x:
            result.append(x)
            x = x.parent
        result.reverse()
        return result

    """Сакаме редицата од јазли кај breadth_first_search или 
    astar_search да не содржи состојби - дупликати, па јазлите што
    содржат иста состојба ги третираме како исти. [Проблем: ова може
    да не биде пожелно во други ситуации.]"""

    def __eq__(self, other):
        return isinstance(other, Node) and self.state == other.state

    def __hash__(self):
        return hash(self.state)


"""
Дефинирање на помошни структури за чување на листата на генерирани, но непроверени јазли
"""


class Queue:
    """Queue е апстрактна класа / интерфејс. Постојат 3 типа:
        Stack(): Last In First Out Queue (стек).
        FIFOQueue(): First In First Out Queue (редица).
        PriorityQueue(order, f): Queue во сортиран редослед (подразбирливо,од најмалиот кон
                                 најголемиот јазол).
    """

    def __init__(self):
        raise NotImplementedError

    def append(self, item):
        """Додади го елементот item во редицата

        :param item: даден елемент
        :return: None
        """
        raise NotImplementedError

    def extend(self, items):
        """Додади ги елементите items во редицата

        :param items: дадени елементи
        :return: None
        """
        raise NotImplementedError

    def pop(self):
        """Врати го првиот елемент од редицата

        :return: прв елемент
        """
        raise NotImplementedError

    def __len__(self):
        """Врати го бројот на елементи во редицата

        :return: број на елементи во редицата
        :rtype: int
        """
        raise NotImplementedError

    def __contains__(self, item):
        """Проверка дали редицата го содржи елементот item

        :param item: даден елемент
        :return: дали queue го содржи item
        :rtype: bool
        """
        raise NotImplementedError


class Stack(Queue):
    """Last-In-First-Out Queue."""

    def __init__(self):
        self.data = []

    def append(self, item):
        self.data.append(item)

    def extend(self, items):
        self.data.extend(items)

    def pop(self):
        return self.data.pop()

    def __len__(self):
        return len(self.data)

    def __contains__(self, item):
        return item in self.data


class FIFOQueue(Queue):
    """First-In-First-Out Queue."""

    def __init__(self):
        self.data = []

    def append(self, item):
        self.data.append(item)

    def extend(self, items):
        self.data.extend(items)

    def pop(self):
        return self.data.pop(0)

    def __len__(self):
        return len(self.data)

    def __contains__(self, item):
        return item in self.data


class PriorityQueue(Queue):
    """Редица во која прво се враќа минималниот (или максималниот) елемент
    (како што е определено со f и order). Оваа структура се користи кај
    информирано пребарување"""
    """"""

    def __init__(self, order=min, f=lambda x: x):
        """
        :param order: функција за подредување, ако order е min, се враќа елементот
                      со минимална f(x); ако order е max, тогаш се враќа елементот
                      со максимална f(x).
        :param f: функција f(x)
        """
        assert order in [min, max]
        self.data = []
        self.order = order
        self.f = f

    def append(self, item):
        bisect.insort_right(self.data, (self.f(item), item))

    def extend(self, items):
        for item in items:
            bisect.insort_right(self.data, (self.f(item), item))

    def pop(self):
        if self.order == min:
            return self.data.pop(0)[1]
        return self.data.pop()[1]

    def __len__(self):
        return len(self.data)

    def __contains__(self, item):
        return any(item == pair[1] for pair in self.data)

    def __getitem__(self, key):
        for _, item in self.data:
            if item == key:
                return item

    def __delitem__(self, key):
        for i, (value, item) in enumerate(self.data):
            if item == key:
                self.data.pop(i)


if __name__ == '__main__':
    obstacles = [[0, 9], [1, 9], [2, 9], [3, 9], [6, 9], [0, 8], [8, 8], [9, 8], [4, 7], [8, 7], [9, 7], [0, 6],
                 [3, 6], [4, 6], [5, 6], [4, 5], [1, 4], [9, 4], [8, 4], [1, 3], [1, 2], [6, 2], [4, 1], [5, 1], [6, 1],
                 [8, 1], [6, 0]]
    x = int(input())
    y = int(input())
    side = input()
    n = int(input())
    dots = list()
    for _ in range(n):
        dot = tuple(map(int, input().split(',')))
        dots.append(dot)

    dots.insert(0, x)
    dots.insert(1, y)
    dots.insert(2, side)
    problem = Problem(obstacles, tuple(dots))
    sol = astar_search(problem)
    print(sol.solution())
