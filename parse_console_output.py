import string

characters = string.ascii_letters + string.digits + '-_.'


def parse(s):
    state = 'start'
    name = ''
    value = ''
    data = [] # a stack
    names = [] # a stack
    for i,c in enumerate(s):
        if c == '{':
            if state == 'start':
                data.append([]) # push the result list to the stack
                state = 'root'
            elif state == 'root': # a new dict starts
                data.append({}) # push an empty dict to the stack, no state change
            elif state == 'value': # the bracket is the first value char, so a list
                data.append([])
                names.append(name)
                state = 'root'
        elif c == '}':
            if state in ['value','root']: # the dict (can it only be a dict) is finished
                d = data[-1] 
                data = data[:-1] # pop the stack
                # where the dict goes to depends on the next item on the stack
                if len(data) == 0: # list now empty? we are done
                    return d
                if isinstance(data[-1],list):
                    data[-1].append(d)
                else: #it is a dict, so pop the name as well
                    data[-1][names[-1]] = d
                    names = names[:-1]    
                state = 'root'        
        elif c in characters:
            if state == 'root': # a new name:value pair starts
                name = c
                state = 'name'
            elif state == 'name':
                name += c
            elif state == 'value':
                value += c
        elif c == ':':
            if state == 'name':
                state = 'value'
                value = ''
        elif c == ',':
            if state == 'value':
                #print('debug', s[:i])
                data[-1][name] = value # set the pair to the top of the stack
                state = 'root'
    print('I am hoping this is not shown')