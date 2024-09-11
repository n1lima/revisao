from quiz import *

if __name__ == '__main__':
    q1 = Quiz(12, 8)
    q2 = Quiz2A(10, 10)
    q3 = Quiz3A(5, 15)

    print(q1)
    print(q2)
    print(q3)

    print('testando')
    print(q1.get_acertos())
    print(q1.get_erros())
    print(q1.calcular_pontos())

    lista_quiz = [q1, q2, q3]
    a1 = Aluno(1, 'Bruna', lista_quiz)
    a2 = Aluno(2, 'Carla', lista_quiz)
    print(a1)

    d = Disciplina('POO', 'Ferauche', 2024, 4)
    d.adicionarAluno(a1)
    d.adicionarAluno(a2)
    print(d)





