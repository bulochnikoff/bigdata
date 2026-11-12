# Технологии обработки больших данных

Вариант 1. Работы 1–6.

| Папка | Работа |
| --- | --- |
| `лаб1` | Анализ 5V, All_Beauty |
| `лаб2` | Pandas, Dask, Spark, Polars, DuckDB |
| `лаб3` | ELT, витрина, dbt |
| `лаб4` | Модели, MLflow, онлайн-обучение |
| `лаб5` | Окна, Kafka и Spark |
| `лаб6` | 80% spot, Docker, Kubernetes |

Файлы отзывов в репозиторий не входят: ссылки на источники стоят в блокнотах.

Проверка dbt: `.github/workflows/lab3_etl.yml`.
Проверка манифестов: `.github/workflows/lab6_manifests.yml`.
Поток работы 5: в папке `лаб5` команда `docker compose -f лаб5_docker-compose.yml up`.
Сервис работы 6: в папке `лаб6` команда `docker compose -f лаб6_docker-compose.yml up --build`, затем `python лаб6_load.py`.
