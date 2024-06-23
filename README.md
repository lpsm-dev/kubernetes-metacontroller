<!-- BEGIN_DOCS -->
<a name="readme-top"></a>

<div align="center">

<img alt="header" src="https://github.com/lpsm-dev/lpsm-dev/blob/02421b0d81397fe8df3ab40e21752b8d0bb9105f/.github/assets/kubernetes.gif" width="300"/>

<h1>Kubernetes Metacontroller</h1>

[![Commitizen friendly](https://img.shields.io/badge/commitizen-friendly-brightgreen.svg)](https://www.conventionalcommits.org/en/v1.0.0/)
[![Semantic Release](https://img.shields.io/badge/%20%20%F0%9F%93%A6%F0%9F%9A%80-semantic--release-e10079.svg)](https://semantic-release.gitbook.io/semantic-release/usage/configuration)
[![Built with Devbox](https://jetpack.io/img/devbox/shield_galaxy.svg)](https://jetpack.io/devbox/docs/contributor-quickstart/)

Uma demonstração simples de como criar recursos personalizados no Kubernetes com o Metacontroller.

</div>

# Summary

- [Summary](#summary)
- [Introduction](#introduction)
- [Overview](#overview)
- [Metacontroller](#metacontroller)
- [References](#references)
- [Contributing](#contributing)
- [Versioning](#versioning)
- [Troubleshooting](#troubleshooting)
- [Show your support](#show-your-support)

# Introduction

O Kubernetes é uma plataforma incrível por vários motivos. Ele é excelente para orquestrar cargas de trabalho em contêineres em diferentes nós dentro de um cluster. No entanto, a verdadeira força do Kubernetes está em sua extensibilidade, que nos dá possibilidades praticamente infinitas.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

# Overview

Como mencionado na introdução, o Kubernetes é uma plataforma projetada para gerenciar cargas de trabalho em contêineres em um cluster. Um dos principais componentes do Kubernetes é o Control Plane. O Control Plane é responsável por manter o "estado desejado" do sistema, que é definido pelo usuário usando arquivos YAML ou JSON. Por exemplo, um usuário pode definir um Deployment com duas réplicas, e o Control Plane garantirá que, no final, existam dois Pods em execução.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

# Metacontroller

O Metacontroller é uma extensão do Kubernetes que simplifica a criação de controladores personalizados. Com o Metacontroller, você pode implementar a lógica do controlador como serviços web. Esses serviços são chamados pelo Metacontroller para garantir que o estado desejado dos recursos no cluster esteja sempre sincronizado com o que foi definido pelo usuário.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

# References

Links relevantes para esse projeto:

- [Metacontroller Docs](https://metacontroller.github.io/metacontroller/intro.html)

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
