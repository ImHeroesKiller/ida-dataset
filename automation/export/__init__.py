"""Factory export stage — CSV / JSONL / Parquet / HF / OpenAI packages."""

__all__ = ["export_dataset", "publish_to_huggingface"]


def __getattr__(name: str):
    if name == "export_dataset":
        from automation.export.packager import export_dataset

        return export_dataset
    if name == "publish_to_huggingface":
        from automation.export.hf_publisher import publish_to_huggingface

        return publish_to_huggingface
    raise AttributeError(name)
