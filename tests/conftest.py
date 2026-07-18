import pathlib
import sys

# scripts/는 패키지가 아니므로 경로를 직접 추가한다
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent / "scripts"))
