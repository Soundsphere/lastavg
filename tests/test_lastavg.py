import importlib.util
import time
from datetime import datetime
from pathlib import Path

# Load lastavg module from file
spec = importlib.util.spec_from_file_location(
    "lastavg", str(Path(__file__).resolve().parents[1] / "lastavg.py")
)
lastavg = importlib.util.module_from_spec(spec)
spec.loader.exec_module(lastavg)


def test_joineddate(tmp_path, monkeypatch):
    temp_home = tmp_path
    config_dir = temp_home / ".config" / "lastavg"
    config_dir.mkdir(parents=True)
    config_path = config_dir / "config.cfg"
    config_path.write_text("[DEFAULT]\nuser=testuser\njoined=01.01.2020\n")

    monkeypatch.setattr(lastavg, "HOME", str(temp_home))

    expected = (
        datetime.strptime(time.strftime("%d.%m.%Y"), "%d.%m.%Y")
        - datetime.strptime("01.01.2020", "%d.%m.%Y")
    ).days + 1
    assert lastavg.joineddate() == expected
