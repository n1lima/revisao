class Quiz:
    def __init__(self, disciplina, aluno, acertos, erros):
        self.disciplina = disciplina
        self.aluno = aluno
        self.__acertos = acertos
        self.__erros = erros

    def calcularPontuacao(self):
        return self.__acertos - self.__erros

    def get_acertos(self):
        return self.__acertos

    def get_erros(self):
        return self.__erros

    def __str__(self):
        info = f'Disiciplina: {self.disciplina}\n Aluno: {self.aluno}'
        info += f'Acertos: {self.__acertos}\n Erros: {self.__erros}'
        info += f'Total: {self.calcularPontuacao()}'
        return info

class Quiz2A(Quiz):
    def calcular_pontos(self):
        return self.get_acertos() - 4 *(self.get_erros())

class Quiz3A(Quiz):
    def calcular_pontos(self):
        return self.get_acertos() - 2 *(self.get_erros())
