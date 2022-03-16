# Introduction to Ploomber

This repository contains a sample pipeline developed using [Ploomber](https://github.com/ploomber/ploomber). It is based on a [reference implementation](https://github.com/florianbussmann/introduction-to-dagster/blob/main/cereal_serial_pipeline.py) using [Dagster](https://www.dagster.io/).

**Note:** For more examples check out the [official sample projects](https://github.com/ploomber/projects).

## Setup environment
You can set up your development environment with:

```sh
source update-python-env.sh
```

## Hello, Ploomber
```sh
ploomber build
```

The result will be a notebook output written to `output/sugar.html` and should state `Nut&Honey Crunch is the sugariest cereal`.