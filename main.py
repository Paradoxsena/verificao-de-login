class user:
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password

users = [
    user('Alisson','teste0@gmail.com','tt0'),
    user('Luiz','teste1@gmail.com','tt1'),
    user('Amanda','teste2@gmail.com','tt2'),
    user('Ana Clara','teste3@gmail.com','tt3'),
]

def getlogin():
    confirmEmail = input('Email: ')
    confirmPassword = input('Senha: ')
    userAllowed = False
    
    for user in users:
        if confirmEmail == user.email and confirmPassword == user.password:
            userAllowed == True
            print('Seja bem vindo(a) {}!'.format(user.name))
            break  
    else:
        print('Email ou senha inválidos, tente novamente.')

if __name__ == "__main__":
    getlogin()
        
    