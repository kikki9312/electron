import os
import subprocess
import sys

SOURCE_ROOT = os.path.dirname(os.path.dirname(__file__))

# Helper to run gn format on multiple files
# (gn only formats a single file at a time)
def main():
  new_env = os.environ.copy()
  new_env['DEPOT_TOOLS_WIN_TOOLCHAIN'] = '0'
  new_env['CHROMIUM_BUILDTOOLS_PATH'] = os.path.realpath(
    os.path.join(SOURCE_ROOT, '..', 'buildtools')
  )
  for gn_file in sys.argv[1:]:
    subprocess.check_call(
      ['gn', 'format', gn_file],
      shell=True,
      env=new_env
    )

if __name__ == '__main__':
  sys.exit(main())
