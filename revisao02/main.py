from quiz import *

def inserirAluno():
    aluno = input('Escreva seu nome:')
    matricula = int(input('Qual disciplina: '))
    return Quiz(aluno, matricula, acertos, erros)

def escolherTipoQuiz():
    tipoQUiz = input('Qual tipo de Quiz você irá utilizar: QUIZ(NORMAL)/ QUIZ2A/ QUIZ3A')
    return tipoQUiz

if __name__ == '__main__':
    while True:
        print('Bem vindo, aluno! Entre com seu nome ')
        aluno_quiz = inserirAluno()

        print(aluno_quiz.get_acertos())
        print(aluno_quiz.get_erros())
        print(aluno_quiz.calcularPontuacao())

        print('Escolha o tipo de quiz você ira escolher:')
        tipoDequiz = escolherTipoQuiz()
        break

    if tipoDequiz:
        while True: