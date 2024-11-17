Import("env")

def copy_data_files(source, target, env):
    # ライブラリのデータディレクトリのパスを取得
    lib_dir = env.get("PROJECT_LIB_DIR")
    data_dir = os.path.join(lib_dir, "ESP32Console/data")
    
    # SPIFFSイメージの作成とアップロード用のコマンドを追加
    env.AddCustomTarget(
        "uploadfs",
        "$BUILD_DIR/spiffs.bin",
        "pio run -t uploadfs"
    )

env.AddPreAction("buildprog", copy_data_files)