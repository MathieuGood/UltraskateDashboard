# UltraskateDashboard

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)

## How to run with debug mode in VSCode

`launch.json` configuration

```json
//
{
	"version": "0.2.0",
	"configurations": [
		{
			"name": "Attach to uv debugpy",
			"type": "python",
			"request": "attach",
			"connect": {
				"host": "localhost",
				"port": 5678
			},
			"justMyCode": true
		}
	]
}
```

Install `debugpy` in your virtual environment:

```bash
uv add debugpy
```

Run app with uv in debug mode

```bash
uv run -m debugpy --listen 5678 --wait-for-client main.py
```
