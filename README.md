# EX3 Dev Containers

Containerizing the three separate systems for development.


## Usage

1. Create Docker Compose stack:

```
make up
```

2. In two separate shells, follow the subsystem logs and the Ground Station CLI:

```
# Follow the subsystem logs
make sub
```

```
# Run the Ground Station CLI
make gnd
```

3. Clean up the Docker Compose Stack after:

```
make down
```
