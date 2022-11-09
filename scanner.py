import sys
class Scanner:
    def __init__(self):
        pass
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
        if token_str != "":
            token_list.append(token_str)
            token_str = ''
        return token_list
    def process_output(self,token_list):
        token_type = []
        keys = list(self.TokenDict.keys())
        values = list(self.TokenDict.values())
        for token in token_list:
            if token in values:
                token_type.append(keys[values.index(token)])
            elif token.startswith('{'):
                token_type.append('COMMENT')
            elif token.isdigit():
                token_type.append(self.TokenType_var[1])
            elif token.isalpha():
                token_type.append(self.TokenType_var[0])
        return token_type
    def output_file(self,token_list,token_type):
        file = open('output_file.txt','x')
        for token , type in zip(token_list, token_type):
            file.write(token + ' - ' + type + '\n')
def main():
    input = sys.argv[1]
    file = open(input,'r')
    x = Scanner()
    file_string = x.convert_file_to_string(file)
    tokens = x.process_input(file_string)
    output_tokens = x.process_output(tokens)
    x.output_file(tokens,output_tokens)
if __name__ == '__main__':
    main()
