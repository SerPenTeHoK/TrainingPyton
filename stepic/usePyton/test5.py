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
    nsok = False
    varok = False
#Check for namespace availabilty
    for names in namespaces.keys():
        if names == str(n_space):
            nsok = True
    if nsok != True:
        print('None')
        return

#Check if variable available
    for v in namespaces.values():
        for vv in v['vars']:
            if vv == str(var):
                varok = True
    if varok != True:
        print('None')
        return

    actualns = n_space
    for i in range(1000):
        if actualns != None:
            for v in namespaces[actualns]['vars']:
                if v == var:
                    print(actualns)
                    return
#                else
#                    if namespaces[actualns]['parent'] == 'khui':
#                        print('None')
#                        return
                else:
                    actualns = namespaces[actualns]['parent']
        else:
            print('None')
            return

# Run the program
n = []

iters = int(input())
if (int(iters) < 1) or (int(iters) > 100) :
    exit

for i in range(iters):
    commands = input()
    n.append(commands.split())

print(n)

for i in range(len(n)):
    cmd = n[i][0]
    n_space = n[i][1]
    var = n[i][2]
    if cmd == 'add':
        add(n_space, var)
    if cmd == 'create':
        create(n_space, var)
    if cmd == 'get':
        print(namespaces)
        get(n_space, var)