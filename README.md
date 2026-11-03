<div align="center">

<img src="assets/profile/terminal.svg" alt="Terminal animado com a stack Java, Spring Boot, PostgreSQL, React, TypeScript, Astro, Docker, Maven, Azure e Cloudflare" width="960">

<br>

<a href="https://github.com/DaviGama08"><img src="https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white" alt="GitHub"></a>
<a href="https://www.linkedin.com/in/davinasser/"><img src="https://img.shields.io/badge/LinkedIn-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white" alt="LinkedIn"></a>

</div>

## Por onde começar

| Quero ver... | Projeto | Foco |
| :--- | :--- | :--- |
| Regras de negócio, segurança e SaaS multi-tenant | **[Skevia](#skevia)** | Java, Spring Boot, PostgreSQL, RLS e agendamentos |
| APIs, WebSocket e comunicação em tempo real | **[AssessFlow](#assessflow)** | Spring Boot, sessões ao vivo e testes |
| Backend em produção e integração com cloud | **[503](#503)** | API Spring Boot, publicação, Azure e Cloudflare |
| Java, concorrência e tolerância a falhas | **[Distributed Quiz](#distributed-quiz)** | TCP/UDP, replicação e failover |
| Interfaces, websites e design | **[Projetos frontend](#frontend-e-websites)** | Astro, React, Next.js e websites para clientes |

## Sobre mim

Sou Davi Gama, licenciado em Engenharia Informática pelo ISEC, em Coimbra. Desenvolvo aplicações backend com Java e Spring Boot, assim como websites e produtos fullstack. Tenho experiência em ambiente empresarial, trabalho em equipa e desenvolvimento freelance, desde o levantamento de requisitos até à publicação. Interesso-me por APIs, bases de dados, arquitetura de software e regras de negócio.

## Tecnologias

| Área | Tecnologias |
| :--- | :--- |
| Linguagens | Java, C#, TypeScript, JavaScript, Python, C/C++, SQL |
| Backend e dados | Spring Boot, Spring Data JPA, Hibernate, ASP.NET Core, FastAPI, PostgreSQL, MySQL, SQL Server, SQLite |
| Frontend | React, Next.js, Astro, Blazor, JavaFX |
| Ferramentas | Git, Maven, Gradle, Docker, JUnit, Testcontainers, CI/CD, Azure, Cloudflare |

<details>
<summary>Material complementar: capturas, estudos e arquitetura</summary>

- [Galeria de interfaces](portfolio/interfaces/README.md)
- [Casos de estudo](portfolio/02_Casos_de_Estudo.pdf)
- [Diagramas de arquitetura](portfolio/03_Arquiteturas.pdf)
- [Vistas técnicas](portfolio/04_Arquiteturas_Tecnicas.pdf)

</details>

## Backend e fullstack

### Skevia

**Fullstack | Produto e serviços para negócios**

Plataforma SaaS de agendamentos para vários negócios. Cada tenant gere serviços, profissionais, horários, clientes e marcações no seu próprio espaço. O Ícaro’s Barbershop é um dos negócios que solicitaram o serviço e é apresentado como exemplo, não como destinatário exclusivo da plataforma.

**Tecnologias:** Java, Spring Boot, PostgreSQL, Flyway, React, TypeScript, Cloudflare

<a href="assets/portfolio/multi-tenant-poster.webp"><img src="assets/portfolio/multi-tenant-poster.webp" alt="Pré-visualização de Skevia | Plataforma de agendamentos" width="720" loading="lazy"></a>

<details>
<summary>Ver funcionalidades e implementação</summary>

- **Funcionalidades:** agendamento online, disponibilidade por profissional, backoffice, personalização do site e relatórios.
- **Backend:** regras de disponibilidade e conflitos, transações, isolamento de tenants, autenticação, RLS e contratos OpenAPI.
- **Frontend:** site público e painel de gestão, com componentes reutilizados no editor visual.

</details>

<details>
<summary>Ver demonstração animada</summary>

<img src="assets/portfolio/multi-tenant.webp" alt="Demonstração de Skevia | Plataforma de agendamentos" width="720" loading="lazy">

</details>

<p>
<a href="architecture/multi-tenant.svg"><img alt="Arquitetura pública" src="https://img.shields.io/badge/Arquitetura_p%C3%BAblica-30363D?style=for-the-badge&logoColor=white"></a>
 
<a href="assets/portfolio/multi-tenant-poster.webp"><img alt="Imagem estática" src="https://img.shields.io/badge/Imagem_est%C3%A1tica-30363D?style=for-the-badge&logoColor=white"></a>


</p>

<details>
<summary>Ver arquitetura e detalhes técnicos</summary>

[Arquitetura](architecture/multi-tenant.svg) | [Vista técnica](architecture/technical/multi-tenant.svg) | [PNG da arquitetura](architecture/multi-tenant.png)

</details>

### AssessFlow

**Projeto pessoal | Fullstack**

Plataforma de avaliações com bancos de perguntas, sessões ao vivo e participação por código ou QR. Funciona na nuvem ou em rede local.

**Tecnologias:** Java 25, Spring Boot 4.1, PostgreSQL, React, WebSocket, STOMP

<a href="assets/portfolio/assessflow-poster.webp"><img src="assets/portfolio/assessflow-poster.webp" alt="Pré-visualização de AssessFlow" width="720" loading="lazy"></a>

<details>
<summary>Ver funcionalidades e implementação</summary>

- **Funcionalidades:** autoria de avaliações, sessões em tempo real, respostas, resultados e exportação CSV.
- **Backend:** organizações isoladas, permissões, API REST, WebSockets e persistência com Flyway.
- **Qualidade:** testes com Testcontainers e integração contínua. Redis e RabbitMQ são opções de escala, não dependências obrigatórias.

</details>

<details>
<summary>Ver demonstração animada</summary>

<img src="assets/portfolio/assessflow.webp" alt="Demonstração de AssessFlow" width="720" loading="lazy">

</details>

<p>
<a href="architecture/assessflow.svg"><img alt="Arquitetura pública" src="https://img.shields.io/badge/Arquitetura_p%C3%BAblica-30363D?style=for-the-badge&logoColor=white"></a>
 
<a href="assets/portfolio/assessflow-poster.webp"><img alt="Imagem estática" src="https://img.shields.io/badge/Imagem_est%C3%A1tica-30363D?style=for-the-badge&logoColor=white"></a>
 <a href="https://github.com/DaviGama08/assessflow"><img alt="Código" src="https://img.shields.io/badge/C%C3%B3digo-30363D?style=for-the-badge&logoColor=white"></a>

</p>

<details>
<summary>Ver arquitetura e detalhes técnicos</summary>

[Arquitetura](architecture/assessflow.svg) | [Vista técnica](architecture/technical/assessflow.svg) | [PNG da arquitetura](architecture/assessflow.png)

</details>


### 503

**Projeto pessoal | Fullstack**

Plataforma pessoal para gerir e publicar artigos. Inclui website público, backoffice de edição e API responsável pelas regras de publicação e persistência.

**Tecnologias:** Java 25, Spring Boot 4.1, PostgreSQL, Flyway, Astro, React, Azure, Cloudflare

<a href="assets/portfolio/503-poster.webp"><img src="assets/portfolio/503-poster.webp" alt="Pré-visualização de 503 | Plataforma de publicação" width="720" loading="lazy"></a>

<details>
<summary>Ver funcionalidades e implementação</summary>

- **Funcionalidades:** rascunhos, edição de artigos, publicação, capas e autenticação administrativa.
- **Backend:** API REST, regras editoriais, segurança, persistência e migrações.
- **Frontend:** site público em Astro e administração separada em React.

</details>

<details>
<summary>Ver demonstração animada</summary>

<img src="assets/portfolio/503.webp" alt="Demonstração de 503 | Plataforma de publicação" width="720" loading="lazy">

</details>

<p>
<a href="architecture/503.svg"><img alt="Arquitetura pública" src="https://img.shields.io/badge/Arquitetura_p%C3%BAblica-30363D?style=for-the-badge&logoColor=white"></a>
 
<a href="assets/portfolio/503-poster.webp"><img alt="Imagem estática" src="https://img.shields.io/badge/Imagem_est%C3%A1tica-30363D?style=for-the-badge&logoColor=white"></a>

 <a href="https://blog503.com"><img alt="Website" src="https://img.shields.io/badge/Website-30363D?style=for-the-badge&logoColor=white"></a>
</p>

<details>
<summary>Ver arquitetura e detalhes técnicos</summary>

[Arquitetura](architecture/503.svg) | [Vista técnica](architecture/technical/503.svg) | [PNG da arquitetura](architecture/503.png)

</details>

## Java e sistemas distribuídos

### Distributed Quiz

**Java | Sistemas distribuídos**

Sistema de questionários para docentes e alunos com clientes JavaFX e servidores que suportam descoberta, replicação e recuperação após falhas.

**Tecnologias:** Java, JavaFX, TCP, UDP, multicast, SQLite, Maven

<a href="assets/portfolio/distributed-quiz-poster.webp"><img src="assets/portfolio/distributed-quiz-poster.webp" alt="Pré-visualização de Distributed Quiz" width="720" loading="lazy"></a>

<details>
<summary>Ver funcionalidades e implementação</summary>

- **Funcionalidades:** perguntas, respostas, códigos de acesso, estatísticas e notificações.
- **Arquitetura:** descoberta de serviços, replicação primário/backup, heartbeats, failover e reconexão.

</details>

<details>
<summary>Ver demonstração animada</summary>

<img src="assets/portfolio/distributed-quiz.webp" alt="Demonstração de Distributed Quiz" width="720" loading="lazy">

</details>

<p>
<a href="architecture/distributed-quiz.svg"><img alt="Arquitetura pública" src="https://img.shields.io/badge/Arquitetura_p%C3%BAblica-30363D?style=for-the-badge&logoColor=white"></a>
 
<a href="assets/portfolio/distributed-quiz-poster.webp"><img alt="Imagem estática" src="https://img.shields.io/badge/Imagem_est%C3%A1tica-30363D?style=for-the-badge&logoColor=white"></a>
 <a href="https://github.com/DaviGama08/distributed-quiz-platform-isec"><img alt="Código" src="https://img.shields.io/badge/C%C3%B3digo-30363D?style=for-the-badge&logoColor=white"></a>

</p>

<details>
<summary>Ver arquitetura e detalhes técnicos</summary>

[Arquitetura](architecture/distributed-quiz.svg) | [Vista técnica](architecture/technical/distributed-quiz.svg) | [PNG da arquitetura](architecture/distributed-quiz.png)

</details>

## Outros projetos técnicos

<details>
<summary>Ver mais projetos académicos</summary>

### MyMEDIA

**.NET | Fullstack académico**

Marketplace académico de produtos multimédia, com loja pública, backoffice e API partilhada por várias interfaces.

**Tecnologias:** C#, ASP.NET Core, Blazor, EF Core, SQL Server

<a href="assets/portfolio/mymedia-poster.webp"><img src="assets/portfolio/mymedia-poster.webp" alt="Pré-visualização de MyMEDIA" width="720" loading="lazy"></a>

<details>
<summary>Ver funcionalidades e implementação</summary>

- **Funcionalidades:** produtos, favoritos, carrinho, encomendas e gestão administrativa.
- **Backend:** API REST, autenticação, permissões e persistência relacional.

</details>

<details>
<summary>Ver demonstração animada</summary>

<img src="assets/portfolio/mymedia.webp" alt="Demonstração de MyMEDIA" width="720" loading="lazy">

</details>

<p>
<a href="architecture/mymedia.svg"><img alt="Arquitetura pública" src="https://img.shields.io/badge/Arquitetura_p%C3%BAblica-30363D?style=for-the-badge&logoColor=white"></a>
 
<a href="assets/portfolio/mymedia-poster.webp"><img alt="Imagem estática" src="https://img.shields.io/badge/Imagem_est%C3%A1tica-30363D?style=for-the-badge&logoColor=white"></a>


</p>

<details>
<summary>Ver arquitetura e detalhes técnicos</summary>

[Arquitetura](architecture/mymedia.svg) | [Vista técnica](architecture/technical/mymedia.svg) | [PNG da arquitetura](architecture/mymedia.png)

</details>

### JavaFX Chess

**Java | Desktop**

Aplicação de xadrez com validação de jogadas, regras completas, histórico, edição de posições e persistência local.

**Tecnologias:** Java, JavaFX, Maven, JUnit

<a href="assets/portfolio/javafx-chess-poster.webp"><img src="assets/portfolio/javafx-chess-poster.webp" alt="Pré-visualização de JavaFX Chess" width="720" loading="lazy"></a>

<details>
<summary>Ver funcionalidades e implementação</summary>

- **Implementação:** regras de xeque, roque, promoção e fim de jogo.
- **Arquitetura:** MVC e padrões Facade, Memento e Observer; testes da lógica de jogo.

</details>

<details>
<summary>Ver demonstração animada</summary>

<img src="assets/portfolio/javafx-chess.webp" alt="Demonstração de JavaFX Chess" width="720" loading="lazy">

</details>

<p>
<a href="architecture/javafx-chess.svg"><img alt="Arquitetura pública" src="https://img.shields.io/badge/Arquitetura_p%C3%BAblica-30363D?style=for-the-badge&logoColor=white"></a>
 
<a href="assets/portfolio/javafx-chess-poster.webp"><img alt="Imagem estática" src="https://img.shields.io/badge/Imagem_est%C3%A1tica-30363D?style=for-the-badge&logoColor=white"></a>
 <a href="https://github.com/davigama-academic/javafx-chess-isec"><img alt="Código" src="https://img.shields.io/badge/C%C3%B3digo-30363D?style=for-the-badge&logoColor=white"></a>

</p>

<details>
<summary>Ver arquitetura e detalhes técnicos</summary>

[Arquitetura](architecture/javafx-chess.svg) | [Vista técnica](architecture/technical/javafx-chess.svg) | [PNG da arquitetura](architecture/javafx-chess.png)

</details>

### SurpriseMe

**Java | Desktop**

Organizador de presentes com destinatários, ocasiões e histórico para apoiar a escolha de sugestões.

**Tecnologias:** Java, JavaFX, Maven

<a href="assets/portfolio/surpriseme-poster.webp"><img src="assets/portfolio/surpriseme-poster.webp" alt="Pré-visualização de SurpriseMe" width="720" loading="lazy"></a>

<details>
<summary>Ver funcionalidades e implementação</summary>

- **Implementação:** gestão de pessoas, eventos e presentes, com persistência local.
- **Integração:** componente de sugestão isolado; a demonstração visual não executa a inferência externa.

</details>

<details>
<summary>Ver demonstração animada</summary>

<img src="assets/portfolio/surpriseme.webp" alt="Demonstração de SurpriseMe" width="720" loading="lazy">

</details>

<p>
<a href="architecture/surpriseme.svg"><img alt="Arquitetura pública" src="https://img.shields.io/badge/Arquitetura_p%C3%BAblica-30363D?style=for-the-badge&logoColor=white"></a>
 
<a href="assets/portfolio/surpriseme-poster.webp"><img alt="Imagem estática" src="https://img.shields.io/badge/Imagem_est%C3%A1tica-30363D?style=for-the-badge&logoColor=white"></a>
 <a href="https://github.com/davigama-academic/surpriseme-gift-assistant-isec"><img alt="Código" src="https://img.shields.io/badge/C%C3%B3digo-30363D?style=for-the-badge&logoColor=white"></a>

</p>

<details>
<summary>Ver arquitetura e detalhes técnicos</summary>

[Arquitetura](architecture/surpriseme.svg) | [Vista técnica](architecture/technical/surpriseme.svg) | [PNG da arquitetura](architecture/surpriseme.png)

</details>

### Unix Topic Message Broker

**C | Sistemas operativos**

Broker local de mensagens por tópico, usando processos e mecanismos POSIX para publicação, subscrição e entrega concorrente.

**Tecnologias:** C, POSIX FIFOs, pthreads, select

<a href="assets/portfolio/unix-broker-poster.webp"><img src="assets/portfolio/unix-broker-poster.webp" alt="Pré-visualização de Unix Topic Message Broker" width="720" loading="lazy"></a>

<details>
<summary>Ver funcionalidades e implementação</summary>

- **Implementação:** gestor central, clientes independentes, sincronização e mensagens persistentes.
- **Demonstração:** execução real em terminal.

</details>

<details>
<summary>Ver demonstração animada</summary>

<img src="assets/portfolio/unix-broker.webp" alt="Demonstração de Unix Topic Message Broker" width="720" loading="lazy">

</details>

<a href="assets/portfolio/unix-broker.mp4">Vídeo da execução</a>

<p>
<a href="architecture/unix-broker.svg"><img alt="Arquitetura pública" src="https://img.shields.io/badge/Arquitetura_p%C3%BAblica-30363D?style=for-the-badge&logoColor=white"></a>
 
<a href="assets/portfolio/unix-broker-poster.webp"><img alt="Imagem estática" src="https://img.shields.io/badge/Imagem_est%C3%A1tica-30363D?style=for-the-badge&logoColor=white"></a>


</p>

<details>
<summary>Ver arquitetura e detalhes técnicos</summary>

[Arquitetura](architecture/unix-broker.svg) | [Vista técnica](architecture/technical/unix-broker.svg) | [PNG da arquitetura](architecture/unix-broker.png)

</details>

### Windows IPC Word Game

**C | Sistemas operativos**

Jogo de palavras com vários processos Windows, jogadores, bots e painel de monitorização.

**Tecnologias:** C, Win32 API, named pipes, shared memory

<a href="assets/portfolio/windows-game-poster.webp"><img src="assets/portfolio/windows-game-poster.webp" alt="Pré-visualização de Windows IPC Word Game" width="720" loading="lazy"></a>

<details>
<summary>Ver funcionalidades e implementação</summary>

- **Implementação:** comunicação entre processos, threads, sincronização e estado de jogo partilhado.
- **Demonstração:** execução dos componentes Win32.

</details>

<details>
<summary>Ver demonstração animada</summary>

<img src="assets/portfolio/windows-game.webp" alt="Demonstração de Windows IPC Word Game" width="720" loading="lazy">

</details>

<a href="assets/portfolio/windows-game.mp4">Vídeo da execução</a>

<p>
<a href="architecture/windows-game.svg"><img alt="Arquitetura pública" src="https://img.shields.io/badge/Arquitetura_p%C3%BAblica-30363D?style=for-the-badge&logoColor=white"></a>
 
<a href="assets/portfolio/windows-game-poster.webp"><img alt="Imagem estática" src="https://img.shields.io/badge/Imagem_est%C3%A1tica-30363D?style=for-the-badge&logoColor=white"></a>


</p>

<details>
<summary>Ver arquitetura e detalhes técnicos</summary>

[Arquitetura](architecture/windows-game.svg) | [Vista técnica](architecture/technical/windows-game.svg) | [PNG da arquitetura](architecture/windows-game.png)

</details>

### SafetySec Android

**Android | Académico**

Aplicação académica de acompanhamento e sinalização de emergência, com papéis de monitor e pessoa protegida.

**Tecnologias:** Android, Firebase

<a href="assets/portfolio/safetysec-android-poster.webp"><img src="assets/portfolio/safetysec-android-poster.webp" alt="Pré-visualização de SafetySec Android" width="720" loading="lazy"></a>

<details>
<summary>Ver funcionalidades e implementação</summary>

- **Interface:** painéis de monitorização e emergência.
- **Âmbito da demonstração:** interface com dados fictícios; sensores e serviços cloud não foram validados na captura.

</details>

<details>
<summary>Ver demonstração animada</summary>

<img src="assets/portfolio/safetysec-android.webp" alt="Demonstração de SafetySec Android" width="720" loading="lazy">

</details>

<p>
<a href="architecture/safetysec-android.svg"><img alt="Arquitetura pública" src="https://img.shields.io/badge/Arquitetura_p%C3%BAblica-30363D?style=for-the-badge&logoColor=white"></a>
 
<a href="assets/portfolio/safetysec-android-poster.webp"><img alt="Imagem estática" src="https://img.shields.io/badge/Imagem_est%C3%A1tica-30363D?style=for-the-badge&logoColor=white"></a>


</p>

<details>
<summary>Ver arquitetura e detalhes técnicos</summary>

[Arquitetura](architecture/safetysec-android.svg) | [Vista técnica](architecture/technical/safetysec-android.svg) | [PNG da arquitetura](architecture/safetysec-android.png)

</details>

### Desert Caravan Simulator

**C++ | POO**

Simulador por turnos em terminal, com caravanas, cidades, recursos e comandos de movimentação.

**Tecnologias:** C++20, STL, POO

<a href="assets/portfolio/desert-caravan-poster.webp"><img src="assets/portfolio/desert-caravan-poster.webp" alt="Pré-visualização de Desert Caravan Simulator" width="720" loading="lazy"></a>

<details>
<summary>Ver funcionalidades e implementação</summary>

- **Implementação:** classes para mapa, caravanas, comandos e evolução de turnos.
- **Demonstração:** execução real no terminal.

</details>

<details>
<summary>Ver demonstração animada</summary>

<img src="assets/portfolio/desert-caravan.webp" alt="Demonstração de Desert Caravan Simulator" width="720" loading="lazy">

</details>

<a href="assets/portfolio/desert-caravan.mp4">Vídeo da execução</a>

<p>
<a href="architecture/desert-caravan.svg"><img alt="Arquitetura pública" src="https://img.shields.io/badge/Arquitetura_p%C3%BAblica-30363D?style=for-the-badge&logoColor=white"></a>
 
<a href="assets/portfolio/desert-caravan-poster.webp"><img alt="Imagem estática" src="https://img.shields.io/badge/Imagem_est%C3%A1tica-30363D?style=for-the-badge&logoColor=white"></a>


</p>

<details>
<summary>Ver arquitetura e detalhes técnicos</summary>

[Arquitetura](architecture/desert-caravan.svg) | [Vista técnica](architecture/technical/desert-caravan.svg) | [PNG da arquitetura](architecture/desert-caravan.png)

</details>

**Outros estudos:** Neural Shape Classifier e AMOV Flutter.

</details>

## Frontend e websites

Sites para clientes com foco em design, conteúdo, navegação e SEO. Não são apresentados como aplicações com backend complexo. A plataforma do Thiago inclui uma integração simples com API de pagamentos.

### Coimbra MMA

**Website informativo | Frontend e design**

Site de uma academia de artes marciais em Coimbra. Reúne modalidades, horários, apresentação da academia e canais de contacto, com conteúdo em oito idiomas.

**Tecnologias:** Astro, JavaScript, i18n, SEO

<a href="assets/portfolio/coimbra-mma-poster.webp"><img src="assets/portfolio/coimbra-mma-poster.webp" alt="Pré-visualização de Coimbra MMA" width="720" loading="lazy"></a>

<details>
<summary>Ver funcionalidades e implementação</summary>

- **Interface:** páginas responsivas, horários e assistente de modalidades.
- **Implementação:** páginas geradas estaticamente e validação das traduções. Não utiliza uma API de negócio.

</details>

<details>
<summary>Ver demonstração animada</summary>

<img src="assets/portfolio/coimbra-mma.webp" alt="Demonstração de Coimbra MMA" width="720" loading="lazy">

</details>

<p>
<a href="architecture/coimbra-mma.svg"><img alt="Arquitetura pública" src="https://img.shields.io/badge/Arquitetura_p%C3%BAblica-30363D?style=for-the-badge&logoColor=white"></a>
 
<a href="assets/portfolio/coimbra-mma-poster.webp"><img alt="Imagem estática" src="https://img.shields.io/badge/Imagem_est%C3%A1tica-30363D?style=for-the-badge&logoColor=white"></a>

 <a href="https://coimbramma.com"><img alt="Website" src="https://img.shields.io/badge/Website-30363D?style=for-the-badge&logoColor=white"></a>
</p>

<details>
<summary>Ver arquitetura e detalhes técnicos</summary>

[Arquitetura](architecture/coimbra-mma.svg) | [Vista técnica](architecture/technical/coimbra-mma.svg) | [PNG da arquitetura](architecture/coimbra-mma.png)

</details>

### Marta | Her Legacy

**Website editorial | Frontend e design**

Site informativo para apresentação de serviços de mentoria, conteúdos, formulários de contacto e lista de espera de um planner. O trabalho concentrou-se na identidade visual, estrutura editorial e experiência de navegação.

**Tecnologias:** Next.js, React, TypeScript, CSS

<a href="assets/portfolio/marta-poster.webp"><img src="assets/portfolio/marta-poster.webp" alt="Pré-visualização de Marta | Her Legacy" width="720" loading="lazy"></a>

<details>
<summary>Ver funcionalidades e implementação</summary>

- **Interface:** páginas responsivas, serviços, apresentação da marca, formulários e SEO.
- **Integração simples:** envio de contactos por email através de um serviço Spring Boot. Sem base de dados ou backend de negócio complexo.

</details>

<details>
<summary>Ver demonstração animada</summary>

<img src="assets/portfolio/marta.webp" alt="Demonstração de Marta | Her Legacy" width="720" loading="lazy">

</details>

<p>
<a href="architecture/marta.svg"><img alt="Arquitetura pública" src="https://img.shields.io/badge/Arquitetura_p%C3%BAblica-30363D?style=for-the-badge&logoColor=white"></a>
 
<a href="assets/portfolio/marta-poster.webp"><img alt="Imagem estática" src="https://img.shields.io/badge/Imagem_est%C3%A1tica-30363D?style=for-the-badge&logoColor=white"></a>


</p>

<details>
<summary>Ver arquitetura e detalhes técnicos</summary>

[Arquitetura](architecture/marta.svg) | [Vista técnica](architecture/technical/marta.svg) | [PNG da arquitetura](architecture/marta.png)

</details>

### Dalliany Tavares Advocacia

**Website editorial | Frontend e design**

Website informativo para apresentação da profissional e das áreas de atuação jurídica. Projeto orientado para design, navegação, conteúdos e presença digital.

**Tecnologias:** Astro, TypeScript, SEO

<a href="assets/portfolio/dalliany-poster.webp"><img src="assets/portfolio/dalliany-poster.webp" alt="Pré-visualização de Dalliany Tavares Advocacia" width="720" loading="lazy"></a>

<details>
<summary>Ver funcionalidades e implementação</summary>

- **Interface:** páginas responsivas, conteúdo estruturado e imagens otimizadas.
- **Implementação:** geração estática sem backend de negócio complexo. Projeto em pré-lançamento, dependente de validações do cliente.

</details>

<details>
<summary>Ver demonstração animada</summary>

<img src="assets/portfolio/dalliany.webp" alt="Demonstração de Dalliany Tavares Advocacia" width="720" loading="lazy">

</details>

<p>
<a href="architecture/dalliany.svg"><img alt="Arquitetura pública" src="https://img.shields.io/badge/Arquitetura_p%C3%BAblica-30363D?style=for-the-badge&logoColor=white"></a>
 
<a href="assets/portfolio/dalliany-poster.webp"><img alt="Imagem estática" src="https://img.shields.io/badge/Imagem_est%C3%A1tica-30363D?style=for-the-badge&logoColor=white"></a>


</p>

<details>
<summary>Ver arquitetura e detalhes técnicos</summary>

[Arquitetura](architecture/dalliany.svg) | [Vista técnica](architecture/technical/dalliany.svg) | [PNG da arquitetura](architecture/dalliany.png)

</details>

### Thiago Santos English Platform

**Website comercial | Frontend, design e pequena integração**

Site para apresentar um professor de inglês, divulgar cursos e ebooks e permitir a navegação por catálogo e carrinho. A maior parte do trabalho foi visual, com uma integração pontual de pagamento.

**Tecnologias:** Eleventy, Node.js, Express, Mercado Pago, Pix

<a href="assets/portfolio/thiago-poster.webp"><img src="assets/portfolio/thiago-poster.webp" alt="Pré-visualização de Thiago Santos English Platform" width="720" loading="lazy"></a>

<details>
<summary>Ver funcionalidades e implementação</summary>

- **Interface:** página inicial, cursos, ebooks, carrinho e contactos.
- **Integração simples:** endpoints Node.js/Express para o fluxo de pagamento com Mercado Pago e Pix. A demonstração pública não realiza transações.

</details>

<details>
<summary>Ver demonstração animada</summary>

<img src="assets/portfolio/thiago.webp" alt="Demonstração de Thiago Santos English Platform" width="720" loading="lazy">

</details>

<p>
<a href="architecture/thiago.svg"><img alt="Arquitetura pública" src="https://img.shields.io/badge/Arquitetura_p%C3%BAblica-30363D?style=for-the-badge&logoColor=white"></a>
 
<a href="assets/portfolio/thiago-poster.webp"><img alt="Imagem estática" src="https://img.shields.io/badge/Imagem_est%C3%A1tica-30363D?style=for-the-badge&logoColor=white"></a>


</p>

<details>
<summary>Ver arquitetura e detalhes técnicos</summary>

[Arquitetura](architecture/thiago.svg) | [Vista técnica](architecture/technical/thiago.svg) | [PNG da arquitetura](architecture/thiago.png)

</details>



## Formação e experiência

- **Engenharia Informática, ISEC (2022 a 2026):** licenciatura com especialização em Desenvolvimento de Aplicações, concluída em julho de 2026.
- **Experiência empresarial (2026):** estágio curricular em engenharia de software, com desenvolvimento de APIs, integração de modelos de IA e colaboração em equipa.
- **Freelance (desde 2025):** websites e aplicações para clientes, com levantamento de requisitos, desenvolvimento e publicação.

<sub>Créditos dos diagramas e ícones: [atribuições](architecture/ATTRIBUTION.md).</sub>
