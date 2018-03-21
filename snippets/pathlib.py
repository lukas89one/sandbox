# Pathlib
# ---------------------------------------------------------------------------------------------------------------------

# Path handling is much more simpler

from pathlib import Path
directory = Path("/etc")
filepath = directory / "test_file.txt"
print(filepath)
# '/etc/test_file.txt'
filepath.exists()
# False

# ---
# Python 2
#
# import os
#
# directory = "/etc"
# filepath = os.path.join(directory, "test_file.txt")
# print filepath
# '/etc/test_file.txt'
# os.path.exists(filepath)
# False
# ---------------------------------------------------------------------------------------------------------------------
