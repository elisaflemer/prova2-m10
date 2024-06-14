# prova2-m10

Esta atividade se refere à segunda prova do módulo 10 de Engenharia da Computação. Ela é composta por um sistema em Docker Compose contendo um backend em FastAPI, com uma API de posts de blog armazenada em memória (dicionário) e um gateway em nginx para redirecionamento através do localhost na porta 80, quando a rota inicia com o prefixo "/blog".

A API em si foi baseada no exemplo de Flask disponibilizado e contém maturidade de Richardson de nível 2. Ela inclui rotas para ver todos os posts, ver um post por ID, adicionar um post, deletar um post e atualizar um post. Além disso, ela loga o acesso às rotas a partir do nível WARNING, em arquivos na pasta logs, na raiz do projeto. Essa pasta é mapeada como volume no Docker Compose.

As rotas foram documentadas em Insomnia (disponível na pasta raiz do projeto).

## Como executar

Todo o desenvolvimento foi feito em Docker Compose. Logo, não é necessário iniciar ambientes virtuais. Em vez disso, certifique-se, primeiro, de ter o Docker baixado em seu sistema e de estar com o daemon ativado. Então, execute, na pasta raiz do projeto:

```bash
docker compose up
```

A partir daí, as rotas estarão acessíveis a partir da URL `http://localhost/blog`.

Para acessar os logs, confira a pasta `logs`. Os arquivos estarão separados por timestamp de 1 em um 1 minuto. Para alterar o nível das mensagens do log, baste modificar o argumento na linha 18 do arquivo `app/logging_config.py`.

```python
logging.basicConfig(level=logging.WARNING, format=LOG_FORMAT)
```

## Vídeo

https://github.com/elisaflemer/prova2-m10/assets/99259251/eaaaacd2-5077-4089-ae06-4b44af715988
