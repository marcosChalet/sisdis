# Atividade 4 - JAVA RMI

## Como rodar o projeto

### Rodando servidor

```bash
javac -d bin *.java
cd bin
rmiregistry 11099
```

**_Em outro terminal execute_**

```bash
java BrokerServer
```

### Rodando cliente

Após esses passos rode o cliente (**_ainda na pasta bin_**)

**_Em outro terminal execute_**

```bash
java BrokerClient
```
