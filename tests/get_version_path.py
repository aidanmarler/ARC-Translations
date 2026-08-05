# get_version_path.py
import os
from bridge.arc.arc_api import ArcApiClient

arc_client = ArcApiClient()
all_versions = arc_client.get_arc_version_list()
most_recent_version_str = all_versions[0] if all_versions else None

print(f"path found: {most_recent_version_str}")

path = most_recent_version_str

print(f"path found: {path}")

with open(os.environ["GITHUB_OUTPUT"], "a") as f:
    f.write(f"path={path}\n")