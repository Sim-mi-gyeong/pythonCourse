# screts.json 을 읽어 해당하는 value 값을 출력해주는 파일
import json
from pathlib import Path
from typing import Optional

# Path(__file__) : 현재 해당하는 파일!
# -> .parent: 경로의 루트 경로 3-동시성-프로그래밍~ 폴더 내의 secrets.json
BASE_DIR = Path(__file__).resolve().parent


def get_secret(
    key: str,
    default_value: Optional[str] = None,
    json_path: str = str(BASE_DIR / "secrets.json"),
):
    with open(json_path) as f:
        secrets = json.loads(f.read())

    try:
        return secrets[key]
    except KeyError:
        if default_value:
            return default_value
        raise EnvironmentError(f"Set the {key} enviroment variable.")
