# Office Tweaks — утилита автоматизации работы с файлами

[![Python](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![Pillow](https://img.shields.io/badge/Pillow-image-4B8BBE)]()

Консольная утилита на **Python** для пакетной обработки офисных файлов: конвертация документов, сжатие изображений и очистка каталогов. Управление через интерактивное меню.

## Возможности

- 📄 **PDF → DOCX** и **DOCX → PDF** — конвертация документов в каталоге (`pdf2docx`, `docx2pdf`).
- 🖼️ **Сжатие изображений** в каталоге (`Pillow`).
- 🗑️ **Удаление файлов** по заданным критериям.
- 🧭 Интерактивное **меню** для выбора операции.

## Функции

| Функция | Назначение |
|---------|-----------|
| `PDF_to_Docx(catalog)` | конвертация PDF → DOCX |
| `Docx_to_PDF(catalog)` | конвертация DOCX → PDF |
| `compress_image(catalog)` | сжатие изображений |
| `delete_files(catalog)` | удаление файлов по критериям |
| `menu()` | главное меню выбора действия |

## Структура

```
Office_Tweaks/
├── App/
│   ├── main.py     # точка входа: меню
│   └── logics.py   # операции с файлами
└── Info/
    └── information.py
```

## Установка и запуск

```bash
git clone https://github.com/DenisDrobyshev/Office_Tweaks.git
cd Office_Tweaks/App
pip install pdf2docx docx2pdf Pillow

python main.py
```

После запуска выберите нужную операцию в меню и укажите каталог с файлами.

## Стек

`Python` · `pdf2docx` · `docx2pdf` · `Pillow`

> Учебный проект: автоматизация рутинных операций с документами и изображениями.
