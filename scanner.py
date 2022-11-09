class Scanner:
    def __init__(self):
        print('Object Initialized...')
    TokenType_var = ['IDENTIFIER','NUMBER']
    TokenDict = {'SEMICOLON':';','IF':'if','THEN':'then','REPEAT':'repeat','UNTIL':'until',
    'ASSIGN':':=','READ':'read','WRITE':'write','LESSTHAN':'<','EQUAL':'=','PLUS':'+',
    'MINUS':'-','MULT':'*','DIV':'/','OPENBRACKET':'(','CLOSEDBRACKET':')'}
    def convert_file_to_string(self,file):
        file_string = ''
        for line in file:
            file_string += line
        file_string = file_string.replace('\n','')
        return file_string
    def process_input(self,input_language):
        special_char = [self.TokenDict['SEMICOLON'],self.TokenDict['LESSTHAN'],self.TokenDict['EQUAL'],self.TokenDict['PLUS'],
        self.TokenDict['MINUS'],self.TokenDict['MULT'],self.TokenDict['DIV'],self.TokenDict['OPENBRACKET'],self.TokenDict['CLOSEDBRACKET']]
        token_str = ''
        token_list = []
        state = 'START'
        for x in input_language:
            if x in special_char and state != 'INCOMMENT' and state != 'INASSIGN':
                if token_str != "":
                    token_list.append(token_str)
                    token_str = ""
                token_str += x
                token_list.append(x)
                token_str = ""
                state = 'START'
            elif state == 'START':
                if x == " ":
                    state = 'START'
                elif x == "{":
                    token_str += x
                    state = 'INCOMMENT'
                elif x == ':':
                    token_str += x
                    state = 'INASSIGN'
                elif x.isalpha():
                    token_str += x
                    state = 'INID'
                elif x.isdigit():
                    token_str += x
                    state = 'INNUM'
                else:
                    state = 'START'
            elif state == 'INCOMMENT':
                if x == "}":
                    token_str += x
                    token_list.append(token_str)
                    token_str = ""
                    state = 'START'
                else:
                    token_str += x
            elif state == 'INNUM':
                if x.isdigit():
                    token_str += x
                elif x == " ":
                    token_list.append(token_str)
                    token_str = ""
                    state = 'START'
                else:
                    token_list.append(token_str)
                    token_str = ""
                    token_str += x
                    state = 'START'
            elif state == 'INID':
                if x.isalpha():
                    token_str += x
                elif x == " ":
                    token_list.append(token_str)
                    token_str = ""
                    state = 'START'
                else:
                    token_list.append(token_str)
                    token_str = ""
                    token_str += x
                    state = 'START'
            elif state == 'INASSIGN':
                if x == '=':
                    token_str += x
                    token_list.append(token_str)
                    token_str = ""
                    state = 'START'
                else:
                    token_str += x
                    token_list.append(token_str)
                    token_str = ""
                    state = 'START'
        return token_list
    def process_output(self,token_list):
        
        pass
file = open('example.txt','r')
x = Scanner()
file_string = x.convert_file_to_string(file)
tokens = x.process_input(file_string)
output_tokens = x.process_output(tokens)
print(tokens)


