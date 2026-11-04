<div align="center">

<img src="assets/profile/terminal.svg" alt="Terminal animado com a stack Java, Spring Boot, PostgreSQL, React, TypeScript, Astro, Docker, Maven, Azure e Cloudflare" width="960">

<br>

<a href="https://github.com/DaviGama08"><img src="https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white" alt="GitHub"></a>
<a href="https://www.linkedin.com/in/davinasser/"><img src="https://img.shields.io/badge/LinkedIn-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white" alt="LinkedIn"></a>

</div>

## Projetos em destaque

Os projetos abaixo mostram diferentes partes do meu trabalho. Seleciona o que for mais relevante para a vaga.

**[Skevia](#skevia)** | SaaS multi-tenant para agendamentos  
Regras de disponibilidade, transações, autenticação, isolamento de dados e backoffice. O Ícaro’s Barbershop é um tenant de exemplo.  
**Stack:** Java 25, Spring Boot 4, PostgreSQL, Flyway, React, TypeScript, Cloudflare.

**[AssessFlow](#assessflow)** | Sessões e avaliações em tempo real (projeto pessoal)  
APIs, WebSocket/STOMP, permissões, testes de integração e execução em cloud ou rede local.  
**Stack:** Java 25, Spring Boot 4, PostgreSQL, React, Testcontainers.

**[503](#503)** | Publicação de artigos (projeto pessoal)  
API de gestão editorial, autenticação, backoffice e aplicação publicada em cloud.  
**Stack:** Java 25, Spring Boot 4, PostgreSQL, Flyway, Astro, React, Azure e Cloudflare.

**[Distributed Quiz](#distributed-quiz)** | Sistemas distribuídos (projeto académico)  
Descoberta de servidores, replicação, heartbeats, recuperação de sessões e failover.  
**Stack:** Java, JavaFX, TCP/UDP, multicast, SQLite e Maven.

**[Frontend e websites](#frontend-e-websites)** | Trabalhos para clientes  
Websites responsivos com foco em interface, conteúdo e SEO. O projeto Thiago inclui uma integração simples com pagamentos.  
**Stack:** Astro, Next.js, React, TypeScript, Node.js/Express e Mercado Pago.

## Sobre mim

Sou Davi Gama, licenciado em Engenharia Informática pelo ISEC, em Coimbra. Desenvolvo aplicações backend com Java e Spring Boot, assim como websites e produtos fullstack. Tenho experiência em ambiente empresarial, trabalho em equipa e desenvolvimento freelance, desde o levantamento de requisitos até à publicação. Interesso-me por APIs, bases de dados, arquitetura de software e regras de negócio.

## Formação e experiência

- **Engenharia Informática, ISEC (2022 a 2026):** licenciatura com especialização em Desenvolvimento de Aplicações, concluída em julho de 2026.
- **Experiência empresarial (2026):** estágio curricular em engenharia de software, com desenvolvimento de APIs, integração de modelos de IA e colaboração em equipa.
- **Freelance (desde 2025):** websites e aplicações para clientes, com levantamento de requisitos, desenvolvimento e publicação.

## Tecnologias

**Linguagens:** Java, C#, TypeScript, JavaScript, Python, C/C++ e SQL.

**Backend e dados:** Spring Boot, Spring Data JPA, Hibernate, ASP.NET Core, FastAPI, PostgreSQL, MySQL, SQL Server e SQLite.

**Frontend:** React, Next.js, Astro, Blazor e JavaFX.

**Ferramentas:** Git, Maven, Gradle, Docker, JUnit, Testcontainers, CI/CD, Azure e Cloudflare.

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

<img src="assets/optimized/multi-tenant.webp" alt="Pré-visualização animada de Skevia | Plataforma de agendamentos" width="720" loading="lazy">

<p>
<a href="https://icarosbarber.skevialtda.com/"><img alt="Ver tenant de exemplo" src="https://img.shields.io/badge/Ver_tenant_de_exemplo-0969DA?style=for-the-badge&logoColor=white"></a>
<a href="architecture/multi-tenant.svg"><img alt="Arquitetura pública" src="https://img.shields.io/badge/Arquitetura_p%C3%BAblica-30363D?style=for-the-badge&logoColor=white"></a>
<a href="architecture/technical/multi-tenant.svg"><img alt="Vista técnica" src="https://img.shields.io/badge/Vista_t%C3%A9cnica-6F42C1?style=for-the-badge&logoColor=white"></a>

</p>

<details>
<summary>Ver funcionalidades e implementação</summary>

- **Funcionalidades:** agendamento online, disponibilidade por profissional, backoffice, personalização do site e relatórios.
- **Backend:** regras de disponibilidade e conflitos, transações, isolamento de tenants, autenticação, RLS e contratos OpenAPI.
- **Frontend:** site público e painel de gestão, com componentes reutilizados no editor visual.

</details>

### AssessFlow

**Projeto pessoal | Fullstack**

Plataforma de avaliações com bancos de perguntas, sessões ao vivo e participação por código ou QR. Funciona na nuvem ou em rede local.

**Tecnologias:** Java 25, Spring Boot 4.1, PostgreSQL, React, WebSocket, STOMP

<img src="assets/portfolio/assessflow.webp" alt="Pré-visualização animada de AssessFlow" width="720" loading="lazy">

<p>
<a href="architecture/assessflow.svg"><img alt="Arquitetura pública" src="https://img.shields.io/badge/Arquitetura_p%C3%BAblica-30363D?style=for-the-badge&logoColor=white"></a>
<a href="architecture/technical/assessflow.svg"><img alt="Vista técnica" src="https://img.shields.io/badge/Vista_t%C3%A9cnica-6F42C1?style=for-the-badge&logoColor=white"></a>

<a href="https://github.com/DaviGama08/assessflow"><img alt="Código" src="https://img.shields.io/badge/C%C3%B3digo-238636?style=for-the-badge&logoColor=white"></a>
</p>

<details>
<summary>Ver funcionalidades e implementação</summary>

- **Funcionalidades:** autoria de avaliações, sessões em tempo real, respostas, resultados e exportação CSV.
- **Backend:** organizações isoladas, permissões, API REST, WebSockets e persistência com Flyway.
- **Qualidade:** testes com Testcontainers e integração contínua. Redis e RabbitMQ são opções de escala, não dependências obrigatórias.

</details>

<!-- Website ainda não publicado: adicionar botão quando existir um URL verificado. -->

### 503

**Projeto pessoal | Fullstack**

Plataforma pessoal para gerir e publicar artigos. Inclui website público, backoffice de edição e API responsável pelas regras de publicação e persistência.

**Tecnologias:** Java 25, Spring Boot 4.1, PostgreSQL, Flyway, Astro, React, Azure, Cloudflare

<img src="assets/optimized/503.webp" alt="Pré-visualização animada de 503 | Plataforma de publicação" width="720" loading="lazy">

<p>
<a href="https://blog503.com/"><img alt="Ver website" src="https://img.shields.io/badge/Ver_website-0969DA?style=for-the-badge&logoColor=white"></a>
<a href="architecture/503.svg"><img alt="Arquitetura pública" src="https://img.shields.io/badge/Arquitetura_p%C3%BAblica-30363D?style=for-the-badge&logoColor=white"></a>
<a href="architecture/technical/503.svg"><img alt="Vista técnica" src="https://img.shields.io/badge/Vista_t%C3%A9cnica-6F42C1?style=for-the-badge&logoColor=white"></a>

</p>

<details>
<summary>Ver funcionalidades e implementação</summary>

- **Funcionalidades:** rascunhos, edição de artigos, publicação, capas e autenticação administrativa.
- **Backend:** API REST, regras editoriais, segurança, persistência e migrações.
- **Frontend:** site público em Astro e administração separada em React.

</details>

## Java e sistemas distribuídos

### Distributed Quiz

**Java | Sistemas distribuídos**

Sistema de questionários para docentes e alunos com clientes JavaFX e servidores que suportam descoberta, replicação e recuperação após falhas.

**Tecnologias:** Java, JavaFX, TCP, UDP, multicast, SQLite, Maven

<img src="assets/portfolio/distributed-quiz.webp" alt="Pré-visualização animada de Distributed Quiz" width="720" loading="lazy">

<p>
<a href="architecture/distributed-quiz.svg"><img alt="Arquitetura pública" src="https://img.shields.io/badge/Arquitetura_p%C3%BAblica-30363D?style=for-the-badge&logoColor=white"></a>
<a href="architecture/technical/distributed-quiz.svg"><img alt="Vista técnica" src="https://img.shields.io/badge/Vista_t%C3%A9cnica-6F42C1?style=for-the-badge&logoColor=white"></a>

<a href="https://github.com/DaviGama08/distributed-quiz-platform-isec"><img alt="Código" src="https://img.shields.io/badge/C%C3%B3digo-238636?style=for-the-badge&logoColor=white"></a>
</p>

<details>
<summary>Ver funcionalidades e implementação</summary>

- **Funcionalidades:** perguntas, respostas, códigos de acesso, estatísticas e notificações.
- **Arquitetura:** descoberta de serviços, replicação primário/backup, heartbeats, failover e reconexão.

</details>

<!-- Website ainda não publicado: adicionar botão quando existir um URL verificado. -->

## Outros projetos técnicos

<details>
<summary>Ver mais projetos académicos</summary>

### MyMEDIA

**.NET | Fullstack académico**

Marketplace académico de produtos multimédia, com loja pública, backoffice e API partilhada por várias interfaces.

**Tecnologias:** C#, ASP.NET Core, Blazor, EF Core, SQL Server

<img src="assets/optimized/mymedia.webp" alt="Pré-visualização animada de MyMEDIA" width="720" loading="lazy">

<p>
<a href="architecture/mymedia.svg"><img alt="Arquitetura pública" src="https://img.shields.io/badge/Arquitetura_p%C3%BAblica-30363D?style=for-the-badge&logoColor=white"></a>
<a href="architecture/technical/mymedia.svg"><img alt="Vista técnica" src="https://img.shields.io/badge/Vista_t%C3%A9cnica-6F42C1?style=for-the-badge&logoColor=white"></a>

</p>

<details>
<summary>Ver funcionalidades e implementação</summary>

- **Funcionalidades:** produtos, favoritos, carrinho, encomendas e gestão administrativa.
- **Backend:** API REST, autenticação, permissões e persistência relacional.

</details>

<!-- Website ainda não publicado: adicionar botão quando existir um URL verificado. -->

### JavaFX Chess

**Java | Desktop**

Aplicação de xadrez com validação de jogadas, regras completas, histórico, edição de posições e persistência local.

**Tecnologias:** Java, JavaFX, Maven, JUnit

<img src="assets/portfolio/javafx-chess.webp" alt="Pré-visualização animada de JavaFX Chess" width="720" loading="lazy">

<p>
<a href="architecture/javafx-chess.svg"><img alt="Arquitetura pública" src="https://img.shields.io/badge/Arquitetura_p%C3%BAblica-30363D?style=for-the-badge&logoColor=white"></a>
<a href="architecture/technical/javafx-chess.svg"><img alt="Vista técnica" src="https://img.shields.io/badge/Vista_t%C3%A9cnica-6F42C1?style=for-the-badge&logoColor=white"></a>

<a href="https://github.com/davigama-academic/javafx-chess-isec"><img alt="Código" src="https://img.shields.io/badge/C%C3%B3digo-238636?style=for-the-badge&logoColor=white"></a>
</p>

<details>
<summary>Ver funcionalidades e implementação</summary>

- **Implementação:** regras de xeque, roque, promoção e fim de jogo.
- **Arquitetura:** MVC e padrões Facade, Memento e Observer; testes da lógica de jogo.

</details>

<!-- Website ainda não publicado: adicionar botão quando existir um URL verificado. -->

### SurpriseMe

**Java | Desktop**

Organizador de presentes com destinatários, ocasiões e histórico para apoiar a escolha de sugestões.

**Tecnologias:** Java, JavaFX, Maven

<img src="assets/portfolio/surpriseme.webp" alt="Pré-visualização animada de SurpriseMe" width="720" loading="lazy">

<p>
<a href="architecture/surpriseme.svg"><img alt="Arquitetura pública" src="https://img.shields.io/badge/Arquitetura_p%C3%BAblica-30363D?style=for-the-badge&logoColor=white"></a>
<a href="architecture/technical/surpriseme.svg"><img alt="Vista técnica" src="https://img.shields.io/badge/Vista_t%C3%A9cnica-6F42C1?style=for-the-badge&logoColor=white"></a>

<a href="https://github.com/davigama-academic/surpriseme-gift-assistant-isec"><img alt="Código" src="https://img.shields.io/badge/C%C3%B3digo-238636?style=for-the-badge&logoColor=white"></a>
</p>

<details>
<summary>Ver funcionalidades e implementação</summary>

- **Implementação:** gestão de pessoas, eventos e presentes, com persistência local.
- **Integração:** componente de sugestão isolado; a demonstração visual não executa a inferência externa.

</details>

<!-- Website ainda não publicado: adicionar botão quando existir um URL verificado. -->

### Unix Topic Message Broker

**C | Sistemas operativos**

Broker local de mensagens por tópico, usando processos e mecanismos POSIX para publicação, subscrição e entrega concorrente.

**Tecnologias:** C, POSIX FIFOs, pthreads, select

<img src="assets/optimized/unix-broker.webp" alt="Pré-visualização animada de Unix Topic Message Broker" width="720" loading="lazy">

<p>
<a href="architecture/unix-broker.svg"><img alt="Arquitetura pública" src="https://img.shields.io/badge/Arquitetura_p%C3%BAblica-30363D?style=for-the-badge&logoColor=white"></a>
<a href="architecture/technical/unix-broker.svg"><img alt="Vista técnica" src="https://img.shields.io/badge/Vista_t%C3%A9cnica-6F42C1?style=for-the-badge&logoColor=white"></a>

</p>

<details>
<summary>Ver funcionalidades e implementação</summary>

- **Implementação:** gestor central, clientes independentes, sincronização e mensagens persistentes.
- **Demonstração:** execução real em terminal.

</details>

<!-- Website ainda não publicado: adicionar botão quando existir um URL verificado. -->

<a href="assets/portfolio/unix-broker.mp4">Vídeo da execução</a>

### Windows IPC Word Game

**C | Sistemas operativos**

Jogo de palavras com vários processos Windows, jogadores, bots e painel de monitorização.

**Tecnologias:** C, Win32 API, named pipes, shared memory

<img src="assets/optimized/windows-game.webp" alt="Pré-visualização animada de Windows IPC Word Game" width="720" loading="lazy">

<p>
<a href="architecture/windows-game.svg"><img alt="Arquitetura pública" src="https://img.shields.io/badge/Arquitetura_p%C3%BAblica-30363D?style=for-the-badge&logoColor=white"></a>
<a href="architecture/technical/windows-game.svg"><img alt="Vista técnica" src="https://img.shields.io/badge/Vista_t%C3%A9cnica-6F42C1?style=for-the-badge&logoColor=white"></a>

</p>

<details>
<summary>Ver funcionalidades e implementação</summary>

- **Implementação:** comunicação entre processos, threads, sincronização e estado de jogo partilhado.
- **Demonstração:** execução dos componentes Win32.

</details>

<!-- Website ainda não publicado: adicionar botão quando existir um URL verificado. -->

<a href="assets/portfolio/windows-game.mp4">Vídeo da execução</a>

### SafetySec Android

**Android | Académico**

Aplicação académica de acompanhamento e sinalização de emergência, com papéis de monitor e pessoa protegida.

**Tecnologias:** Android, Firebase

<img src="assets/portfolio/safetysec-android.webp" alt="Pré-visualização animada de SafetySec Android" width="720" loading="lazy">

<p>
<a href="architecture/safetysec-android.svg"><img alt="Arquitetura pública" src="https://img.shields.io/badge/Arquitetura_p%C3%BAblica-30363D?style=for-the-badge&logoColor=white"></a>
<a href="architecture/technical/safetysec-android.svg"><img alt="Vista técnica" src="https://img.shields.io/badge/Vista_t%C3%A9cnica-6F42C1?style=for-the-badge&logoColor=white"></a>

</p>

<details>
<summary>Ver funcionalidades e implementação</summary>

- **Interface:** painéis de monitorização e emergência.
- **Âmbito da demonstração:** interface com dados fictícios; sensores e serviços cloud não foram validados na captura.

</details>

<!-- Website ainda não publicado: adicionar botão quando existir um URL verificado. -->

### Desert Caravan Simulator

**C++ | POO**

Simulador por turnos em terminal, com caravanas, cidades, recursos e comandos de movimentação.

**Tecnologias:** C++20, STL, POO

<img src="assets/optimized/desert-caravan.webp" alt="Pré-visualização animada de Desert Caravan Simulator" width="720" loading="lazy">

<p>
<a href="architecture/desert-caravan.svg"><img alt="Arquitetura pública" src="https://img.shields.io/badge/Arquitetura_p%C3%BAblica-30363D?style=for-the-badge&logoColor=white"></a>
<a href="architecture/technical/desert-caravan.svg"><img alt="Vista técnica" src="https://img.shields.io/badge/Vista_t%C3%A9cnica-6F42C1?style=for-the-badge&logoColor=white"></a>

</p>

<details>
<summary>Ver funcionalidades e implementação</summary>

- **Implementação:** classes para mapa, caravanas, comandos e evolução de turnos.
- **Demonstração:** execução real no terminal.

</details>

<!-- Website ainda não publicado: adicionar botão quando existir um URL verificado. -->

<a href="assets/portfolio/desert-caravan.mp4">Vídeo da execução</a>

**Outros estudos:** Neural Shape Classifier e AMOV Flutter.

</details>

## Frontend e websites

Sites para clientes com foco em design, conteúdo, navegação e SEO. Não são apresentados como aplicações com backend complexo. A plataforma do Thiago inclui uma integração simples com API de pagamentos.

### Coimbra MMA

**Website informativo | Frontend e design**

Site de uma academia de artes marciais em Coimbra. Reúne modalidades, horários, apresentação da academia e canais de contacto, com conteúdo em oito idiomas.

**Tecnologias:** Astro, JavaScript, i18n, SEO

<img src="assets/optimized/coimbra-mma.webp" alt="Pré-visualização animada de Coimbra MMA" width="720" loading="lazy">

<p>
<a href="https://coimbramma.com/"><img alt="Ver website" src="https://img.shields.io/badge/Ver_website-0969DA?style=for-the-badge&logoColor=white"></a>
<a href="architecture/coimbra-mma.svg"><img alt="Arquitetura pública" src="https://img.shields.io/badge/Arquitetura_p%C3%BAblica-30363D?style=for-the-badge&logoColor=white"></a>
<a href="architecture/technical/coimbra-mma.svg"><img alt="Vista técnica" src="https://img.shields.io/badge/Vista_t%C3%A9cnica-6F42C1?style=for-the-badge&logoColor=white"></a>

</p>

<details>
<summary>Ver funcionalidades e implementação</summary>

- **Interface:** páginas responsivas, horários e assistente de modalidades.
- **Implementação:** páginas geradas estaticamente e validação das traduções. Não utiliza uma API de negócio.

</details>

### Marta | Her Legacy

**Website editorial | Frontend e design**

Site informativo para apresentação de serviços de mentoria, conteúdos, formulários de contacto e lista de espera de um planner. O trabalho concentrou-se na identidade visual, estrutura editorial e experiência de navegação.

**Tecnologias:** Next.js, React, TypeScript, CSS

<img src="assets/optimized/marta.webp" alt="Pré-visualização animada de Marta | Her Legacy" width="720" loading="lazy">

<p>
<a href="architecture/marta.svg"><img alt="Arquitetura pública" src="https://img.shields.io/badge/Arquitetura_p%C3%BAblica-30363D?style=for-the-badge&logoColor=white"></a>
<a href="architecture/technical/marta.svg"><img alt="Vista técnica" src="https://img.shields.io/badge/Vista_t%C3%A9cnica-6F42C1?style=for-the-badge&logoColor=white"></a>

</p>

<details>
<summary>Ver funcionalidades e implementação</summary>

- **Interface:** páginas responsivas, serviços, apresentação da marca, formulários e SEO.
- **Integração simples:** envio de contactos por email através de um serviço Spring Boot. Sem base de dados ou backend de negócio complexo.

</details>

<!-- Website ainda não publicado: adicionar botão quando existir um URL verificado. -->

### Dalliany Tavares Advocacia

**Website editorial | Frontend e design**

Website informativo para apresentação da profissional e das áreas de atuação jurídica. Projeto orientado para design, navegação, conteúdos e presença digital.

**Tecnologias:** Astro, TypeScript, SEO

<img src="assets/optimized/dalliany.webp" alt="Pré-visualização animada de Dalliany Tavares Advocacia" width="720" loading="lazy">

<p>
<a href="architecture/dalliany.svg"><img alt="Arquitetura pública" src="https://img.shields.io/badge/Arquitetura_p%C3%BAblica-30363D?style=for-the-badge&logoColor=white"></a>
<a href="architecture/technical/dalliany.svg"><img alt="Vista técnica" src="https://img.shields.io/badge/Vista_t%C3%A9cnica-6F42C1?style=for-the-badge&logoColor=white"></a>

</p>

<details>
<summary>Ver funcionalidades e implementação</summary>

- **Interface:** páginas responsivas, conteúdo estruturado e imagens otimizadas.
- **Implementação:** geração estática sem backend de negócio complexo. Projeto em pré-lançamento, dependente de validações do cliente.

</details>

<!-- Website ainda não publicado: adicionar botão quando existir um URL verificado. -->

### Thiago Santos English Platform

**Website comercial | Frontend, design e pequena integração**

Site para apresentar um professor de inglês, divulgar cursos e ebooks e permitir a navegação por catálogo e carrinho. A maior parte do trabalho foi visual, com uma integração pontual de pagamento.

**Tecnologias:** Eleventy, Node.js, Express, Mercado Pago, Pix

<img src="assets/optimized/thiago.webp" alt="Pré-visualização animada de Thiago Santos English Platform" width="720" loading="lazy">

<p>
<a href="architecture/thiago.svg"><img alt="Arquitetura pública" src="https://img.shields.io/badge/Arquitetura_p%C3%BAblica-30363D?style=for-the-badge&logoColor=white"></a>
<a href="architecture/technical/thiago.svg"><img alt="Vista técnica" src="https://img.shields.io/badge/Vista_t%C3%A9cnica-6F42C1?style=for-the-badge&logoColor=white"></a>

</p>

<details>
<summary>Ver funcionalidades e implementação</summary>

- **Interface:** página inicial, cursos, ebooks, carrinho e contactos.
- **Integração simples:** endpoints Node.js/Express para o fluxo de pagamento com Mercado Pago e Pix. A demonstração pública não realiza transações.

</details>

<!-- Website ainda não publicado: adicionar botão quando existir um URL verificado. -->

<sub>Créditos dos diagramas e ícones: [atribuições](architecture/ATTRIBUTION.md).</sub>
