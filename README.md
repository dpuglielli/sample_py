# Poetry Sample App

A Python app using Poetry.

## Setup

[Poetry](https://python-poetry.org/) is required.

```bash
poetry install
```

## Run program

```bash
poetry run sample_py
```

## Tests

Run all tests:

```bash
poetry run pytest
```

## Coverage

```bash
poetry run pytest --cov=sample_py
```

To view an HTML report:

```bash
poetry run pytest --cov=sample_py --cov-report html
open coverage_html_report/index.html
```

For [Coverage Gutters](https://marketplace.visualstudio.com/items?itemName=ryanluker.vscode-coverage-gutters)
```bash
poetry run pytest --cov=sample_py --cov-report xml
```

## Mypy typechecking

```bash
poetry run mypy sample_py
```

## Graph dependencies

```bash
poetry run pydeps sample_py --max-bacon=4 --cluster
```
### Dependency output

<svg width="382pt" height="216pt"
 viewBox="0.00 0.00 382.41 216.41" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
<g id="graph0" class="graph" transform="scale(1 1) rotate(0) translate(4 212.41)">
<title>G</title><style>.edge>path:hover{stroke-width:8}</style>
<polygon fill="white" stroke="transparent" points="-4,4 -4,-212.41 378.41,-212.41 378.41,4 -4,4"/>
<!-- sample_py_area -->
<g id="node1" class="node">
<title>sample_py_area</title><style>.edge>path:hover{stroke-width:8}</style>
<ellipse fill="#c24747" stroke="black" cx="85.2" cy="-93.21" rx="54.99" ry="18"/>
<text text-anchor="middle" x="85.2" y="-90.71" font-family="Helvetica,sans-Serif" font-size="10.00" fill="#ffffff">sample_py.area</text>
</g>
<!-- sample_py_cli -->
<g id="node6" class="node">
<title>sample_py_cli</title><style>.edge>path:hover{stroke-width:8}</style>
<ellipse fill="#8f3d3d" stroke="black" cx="207.2" cy="-18" rx="48.72" ry="18"/>
<text text-anchor="middle" x="207.2" y="-15.5" font-family="Helvetica,sans-Serif" font-size="10.00" fill="#ffffff">sample_py.cli</text>
</g>
<!-- sample_py_area&#45;&gt;sample_py_cli -->
<g id="edge1" class="edge">
<title>sample_py_area&#45;&gt;sample_py_cli</title><style>.edge>path:hover{stroke-width:8}</style>
<path fill="none" stroke="black" d="M110.48,-77.04C128.88,-66 153.98,-50.94 173.99,-38.93"/>
<polygon fill="#c24747" stroke="black" points="176.02,-41.8 182.79,-33.65 172.42,-35.8 176.02,-41.8"/>
</g>
<!-- sample_py_area_ellipse -->
<g id="node2" class="node">
<title>sample_py_area_ellipse</title><style>.edge>path:hover{stroke-width:8}</style>
<ellipse fill="#c24747" stroke="black" cx="50.2" cy="-179.42" rx="50.41" ry="28.98"/>
<text text-anchor="middle" x="50.2" y="-187.92" font-family="Helvetica,sans-Serif" font-size="10.00" fill="#ffffff">sample_py.</text>
<text text-anchor="middle" x="50.2" y="-176.92" font-family="Helvetica,sans-Serif" font-size="10.00" fill="#ffffff">area.</text>
<text text-anchor="middle" x="50.2" y="-165.92" font-family="Helvetica,sans-Serif" font-size="10.00" fill="#ffffff">ellipse</text>
</g>
<!-- sample_py_area_ellipse&#45;&gt;sample_py_cli -->
<g id="edge2" class="edge">
<title>sample_py_area_ellipse&#45;&gt;sample_py_cli</title><style>.edge>path:hover{stroke-width:8}</style>
<path fill="none" stroke="black" d="M89.22,-161.14C116.04,-147.11 149.98,-124.66 168.2,-94.21"/>
<path fill="none" stroke="black" d="M168.2,-92.21C177.4,-76.85 186.86,-59.14 194.16,-44.99"/>
<polygon fill="#c24747" stroke="black" points="197.41,-46.33 198.84,-35.84 191.17,-43.15 197.41,-46.33"/>
</g>
<!-- sample_py_area_polygon -->
<g id="node3" class="node">
<title>sample_py_area_polygon</title><style>.edge>path:hover{stroke-width:8}</style>
<ellipse fill="#c24747" stroke="black" cx="168.2" cy="-179.42" rx="50.41" ry="28.98"/>
<text text-anchor="middle" x="168.2" y="-187.92" font-family="Helvetica,sans-Serif" font-size="10.00" fill="#ffffff">sample_py.</text>
<text text-anchor="middle" x="168.2" y="-176.92" font-family="Helvetica,sans-Serif" font-size="10.00" fill="#ffffff">area.</text>
<text text-anchor="middle" x="168.2" y="-165.92" font-family="Helvetica,sans-Serif" font-size="10.00" fill="#ffffff">polygon</text>
</g>
<!-- sample_py_area_polygon&#45;&gt;sample_py_cli -->
<g id="edge3" class="edge">
<title>sample_py_area_polygon&#45;&gt;sample_py_cli</title><style>.edge>path:hover{stroke-width:8}</style>
<path fill="none" stroke="black" d="M161.29,-150.34C158.61,-132.97 158.22,-110.9 168.2,-94.21"/>
</g>
<!-- sample_py_arith -->
<g id="node4" class="node">
<title>sample_py_arith</title><style>.edge>path:hover{stroke-width:8}</style>
<ellipse fill="#c24747" stroke="black" cx="246.2" cy="-93.21" rx="50.41" ry="21.43"/>
<text text-anchor="middle" x="246.2" y="-96.21" font-family="Helvetica,sans-Serif" font-size="10.00" fill="#ffffff">sample_py.</text>
<text text-anchor="middle" x="246.2" y="-85.21" font-family="Helvetica,sans-Serif" font-size="10.00" fill="#ffffff">arith</text>
</g>
<!-- sample_py_arith&#45;&gt;sample_py_cli -->
<g id="edge4" class="edge">
<title>sample_py_arith&#45;&gt;sample_py_cli</title><style>.edge>path:hover{stroke-width:8}</style>
<path fill="none" stroke="black" d="M235.55,-72.21C231.06,-63.79 225.78,-53.88 221.01,-44.91"/>
<polygon fill="#c24747" stroke="black" points="224.05,-43.18 216.26,-36 217.87,-46.48 224.05,-43.18"/>
</g>
<!-- sample_py_arith_basic -->
<g id="node5" class="node">
<title>sample_py_arith_basic</title><style>.edge>path:hover{stroke-width:8}</style>
<ellipse fill="#c24747" stroke="black" cx="324.2" cy="-179.42" rx="50.41" ry="28.98"/>
<text text-anchor="middle" x="324.2" y="-187.92" font-family="Helvetica,sans-Serif" font-size="10.00" fill="#ffffff">sample_py.</text>
<text text-anchor="middle" x="324.2" y="-176.92" font-family="Helvetica,sans-Serif" font-size="10.00" fill="#ffffff">arith.</text>
<text text-anchor="middle" x="324.2" y="-165.92" font-family="Helvetica,sans-Serif" font-size="10.00" fill="#ffffff">basic</text>
</g>
<!-- sample_py_arith_basic&#45;&gt;sample_py_cli -->
<g id="edge5" class="edge">
<title>sample_py_arith_basic&#45;&gt;sample_py_cli</title><style>.edge>path:hover{stroke-width:8}</style>
<path fill="none" stroke="black" d="M325.61,-150.06C325.33,-127 321.59,-94.66 305.2,-72 292.6,-54.57 272.46,-42.28 253.7,-33.95"/>
<polygon fill="#c24747" stroke="black" points="254.93,-30.67 244.35,-30.07 252.24,-37.14 254.93,-30.67"/>
</g>
</g>
</svg>
