import subprocess
import shutil
import os


def get_last_commit_id():
    try:
        result = subprocess.run(
            ['git', 'log', '-n', '1', '--pretty=format:%h'], capture_output=True, text=True)
        return result.stdout.strip()
    except Exception as e:
        print(f"Error getting last commit ID: {e}")
        return ''


if __name__ == '__main__':
    # version = datetime.now().strftime('%y_%m_%d')
    # last_commit_id = get_last_commit_id()

    # Define source and destination paths
    source_file = 'app.py'
    source_dir = '.streamlit'
    dist_dir = 'dist'

    # Copy the app.py file to the dist directory
    shutil.copy(source_file, os.path.join(dist_dir, source_file))

    # Copy the .streamlit directory to the dist directory
    shutil.copytree(source_dir, os.path.join(
        dist_dir, source_dir), dirs_exist_ok=True)

    print(f"Copied {source_file} and {source_dir} to {dist_dir}")

    subprocess.run(['pyinstaller',
                    'run_app.spec',
                    '--clean'
                    ])
