from flask import Flask

app = Flask(__name__)

@app.route('/decorator')
def home():
    return '''
    <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <h1> Currículo Miguel Alves </h1>

    <h1> CONTATO </h1>
    <p>Telefone:(31) 99162-3839</p>
    <p>Endereço: Rua Alfa, 125 - Jardim Riacho das Pedras, Contagem</p>
    <p>E-mail: miguelalves1575@gmail.com</p>

    <h1> OBJETIVO </h1> 
    <p>Estágio na área de TI / Suporte Técnico / Desenvolvimento. Busco aplicar os
conhecimentos do curso Técnico do Cotemig e minha experiência em
automação de processos para contribuir com a infraestrutura tecnológica
da empresa.</p>

<h1>EXPERIÊNCIA PROFISSIONAL</h1>
<p>Draft Solutions | Jovem Aprendiz
Período: Fevereiro/2026 – Presente
Automação e Dados:Gerenciamento e organização de fluxos de dados
utilizando Excel Avançado (fórmulas, tabelas dinâmicas e automação
de planilhas).
Gestão de Documentação: Controle e estruturação de arquivos digitais
e documentação técnica de engenharia.
Otimização de Processos: Redução de tempo em tarefas manuais
através da padronização de arquivos em Word e Excel.
Suporte Interno: Auxílio básico em rotinas administrativas e
tecnológicas do setor.</p>

<h1>HABILIDADES</h1>
<p>- Programação Básica: Conhecimento em linguagens de
programação como C# e
Visual studio.
- Manutenção de Computadores: Habilidade em
manutenção básica de hardware e
software.
- Instalação e Configuração de SistemasOperacionais:
Conhecimentos básicos em
Windows.
- Suporte Técnico: Habilidade em identificar e resolver
problemas simples de
informática, tanto em
software quanto em hardware.
- Banco de Dados: Noções básicas de criação e consulta
de banco de dados,
utilizando ferramentas
como MySQL.</p>

<h1>FORMAÇÃO ACADÊMICA</h1>
<p>Ensino Médio Técnico em
Informática – Colégio Cotemig
Conclusão prevista: 2026 (Manhã)</p>

</body>
</html>    
    '''


if __name__ == '__main__':
    app.run(debug=True)