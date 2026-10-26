class Aluno:
  def __init__(self, nome, sobrenome, nota):
    if nota < 0 or nota > 10:
      raise ValueError('A nota deve estar entre zero e dez')
    self.nome = nome;
    self.sobrenome = sobrenome;
    self.nota = nota;

  def mostrarAluno(self):
    return 'Aluno: ' + self.nome + ' ' + self.sobrenome + ' - Nota: ' + str(self.nota);