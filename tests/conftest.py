import sys
from pathlib import Path

project_root_dir = Path(__file__).parent.resolve()
project_src_dir = project_root_dir / "src"
project_tests_dir = project_root_dir / "tests"

sys.path.insert(0, project_src_dir)
sys.path.insert(1, project_tests_dir)
