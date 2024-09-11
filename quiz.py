from typing import List

class Quiz:
    def __init__(self, acertos, erros):
        self.__acertos = acertos
        self.__erros = erros

    def calcularPontuacao(self):
        return self.__acertos - self.__erros

    def get_acertos(self):
        return self.__acertos

    def get_erros(self):
        return self.__erros

    def __str__(self):
        info = f'Acertos: {self.__acertos}\n Erros: {self.__erros}'
        info += f' Total: {self.calcularPontuacao()}'
        return info

class Quiz2A(Quiz):
    def calcular_pontos(self):
        return self.get_acertos() - 4 *(self.get_erros())

class Quiz3A(Quiz):
    def calcular_pontos(self):
        return self.get_acertos() - 2 *(self.get_erros())

class Aluno:
    def __init__(self, matricula: int, nome: str, quiz: List[Quiz]): #uma composição
        self.__matricula = matricula
        self.__nome = nome
        self.__quiz = quiz

    def __str__(self):
        info = f'matricula: {self.__matricula}\n nome:{self.__nome}\n'
        sum = 0
        for q in self.__quiz:
            sum += q.calcular_pontos()
        info += f'Total: {sum}\n'
        return info

    def get_matricula(self):
        return self.__matricula #para conseguirmos pegar a matricula que é um dado sensivel

class Disciplina:
    __alunos : List[Aluno] = []

    def __init__(self, nome, professor, ano, semestre):
        self.__nome = nome
        self.__professor = professor
        self.__ano = ano
        self.__semestre = semestre

    def adicionarAluno(self, a: Aluno):
        for aluno in self.__alunos:
            if aluno.get_matricula() == a.get_matricula():
                raise Exception('ALuno já existe!')
            self.__alunos.append(a)

    def __str__(self):
        info = f'Disciplina: {self.__nome}\n professor:{self.__professor}\n Ano: {self.__ano}\n Semestre: {self.__semestre}\n'
        for aluno in self.__alunos:
            info += f'{aluno}'
        return info
