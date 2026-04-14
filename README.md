# Документация платформы Citeck

Документация для платформы [Citeck](https://www.citeck.ru/) — low-code платформа для управления бизнес-процессами, документами и задачами.

## Требования

- Python 3.12+
- [pre-commit](https://pre-commit.com/) — git-хуки для автоматического сжатия изображений
- [pngquant](https://pngquant.org/) — сжатие PNG
- [jpegoptim](https://github.com/tjko/jpegoptim) — сжатие JPEG
- [gifsicle](https://www.lcdf.org/gifsicle/) — сжатие GIF
- [webp](https://developers.google.com/speed/webp/) — сжатие WebP (cwebp)

### macOS

```bash
brew install pngquant jpegoptim gifsicle webp pre-commit
```

### Ubuntu/Debian

```bash
sudo apt install pngquant jpegoptim gifsicle webp
pip install pre-commit
```

### Windows

```powershell
choco install pngquant jpegoptim gifsicle libwebp
pip install pre-commit
```

Или через [Scoop](https://scoop.sh/):

```powershell
scoop install pngquant jpegoptim gifsicle libwebp
pip install pre-commit
```

## Настройка

```bash
pip install -r docs/requirements.txt
pre-commit install
```

После `pre-commit install` каждый коммит с изображениями будет автоматически сжимать их.

### Ручной запуск сжатия

Если pre-commit хук не настроен, можно сжать изменённые изображения перед коммитом вручную:

```bash
python3 scripts/compress-images.py path/to/image1.png path/to/image2.jpg
```

Для сжатия всех изображений в репозитории:

```bash
pre-commit run compress-images --all-files
```

## Локальная сборка

```bash
cd docs
make html
```

Результат сборки будет в `_build/html/`. Для просмотра в браузере:

```bash
python3 -m http.server 8030 --directory _build/html/
```

Затем откройте http://localhost:8030.
