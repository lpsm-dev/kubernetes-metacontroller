<!-- BEGIN_DOCS -->
<div align="center">

<a name="readme-top"></a>

<img alt="header" src="https://github.com/lpsm-dev/lpsm-dev/blob/02421b0d81397fe8df3ab40e21752b8d0bb9105f/.github/assets/kubernetes.gif" width="300"/>

## Kubernetes Metacontroller

Hello Human 👽! Bem-vindo ao meu repositório 👋

Pronto para derrubar um cluster Kubernetes? 🤡 hahaha

[![Commitizen friendly](https://img.shields.io/badge/commitizen-friendly-brightgreen.svg)](https://www.conventionalcommits.org/en/v1.0.0/)
[![Semantic Release](https://img.shields.io/badge/%20%20%F0%9F%93%A6%F0%9F%9A%80-semantic--release-e10079.svg)](https://semantic-release.gitbook.io/semantic-release/usage/configuration)
[![Built with Devbox](https://jetpack.io/img/devbox/shield_galaxy.svg)](https://jetpack.io/devbox/docs/contributor-quickstart/)

</div>

# Sumário

<details>
  <summary><strong>Expandir</strong></summary>

- [Visão Geral](#introduction)
- [Overview](#overview)
- [References](#references)
- [Contributing](#contributing)
- [Versioning](#versioning)
- [Troubleshooting](#troubleshooting)
- [Show your support](#show-your-support)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

</details>

# Visão Geral

## Objetivo

Deixando as brincadeiras de lado, nesse repositório apresento a vocês um exemplo prático de como eu criei um controlador personalizado no Kubernetes utilizando a ferramenta [Metacontroller](https://github.com/metacontroller/metacontroller).

Minha proposta foi colocar a mão e documentar o processo para facilitar a compreensão de como o Metacontroller funciona.

## Contexto e Motivação

O Kubernetes é uma plataforma incrível por inúmeras razões. Ele não só gerencia e organiza cargas de trabalho por diversos nós (nodes), mas sua verdadeira força reside na flexibilidade. Com essa característica intrínseca, o Kubernete pode ser ampliado e personalizado de forma praticamente infinita, permitindo que você o adapte exatamente de acordo com as suas necessidades. É essa capacidade de moldar o Kubernetes para atender a requisitos únicos que o torna uma ferramenta indispensável para qualquer empresa e que me motivo a explorar e compartilhar esse conhecimento.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

# Metacontroller

O Metacontroller é uma extensão do Kubernetes que simplifica a criação de controladores personalizados. Com o Metacontroller, você pode implementar a lógica do controlador como serviços web. Esses serviços são chamados pelo Metacontroller para garantir que o estado desejado dos recursos no cluster esteja sempre sincronizado com o que foi definido pelo usuário.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

# References

Links relevantes para esse projeto:

- [Metacontroller Docs](https://metacontroller.github.io/metacontroller/intro.html)
- [What is a Kubernetes Controller?](https://book-v1.book.kubebuilder.io/basics/what_is_a_controller.html)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

# Contributing

Gostaria de contribuir? Isso é ótimo! Temos um guia de contribuição para te ajudar. Clique [aqui](CONTRIBUTING.md) para lê-lo.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

# Versioning

Para verificar o histórico de mudanças do projeto, acesse o arquivo [**CHANGELOG.md**](CHANGELOG.md).

<p align="right">(<a href="#readme-top">back to top</a>)</p>

# Troubleshooting

Se você tiver algum problema, [abra uma issue nesse projeto](https://github.com/homelabsz/helm-charts/issues).

<p align="right">(<a href="#readme-top">back to top</a>)</p>

# Show your support

<div align="center">

Dê uma ⭐️ para esse projeto se ele te ajudou!

<img alt="gif-footer" src="https://github.com/lpsm-dev/lpsm-dev/blob/main/.github/assets/yoda.gif" width="225"/>

<br>
<br>

Feito com 💜 por [mim](https://github.com/lpsm-dev) :wave: inspirado no [readme-md-generator](https://github.com/kefranabg/readme-md-generator)

</div>

<p align="right">(<a href="#readme-top">back to top</a>)</p>
<!-- END_DOCS -->
