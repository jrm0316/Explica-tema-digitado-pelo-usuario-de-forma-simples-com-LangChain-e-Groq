# Explica-tema-digitado-pelo-usuario-de-forma-simples-com-LangChain-e-Groq

Propósito do projeto
- Este projeto tem como objetivo criar um assistente educacional interativo, onde o usuário fornece um tema via terminal e a IA responde com uma explicação simples e acessível.
- A proposta é demonstrar como utilizar LangChain para construir prompts dinâmicos, transformando a IA em um componente reutilizável dentro de aplicações de backend e ferramentas internas.


Como a IA responde
A IA funciona de forma interativa, seguindo este fluxo:
- O usuário digita um tema no terminal
- O Python captura essa entrada (input())
- O conteúdo é injetado em um PromptTemplate
- O modelo da Groq gera uma explicação voltada para iniciantes
- A resposta é exibida diretamente no terminal
- Esse padrão é a base para chatbots, copilotos e ferramentas educacionais.


Tecnologias e conceitos utilizados
- Python
- LangChain
- Groq (LLaMA 3.1)
- PromptTemplate
- Entrada dinâmica do usuário (CLI)
- Prompt Engineering
- Integração com LLM
- Variáveis de ambiente (.env)


Estrutura do projeto
projeto/

├── assistente_interativo_ia.py

├── .env

└── README.md


Projeto simples e direto, focado em clareza de arquitetura e aprendizado prático.


Como executar o projeto

  1.) Clone o repositório:

      git clone https://github.com/seu-usuario/Explica-tema-digitado-pelo-usuario-de-forma-simples-com-LangChain-e-Groq

  2.) Instale as dependências:

      pip install langchain langchain-groq python-dotenv

  3.) Crie o arquivo .env com sua chave da Groq:
  
      GROQ_API_KEY=sua_chave_aqui

  4.) Execute o script:

      python assistente_interativo_ia.py

Alterando o tema analisado
- O tema é definido em tempo de execução.
- Basta digitar qualquer assunto quando o programa solicitar, por exemplo:

      Digite um tema para a IA explicar: Banco de Dados

-O mesmo código funciona para qualquer tema, sem necessidade de alterações no script.

Por que este projeto é relevante?
- Porque ele demonstra que você sabe:
  * Criar IA interativa
  * Trabalhar com entrada dinâmica de usuários
  * Separar lógica de prompt da lógica de execução
  * Usar LangChain além de chamadas diretas de API
  * Construir a base de chatbots e assistentes inteligentes
- Esse tipo de arquitetura é comum em:
  * Ferramentas internas
  * Copilotos educacionais
  * Sistemas de suporte
  * Interfaces CLI com IA


Resumo profissional
- Projeto desenvolvido em Python utilizando LangChain e Groq para criação de um assistente educacional interativo.
- O sistema recebe entradas dinâmicas do usuário via terminal e utiliza um modelo de linguagem para gerar explicações claras e acessíveis, aplicando boas práticas de engenharia de prompts e integração com LLMs.
