import os, yaml, pathlib

DEFAULT_CONFIG_PATH = os.environ.get("CONFIG", "/mnt/data/seo_automation_config.yaml")

class Config:
    def __init__(self, path: str | None = None):
        self.path = path or DEFAULT_CONFIG_PATH
        with open(self.path, "r") as f:
            self.data = yaml.safe_load(f)

    def get(self, *keys, default=None):
        d = self.data
        for k in keys:
            if d is None: return default
            d = d.get(k)
        return d if d is not None else default

    @property
    def warehouse_path(self):
        # Default to a local DuckDB file next to the config, if not specified
        storage = self.get("storage") or {}
        if isinstance(storage, dict) and storage.get("warehouse", "").lower().startswith("duckdb"):
            return storage.get("path") or str(pathlib.Path("warehouse/seo.duckdb"))
        # Fallback to portable DuckDB
        return str(pathlib.Path("warehouse/seo.duckdb"))
