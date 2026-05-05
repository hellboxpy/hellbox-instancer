# hellbox-instancer

A [hellbox](https://github.com/hellboxpy/hellbox) plugin that generates static instances from variable fonts using [fonttools](https://github.com/fonttools/fonttools).

## Usage

Pin one or more axes by passing axis tags as keyword arguments:

```python
from hellbox import Hellbox
from hellbox.jobs.instancer import Instance

with Hellbox("instance") as task:
    task.read("build/*.ttf") >> Instance(wght=700) >> task.write("instances")
```

Restrict an axis to a range rather than pinning it by passing a tuple:

```python
Instance(wght=(300, 700))
```

Multiple axes can be combined:

```python
Instance(wght=700, wdth=100)
```

## Installation

```sh
pip install hellbox-instancer
```
