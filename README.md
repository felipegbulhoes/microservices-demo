# 🧱 Microservices Demo – Python + Flask + Docker + API Gateway

Este projeto é um exemplo completo de arquitetura baseada em **microserviços**, utilizando:

- **Python + Flask**  
- **Docker**  
- **Docker Compose**  
- **API Gateway**  
- Comunicação entre containers via rede interna

O objetivo é demonstrar como estruturar, orquestrar, testar e integrar múltiplos microserviços em um ambiente simples, extensível e ideal para estudo ou como base para projetos reais.

---

# 📦 Arquitetura dos Microserviços

O sistema é composto por **4 serviços**:

| Serviço | Porta Externa | Porta Interna | Descrição |
|--------|---------------|---------------|-----------|
| `service-users` | 8001 | 5001 | Fornece dados de usuários |
| `service-products` | 8002 | 5002 | Fornece dados de produtos |
| `service-orders` | 8003 | 5003 | Integra usuários + produtos para gerar pedidos |
| `gateway` | 8000 | 8000 | API Gateway que concentra todas as chamadas |

Cada serviço roda em um container separado e se comunicam entre si pelo nome do serviço no Docker Compose.

---

# 🗂️ Estrutura do Repositório

```

microservices-demo/
│
├── docker-compose.yml
│
├── gateway/
│   ├── app.py
│   └── Dockerfile
│
├── service-users/
│   ├── app.py
│   └── Dockerfile
│
├── service-products/
│   ├── app.py
│   └── Dockerfile
│
└── service-orders/
├── app.py
└── Dockerfile

````

---

# 🚀 Como Executar o Projeto

Certifique-se de ter instalado:

- Docker
- Docker Compose

### 1. Clone o repositório
```bash
git clone https://github.com/SEU_USUARIO/microservices-demo.git
cd microservices-demo
````

### 2. Build dos serviços

```bash
docker compose build
```

### 3. Subir os containers

```bash
docker compose up -d
```

### 4. Verificar se está tudo rodando

```bash
docker ps
```

---

# 🔗 Endpoints Disponíveis

## Gateway (porta 8000)

* `GET /` — Status do gateway
* `GET /users` — Retorna todos os usuários
* `GET /products` — Retorna todos os produtos
* `GET /orders` — Retorna todos os pedidos

## Microserviços Individuais (acesso direto)

* `http://localhost:8001/users`
* `http://localhost:8002/products`
* `http://localhost:8003/orders`

---

# 🧪 Testes Simples com curl

```bash
curl http://localhost:8000/users
curl http://localhost:8000/products
curl http://localhost:8000/orders
```

---

# 🛠️ Tecnologias Utilizadas

* Python 3.10
* Flask
* Requests
* Docker / Docker Compose
* API Gateway simples (Flask)

---

# 🌱 Possíveis Melhorias

Contribuições são bem-vindas! Ideias futuras:

* Autenticação com JWT
* Logs centralizados
* Observabilidade com Prometheus + Grafana
* Banco de dados para cada microserviço
* Mensageria (RabbitMQ / Kafka)
* API Gateway com FastAPI ou NGINX
* Testes unitários e de integração
* CI/CD com GitHub Actions

Abra uma **issue** com sua sugestão! 😄

---

# 👥 Como Contribuir

1. Faça um **fork** do projeto
2. Crie uma branch:

   ```bash
   git checkout -b minha-feature
   ```
3. Faça suas alterações e commit:

   ```bash
   git commit -m "Minha nova feature"
   ```
4. Envie para o seu fork:

   ```bash
   git push origin minha-feature
   ```
5. Abra um **Pull Request**

---

# 📄 Licença

Este projeto está sob a licença MIT — sinta-se livre para utilizar, modificar e evoluir!

---

# ⭐ Deixe uma estrela!

Se este projeto te ajudou, considere deixar uma ⭐ no repositório para ajudar sua divulgação e incentivar melhorias futuras.

```
