<!-- BEGIN_DOCS -->
<a name="readme-top"></a>

[◀ Voltar](README.md)

<div align="center">

<img alt="contributing" src="https://github.com/lpsm-dev/lpsm-dev/blob/98272299ea611ba50254b132490ea385149dc5cf/.github/assets/contributing.png" width="225"/>

**Diretrizes para o processo de contribuição**

</div>

Seja bem-vindo e obrigado por considerar contribuir com este projeto! Ler e seguir nossas diretrizes te ajudará a entrar com rapidez em nosso fluxo de trabalho, além tornar o processo de contribuição mais fácil e eficaz para todos. As contribuições são essenciais para a evolução contínua do projeto, então contamos com seu apoio!

# Summary

- [Summary](#summary)
- [Melhores Práticas](#melhores-práticas)
- [Setup](#setup)
  - [DevBox](#devbox)
  - [Direnv](#direnv)
  - [Task](#task)
- [Commit Messages](#commit-messages)
- [MR Process](#mr-process)
  - [Steps](#steps)
  - [Reviewing](#reviewing)
- [Versioning Process](#versioning-process)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

# Melhores Práticas

- Se você não conseguir continuar uma tarefa, informe imediatamente a equipe. A comunicação rápida evita atrasos e permite que outras pessoas te ajudem a resolver os problemas mais rapidamente.
- Não reinvente a roda. Se já existe uma solução bem estabelecida para um problema, use-a. Isso economiza tempo e recursos.
- Minimize o uso de IA na comunicação diária com a equipe. Valorizamos interações reais e genuínas.
- Trabalhando remotamente, é essencial termos uma boa comunicação por texto. Muitas vezes, seu colega de trabalho pode estar ocupado, mas ainda sim você precisa falar com ele. Para facilitar essa interação, use uma comunicação assíncrona e direta. Isso não significa ser rude, mas sim ser claro e objetivo. Para mais detalhes, clique [aqui](https://nohello.net/en/).

<p align="right">(<a href="#readme-top">back to top</a>)</p>

# Setup

Para você entrar no nosso fluxo de trabalho, é fundamental configurar seu ambiente de trabalho local: 

- Instalar ferramentas CLI.
- Configurar variáveis de ambiente.
- Rodar scripts de automação e etc.
  
Para facilitar isso, siga as etapas abaixo.

>>>
Lembre-se: cada projeto tem seu próprio contexto e necessidades!
>>>

## DevBox

O **DevBox** é uma ferramenta CLI que cria ambientes de desenvolvimento isolados e reproduzíveis, sem precisar usar containers Docker ou a linguagem Nix.

>>>
Use essa opção se você não quiser instalar muitas ferramentas CLI diretamente no seu ambiente de trabalho.
>>>

Siga essas etapas para configurar seu ambiente:

- Instale o [devbox](https://www.jetify.com/devbox/docs/installing_devbox/):

```bash
curl -fsSL <https://get.jetpack.io/devbox> | bash
```

- Inicialize seu projeto:

```bash
devbox init
```

- Adicione os pacotes que deseja (pode mudar de projeto para projeto). Ex:

```json
{
  "$schema": "https://raw.githubusercontent.com/jetify-com/devbox/0.10.7/.schema/devbox.schema.json",
  "packages": [
    "awscli2@latest",
    "kubectl@1.29.3",
    "kubernetes-helm@3.14.3"
  ],
  "shell": {
    "init_hook": [
      "echo 'Welcome to devbox!' > /dev/null"
    ],
    "scripts": {
      "test": [
        "echo \"Error: no test specified\" && exit 1"
      ]
    }
  }
}
```

- Execute o seguinte comando para inicializar o shell temporário:

```bash
devbox shell
```

Com isso, podemos garantir que todos no projeto tenham as mesmas ferramentas, nas mesmas versões, que forem necessárias para o processo de desenvolvimento.

>>>
Se você precisar de mais detalhes sobre essa configuração, verifique o arquivo [devbox.json](devbox.json) do seu projeto. Caso não exista, crie ele seguindo o passo a passo descrito acima.
>>>

## Direnv

Para você automatizar certas ações em seu terminal sempre que você for trabalhar nesse projeto, configure o **Direnv**. Essa ferramenta vai ajustar o seu shell conforme o seu diretório atual. Assim, sempre que você entrar na pasta do projeto, o **Direnv** fará algo, como: carregará as variáveis definidas no `.env` ou disparar o shell do **DevBox**.

Siga essas etapas para configurar seu ambiente:

- Acesse a documentação do [direnv](https://direnv.net/docs/installation.html) e siga as instruções para instalá-lo.

- Após a instalação, crie um arquivo `.env` na raiz do seu projeto para armazenar as variáveis de ambiente utilizadas.

- Crie o arquivo `.envrc` com o seguinte conteúdo:

```bash
# Dotenv Support
[[ ! -f .env ]] || dotenv .env

# Devbox Support
has devbox && eval "$(devbox generate direnv --print-envrc)" && exit 0
```

- A primeira vez que você criar ou modificar um arquivo `.envrc`, você precisará autorizá-lo com o comando:

```bash
direnv allow
```

Seguindo essas etapas, quando você navegar para a pasta do seu projeto, as variáveis de ambiente serão carregadas automaticamente e o **DevBox** será inicializado.

>>>
Se você precisar de mais detalhes sobre esse configuração, verifique o arquivo [.envrc](.envrc) do seu projeto.
>>>

## Task

A ferramenta **task** oferece uma maneira conveniente de definir e gerenciar tarefas específicas do projeto, facilitando a automatização de scripts comuns e simplificando os fluxos de trabalho de desenvolvimento.

>>>
É semelhante à ferramenta `make`, que é utilizada principalmente para automatizar tarefas.
>>>

Siga essas etapas para configurar seu ambiente:

- Certifique-se de que você instalou o comando `task` seguindo as etapas de configuração do **DevBox**.
  - Caso não tenha seguido, acesse a documentação do [task](https://taskfile.dev/installation/) e siga as instruções para instalá-lo.
- Execute o comando `task` no diretório raiz do projeto para ver todos os comandos disponíveis.

>>>
Se você precisar de mais detalhes sobre cada tarefa definida, verifique o arquivo [Taskfile.yaml](Taskfile.yaml) do seu projeto. Caso não exista, crie ele seguindo o passo a passo descrito acima.
>>>

<p align="right">(<a href="#readme-top">back to top</a>)</p>

# Commit Messages

Nesse projeto, exigimos que todos os commits sigam um formato específico de mensagem. Isso torna mais fácil para qualquer pessoa que contribua ao projeto, possa ler o histórico de commits e entender as alterações feitas ao longo do tempo.

Veja como isso funciona:

```
<type>(optional scope): <description>

[optional body]
```

Esse formato é baseado no [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/). Consulte a documentação para obter mais detalhes.

`<type>`

Descreve o tipo de alteração do commit. Temos as seguintes opções:

- **feat**: Um novo recurso (adição de um novo componente, fornecimento de novas variantes para um componente existente, etc.).
- **fix**: Uma correção de bug (correção de um problema de estilo, resolução de um bug na API de um componente etc.). Ao atualizar dependências que não sejam de desenvolvimento, marque suas alterações como `fix`.
- **docs**: Alterações somente na documentação.
- **style**: Alterações que não afetam o significado do código (espaços em branco, formatação, falta de ponto e vírgula etc.). Não deve ser usado para alterações na interface do usuário, pois essas são alterações significativas; em vez disso, considere usar `feat` ou `fix`.
- **refactor**: Uma alteração de código que não corrige um bug nem adiciona um recurso.
- **perf**: Uma alteração de código que melhora o desempenho.
- **test**: Adição de testes ausentes ou correção de testes existentes.
- **build**: Alterações que afetam o sistema de build.
- **ci**: Alterações em arquivos e scripts de configuração de CI/CD.
- **chore**: Outras alterações que não modificam arquivos de origem ou de teste. Use esse tipo ao adicionar ou atualizar dependências de desenvolvimento.
- **revert**: Reverte um commit anterior.

`<scope>`

É qualquer coisa que forneça informações adicionais ou que especifique o local de alteração do seu código. Por exemplo `events`, `kafka`, `dockerfile`, `authorization`, etc. Cada tipo (type) de commit pode ter um escopo (scope) opcional, cabendo a você adicionar ou omitir essa informação. Por exemplo:

```
feat(login): add route
```

> Use a convenção PascalCase na hora de definir seu scope.

`<description>`

É você dizer o que foi feito no commit, porém de forma breve. Para isso, recomendamos que:

- Priorize descrições em inglês.
- Use o imperativo, tempo presente: "change", não "changed" ou "changed".
- Não coloque a primeira letra em maiúscula.
- Não coloque ponto (.) no final.

>
> [NOTE] 📌
> Cada tipo de commit tem um efeito sobre a próxima versão que você vai lançar.
>

<p align="right">(<a href="#readme-top">back to top</a>)</p>

# MR Process

Ao criar MRs, é uma boa ideia seguir as convenções para o título do seu MR, assim como para as mensagens de commit. Dessa forma, se seu MR for sofrer um **squash** após a mesclagem, o maintainer poderá usar o título como a mensagem final do commit, criando um histórico devidamente formatado e mais enxuto.

## Steps

- Crie uma branch a partir da branch de produção `main`:

```bash
git checkout main
git pull origin main
git checkout -b sua-nova-branch
```

- Trabalhe na nova branch:
  - Realize as alterações necessárias localmente e faça commits das mudanças.
  - Certifique-se de que seu código atenda aos padrões de qualidade estabelecidos.
  - Garanta que seus commits sigam a convenção de commits definida pela equipe.

```bash
git add .
git commit -m "fix: change the commit"
```

- Faça o push da sua branch:

```bash
git push origin sua-nova-branch
```

- Abra uma solicitação de merge (Merge Request):
  - No GitLab, navegue até o repositório e abra uma nova Merge Request da sua branch para a branch de produção `main`.
  - Adicione uma descrição clara do que foi feito e qualquer informação relevante para a revisão.
  - Defina o título usando commits convencionais.
  - Marque a opção de remover a branch de origem após a mesclagem.
  - Marque a opção para squash dos commits.

- Revisão e Aprovação:
  - Um mantenedor revisará seu código.
  - Se o código atender aos requisitos e padrões, ele será aprovado.
  - Após a aprovação, seu código será mesclado na branch `main`.

- Finalização:
  - Após a mesclagem, sua branch pode ser deletada se não for mais necessária.
  - Certifique-se de atualizar sua branch local `main`.

Seguir este processo garante que as alterações sejam revisadas adequadamente e que o código de produção permaneça estável e de alta qualidade.

>
> [NOTE] 📌
> Se você tiver vários commits em seu PR que resolvem o mesmo problema, **squash os commits**.
>

## Reviewing

Durante o processo de revisão do MR, siga essas políticas:

- Seja respeitoso e construtivo.
- Sempre realize a revisão em pares.
- Sugira alterações em vez de simplesmente comentar os problemas encontrados.
- Exigimos pelo menos um aprovador no MR, que não seja o autor.
- Se não tiver certeza sobre algo, pergunte ao autor do MR.
- Se você estiver satisfeito com as alterações, aprove o MR.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

# Versioning Process

Este projeto segue a especificação [SemVer](https://semver.org/). Consulte a documentação para obter mais detalhes.

<p align="right">(<a href="#readme-top">back to top</a>)</p>
<!-- END_DOCS -->
