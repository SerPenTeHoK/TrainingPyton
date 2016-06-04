namespaces={
    'global': {'parent': None, 'vars': []},
    }
def create(n_space, parent):
    """Creates a namespace"""
    global namespaces
    namespaces.update({n_space : {'parent': parent, 'vars': []}})
    return

def add(n_space, var):
    """Adds variable to namespace"""
    global namespaces
    namespaces[n_space]['vars'].append(var)
    return

def get(n_space, var):
    """Get namespace by variable"""
    global namespaces

    if not (n_space in namespaces.keys()):
        print('None')
        return

    dict = namespaces.get(n_space)

    if var in dict.get('vars'):
        print(n_space)
        return
    else:
        get(dict.get('parent'), var)
"""
add("global", "a")
create("foo", "global")
add("foo", "b")
get("foo", "a")
get("foo", "c")
create("bar", "foo")
add("bar", "a")
get("bar", "a")
get("bar", "b")
"""


n = []
iters = int(input())
if (int(iters) < 1) or (int(iters) > 100) :
    exit

for i in range(iters):
    commands = input()
    n.append(commands.split())
#print(n)

for i in range(len(n)):
    cmd = n[i][0]
    n_space = n[i][1]
    var = n[i][2]
    if cmd == 'add':
        add(n_space, var)
    if cmd == 'create':
        create(n_space, var)
    if cmd == 'get':
        #print(namespaces)
        get(n_space, var)
