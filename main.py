from quiz import Quiz



def inserirAluno():
    aluno = input('Escreva seu nome:')
    disciplina = input('Qual disciplina: ')
    acertos = int(input('Quantas questões você acertou?'))
    erros = int(input('Quantas questões você errou?'))
    return Quiz(aluno, disciplina, acertos, erros)


if __name__ == '__main__':
    while True:
        print('Bem vindo, aluno! Entre com seu nome ')
        aluno_quiz = inserirAluno()

        print(aluno_quiz.get_acertos())
        print(aluno_quiz.get_erros())
        print(aluno_quiz.calcularPontuacao())

