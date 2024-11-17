import os
import shutil
Import("projenv", "env")

print("==============================================")
print("ESP32Console.handle_data.py")

def copy_data_files(source, target, env):
  print("==============================================")
  print("ESP32Console.handle_data.py.copy_data_files")

  # プロジェクトのルートディレクトリを取得
  project_dir = env['PROJECT_DIR']
  
  # libdepsディレクトリのパスを構築
  lib_deps_dir = os.path.join(project_dir, '.pio', 'libdeps')
  
  # 現在のボード環境を取得
  current_env = env['PIOENV']
  
  # ライブラリのデータディレクトリのパス
  lib_data_dir = os.path.join(lib_deps_dir, current_env, 'ESP32Console', 'data')
  
  # プロジェクトのdataディレクトリのパス
  project_data_dir = os.path.join(project_dir, 'data')

  print("Library Data Dir:", lib_data_dir)
  print("Project Data Dir:", project_data_dir)
  
  # ライブラリのdataディレクトリが存在するか確認
  if not os.path.exists(lib_data_dir):
    print("Library data directory not found:", lib_data_dir)
    return

  # プロジェクトのdataディレクトリが存在しない場合は作成
  os.makedirs(project_data_dir, exist_ok=True)

  try:
    # ライブラリのdataディレクトリ内のファイルをコピー
    for item in os.listdir(lib_data_dir):
      source_path = os.path.join(lib_data_dir, item)
      dest_path = os.path.join(project_data_dir, item)
      
      if os.path.isfile(source_path):
        print(f"Copying file: {item}")
        shutil.copy2(source_path, dest_path)
      elif os.path.isdir(source_path):
        print(f"Copying directory: {item}")
        # ディレクトリが存在する場合は削除してからコピー
        if os.path.exists(dest_path):
          shutil.rmtree(dest_path)
        shutil.copytree(source_path, dest_path)
              
    print("Data files copied successfully")
  except Exception as e:
    print("Error copying files:", str(e))
  
  print("==============================================")

# uploadとuploadfsの両方のターゲットで実行
for e in (env, projenv, DefaultEnvironment()):
  e.AddPreAction("uploadfs", copy_data_files)
print("==============================================")