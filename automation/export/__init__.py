"""Factory export stage — CSV / JSONL / Parquet / HF / OpenAI packages."""

__all__ = ["export_dataset"]


def __getattr__(name: str):
    if name == "export_dataset":
        from automation.export.packager import export_dataset

        return export_dataset
    raise AttributeError(name)
