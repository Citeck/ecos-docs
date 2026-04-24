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

Рекомендуется устанавливать зависимости в виртуальное окружение — на современных macOS/Linux прямой `pip install` часто блокируется (PEP 668, ошибка `externally-managed-environment`).

```bash
python3 -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r docs/requirements.txt
pre-commit install
```

Перед каждой сборкой активируйте окружение командой `source .venv/bin/activate`.

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

## Выгрузка в PDF

Для сборки PDF используется LaTeX-сборщик Sphinx с движком XeLaTeX (нужен для корректного отображения кириллицы).

### Требования

Нужны:

- TeX Live с XeLaTeX, `latexmk` и шрифтами для кириллицы;
- `rsvg-convert` из `librsvg` — `xelatex` не умеет встраивать SVG напрямую, Sphinx конвертирует их в PDF через `sphinxcontrib-svg2pdfconverter`;
- ImageMagick (`convert`/`magick`) — для расширения `sphinx.ext.imgconverter`, которое автоматически ужимает слишком большие растровые изображения, чтобы `xelatex` не падал с `Dimension too large`.

#### macOS

```bash
brew install --cask mactex-no-gui
brew install librsvg imagemagick
```

Или минимальный вариант TeX Live:

```bash
brew install --cask basictex
sudo tlmgr update --self
sudo tlmgr install latexmk xetex collection-fontsrecommended collection-langcyrillic
brew install librsvg imagemagick
```

#### Ubuntu/Debian

```bash
sudo apt install texlive-xetex texlive-fonts-recommended texlive-lang-cyrillic latexmk librsvg2-bin imagemagick
```

#### Windows

Установите [MiKTeX](https://miktex.org/) или [TeX Live](https://tug.org/texlive/) — недостающие пакеты подтянутся автоматически при первой сборке. Дополнительно нужны `rsvg-convert` из [librsvg](https://gnome.pages.gitlab.gnome.org/librsvg/) и [ImageMagick](https://imagemagick.org/script/download.php) (например, `choco install rsvg-convert imagemagick` или `scoop install librsvg imagemagick`).

### Сборка

```bash
cd docs
make latexpdf
```

Готовый PDF будет доступен по пути `_build/latex/citeck.pdf`.
