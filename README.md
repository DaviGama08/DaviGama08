<div align="center">

# Davi Gama

### Software Engineer · Distributed Systems · Backend · Full-Stack · Applied AI

Computer Engineering graduate based in Coimbra, Portugal.

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Davi%20Gama-0A66C2?style=flat-square&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/davinasser/)
[![Email](https://img.shields.io/badge/Email-Contact%20Me-EA4335?style=flat-square&logo=gmail&logoColor=white)](mailto:davi.torres00pro@gmail.com)

</div>

## About Me

I am a **Computer Engineering graduate from the Instituto Superior de Engenharia de Coimbra — ISEC**, specialising in **Application Development**.

My main interests are backend engineering, distributed systems and full-stack development. I have built applications involving replicated servers, network communication, REST APIs, web platforms, mobile applications, concurrent processes and applied artificial intelligence.

My experience covers different stages of software development, including requirements analysis, architecture, domain modelling, implementation, persistence, API integration, testing, documentation and deployment.

I am currently open to **junior and graduate software engineering opportunities** in Portugal, across Europe or remotely.

## Featured Projects

> Most academic repositories are currently private while I remove credentials, generated files and course-specific material, improve their documentation and prepare safe public portfolio versions.

### Distributed Quiz Platform

Distributed question-and-answer platform developed in Java, supporting separate interfaces and operations for teachers and students.

The system uses a directory service to discover available servers and a replicated server cluster with primary and backup nodes. It includes heartbeat communication, database replication, automatic reconnection and session recovery.

**Engineering highlights:**

- Client-server architecture using TCP and UDP
- Directory service for server discovery
- Multicast communication between server nodes
- Primary and backup server coordination
- SQLite database replication
- Incremental SQL update propagation
- Client reconnection and session recovery
- Separate teacher and student workflows
- Authentication, question management and answer statistics
- JavaFX desktop interface

`Java` · `JavaFX` · `TCP` · `UDP` · `Multicast` · `Threads` · `SQLite` · `Jackson` · `Maven`

---

### MyMEDIA — Multimedia Marketplace

Full-stack marketplace that connects multimedia-product suppliers with customers through a structured platform.

The solution follows a multi-application architecture composed of a management back office, a REST API and a customer-facing frontend. The web and .NET MAUI Hybrid clients share reusable components and services.

**Engineering highlights:**

- Separate frontend, back office and REST API applications
- Shared components between Blazor Web and .NET MAUI
- Role-based access control
- Administrator, employee, supplier and customer profiles
- Employee and supplier approval workflows
- Product and category management
- Shopping cart and favourites
- Sale and rental order processing
- Cookie and JWT authentication
- API documentation with Swagger/OpenAPI
- Persistence with Entity Framework Core

`C#` · `.NET` · `ASP.NET Core` · `Blazor` · `.NET MAUI` · `REST API` · `Entity Framework Core` · `SQL Server` · `Identity` · `JWT` · `Swagger`

---

### SafetySec — Mobile Safety Monitoring

Android application designed to support safety monitoring between protected users and designated monitors.

The application combines location tracking, mobile sensors, emergency alerts and cloud services. It supports different user roles, background monitoring and the recording of emergency-related information.

**Engineering highlights:**

- Native Android application with Jetpack Compose
- Protected-user and monitor workflows
- Fall, accident and panic alerts
- Location and speed monitoring
- Geofencing and inactivity detection
- Background and foreground Android services
- Firebase authentication and cloud persistence
- Push notifications with Firebase Cloud Messaging
- Biometric authentication and multi-factor authentication
- CameraX video recording
- Google Maps integration
- Alert history and statistics
- CSV data export

`Kotlin` · `Jetpack Compose` · `Firebase` · `Coroutines` · `CameraX` · `Google Maps` · `Android Services` · `Biometric Authentication`

---

### Coimbra MMA — Production Website

Production website developed for a martial arts academy in Coimbra.

The website provides information about classes, instructors, schedules, facilities and contact channels through a responsive and multilingual interface.

**Engineering highlights:**

- Component-based Astro architecture
- Responsive layout
- Content available in multiple languages
- Configuration-driven content management
- Technical SEO
- Structured data with JSON-LD
- Sitemap and robots configuration
- Automated translation-consistency validation
- CI and deployment checks with GitHub Actions

`Astro` · `JavaScript` · `CSS` · `i18n` · `SEO` · `JSON-LD` · `GitHub Actions`

[Visit the live website](https://coimbramma.com/)

---

### Neural Shape Classifier

Machine-learning experimentation and classification platform developed in MATLAB using feedforward neural networks.

The project classifies six categories of geometric shapes and explores how network topology, activation functions, training algorithms and dataset divisions affect performance and generalisation.

**Engineering highlights:**

- Image conversion to grayscale and binary matrices
- Image resizing and feature-vector generation
- Feedforward neural-network training
- Comparison of network topologies
- Comparison of activation and training functions
- Repeated experiments for more reliable measurements
- Training, validation and test dataset evaluation
- Confusion matrices and per-class analysis
- CSV result generation
- Model saving and loading
- Classification of user-drawn shapes
- Interactive graphical application built with MATLAB App Designer

The best evaluated configuration reached approximately **91.47% global accuracy**, while additional experiments demonstrated the difference between internal test performance and generalisation to newly drawn shapes.

`MATLAB` · `Deep Learning Toolbox` · `Feedforward Neural Networks` · `Image Processing` · `App Designer` · `Model Evaluation`

---

### Coimbra Tourist Guide

Cross-platform mobile application developed in Flutter for exploring tourist attractions, museums and gastronomic locations in Coimbra.

The application combines local structured information with real-time weather data and persistent user preferences.

**Engineering highlights:**

- Modular Flutter project structure
- Tourist information loaded from local JSON
- Model mapping and data encapsulation
- IPMA weather API integration
- Asynchronous HTTP requests
- Persistent favourite locations
- Shared Preferences local storage
- Category and point-of-interest navigation
- Adaptive portrait and landscape layouts
- Material Design 3 interface
- Error and loading-state handling

`Flutter` · `Dart` · `Material 3` · `REST API` · `JSON` · `Shared Preferences` · `Responsive UI`

## Additional Engineering Projects

### JavaFX Chess

Complete chess application developed to explore advanced object-oriented programming and software design patterns.

The application implements chess rules such as castling, en passant, pawn promotion, check and checkmate. It also includes game persistence, multimedia resources, a learning mode and undo/redo functionality.

**Patterns and concepts:** MVC, Memento, Factory, Facade, Observer, serialization, polymorphism and domain modelling.

`Java` · `JavaFX` · `MVC` · `Design Patterns` · `Serialization` · `Maven`

---

### Windows IPC Word Game

Multi-process word game developed using Windows inter-process communication mechanisms.

The system contains a central referee, multiple players, autonomous bots and a graphical monitoring panel.

**Engineering highlights:**

- Multiple coordinated processes
- Named-pipe communication
- Shared-memory state
- Threads and synchronization
- Events and process notifications
- Concurrent player handling
- Autonomous bot execution
- Graphical monitoring panel
- Structured shutdown of system components

`C` · `C++` · `Win32 API` · `Named Pipes` · `Shared Memory` · `Threads` · `Events` · `Process Synchronization`

---

### SurpriseMe — AI-Assisted Gift Recommendations

Java desktop application that helps users organise recipients, occasions and gift history while generating personalised gift and gift-card message suggestions through an LLM API.

The project was developed incrementally using user stories, sprint planning, risk management, acceptance criteria and collaborative code reviews.

**Engineering highlights:**

- Recipient and preference management
- Event and occasion tracking
- Gift-history persistence
- Personalised prompt construction
- LLM API integration
- Gift and message generation
- JavaFX desktop interface
- Domain modelling
- Iterative development with GitLab issues and merge requests
- Continuous-integration workflow

`Java` · `JavaFX` · `Maven` · `LLM API` · `Prompt Engineering` · `GitLab CI` · `Agile Development`

## Technical Toolkit

| Area | Technologies |
| --- | --- |
| **Backend and APIs** | Java, Spring Boot, C#, ASP.NET Core, Python, FastAPI, REST, OpenAPI |
| **Distributed Systems** | TCP, UDP, multicast, Apache Kafka, microservices, replication, asynchronous processing |
| **Web Development** | React, Vite, Blazor, Astro, JavaScript, HTML, CSS |
| **Mobile Development** | Kotlin, Jetpack Compose, Flutter, Dart, .NET MAUI |
| **Artificial Intelligence** | PyTorch, Transformers, MATLAB Deep Learning Toolbox, NER, local model evaluation, LLM APIs |
| **Data and Persistence** | PostgreSQL, SQL Server, MySQL, SQLite, Firebase, Entity Framework Core, Hibernate |
| **Systems Programming** | C, C++, Win32 API, threads, shared memory, named pipes and synchronization |
| **Engineering Tools** | Git, GitHub, GitLab, Docker, Docker Compose, Maven, Gradle, Postman, Swagger and CI workflows |

## Education

### Bachelor's Degree in Computer Engineering

**Instituto Superior de Engenharia de Coimbra — ISEC**  
Specialisation in Application Development · 2022–2026

Relevant areas include:

- Object-oriented and advanced programming
- Distributed programming
- Web and mobile development
- Operating systems and concurrency
- Databases and computer networks
- Artificial intelligence and knowledge representation
- Data structures and algorithms
- Software modelling and design
- Human-computer interaction
- Software project management

## Professional Experience

### Freelance Web Developer

Developed and delivered websites from requirements gathering through implementation and deployment. Worked directly with clients, managed project requirements and maintained production solutions.

## Engineering Principles

I value:

- Clear and maintainable architecture
- Explicit functional and quality requirements
- Separation of responsibilities
- Reliable and measurable results
- Useful technical documentation
- Secure management of credentials and configuration
- Software designed to evolve over time

## Contact

The best ways to reach me are through [LinkedIn](https://www.linkedin.com/in/davinasser/) or [email](mailto:davi.torres00pro@gmail.com).
